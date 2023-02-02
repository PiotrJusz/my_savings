import sqlite3

# open databese from file
try:
    db = sqlite3.connect("data/database.db")
    cursor = db.cursor()
    try:
        db.execute(""" CREATE TABLE financial_operations(id integer PRIMARY KEY, type char, description TEXT, amount real NOT NULL) """)
    except:
        print("Can't create main table in database.")
        print("Table probably exist.")
except Exception:
    print("Something's wrong.\nCan't create or open database.\nEnd of program.")
    exit()

def add_category():
    # add a category to the database
    # request the name and type of category
    category_name = input("Enter the name of category: ")
    category_type = input("Type of category:\nP - profit type,\nL - loss type\nType: ")

    # depends of category tape - create a new category in proper database
    # cursor.execute(""" """)
    if category_type.upper() == "P":
        pass
    elif category_type.upper() == "L":
        pass

# display welcome mesage
print("""\nHello in 'My Savings' console program.
This Application using Mysql database.
All data are store in file.
Happy savings through Your life.\n""")

while True:
    # display main menu
    print("""Main menu.
    1 - add new income,
    2 - add new cost,
    3 - add new categories
    10 - display ...,
    0 - save and exit.""")
    menu_option = input("Enter the number of activity: ")

    if menu_option == "1":
        pass

    elif menu_option == "2":
        pass

    elif menu_option == "3":
        # add new categories for income or cost
        add_category()

    elif menu_option == "10":
        pass
    
    if menu_option == "0":
        # save changes in database and close program
        # save databese     
        db.commit()
        db.close()
        print("Save and exit. Thank you.")
        exit()

    else:
        # entered number isn't correct
        print("\nEnter the activity number located on the left side of the menu\nor enter 0 to end the program.")