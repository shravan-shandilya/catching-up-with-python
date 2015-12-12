#!/usr/bin/python
def decorator(func):
	def replaced_function():
		print "Boom..!",func.__name__,"got replaced ",
		print "Inside the replaced function now.."
	return replaced_function

@decorator
def actual_function():
	print "I think something is replacing me. :("


actual_function()
