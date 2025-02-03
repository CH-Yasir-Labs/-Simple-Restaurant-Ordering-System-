#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     30/01/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
menu= {

 'Pasta': 80,
 'Pizza':150,
 'Drink':60,
 'Burger':100,
 'Coffee':100
}
print("Welcome TO Naran Resturent \nPasta: Rs80\nPizza: Rs150\nDrink: Rs60\nBurger:Rs100\nCoffee:Rs100")

price = 0

itm1=input("Enter the name of Item U want to order:\n")
if itm1 in menu:
    price += menu[itm1]
    print(f"Your choice {itm1} is added\n:")
else:
    print("Ivalid Choice")

another=input("Do you want to Add another Item? (Yes/No)")
if another=="Yes":
    itm2=input("Enter the name of your 2nd item:")
    if itm2 in menu:
        price +=menu[itm2]
        print(f"Item {itm2} has been added to order:")

    else:
        print("Invalid Choice")



another2=input("Do you want to Add more Item? (Yes/No)")
if another2 =="Yes":
    itm3=input("Enter the name of your 3rd item:")
    if itm3 in menu:
        price +=menu[itm3]
        print(f"Item {itm3} has been added to order:")
        print(f"Total Bill Is Rs:{price} ")
        print("Thank You For Ordering")
    else:
        print("Invalid Choice")
        print(f"Total Bill Is Rs:{price} ")
        print("Thank You For Ordering")





