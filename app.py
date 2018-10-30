#!/usr/bin/env python
from flask import Flask
from flask_ask import Ask, statement, question, session
import math
import requests


# This script relies on Cricinfo RSS Live Feed (http://static.cricinfo.com/rss/livescores.xml)


app = Flask(__name__)
ask = Ask(app, '/')

 
# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
     
@app.route('/')
def homepage():
    return 'Welcome to GetFibo'

@ask.launch
def start_skill():
    message = 'Hey.. Ask me whether a number is in fibonacci sequence or not?'
    return question(message)

@ask.intent("NumberIntent")
def number_intent(num):
	ans =  isFibonacci(num)
	if ans:
		return statement("Yes")
	else:
		return statement("No")

@ask.intent("NoIntent")
def no_Intent():
    message = 'Well that is fine...Maybe next time'
    return statement(message)

@ask.intent("AMAZON.CancelIntent")
def cancel_Intent():
    message = 'See you again...bye'
    return statement(message)

@ask.intent("AMAZON.StopIntent")
def stop_Intent():
    message = 'See you again...bye'
    return statement(message)

@ask.intent("AMAZON.HelpIntent")
def help_Intent():
    message = 'Say a number.'
    return question(message)

if __name__ == '__main__':
    app.run(threaded = True)