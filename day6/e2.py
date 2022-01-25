#ciclo que se dentenga hasta que diga stop
import os
os.system("clear")
count=0
while input("Type a message: ").lower() != "stop":
    print(count)
    count += 1