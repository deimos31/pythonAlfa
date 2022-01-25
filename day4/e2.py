#un volado
import random
coin = ["head","tails"]

print(random.choice(coin))

if random.choice(coin) == "head":
    print("head")
else:
    print("tails")    