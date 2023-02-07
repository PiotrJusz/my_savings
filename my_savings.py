import sqlite3

# lenght of description used at creating table for display
lenght = {"id":5, "type":4, "category":15, "description": 30, "amount":10}

# open databese from file
try:
    db = sqlite3.connect("data/database.db")
    cursor = db.cursor()
    try:
        db.execute(""" CREATE TABLE financial_operations(id integer PRIMARY KEY, type char, category text, description TEXT, amount real NOT NULL) """)
        db.execute(""" CREATE TABLE a_set_of_categories(id integer PRIMARY KEY, genre char)""")
    except:
        print("Can't create main table in database.")
        print("Table probably exist.")
except Exception:
    print("Something's wrong.\nCan't create or open database.\nEnd of program.")
    exit()



"""
def add_category():
    while True:
        # add a category to the database
        # request the name and type of category
        category_name = input("Enter the name of category: ")
        #category_type = input("Type of category:\nP - profit type,\nL - loss type\nType: ")

        # depends of category tape - create a new category in proper database
        try:
            #cursor.execute(""" """CREATE TABLE {}(id integer PRIMARY KEY, type char, category text, description TEXT, amount real)""" """.format(category_name))
            break
        except Exception:
            # this name exist in database
            # request to fix or end adding new category
            print( "This category:'{}' already exist.".format(category_name) )
            decision = input("Try again? yes/no ").lower()
            if decision == "no":
                break
            elif decision != "yes" and decision != "no":
                print("Back to main menu.")
                break
"""

# creating or adding category to database stored category
def add_category():
    while True:
        # add a category to the database
        # request the name and type of category
        # category name is list type - then is a agument in searching in database
        category_name = []
        print("Add a  ategory. Enter '0'(zero) to interapt and back to main menu. ")
        category_name.append( input("Enter the name of category: ") )
        if category_name == "0":
            # back to main menu - user interapt adding category
            break
        else:
            try:
                # adding category to database
                db.execute(""" INSERT INTO a_set_of_categories(genre) VALUES (?) """, ( category_name ) )
                print("Category: {} added to database.".format(category_name))
                break
            except Exception as e:
                # print(repr(e)) 
                # this name exist in database
                # request to fix or end adding new category
                print( "This category:'{}' already exist.".format(category_name) )
                decision = input("Try again? yes/no ").lower()
                if decision == "no":
                    break
                elif decision != "yes" and decision != "no":
                    print("Back to main menu.")
                    break
            

"""
def list_all_cetegories():
    # Getting all tables from sqlite_master
    sql_query = """"SELECT name FROM sqlite_master WHERE type='table';""""

    # Creating cursor object using connection object        #%%cursor = sqliteConnection.cursor()
    
    # executing our sql query
    cursor.execute(sql_query)
    
    # printing all categories

    list_of_categories = []
    for item in cursor:
        print( str(item)[2: -3] +", ", end="")
        list_of_categories.append(str(item)[2: -3])

    return list_of_categories
"""


def get_all_categories():
    # read all categories from a_set_of_categories table and retyrn it as a array
    all_categories = []
    db.execute( """ SELECT id, genre FROM a_set_of_categories """)
    temp_data = cursor.execute(""" SELECT genre FROM a_set_of_categories""")
    for record in temp_data:
        #print("Record: ", record[0])
        all_categories.append(record[0])

    type(all_categories)
    return all_categories



def add_operation(type_of_transaction):
    # request category
    if type_of_transaction == "P":
        print("Add new profit operation:")
    else:
        print("Add new loss operation:")
    while True:
        check = False
        # remind categories added previoslu by user
        print("Existing categories: ", end = "")
        list_of_categories = []
        list_of_categories = get_all_categories()
        
        for item in list_of_categories:
            print(item,end="")
            # when item isn't the last one - add coma
            if item != ( list_of_categories[len( list_of_categories ) - 1]):
                print(", ", end="")
            else:
                # go to the next line
                print("")
        
        category= input("Category: ")
        for num in range(0, len(list_of_categories)):
            # print(list_of_categories[num], " - ", category)
            if list_of_categories[num] == category:
                # print(list_of_categories[num], " - ", category)
                check = True
                break

        if check == True:
            break
        else:
            print("Category: {} not exist. Try again. ".format(category))
        
        

        
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
    if type_of_transaction == "L":
        print("\nOperation: LOSS.")
    elif type_of_transaction == "P":
        print("\nOperation: PROFIT.")
    print(F"{category}\t{description}\t{amount}")

    # request confirm or reject operation
    while True:
        decision_1 = input("Add operation? (yes, no): ")
        if decision_1.lower() == "yes":
            # save the operation
            print("Your operation will be save.")
            print(F"{type_of_transaction}\t{amount}\t{description}")
            # db.execute(""" CREATE TABLE financial_operations(id integer PRIMARY KEY, type char, description TEXT, amount real NOT NULL) """)
            # cursor.execute(""" INSERT INTO ebookstore(ID, TITLE, AUTHOR, QTY) VALUES (?,?,?,?)""", (id, title, author, qty))
            db.execute(""" INSERT INTO financial_operations(type, category, description, amount ) VALUES (?, ?, ?, ?) """, (type_of_transaction, category, description, amount) )

            break
        elif decision_1.lower()== "no":
            decision_2 = input("Do you want to improve operations? (yes, no): ")
            if decision_2.lower() == "yes":
                add_operation(type_of_transaction)
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
            print(F"|{row[0]} " + ( lenght["id"] - len(str( row[0] ) ) - 1)* " " + F"|{row[1]}" + ( lenght["type"] - len(str( row[1] )) )  * " " + F"|{row[2]}" + ( lenght["category"] - len(str( row[2]) ) ) * " "  + F"|{row[3]}" + ( lenght["description"] - len(str( row[3]) ) ) * " " +F"|{row[4]}" + ( lenght["amount"] - len(str( row[4] )) ) * " " + "|" ) # - 1 of " "
            #print(F"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")
            # print("+"+lenght["id"] * "-" + "+" + lenght["type"] * "-" + "+" + lenght["description"] * "-" + "+" + lenght["amount"] * "-" + "+")
            print("+"+lenght["id"] * "-" + "+" + lenght["type"] * "-" + "+" +lenght["category"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
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
        # list_all_cetegories()
        db.commit()
        db.close()
        print("Save and exit. Thank you.")
        exit()

    else:
        # entered number isn't correct
        print("\nEnter the activity number located on the left side of the menu\nor enter 0 to end the program.")