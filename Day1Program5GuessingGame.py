hardCodedNum = 10
number = int(input("Enter a guess number: "))
if number<hardCodedNum:
	print(str(number) + " is less than the hardcoded number")
elif number>hardCodedNum:
    print(str(number) + " is greater than the hardcoded number")
else:    
    print(str(number) + " is equal to the hardcoded number")
