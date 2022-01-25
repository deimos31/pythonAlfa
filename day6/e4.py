import os
os.system("clear")
list =[]
i=0

another_number= True
while another_number:
    answer=input("Do you want add another number?: ").lower( ) 
    if answer =="stop":
        another_number= False
    elif answer== "yes":
        list.append(i)
        i+=1
        print(list)
    elif answer=="two":
        list.extend([i,i + 1])
        print(list)
        i+=1
    else:
        print("Its no defined")
        another_number= False    