
firstcal = float(input("Enter a number: "))
secondcal = float(input("Enter another number: "))

usersinput = input("What to calculate? \n1 = Add\n2 = Subtract\n3 = Mutliply\n4 = Divide\n Please enter a value 1-4!\n")
if usersinput == "1":
    print(firstcal + secondcal)
if usersinput == "2":
    print(firstcal - secondcal)
if usersinput == "3":
    print(firstcal * secondcal)
if usersinput == "4":
    print(firstcal / secondcal)

input("Press enter to exit.")