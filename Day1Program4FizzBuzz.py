numbers = int(input("Enter range of values: ")) 
for num in range(1,numbers+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
        continue
    elif num % 3 == 0:
        print("fizz") 
        continue
    elif num % 5 == 0:
        print("buzz") 
        continue     
    else:
        print(num)