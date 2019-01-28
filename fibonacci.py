#!usr/bin/python3.7
#Date : Mon 28 Jan 2019 03:24:59 PM CET 
#Author: Nicolas Flandrois

def fib(n:int):
	"""This generator yield each iteration of the fibonacci sequence, for iteration of a range n number."""
	a, b = 0, 1
	for i in range(n):
		yield a
		a, b = b, a+b
		
fibonacci = [f for f in fib(200)]
#Comprehension list applying the fibonacci generator, and holding the result in a list, sequences.

print(fibonacci)
