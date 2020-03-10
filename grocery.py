"""
This is a console app that: 
(1) Allows warehouse employees to enter a list of goods (including names only - using
a string separated by commas) that are available in his/her shop
(2) Allows customers to check whether an item is in stock or not by inputting a name:
just show “Available” or “Out of stock!” on screen
"""
def printMenu():
    print("1 - WareHouse")
    print("2 - Customer")

list_good = []
printMenu()
choice = input("Who are you? Select 1 or 2: ")
while choice != 'q':
    if choice == '1':
        goods = input("Input list of goods, separated by commas: ")
        list_good = goods.split(",")
        list_good = list(map(lambda name: name.lower(), list_good))
    elif choice == '2':
        keyword = input("Input keyword to search: ")
        if keyword.lower() in list_good:
            print("Available")
        else:
            print("Out of stock")
        printMenu
    else:
        print("Your select is invalid")
    choice = input("Who are you? Select 1 or 2: ")