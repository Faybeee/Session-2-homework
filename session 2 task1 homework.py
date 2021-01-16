print("Hello and welcome to Faybee's restaurant")
Drinks = str(input("What would you like to drink?"))
print("Great choice")

Choice1 = str(input("Would you like to order a starter? Yes/No"))
if Choice1 == "Yes":
    Starter = str(input("What would you like for your starter?"))
    Pay1 = 5
else:
    print("No starter, that's fine.")
    Pay1 = 0

Choice2 = str(input("Would you like to order a main course? Yes/No"))
if Choice2 == "Yes":
    Main = str(input("What would you like for your main course?"))
    Pay2 = 10
else:
    print("No main course, that's fine.")
    Pay2 = 0

Choice3 = str(input("Would you like to order dessert? Yes/No"))
if Choice3 == "Yes":
    Starter = str(input("What would you like for your dessert?"))
    Pay3 = 5
else:
    print("No dessert, that's fine")
    Pay3 = 0

Choice4 = str(input("Would you like to order after dinner drinks? Yes/No"))
if Choice4 == "Yes":
    Starter = str(input("What would you like for your after dinner drinks?"))
    Pay4 = 5
else:
    print("No after dinner drinks, that's fine.")
    Pay4 = 0

Bill = int(Pay1 + Pay2 + Pay3 + Pay4)

print ("Thank you for coming to our restaurant, your bill comes to £", Bill, ". Please Pay at the Cashier.")

