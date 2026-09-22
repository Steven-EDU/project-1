"""
    First Project -- main.py

    Steven, Salma, Ethil

    
"""
#                C:\Users\necro\.local\bin\python3.14.exe "d:/Working/VS Code Project Files/Project_1/main.py"
#Beginning Variables
#Eventually swap to "dictionaries"
#Code For Entering Shop
print("Welcome to Slow Way!")
print("What can i help you with?\n")
menu = ["[1] Food","[2] Snacks", "[3] Drinks", "[4] Lottery Ticket."]
for option in menu :
    print (option)
user_category = input("type here:")


total: float = 0


is_Shopping = True
# Dictionary price
Shop = {"Chips": 2.50, "Cookies": 3.20,"Pretzels": 2.48,"Milk": 2.87,"Bread": 1.82,"Eggs": 3.89,"$10 Ticket": 10.0,"$100 Ticket": 100}
Snacks= ["Chips", "Cookies", "Pretzels"]
Food = ["Milk", "Bread", "Eggs"]
Drinks = ["Water, Juice, Soda"]
lottery_ticket= ["$10 Ticket", "$100 Ticket"]

if user_category == "1" or user_category == "Food":
    print(Food)

elif  user_category == "2" or user_category == "Snacks":
    print(Snacks)

elif  user_category == "3" or user_category == "Drinks":
    print(Drinks)

elif  user_category == "4" or user_category == "Lottery Ticket":
    print(lottery_ticket)
else:
    print("Try typing that again please!")

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




categories = ["Food", "Snacks", "Drinks", "Lottery Ticket"]




#Code for Shopping



# while is_Shopping:
# """ The whole loop for shopping/decision making for the user """
#     if var == 1
#         # Food
#     elif var == 2
#         # Snacks
#     elif var == 3
#         # Drinks
#         print("What type of drink would you like?")
#         varTemp = input("[1] Drink")
#     else:
#         print("That's not an option. Try again:")

#Code for Checkout
# Should receive a list of items + how many items
# Items to list
# Number to get prices

