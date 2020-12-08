total=0
sandwich = input("Please pick a ype of sandwich, chicken(c) for $5.25, beef(b) for $6.25, tofu(t) for $5.75.")
print(sandwich)

beverage = input("Would you like a drink, y or n? ")
if(beverage=="y"):
    beverage=input("s for $1.00, m for $1.75, l for $2.25, c for $2.63 ")
    print("you said ", beverage, "drink.")    #print(string,string,string,string)

if sandwich=="c":
    total += 5.25
elif sandwich=="b":
    total += 6.25
elif sandwich=="t":
    total += 5.75

if beverage=="s":
        total += 1.00
elif beverage=="m":
    total += 1.75
elif beverage=="l":
    total += 2.25
elif beverage=="c":
    total += 2.63

fries = input("Would you like fench fries, y or no? ")
if(fries=="y"):
    fries = input("Would you like a s for $1, m for $1.50, or l for $2? ")


if (fries == "s"):
    total = + 1
elif (fries == "m"):
    total = total + 1.50
elif (fries =="l"):
    fries=input("Would you like a child size fry instead fro an addition $.38? (y or n)")
    if (fries == "y"):                  #nested condtional statement
        total += 2.38
    else:
        total+=2

#print("You're total is ",total)
print('${:,.2f}'.format(total))
