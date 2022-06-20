# x=[1,2]
# for y in x:
#     y[x]*2
# print(y)

# x=[2,3]
# y=(n*n for n in x):

from itertools import pairwise


A={1,2,3,4,5}
B={6,7,8,9}
print(A.union(B))

S={1,2,3,6}
V={4,5,6}
print(S.intersection(V))

cars=['benz','toyota','vivo']
print("te return value is:",cars.pop(1))
print(cars)
# df=cars.pop(2)

cars=["Benx","Toyota","voxy"]
cars.sort()
print(cars)

x=[20,49,50,40]
x=x.pop()
print(x)

numbers=[11,12,13,14,15]
sum=0
for val in numbers:
    sum=sum+val

    print("The sum is,sum")

print(range(10))

# list is a collection of items they are immutable and takes all types of data like int float and string
# set-unordered collections of items and is imutavble does not allow duplicates 
# tuple is used to store /multiple items in a single variavle
# Dictionaries keys and values 
# range-returns numbers starting from zero aby default and increaments by 1z

days=["monday","tuesday"]




