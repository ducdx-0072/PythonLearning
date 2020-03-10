"""
This is a console app that:
(1) Allows clerks to enter a list of books (including titles and quantities – using a
dictionary) that are available in his/her shop
(2) Allows customers to check whether an item is in stock or not by inputting a title:
just show “N items available” or “Out of stock!” on screen
"""
def printMenu():
    print("1 - Clerk")
    print("2 - Customer")

def convertToInt(str):
    try:
        number = int(str)
        return number
    except ValueError:
        return None

printMenu()
choice = input("Who are you? Select 1 or 2")
list_book = {}
while choice != 'q':
    if choice == '1':
        cont = input("Enter books, y - Yes, n - No:")
        while cont == 'y':  
            name = input("Book's Name: ")
            quantity = input("Book's quantity: ")
            if convertToInt(quantity) != None:
                list_book[name.lower().strip()] = quantity
            else:
                print("You have entered invalid value")
                break
            cont = input("Enter books, y - Yes, n - No:")
    elif choice == '2':
        keyword = input("Input book's name to search: ")
        quan = list_book.get(keyword.lower().strip(),None)
        if  quan == None or quan == '0':
            print("Out of stock")
        else:
            print(list_book.get(keyword.lower().strip(),None),"items available")
    else:
        print("Your select is invalid")
    choice = input("Who are you? Select 1 or 2: ")
