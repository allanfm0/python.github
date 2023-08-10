#and
#or
#not
# a = 12
# print(a < 20)


print("Welcome to rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Whats your age? "))
    if age < 12:
        bill = 5
        print(f"Please pay ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Please pay ${bill}.")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")

    else:
        bill = 12
        print(f"Please pay ${bill}.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is {bill}!")
    if wants_photo == "N":
        print("")
else:
    print("Sorry, you have to grow taller before you can ride.")