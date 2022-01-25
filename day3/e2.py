height= int(input("whats your heigth in cm: "))

can_ride= False

if height >= 120:
    can_ride = True


if can_ride:
    age = int(input("how old are you?: "))
    ticket = 0
    if age < 12:
        ticket += 5
    elif age <= 18:
        ticket += 7
    elif age <= 45:
        ticket += 9
    photo = input(" Do ypu want a photo?: (y/n): ").lower()
    if photo == "y":
         ticket += 3

    print(f"you have to pay {ticket}")
elif not can_ride:
    print("you cannot ride")


