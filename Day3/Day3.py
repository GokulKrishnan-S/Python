'''
Day 3
Python Pratice Programs
'''

#Program 1
nums = [1, 2, 3]
square_dict = {num: num*num for num in nums}
print(square_dict)
square_list = [num*num for num in nums]
print(square_list)



#Program 2
nums = [1, 2, 5, 2, 3, 1, 4, 5]
unique_squares = {num*num for num in nums} 
print(unique_squares)



#Program 3
current_and_min_balances = [("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]

#Case 1
above_or_equal_than_min_balances = {name : current_balance for (name, current_balance, min_balance) in current_and_min_balances if current_balance >= min_balance}
print(above_or_equal_than_min_balances)

#Case 2
balances_set = {current_balance for (name, current_balance, min_balance) in current_and_min_balances}
print(balances_set)

#Case 3
account_holders_list = [name for (name, current_balance, min_balance) in current_and_min_balances]
print(account_holders_list)

#Case 4
min_balance_requirement_dict = {name : min_balance-current_balance for (name, current_balance, min_balance) in current_and_min_balances if current_balance < min_balance}
print(min_balance_requirement_dict)

#Case 5
name_and_balance_tuple_list = [(name, current_balance) for(name, current_balance, min_balance) in current_and_min_balances if current_balance > 0]
print(name_and_balance_tuple_list)




#Program 4
class Developer:
    def __init__(self):
      self.languages = ['Python', 'C', 'C++', 'Java', 'Ruby', 'PHP']
      self.developer_languages = []

    def code(self, language):
        if language in self.languages:
            print("code in ", language) 
            self.developer_languages.append(language)
   
    def resume(self):
        print(self.developer_languages)


developer1 = Developer()
developer1.code('Python')
developer1.code('Java')
developer1.resume()

developer2 = Developer()
developer2.code('C')
developer2.code('C++')
developer2.resume()
print('\n')

class SrDeveloper(Developer):
    def __init__(self):
        Developer.__init__(self)
        self.reviews = []

    def review(self, review):
        if(len(self.reviews) <= len(self.developer_languages)):
            self.reviews.append(review)  

    def reviews_by_srdeveloper(self):
        print(self.reviews)        

developer3 = SrDeveloper()
developer3.code('C')
developer3.review("Good")
developer3.code('Python')
developer3.review("Very Good")
developer3.reviews_by_srdeveloper()
print('\n')


class TechLead(SrDeveloper):
    def __init__(self):
        SrDeveloper.__init__(self)

    def design(self):
        print("Design for project invoked")


developer4 = TechLead()
developer4.code('Python')
developer4.design()
 



#Program 5
import math
class Factorial:
    def factorials(self, nums):
        for num in nums:
            print(math.factorial(num))


factorialization = Factorial()
factorialization.factorials([1, 2, 4, 6, 5])



#Program 6
from moduleDay3 import print_something
print_something()


#Program 7
from moduleDay3 import print_something as greeting
greeting()

#Program 7 is in moduleDay3.py

#Program 9 - Extra Mile
class Greeting:
    def __init__(self, greetings, name):
        self.greetings = greetings
        self.name = name

greet = Greeting('Hi', 'There')

print(greet.__str__())
print(greet.__repr__())