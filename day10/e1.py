import os
import time
os.system("clear")
def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

operations_dict = {'+': add ,'-': substract,'*': multiply,'/': divide }

symbol_list= ["+","-","*","/"]

for _ in range(0,3):
    symbol = input(" select an operation from the dictionary: ")
    

    if symbol in symbol_list:
        
        calculation_function= operations_dict[symbol]
        x= int(input("Type a number: "))
        y= int(input("type another one: "))
        result = calculation_function(x,y)
        print(result)
    elif symbol not in symbol_list:
        print("Invalid symbol")
    time.sleep(5)
    os.system("clear")    




