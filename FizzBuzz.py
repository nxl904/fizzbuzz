import sys


n = range(1,100)

def FizzBuzz():
	for a in n: 
		if a%5 == 0 and a%3==0: 
			print ("FizzBuzz")
		elif a%3 == 0: 
			print ("Buzz")
		elif a%5 == 0: 
		    print ("Fizz")
		else: 
		    print(n[a])

FizzBuzz()
