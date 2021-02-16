""" 
Day2
Python Practice Programs
"""

#Program 1
hardCodedValue = 10
for tries in range(3):
	num = int(input("Enter your number: "))
	if num > hardCodedValue:
		print("You guessed greater than the hardCodedValue")
	if num < hardCodedValue:
	    print("You guessed lesser than the hardCodedValue")
	if num == hardCodedValue:
	    print("You guessed right")
	    break    	


#Program 2
alphaList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for count, item in enumerate(alphaList):
  print(count, ": ", item)


#Program 3
carDict = {'make': 'Honda', 'model': 'City', 'cc': '1500'}
for key, value in carDict.items():
    print(key, value)


#Program 4   
#else being invoked 
i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("The number cannot be less than 4")

#else not being invoked
i = 1
while i < 4:
    print(i)
    i += 1
    if i == 4:
      break
else:
    print("The number cannot be less than 4")



#Program 5
def add(num1: int, num2: int) -> int:
    '''Takes in num1 and num2 and returns the added value'''
    sum = num1 + num2
    return sum
    
print(add(2, 3))
print(add(6, 10))

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(add.__doc__)
print(add(a, b))


#Program 6
def greet(*args):  
    for arg in args:  
        print (arg) 
    
greet("Hello", "Hi", "Howdy", "Namaste") 



#Program 7
def greet(**kwargs):  
        print(len(kwargs))    

greet(greeting="Hi", name="Gokul", punctuation="!")



#Program 8
def collections(*args, **kwargs):
    print(len(args) + len(kwargs))

collections('hi','hello','howdy', greeting="Hi", name="Gokul", punctuation="!")   



#Program 9
i = 1
while i < 4:
    print(i)
    i += 1
    if i == 4:
      break
else:
    print("The number cannot be less than 4")



#Program 10
numList = [1, 3, 3, 4, 5, 6]
oddList = [num*num for num in numList if num%2 == 1]
for oddSquare in oddList:
	print(oddSquare)



#Program 11	
average = lambda total, count : total/count
total = int(input("Enter total: "))
count = int(input("Enter count: "))
print(average(total, count))