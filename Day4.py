'''
Day 4
Python Practice Programs
'''


#Program 1
#Case 1
class Even:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        print(num)   
        return num 

even_nums = Even()
it = iter(even_nums)
next(it)
next(it)
next(it)
next(it)



#Case 2
class Print_even_letters:
    def __init__(self, word):
        self.word = word
        self.index = 0
        self.end = len(self.word)

    def __iter__(self):
        return self

    def __next__(self):
       if self.index >= self.end:
           raise StopIteration 
       else:
           char = self.word[self.index]
           self.index += 2
           return char
           
even_letters = Print_even_letters('Python')
it = iter(even_letters)
print(next(it))
print(next(it))
print(next(it))
print(next(it))



#Program 2
import csv

experience_list = [["Name", "Experience"], ["Mark Zuckerberg", "Java"], ["Elon Musk", "Python"]]
with open('experience.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(experience_list)



#Program 3
import pathlib

myDirectory = pathlib.Path('.')
for file in myDirectory.glob("*.py"):
    print(file)



#Program 4
import sys

print(sys.argv[0]) #Name of the the python file
print(sys.argv[1:]) #List of arguments



#Program 5
hardCodedValue = 10
count = 0
for tries in range(3):
	num = int(input("Enter your number: "))
	if num > hardCodedValue: 
		print("You guessed greater than the hardCodedValue")
	elif num < hardCodedValue:
	    print("You guessed lesser than the hardCodedValue")
	elif num == hardCodedValue:
		print("You guessed right")
		break
	count = count + 1 

if count > 2:
    raise Exception("You are out of tries")



#Program 6
#Type Error
try :
    str = input("Enter a String: ")
    num = int(input("Enter a number: "))
    print(str + num)
except TypeError:
    print("TypeError occurred")    


#Value Error
import math

num = int(input("Enter a negative number for value error to occur:"))
try:
    print("Square Root of num is", math.sqrt(num))
except ValueError:
    print("Value Error Occured")



#Program 7
#Key Error
dict = {"John" : "Python", "Jack" : "java", "Jacob" : "C"}
try:
    print(dict["Jay"])
except KeyError:
    print("KeyError Occured")


#Index Error
list = ["John", "Jack" , "Jacob"]
try:
    print(list[3])
except IndexError:
    print("IndexError Occurred")               