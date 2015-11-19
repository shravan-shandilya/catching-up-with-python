#! /usr/bin/python
import thread

def thr_fun(char,num):
	ctr=0
	while ctr<num:
		print char,
		ctr+=1

thread.start_new_thread(thr_fun,('O',900000))
thread.start_new_thread(thr_fun,('X',900000))
thread.start_new_thread(thr_fun,('O',900000))
thread.start_new_thread(thr_fun,('Y',900000))

while True:
	print "A"
	pass