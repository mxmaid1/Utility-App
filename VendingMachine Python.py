# code written by Argeo Garcia Locson for assessment 2 Utility APP (intro to programming)
# vending machine dictionary items  
VendingMachine = {
    "ItemRow1": {
        "Doritos": {"Cost": 2.50, "ID": "A1", "Stock": 5},
        "Chocolate Bar": {"Cost": 3.00, "ID": "A2", "Stock": 3},
        "Water": {"Cost": 1.00, "ID": "A3", "Stock": 10},
    },
    "ItemRow2": {
        "Coke": {"Cost": 1.00, "ID": "B1", "Stock": 7},
        "Strawberry Juice": {"Cost": 2.00, "ID": "B2", "Stock": 4},
        "Lemon Juice": {"Cost": 2.00, "ID": "B3", "Stock": 1},
    },
    "ItemRow3": {
        "Choco Pretzels": {"Cost": 2.00, "ID": "C1", "Stock": 8},
        "Choco Cake Snack": {"Cost": 3.50, "ID": "C2", "Stock": 8},
        "Kinders": {"Cost": 1.50, "ID": "C3", "Stock": 8},
    },
}

# function to find item by a ID on vendimg machine dictionary
def FindItem(IDcode):
    for row in VendingMachine.values():
        for item_name, item in row.items():
            if item["ID"].lower() == IDcode.lower():
                return item_name, item["Cost"], item["Stock"]
    return None, None, None

# Item purchasing
def process(IDcode, balance):
    NameOfItem, cost, stock = FindItem(IDcode)  # returns the data of item

    if not NameOfItem:
        print("Item not found. Please check the code and try again.")
        return balance

    if stock == 0:
        print(NameOfItem+" is out of stock.") 
        return balance

    if balance < cost:
        print("Insufficient funds. "+NameOfItem+" costs "+str(cost)+" AED. You have "+str(balance)+" AED Balance.") 
        return balance

    # deduct stocks of the item
    for row in VendingMachine.values():
        try:
            row[NameOfItem]["Stock"] -= 1
            break
        except KeyError:
            continue

    # calculate change then dispensation of item
    change = balance - cost
    print("Dispensing "+ NameOfItem+ ". Your Balance is " +str(change)+" AED.") 

    # suggesting an item to pair purchased item
    suggest_item(NameOfItem)

    return change

# suggestion function for an item 
def suggest_item(PurchasedItem):
    if PurchasedItem == "Chocolate Bar":
        if VendingMachine["ItemRow3"]["Choco Cake Snack"]["Stock"]>0: # dont suggest when out of stock
            print("Buy Choco Cake Snack to pair with your Chocolate Bar? (Code: C2)")
    elif PurchasedItem == "Doritos":
        if VendingMachine["ItemRow2"]["Coke"]["Stock"]>0:
            print("Buy Coke to pair with your Doritos? (Code: B1)")

# vending machine system
def system():
    print("Welcome to the Vending Machine!")
    print("These are the Available Items:")
    for row in VendingMachine.values():
        for item_name, item in row.items():
            print(item_name+" (Code: "+item["ID"]+", Price: "+str(item["Cost"])+" AED, Stock: "+str(item["Stock"])+")")
    balance = 0
    
    try:
        balance = float(input("Insert money: "))
    except ValueError:
        print("\nError. Please enter a valid amount.\n")
        return system()

    while True:
        print("Please Enter the ID of the item you want to purchase, or Enter exit to finish, or Enter itemcheck to check vending machine's items again:")
        user_input = input()
        if user_input.lower() == "exit":
            print("Transaction complete. Returning "+str(balance)+" Balance.")  
            break
        elif user_input.lower() == "itemcheck":
            print("\n")
            for row in VendingMachine.values():
                for item_name, item in row.items():
                    print(item_name+" (Code: "+item["ID"]+", Price: "+str(item["Cost"])+" AED, Stock: "+str(item["Stock"])+")")
        else:
            balance = process(user_input, balance)

system()