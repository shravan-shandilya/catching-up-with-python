#!/usr/bin/python
def decorator(func):
	def wrapper():
		print "Boom..! some feature wrapping before actually calling",func.__name__," ",
		func(); 					
		print "wrapping some features after actually calling the real function"
	return wrapper

@decorator
def actual_function():
	print "The core feature :) "


actual_function()
