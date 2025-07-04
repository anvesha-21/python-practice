# MAP

# def cube (x):
#     return x*x*x
# print(cube(2))

l=(1,2,4,6,4,3)

newl = list(map(lambda x: x*x*x ,l))
print(newl)

# FILTER

def filter_function(a):
    return a>3

newnewl = list(filter(filter_function , l))
print(newnewl)

# REDUCE

from functools import reduce


numbers = [1,2,3,4,5]

def mysum (x,y):
    return x+y

sum = reduce(mysum, numbers)
print(sum)

