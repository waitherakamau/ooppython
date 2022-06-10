# def greeting(name ,age)
#      year=2022-age
#      returnf"Hello{name}you were born in {year}"
#      greeting(name ="Effence",age=21)
#      greeting(age=21,name="Effence") 
#      greeting(age=22,name="Alice")
     # position arguments must be supplied to the ffunction in the correct.
     #key word argument can be sent to the function oin any order.
# from unicodedata import name


# def my_country(country="Uganda",student="susan"):
#          return f"Helllo {student}you are from {country}"

# my_country()
# my_country(country="Rwanda",student="Verite")

# def greet_multiple(*names):
#     for name in names:
#         print(f"Hello{name}")   

#         #Write a function that accepts any number of intergers and return the sum of them
#         # sum(1,2)   
#         #sum(1,2,3)
#         #sum ()
#         # 
# def add(*numbers):
#      for numbers in numbers:
#         sum+=numbers
#         return sum

# def greet_mult(**kwargs):
#     keys = kwargs.keys()
#     if "Counrty" in keys:
#      print (f"Hello{kwargs['name' ]}you are form{kwargs['country']}")
#     elif "age" in keys:
#       year = 2022-kwargs["age"]
#       print(f"Hello{kwargs['name']} you were born in {kwargs['year']}")
#     elif not  kwargs:
#             print(f"Hello Anonymous")

def sum_and_greet(*args,**kwargs):
    sum=0
    for num in args:
        sum+=num

        keys = kwargs.keys()
        if "name" in keys:
            print(f"Hello{kwargs['name']},the answer is {sum}") 
        elif "country"in keys:
            print(f"Hello {kwargs['name']} from{kwargs['country']} the anwer is{sum}")
        elif not kwargs:
            print(f"Hello anaonymoys the answer is{sum}")

sum_and_greet(1,2,3,name="waithera")

def withdraaw (self,amount):
    if amount 
    hello 



        



         









