import sqlite3
import datetime
import matplotlib.pyplot as plt
from pylab import plot, show, legend, title, xlabel, ylabel, axis
import budget_chart_horizontal_package as bch

# lenght of description used at creating table for display
lenght = {"id":5, "date_of_operation":10, "type":4, "category":25, "description": 40, "amount":10}

# open databese from file
try:
    db = sqlite3.connect("data/database.db")
    cursor = db.cursor()
    try:
        db.execute(""" CREATE TABLE financial_operations(id integer PRIMARY KEY, date_of_operation text, type char, category text, description TEXT, amount real NOT NULL) """)
        db.execute(""" CREATE TABLE a_set_of_categories(id integer PRIMARY KEY, genre TEXT NOT NULL UNIQUE)""")
    except:
        print("Can't create main table in database.")
        print("Table probably exist.")
except Exception:
    print("Something's wrong.\nCan't create or open database.\nEnd of program.")
    exit()

# creating or adding category to database stored category
def add_category():
    while True:
        # add a category to the database
        # request the name and type of category
        # category name is list type - then is a agument in searching in database
        category_name = []
        print("Add a category. Enter '0'(zero) to interapt and back to main menu. ")
        category_name.append( input("Enter the name of category: ") )
        if category_name == "0":
            # back to main menu - user interapt adding category
            break
        else:
            try:
                # adding categ""ory to database
                db.execute(""" SELECT genre from a_set_of_categories""")
                cursor.execute(""" INSERT INTO a_set_of_categories(genre) VALUES (?) """, ( category_name ) )
                print("Category: {} added to database.".format(category_name))
                break
            except Exception as e:
                print(repr(e)) 
                # this name exist in database
                # request to fix or end adding new category
                print( "This category:{} already exist.".format(category_name) )
                decision = input("Try again? yes/no ").lower()
                if decision == "no":
                    break
                elif decision != "yes" and decision != "no":
                    print("Back to main menu.")
                    break
        # save changes to database
        save()
            

def get_all_categories():
    # read all categories from a_set_of_categories table and retyrn it as a array
    all_categories = []
    db.execute( """ SELECT genre FROM a_set_of_categories """)
    temp_data = cursor.execute(""" SELECT genre FROM a_set_of_categories""")
    for record in temp_data:
        #print("Record: ", record[0])
        all_categories.append(record[0])
    # print("Test for get_all_categories function:")
    # print("all_categories: ", type(all_categories) )
    # print("all_categories: ", all_categories)
    # input()
    return all_categories

def get_current_day():
    # get date from system and return as string
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d")
    return current_time

def add_new_category(new_category):
    # adding new category in other menu than add category from main menu
    try:
        # adding category to database
        # "cast string into []"
        new_list = []
        new_list.append(new_category)
        db.execute(""" INSERT INTO a_set_of_categories(genre) VALUES (?) """, ( new_list ) )
        print("Category: {} added to database.".format(new_list[0]))
    except Exception as e:
        # print(repr(e)) 
        # this name exist in database
        # request to fix or end adding new category
        print(e,":",new_list)
        print( "Something's wrong. Program will be closed shortly" )
        exit()
    # save changes to database
    save()

def add_operation(type_of_transaction):
    # request category
    if type_of_transaction == "P":
        print("Add new profit operation:")
    else:
        print("Add new loss operation:")

    # request date or put current date
    while True:
        date_of = input("Enter the day of operation in format YYYY-MM-DD\nor put enter for current date " + get_current_day() + ": ")
        if date_of == "":
            date_of = get_current_day()
            break
        else:
        # checking correct data entry
            try:
                date_object = datetime.datetime.strptime(date_of, '%Y-%m-%d').date()
                break
            except Exception as e:
                print("Exception: ",e)
                print("Enter date of operation in format: YYYY-M-D.")

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
        
        category= input("\nCategory: ")
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
            decision_3 = input("Add a new category: " + category+" (yes/no): ")
            if decision_3.lower() == "yes":
                add_new_category(category)
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
    if type_of_transaction == "L":
        print("\nOperation: LOSS.")
    elif type_of_transaction == "P":
        print("\nOperation: PROFIT.")
    print(F"Category: {category}\tDescription: {description}\tAmount: \t{amount}")

    # request confirm or reject operation
    while True:
        decision_1 = input("Add operation? (yes, no): ")
        if decision_1.lower() == "yes":
            # save the operation
            print("Your operation will be save.")
            print(F"{type_of_transaction}\t{amount}\t{description}")
            # db.execute(""" CREATE TABLE financial_operations(id integer PRIMARY KEY, type char, description TEXT, amount real NOT NULL) """)
            # cursor.execute(""" INSERT INTO ebookstore(ID, TITLE, AUTHOR, QTY) VALUES (?,?,?,?)""", (id, title, author, qty))
            db.execute(""" INSERT INTO financial_operations(type, date_of_operation, category, description, amount ) VALUES (?, ?, ?, ?, ?) """, (type_of_transaction, date_of, category, description, amount) )

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
    # save changes in database
    save()


def print_data(data_):
    # display header
    print("+"+lenght["id"] * "-" + "+" + lenght["date_of_operation"] * "-" + "+" + lenght["type"] * "-" + "+" +lenght["category"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
    print("|no" + ( lenght["id"] - len("no") )* " "+ "|date" + ( lenght["date_of_operation"] - len("date") )* " " + "|type" + ( lenght["type"] - len("type") )  * " " + "|category" + ( lenght["category"] - len("category")) * " "  + "|description" + ( lenght["description"] - len("description") ) * " " + "|amount" + ( lenght["amount"] - len("amount") ) * " " + "|" )
    print("+"+lenght["id"] * "-" + "+" + lenght["date_of_operation"] * "-" + "+" + lenght["type"] * "-" + "+" +lenght["category"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
    for row in data_:
            print(F"|{row[0]} " + ( lenght["id"] - len(str( row[0] ) ) - 1)* " " + F"|{row[1]}" + ( lenght["date_of_operation"] - len(str( row[1] )) )  * " " +F"|{row[2]}" + ( lenght["type"] - len(str( row[2] )) )  * " " + F"|{row[3]}" + ( lenght["category"] - len(str( row[3]) ) ) * " "  + F"|{row[4]}" + ( lenght["description"] - len(str( row[4]) ) ) * " " +F"|{row[5]}" + ( lenght["amount"] - len(str( row[5] )) ) * " " + "|" ) # - 1 of " "
            #print(F"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")
            # print("+"+lenght["id"] * "-" + "+" + lenght["type"] * "-" + "+" + lenght["description"] * "-" + "+" + lenght["amount"] * "-" + "+")
            print("+"+lenght["id"] * "-" + "+" + lenght["date_of_operation"] * "-" + "+" + lenght["type"] * "-" + "+" +lenght["category"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
    input("Press enter to continue.")
    print()

def print_data_for_continue(data_):
    # display header
    print("+"+lenght["id"] * "-" + "+" + lenght["date_of_operation"] * "-" + "+" + lenght["type"] * "-" + "+" +lenght["category"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
    print("|no" + ( lenght["id"] - len("no") )* " "+ "|date" + ( lenght["date_of_operation"] - len("date") )* " " + "|type" + ( lenght["type"] - len("type") )  * " " + "|category" + ( lenght["category"] - len("category")) * " "  + "|description" + ( lenght["description"] - len("description") ) * " " + "|amount" + ( lenght["amount"] - len("amount") ) * " " + "|" )
    print("+"+lenght["id"] * "-" + "+" + lenght["date_of_operation"] * "-" + "+" + lenght["type"] * "-" + "+" +lenght["category"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
    for row in data_:
            print(F"|{row[0]} " + ( lenght["id"] - len(str( row[0] ) ) - 1)* " " + F"|{row[1]}" + ( lenght["date_of_operation"] - len(str( row[1] )) )  * " " +F"|{row[2]}" + ( lenght["type"] - len(str( row[2] )) )  * " " + F"|{row[3]}" + ( lenght["category"] - len(str( row[3]) ) ) * " "  + F"|{row[4]}" + ( lenght["description"] - len(str( row[4]) ) ) * " " +F"|{row[5]}" + ( lenght["amount"] - len(str( row[5] )) ) * " " + "|" ) # - 1 of " "
            #print(F"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")
            # print("+"+lenght["id"] * "-" + "+" + lenght["type"] * "-" + "+" + lenght["description"] * "-" + "+" + lenght["amount"] * "-" + "+")
            print("+"+lenght["id"] * "-" + "+" + lenght["date_of_operation"] * "-" + "+" + lenght["type"] * "-" + "+" +lenght["category"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")


def display_summary(type_of_transaction):
    # display transaction by print_data function
    if type_of_transaction == "LP": # gather data for all operations and display them
        db.execute(""" SELECT id, date_of_operation, type,  category, description, amount FROM financial_operations """)
        print_data_for_continue( cursor.execute(""" SELECT id, date_of_operation, type, category,  description, amount from financial_operations  """) )
    else:   # gather data for operations depend from a type_of_transaction and diplay them
        db.execute(""" SELECT id, date_of_operation, type,  category, description, amount FROM financial_operations WHERE type = ?""", (type_of_transaction))
        print_data_for_continue( cursor.execute(""" SELECT id, date_of_operation, type, category,  description, amount from financial_operations  WHERE type = ?""", (type_of_transaction)) )

    # variable used for store sum of profits and losses
    profit_record = []
    loss_record = []

    # count sum of profits operations and store it in variable called profit_record
    db.execute(""" SELECT  SUM(amount) FROM financial_operations WHERE type = ? """, ("P",))
    data_profit = cursor.execute(""" SELECT  SUM(amount) FROM financial_operations WHERE type is 'P' """)
    for profit_record in data_profit:
        profit_record = profit_record

    # count sum of losses operations and store it in variable called loss_record
    db.execute(""" SELECT  SUM(amount) FROM financial_operations WHERE type = ? """,("L",))
    data_loss = cursor.execute(""" SELECT  SUM(amount) FROM financial_operations WHERE type is 'L' """)
    for loss_record in data_loss:
        loss_record = loss_record

    # if database is empty do nothing
    if profit_record[0] != None:
        if type_of_transaction == "P":  # collect all amount from profit-type operation 
            # print table with sum of profit operations
            print_table_sum(profit_record, "Sum of profits:")   
            # print("Sum is: ", profit_record)
    if loss_record[0] != None:
        if (type_of_transaction == "L"):   # collect all Loss amount
            # display result
            # print table with lsum of osses operations 
            print_table_sum(loss_record, "Sum of losses:")
            # print("Sum is: ", loss_record)
    if profit_record[0] != None and loss_record[0] != None:
        if type_of_transaction == "LP": # print sum Profit and Loss operation
            print_table_sum(profit_record, "Sum of profits:")  
            print_table_sum(loss_record, "Sum of losses:")
            profit_loss = []
            profit_loss.append(profit_record [0]- loss_record[0])
            print_table_sum(profit_loss, "profit / loss:")
            # print("Profits: ", profit_record, end = "")
            # print("\tLosses: ", loss_record)
    if type_of_transaction == "LP" and profit_record[0] == None and loss_record[0] != None: # display only losses
        print_table_sum(loss_record, "Sum of losses:")
    elif type_of_transaction == "LP" and profit_record[0] != None and loss_record[0] == None: # display only profits
        print_table_sum(profit_record, "Sum of profit:")

def print_table_sum(data_, text_in):    # print bottom table for sum
    # print("|" + ( (lenght["id"] + lenght["date_of_operation"] + lenght["type"] + lenght["category"]) * " " ) + 3 * " " + "|" + text_in + ( (lenght["description"] - len(text_in)) * " ") + "|" + str(data_[0]) + (lenght["amount"] - len(str(data_[0])) ) * " " + "|")
    # print("+"+lenght["id"] * "-" + "+" + lenght["date_of_operation"] * "-" + "+" + lenght["type"] * "-" + "+" +lenght["category"] * "-" + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
    # version 2
    # print("TEST:\ntype of data_: ",type(data_))
    # print("Test:\ndata_ = ", data_)
    if data_[0] != None:
        print(" " + ( (lenght["id"] + lenght["date_of_operation"] + lenght["type"] + lenght["category"]) * " " ) + 3 * " " + "|" + text_in + ( (lenght["description"] - len(text_in)) * " ") + "|" + str( round(data_[0], 2) ) + ( (lenght["amount"] - len( str( round(data_[0], 2))) ) * " " )  + "|") 
        print(" "+lenght["id"] * " " + " " + lenght["date_of_operation"] * " " + " " + lenght["type"] * " " + " " +lenght["category"] * " " + "+" + lenght["description"]* "-" + "+" + lenght["amount"] * "-" + "+")
        

    
      
        #db.execute(""" SELECT id, date_of_operation, type,  category, description, amount FROM financial_operations """)
        #print_data( cursor.execute(""" SELECT id, date_of_operation, type, category,  description, amount from financial_operations  """) )
        #db.execute(""" SELECT  SUM(amount) FROM finacial_operation WHEN category is "P" """)
        #profit_summary = db.execute(""" SELECT  SUM(amount) FROM finacial_operation WHEN category is "P" """)
        #loss_summary = db.execute(""" SELECT  SUM(amount) FROM finacial_operation WHEN category is "L" """)

def rename_category():
    # display all categories
    list_of_categories = []
    list_of_categories = get_all_categories()
    print("Categories already used in:")
    if list_of_categories == None:
        print("There aren't any categories.")
    else:
        for item_category in list_of_categories:
            print(item_category, end = "")
            if item_category == list_of_categories[-1]:
                print("")   # go to next line
            else:
                print(", ", end = "")

        # request to enter category which names will be change
        rename_category = input("Enter the name of category which names you want change: ")
        if rename_category in list_of_categories:
            new_category_name = input(F"Enter the new name for {rename_category}: ")

            categories = []
            categories.append(new_category_name)
            categories.append(rename_category)

            # add new_category_name if not exist in database
            list_of_categories = get_all_categories()
            if new_category_name is not list_of_categories: 
                print(new_category_name," added to database.")
                add_new_category(new_category_name)

            # rename category's name
            try:

                # id integer PRIMARY KEY, date_of_operation text, type char, category text, description TEXT, amount real NOT NULL) """)
                db.execute(""" SELECT id, genre from a_set_of_categories WHERE genre = ?""",(categories[0][1]))
                cursor.execute("""UPDATE a_set_of_categories SET genre = ? WHERE genre = ?""",(categories))
                # update financial_operation database
                db.execute(""" SELECT  id, category from financial_operations where category = ?""",(categories[0][1]))
                cursor.execute(""" UPDATE financial_operations SET category = ? WHERE category = ?""", (categories))
                print("Category's name is changed.")
            except Exception as e:
                print(e)
                print(new_category_name + " already exist.")
                # print("categories: ", categories)
        else:
            print("This category not exist.")

def save():
    db.commit()

def save_and_exit():
    # save changes in database and close program
    # save databese   
    # list_all_cetegories()
    db.commit()
    db.close()
    print("Save and exit. Thank you.")
    exit()      

def collect_data_for_create_graph(type_of_transaction):
    """ type_of_transaction = LP for Losses and Profits,
        type_of_transaction = L for only losses,
        type_of_transaction = P for only profits
    """
    """
    graph for year (months from 1 to 12)
    every month is a sum of all profits or losses
    """
    months = [] # list of months from 1 -12
    months = range(1,13)
    profit_record = []
    loss_record = []

    # extraction data from database
    if (type_of_transaction == "LP" or type_of_transaction == "L"):
        # colecting data for 'L' transaction
        db.execute(""" SELECT  SUM(amount) FROM financial_operations WHERE type = ? """,("L",))
        data_loss = cursor.execute(""" SELECT  SUM(amount) FROM financial_operations WHERE type is 'L' """)
        for record in data_loss:
            amount_2 = float(record[0])
            


        

    
    if (type_of_transaction == "LP" or type_of_transaction == "P"):
        # colecting data for 'P' transaction
        db.execute(""" SELECT  SUM(amount) FROM financial_operations WHERE type = ? """,("P",))
        data_profit = cursor.execute(""" SELECT  SUM(amount) FROM financial_operations WHERE type is 'P' """)
        for record in data_profit:
            # profit_record.append(["Profits", record[0]])
            amount_1 = float(record[0])


    

    # creating data for chart - horizontal
    # [name of account, sum]
    #
    profit_record.append("Profits")
    profit_record.append(amount_1)
    loss_record.append("Losses")
    loss_record.append(amount_2)
    chart_data = []
    chart_data.append(profit_record)
    chart_data.append(loss_record)
    bch.create_graph_chart(chart_data)
    

    # create graph
    """
    x_numbers = [1, 2, 3]
    y_numbers = [2, 4, 6]
    plt.plot(x_numbers, y_numbers,marker = "+")
    legend(["X"],["Y"])
    title("Plot")
    xlabel("xlabel")
    ylabel("ylabel")
    axis([0,4,1,7])

    plt.savefig("plot.png")
    plt.show()
    """
# extract data from cursor.execute

def extract_data(data_, number_of_columns):
    extracted_data = []
    temp_extracted_data = []
    for record in data_:
        # test: print("record: ", record)
        extracted_data.append(record[number_of_columns])
    # print("extractrd_data: ", extracted_data)
    # print(extracted_data[0])
    # test: input()
    

    # return list [record1, record1,...] if numbers_of_column == 1 and list [[record1], [record2], ...] if numbers_of_columns > 1
    return extracted_data



def edit_operation():
    # edit one operation by ID
    while True:
        id_of_operation = input("Enter the unique number of operation for edit.\nTo exit to main menu enter '0',\nTo display all operation enter 'all',\nEnter the action: ")
        if id_of_operation == "0":
            # back to main menu
            break
        elif id_of_operation.lower() == "all":
            # display all operation
            display_summary("LP")
            # pass
        else:
            # received number of operation to edit
            # or random text
            # read database to get unique ID
            all_IDs = [] # stored all ids extracted from ids
            ids = [] # stored all id's from database
            db.execute(""" SELECT * from financial_operations""")
            ids = cursor.execute(""" SELECT id, amount FROM financial_operations WHERE id > 0""")            
            all_IDs = extract_data(ids, 0) # 0 0  - extract only numbers of id from database
            try:
                if int(id_of_operation) in  all_IDs:
                    # break
                    # edit operation here
                    # db.execute(""" SELECT * from financial_operations""")
                    operation = []
                    # print("operation_data: ", operation_data)
                    option = input("""Edit menu:
                    31 - change date,
                    32 - change type,
                    33 - change category,
                    34 - change description,
                    35 - change amount,
                    36 - delete operation,
                    0 - back to main menu
                    Your choice: 
                    """)
                    if option == "0":
                        break
                    if option == "31":
                        update_one_col_in_record(1, id_of_operation)
                    if option == "32": # edit type
                        update_one_col_in_record(2, id_of_operation)
                    if option == "33":
                        update_one_col_in_record(3, id_of_operation)
                    if option == "34": # edit description
                        update_one_col_in_record(4, id_of_operation)
                    if option == "35":
                        update_one_col_in_record(5, id_of_operation)
                        
                        
                    if option == "36":
                        # delete operation
                        ask = input(F"Deleting operation with id {id_of_operation}.\nAre You sure? (yes/no): ")
                        if ask.lower() == "yes":
                             cursor.execute("DELETE FROM financial_operations WHERE id = ?",(id_of_operation,))
                             print("Entered record was deleted.")

                    save()
                    


                else:
                    print("Unfortunately, there are no operations at this number. Try again.")
            except ValueError:
                print("Something's wrong. Try again.")


def check_is_datatype(datatype, question):
    while True:
        # float temp_data
        temp_data = 0.00
        if datatype == "float":
            try:
                temp_data = round (float(input(question)), 2)
                break
            except ValueError:
                print("Something's wrong. Try again. Enter properly value.")

        if datatype == "type_of_operation": # for "L" or "P"
            while True:
                temp_data = input(question)
                temp_data = temp_data.upper()
                # test: print("temp_data: ", temp_data)
                # test: input("Enter to continue...")
                if temp_data == "L" or temp_data == "P":
                    break
            break

        if datatype == "string":
            temp_data = input(question)
            break

        if datatype == "date":
            while True:
                # check date in datatype
                try:
                    temp_data = input(question)
                    date_object = datetime.datetime.strptime(temp_data, '%Y-%m-%d').date()
                    break
                except Exception as e:
                    print("Exception: ",e)
                    print("Enter date of operation in format: YYYY-M-D.")
            
            break

    return temp_data   


def update_one_col_in_record(num_of_column, id_of_operation):
    
    # access to database to display edited operation
    db.execute(""" SELECT * FROM financial_operations WHERE id = ? """,(id_of_operation,))
    operation = cursor.execute(""" SELECT * FROM financial_operations WHERE id = ? """,(id_of_operation,))
    print_data(operation)

    # prepairng for extraction data or one column from record
    operation_data = ""
    db.execute(""" SELECT * FROM financial_operations WHERE id = ? """,(id_of_operation,))
    operation = cursor.execute(""" SELECT * FROM financial_operations WHERE id = ? """,(id_of_operation,))

    if num_of_column == 0:  # id
        # extract data from operation
        operation_data = extract_data(operation, num_of_column)
        print("Current id: ",operation_data[0])
        temp_column = check_is_datatype ("integer", "New id: ")

        # update
        # access to database to update amount
        # update database - change amount
        db.execute(""" SELECT * FROM financial_operations WHERE id = ? """,(id_of_operation,))
        operation = cursor.execute(""" Update  financial_operations SET id = ? WHERE id = ? """,(temp_column,  id_of_operation,))
    elif num_of_column == 1:    # edit date
         # extract data from operation
        operation_data = extract_data(operation, num_of_column)
        print("Current date: ",operation_data[0])
        temp_column = check_is_datatype ("date", "New date: ")

        # update
        # access to database to update description
        # update database - change description
        db.execute(""" SELECT * FROM financial_operations WHERE id = ? """,(id_of_operation,))
        operation = cursor.execute(""" Update  financial_operations SET date_of_operation = ? WHERE id = ? """,(temp_column,  id_of_operation,))
    elif num_of_column == 2:    # edit type of operation
        # extract data from operation
        operation_data = extract_data(operation, num_of_column)
        print("Current type: ",operation_data[0])
        temp_column = check_is_datatype ("type_of_operation", "New type of operation: ")

        # update
        # access to database to update operation
        # update database - change operation
        db.execute(""" SELECT * FROM financial_operations WHERE id = ? """,(id_of_operation,))
        operation = cursor.execute(""" Update  financial_operations SET type = ? WHERE id = ? """,(temp_column,  id_of_operation,))
    elif num_of_column == 3:    # edit category
        # extract data from operation
        operation_data = extract_data(operation, num_of_column)
        print("Current category: ",operation_data[0])
        temp_column = check_is_datatype ("string", "Assign to category: ")

        # add edited category if not exisyt indatabase
        list_of_categories = get_all_categories()
        if temp_column is not list_of_categories: 
                print(temp_column," added to database.")
                add_new_category(temp_column)
        # update
        # access to database to update category
        # update database - change category
        db.execute(""" SELECT * FROM financial_operations WHERE id = ? """,(id_of_operation,))
        operation = cursor.execute(""" Update  financial_operations SET category = ? WHERE id = ? """,(temp_column,  id_of_operation,))
    elif num_of_column == 4:    # edit description
        # extract data from operation
        operation_data = extract_data(operation, num_of_column)
        print("Current description: ",operation_data[0])
        temp_column = check_is_datatype ("string", "New description: ")

        # update
        # access to database to update description
        # update database - change description
        db.execute(""" SELECT * FROM financial_operations WHERE id = ? """,(id_of_operation,))
        operation = cursor.execute(""" Update  financial_operations SET description = ? WHERE id = ? """,(temp_column,  id_of_operation,))
    elif num_of_column == 5:    # edit  amount
        # extract data from operation
        operation_data = extract_data(operation, num_of_column)
        print("Current category: ",operation_data[0])
        temp_column = check_is_datatype ("float", "New amount: ")

        # update
        # access to database to update amount
        # update database - change amount
        db.execute(""" SELECT * FROM financial_operations WHERE id = ? """,(id_of_operation,))
        operation = cursor.execute(""" Update  financial_operations SET amount = ? WHERE id = ? """,(temp_column,  id_of_operation,))
    else:
        print("Something's wrong. Back to main menu")


    # access to database to update amount
    # update database - change amount
    # db.execute(""" SELECT * FROM financial_operations WHERE id = ? """,(id_of_operation,))
    # operation = cursor.execute(""" Update  financial_operations SET amount = ? WHERE id = ? """,(temp_column,  id_of_operation,))
    save()       

            
            

        
        




# ****************MAIN*********************************@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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
    20 - Rename ...,
    30 - Edit operation by number ID,
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
        while True:
            # menu of accounts summary
            # reqesust action
            decision = input("""\t
            11 - View profit and loss summary with all operations,
            11p - View profit and loss summary with all operations on graph,
            12 - view profit summary with all operations,
            12p - view profit summary with all operations on graph,
            13 - view loss sumary with all operations,
            13p - view loss sumary with all operations on graph,
            1 - back to main menu,
            0 - save and exit:\t""")
            
            if decision == "11":
                # display of summary loss and profit operation
                display_summary("LP")
            elif decision == "12":
                # display of summary loss and profit operation
                display_summary("P")
            elif decision == "13":
                # display of summary loss and profit operation
                display_summary("L")

            # graph
            elif decision == "11p":
                # create graph for profits and losses
                collect_data_for_create_graph("LP")

            elif decision == "1": # back to main menu
                break
            elif decision == "0": #s ave and exit
                save_and_exit()
            else:
                print("Enter the properly number of action or '1' to back to main menu.")

    # menu for rename's categoty
    elif menu_option == "20":
        while(True):
            decision = input("""\t\t21 - Rename category,
            \t1 - back to main menu,
            \tEnter the number of activity:\t""")
            
            if decision == "21": # rename category bname here
                # rename categor
                rename_category()

            elif decision == "1":
                print("Back to main menu")
                break
            else:
                print("Enter the properly number of action or '1' to back to main menu.")

    elif menu_option == "30":
        # edit one operation by number ID
        edit_operation()
                


    
    if menu_option == "0":
        save_and_exit()
    else:
        # entered number isn't correct
        print("\nEnter the activity number located on the left side of the menu\nor enter 0 to end the program.")