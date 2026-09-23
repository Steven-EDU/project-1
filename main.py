"""
    First Project -- main.py

    Steven, Salma, Ethil

    
"""
#  C:\Users\necro\.local\bin\python3.14.exe "d:/Working/VS Code Project Files/Project_1/main.py"
# Test

#Setting Variables
total: float = 0
is_Shopping = True
is_Choosing = True
shop_category = 0

# Dictionary price
Shop = {
    "Snacks": {"Chips": 2.50, "Cookies": 3.20,"Pretzels": 2.48},
    "Food":  {"Milk": 2.87,"Bread": 1.82,"Eggs": 3.89},
    "Drinks": {"Water": 1.00, "Juice": 1.50, "Soda": 2.15},
    "Lottery_Ticket": {"$10 Ticket": 10.0, "$100 Ticket": 100.0}
}
menu = ["[1] Food","[2] Snacks", "[3] Drinks", "[4] Lottery Ticket."]


#Code For Entering Shop
print("Welcome to Slow Way!")

while is_Shopping:
    print("What can i help you with?\n")
    #Print Menu + Let User Choose



    while True:
        for option in menu:
            print(option)
        user_category = input("Type the number of the item you want here:")
        

        if user_category == "1":
            shop_category = Shop.get("Food")
            break

        elif  user_category == "2":
            shop_category = Shop.get("Snacks")
            break

        elif  user_category == "3":
            shop_category = Shop.get("Drinks")
            break

        elif  user_category == "4":
            shop_category = Shop.get("Lottery Ticket")
            break
        else:
            print("Try typing that again please!")


    # Display category ITEMS and PRICES
    counter = 0
    while True:
        for item in shop_category:
            counter = counter + 1
            print(f"[{counter}] ${shop_category[item]:.2f} for {item}")
        user_item = int(input("Type the number of the item you want here: "))
        
        if user_item > 0 and user_item <= 4:
            item_price = list(shop_category.values())   # 12.3 dict.values
            user_item -= 1
            break
        else:
            print("Try typing that again please!")





    # Pre-Checkout -- Display total and ask if they desire to shop more
    total += item_price[user_item]
    print(f"Your total is ${total:.2f}")
    print("Would you like to purchase something else? (Yes/No)")
    user_input2 = input("type here: ")
    if user_input2 == "no" or user_input2 == "No":
        print(f"Your total is ${total:.2f}")
        break

print("Complete")





#Code for Checkout
# Should receive a list of items + how many items
# Items to list
# Number to get prices

