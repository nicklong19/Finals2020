total=0
sandwich = input("Please pick a ype of sandwhich, chicken(c) for $5.25, beef(b) for $6.25, tofu(t) for $5.75")
print(sandwhich)

beverage = input("Would you like a drink, y or n? ")
if(beverages=="y"):
    beverage=input("s for $1.00, m for $1.75, l for $2.25")
    print("you said ", beverage, "drink.")    #print(string,string,string,string)

if sandwhich=="c":
    total += 5.25
elif sandwhich=="b":
    total += 6.25
elif sandwhich=="t":
    total += 5.75

if beverage=="s":
        total += 1.00
elif beverage=="m":
    total += 1.75
elif beverage=="l":
    total += 2.25


print("You're total is ",total)

