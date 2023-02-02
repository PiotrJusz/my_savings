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
                pass
            else:
                # decision is yes
                pass

def list_all_tables():
    # Getting all tables from sqlite_master
    sql_query = """SELECT name FROM sqlite_master
    WHERE type='table';"""

    # Creating cursor object using connection object        #%%cursor = sqliteConnection.cursor()
    
    # executing our sql query
    cursor.execute(sql_query)
    print("List of tables\n")
    
    # printing all tables list
    print(cursor.fetchall())

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
        list_all_tables()
        db.commit()
        db.close()
        print("Save and exit. Thank you.")
        exit()

    else:
        # entered number isn't correct
        print("\nEnter the activity number located on the left side of the menu\nor enter 0 to end the program.")