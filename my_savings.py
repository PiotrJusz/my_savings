import sqlite3

# lenght of description used at creating table for display
lenght = {"id":5, "type":4, "category":15, "description": 30, "amount":10}

# open databese from file
try:
    db = sqlite3.connect("data/database.db")
    cursor = db.cursor()
    try:
        db.execute(""" CREATE TABLE financial_operations(id integer PRIMARY KEY, type char, category text, description TEXT, amount real NOT NULL) """)
    except:
        print("Can't create main table in database.")
        print("Table probably exist.")
except Exception:
    print("Something's wrong.\nCan't create or open database.\nEnd of program.")
    exit()

def add_category():
    while True:
        # add a category to the database
        # request the name and type of category
        category_name = input("Enter the name of category: ")
        #category_type = input("Type of category:\nP - profit type,\nL - loss type\nType: ")

        # depends of category tape - create a new category in proper database
        try:
            cursor.execute(""" CREATE TABLE {}(id integer PRIMARY KEY, type char, description TEXT, amount real) """.format(category_name))
            break
        except Exception:
            # this name exist in database
            # request to fix or end adding new category
            print( "This category:'{}' already exist.".
            format(category_name) )
            decision = input("Try again? yes/no ").lower()
            if decision == "no":
                break
            elif decision != "yes" and decision != "no":
                print("Back to main menu.")
                break
            

def list_all_cetegories():
    # Getting all tables from sqlite_master
    sql_query = """SELECT name FROM sqlite_master
    WHERE type='table';"""

    # Creating cursor object using connection object        #%%cursor = sqliteConnection.cursor()
    
    # executing our sql query
    cursor.execute(sql_query)
    
    # printing all categories

    list_of_categories = []
    for item in cursor:
        print( str(item)[2: -3] +", ", end="")

def add_operation(type):
    # request category
    while True:
        break
    # request description and amount
    while True:
        # checking lenght of description, lenght is reading from dictionary called lenght
        description = input("Description of operation: ") 
        if len(description) > lenght["description"] :
            print("Description is too long. Make a shorter note, please.")
        else:
            break
    while True:
        try:
            # cast amount to float and round to 2 numbers
            amount = float( input("Amount: ") )
            amount = round(amount, 2)
            break
        except ValueError:
            print("Enter a number.\nFor the decimal part, use '.'.")
    # display operation
    if type == "L":
        print("Operation: LOSS.")
    elif type == "P":
        print("Operation: PROFIT.")
    print(F"{amount}\t{description}")

    # request confirm or reject operation
    while True:
        decision_1 = input("Add operation? (yes, no): ")
        if decision_1.lower() == "yes":
            # save the operation
            print("Your operation will be save.")
            print(F"{type}\t{amount}\t{description}")
            # db.execute(""" CREATE TABLE financial_operations(id integer PRIMARY KEY, type char, description TEXT, amount real NOT NULL) """)
            # cursor.execute(""" INSERT INTO ebookstore(ID, TITLE, AUTHOR, QTY) VALUES (?,?,?,?)""", (id, title, author, qty))
            db.execute(""" INSERT INTO financial_operations(type, description, amount ) VALUES (?, ?, ?) """, (type, description, amount) )

            break
        elif decision_1.lower()== "no":
            decision_2 = input("Do you want to improve operations? (yes, no): ")
            if decision_2.lower() == "yes":
                add_operation(type)
                break
            elif decision_2.lower() == "no":
                break
            else:
                print("Give the correct answer? (yes, no)")

"""
# no category
def print_data(data_):
    # display header
    print("+"+lenght["id"] * "-" + "+" + lenght["type"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
    print("|no" + ( lenght["id"] - len("no") )* " " + "|type" + ( lenght["type"] - len("type") )  * " "  + "|description" + ( lenght["description"] - len("description") ) * " " +"|amount" + ( lenght["amount"] - len("amount") ) * " " + "|" )
    print("+"+lenght["id"] * "-" + "+" + lenght["type"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
    for row in data_:
            print(F"|{row[0]} " + ( lenght["id"] - len(str( row[0] ) ) - 1)* " " + F"|{row[1]}" + ( lenght["type"] - len(str( row[1] )) )  * " "  + F"|{row[2]}" + ( lenght["description"] - len(str( row[2]) ) ) * " " +F"|{row[3]}" + ( lenght["amount"] - len(str( row[3] )) ) * " " + "|" ) # - 1 of " "
            #print(F"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")
            print("+"+lenght["id"] * "-" + "+" + lenght["type"] * "-" + "+" + lenght["description"] * "-" + "+" + lenght["amount"] * "-" + "+")
    input("Press enter to continue.")
    print()
"""

def print_data(data_):
    # display header
    print("+"+lenght["id"] * "-" + "+" + lenght["type"] * "-" + "+" +lenght["category"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
    print("|no" + ( lenght["id"] - len("no") )* " " + "|type" + ( lenght["type"] - len("type") )  * " " + "|category" + ( lenght["category"] - len("category")) * " "  + "|description" + ( lenght["description"] - len("description") ) * " " + "|amount" + ( lenght["amount"] - len("amount") ) * " " + "|" )
    print("+"+lenght["id"] * "-" + "+" + lenght["type"] * "-" + "+" +lenght["category"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
    for row in data_:
            print(F"|{row[0]} " + ( lenght["id"] - len(str( row[0] ) ) - 0)* " " + F"|{row[1]}" + ( lenght["type"] - len(str( row[1] )) )  * " " + F"|{row[2]}" + ( lenght["category"] - len(str( row[2]) ) ) * " "  + F"|{row[3]}" + ( lenght["description"] - len(str( row[3]) ) ) * " " +F"|{row[4]}" + ( lenght["amount"] - len(str( row[4] )) ) * " " + "|" ) # - 0 of " "
            #print(F"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")
            print("+"+lenght["id"] * "-" + "+" + lenght["type"] * "-" + "+" + lenght["description"] * "-" + "+" + lenght["amount"] * "-" + "+")
    input("Press enter to continue.")
    print()

# ****************MAIN*********************************

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
        add_operation("P")

    elif menu_option == "2":
        add_operation("L")


    elif menu_option == "3":
        # add new categories for income or cost
        add_category()

    elif menu_option == "10":
        db.execute(""" SELECT id, type,  category, description, amount FROM financial_operations """)
        print_data( cursor.execute(""" SELECT id, type, category,  description, amount from financial_operations  """) )
    
    if menu_option == "0":
        # save changes in database and close program
        # save databese   
        list_all_cetegories()
        db.commit()
        db.close()
        print("Save and exit. Thank you.")
        exit()

    else:
        # entered number isn't correct
        print("\nEnter the activity number located on the left side of the menu\nor enter 0 to end the program.")