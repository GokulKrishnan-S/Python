'''
Day 5
Python Practice Programs
'''

#Program 1
def reverse(data):
    for index in range(len(data)-1, -1, -1):
         yield data[index]


it = reverse('Hello')
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))



#Program 2
#Overwriting __len__
class Length_plus_ten(list):
     def __len__(self):
        return super().__len__() + 10

list = Length_plus_ten(['Python', 'C', 'Java'])
print(len(list))



#Overwriting __repr__
class Expereience_in_years:
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp

    def __repr__(self):
        string = f'Expereience in years of employee ( {self.name},  {str(self.exp)} )'
        return string


experience1 = Expereience_in_years("John", 10)
experience2 = Expereience_in_years("Jacob", 11)

print(repr(experience1))
print(repr(experience2))






#Program 3
import timeit

def timer(function):
    def inner():
        start_time = timeit.default_timer()
        function()
        end_time = timeit.default_timer()
        diff = end_time - start_time
        print('{name} ran in {time} seconds.'.format(name = function.__name__, time = diff))
    return inner()

@timer
def addition():
    sum = 0
    for i in range(0,1000):
        sum += i
    return sum