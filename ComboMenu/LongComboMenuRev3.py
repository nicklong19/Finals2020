"""total=0
sandwichSelected=False
beverageSelected=False
friesSelected=False

sandwich = input("Please pick a ype of sandwich, chicken(c) for $5.25, beef(b) for $6.25, tofu(t) for $5.75.")
if (sandwich=="c" or sandwich=="b" or sandwich=="t"):
    sandwichSelected=True
print(sandwich)

beverage = input("Would you like a drink, y or n? ")
if(beverage=="y"):
    beverageSelected=True
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

#iteration 3 asking for fries

fries = input("Would you like fench fries, y or no? ")
if(fries=="y"):
    fries = input("Would you like a s for $1, m for $1.50, or l for $2? ")
    friesSelected=True

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

#iteration 4
#if yo do not convert input to int() it will be a sequence or a string
ketchup = int(input("How many ketchup packets would you like? "))*.25
total+=ketchup
#but you could combine the top two lines into one

if(sandwichSelected and beverageSelected and friesSelected):         #and looks for 2 true statements
#if variable==true AND variable==true AND variable==true
    total-=1


#print('Your order is a {0} sandwich, a {1} drink, a {2} fry, and {3} ketchup packet(s) \nfor a total of '.format(sandwich,beverage,fries,ketchup))

print('''
Your order is:
    {0} sandwich,
    {1] drink,
    {2} fries,
    {3} packets
For a total of ${4}
'''.format(sandwich,beverage,fries,ketchup,total))

#print('${:,.2f}'.format(total))    #string"""






#KrustyKrabMenu
total=0
pattySelected=False
beverageSelected=False
sideSelected=False

patty = input("Please pick a krabby entree:Krabby Patty(kb) for $1.25, Double Krabby Patty(dkp) for $2, Triple Krabby Patty(tkp) for $3, Krabby Meal(km) for $3.50, Double Krabby meal(dk) for $3.75, Triple Krabby meal(tk) for $4, Salty Sea Dog(ssd) for $1.25, Footlong(fl) for $2, Sailors Surprise(ss) for $3, Golden Loaf(gl) for $2 ")
if (patty=="kb" or patty=="dkp" or patty=="tkp" or patty=="km" or patty=="dk" or patty=="tk" or patty=="ssd" or patty=="fl" or patty=="ss" or patty=="gl"):
    pattySelected=True
print(patty)

beverage = input("Would you like something to drink? y/n ")
if(beverage=="y"):
    beverageSelected=True
    beverage=input("Kelp Shake for $2 (ks), Seafoam Soda - small for $1(s), medium for $1.25(m), large for $1.50(l) ")
    print("You said ", beverage, "drink")

if patty=="kb":
    total += 1.25
elif patty=="dkp":
    total += 2
elif patty=="tkp":
    total += 3
elif patty=="km":
    total += 3.50
elif patty=="dk":
    total += 3.75
elif patty=="tk":
    total += 4
elif patty=="ssd":
    total += 1.25
elif patty=="fl":
    total += 2
elif patty=="ss":
    total += 3
elif patty=="gl":
    total += 2

if beverage=="ks":
    total += 2
elif beverage=="s":
    total += 1
elif beverage=="m":
    total += 1.25
elif beverage=="l":
    total += 1.50

side = input("Would you like a side? y or n ")
if(side=="y"):
    side = input("Would you like Coral Bits - small for $1(s), medium for $1.25(m), large for $1.50(l) or Kelp Rings for $1.50(kr)? ")
    sideSelected=True

total=total-total*.7


