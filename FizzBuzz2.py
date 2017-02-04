n = int(input("Select first number of range: "))
n2 = int(input("Select second number of range: "))
r = range(n,n2)

def FizzBuzz():
	for a in r: 
		if a%5 == 0 and a%3==0: 
			print ("FizzBuzz")
		elif a%3 == 0: 
			print ("Buzz")
		elif a%5 == 0: 
		    print ("Fizz")
		else: 
		    print(r[a])

FizzBuzz()
