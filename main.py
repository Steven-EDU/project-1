"""
    First Project -- main.py

    Steven, Salma, Ethil

    
"""
# test
#  C:\Users\necro\.local\bin\python3.14.exe "d:/Working/VS Code Project Files/Project_1/main.py"
#Beginning Variables
#Eventually swap to "dictionaries"

#Setting Variables
total: float = 0
is_Shopping = True

# Dictionary price
Shop = {
    "Snacks": {"Chips": 2.50, "Cookies": 3.20,"Pretzels": 2.48},
    "Food":  {"Milk": 2.87,"Bread": 1.82,"Eggs": 3.89},
    "Drinks": {"Water": 1.00, "Juice": 1.50, "Soda": 2.15},
    "Lottery_Ticket": {"$10 Ticket": 10.0, "$100 Ticket": 100.0}
}

#Code For Entering Shop
print("Welcome to Slow Way!")
print("What can i help you with?\n")

#Print Menu + Let User Choose
menu = ["[1] Food","[2] Snacks", "[3] Drinks", "[4] Lottery Ticket."]

for option in menu :
    print (option)

user_category = input("type here:")



# Display Items
if user_category == "1" or user_category == "Food":
    chosen = Shop.get("Food")

elif  user_category == "2" or user_category == "Snacks":
    chosen = Shop.get("Snacks")

elif  user_category == "3" or user_category == "Drinks":
    chosen = Shop.get("Drinks")

elif  user_category == "4" or user_category == "Lottery Ticket":
    chosen = Shop.get("Lottery Ticket")
else:
    print("Try typing that again please!")


# Display category items and prices
for item in chosen:
     print(f"${chosen[item]:.2f} for {item}")


text : str = input()
if text in Shop:
    print(f"We do have that item! It's ${Shop[text]:.2f}")
else:
    print("We don't have it")

print("Would you like to purchase something else?")

user_input2 = input("type here:")
if user_input2 == "yes" or user_input2 == "Yes":
    print(total)
else:
    print("What else would you like to purchase?")






#Code for Checkout
# Should receive a list of items + how many items
# Items to list
# Number to get prices

