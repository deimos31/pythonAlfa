#if statment

num1=int(input("type a number: "))
is_even = False
is_eigth = False

if num1 % 2 == 0:
    is_even= True
    if num1 == 8:
        is_eigth= True
    elif num1== 4:
        pass    

#print(f"{num1} is even")

if is_even == True:
    print(f"{num1} is even")
    if is_eigth:
        print("num1 = 8")
elif is_even == False:
    print(f"{num1} is odd")