import matplotlib.pyplot as plt


# draw chart of losses in last month

def get_data():
    budget = []

    # request yne number of categories
    number_of_category = int (input("Enter the numbers of categories: "))
    for num in range(0, number_of_category):
        # request the name of every category and value for it and stored in variable called budget
        budget.append([input(F"Enter the name of category no. {num+1}: "), int(input(F"Enter the value: "))])
        # budget[num][1] = input("Enter the value: ")

    budget = sort(budget)
    for elem in budget:
        print(elem)
    return budget

# sort list data_ with second value
def sort(data_):
    temp = []
    for i in range(0, len(data_)):
        for num in range(1, len(data_)):
            if data_[num - 1][1] < data_[num][1]:
                temp = data_[num]
                data_[num] = data_[num - 1]
                data_[num - 1] = temp
    return data_



def get_max(data_):
    max = 0
    for num in range(0 , len(data_)):
        try:
            
            if max < (data_[num][1]):
                
                max = (data_[num][1])
        except IndexError as e:
            print(e)
            print("num: ", num)
            input()
    return max

# get names of categories from date_ - list and stored them in list calles names
def get_names(data_):
    names = []
    for num in range(0, len(data_)):
        names.append(data_[num][0])

    return names

def get_values(data_):
    values = []
    for num in range(0, len(data_)):
        values.append(data_[num][1])

    return values

def create_graph_chart(data_):
    # number of bars
    num_of_bars = len(data_)
    # middle of every chart
    positions = range(1, num_of_bars + 1)
    # x value on axis
    x_axis = range(0, int(get_max(data_)))
    # y axis
    y_axis = get_names(data_)
    plt.bar(positions, get_values(data_), align = "center")

    labels = get_names(data_)
    plt.xticks(positions, labels)

    plt.ylabel("Value in [$]")
    plt.xlabel("Categories")

    plt.title("Monthly expense summary.")

    plt.grid()
    plt.show()



#********MAIN
# request data from user
"""
data = []
data  = get_data()

# create graph
create_graph_chart(data)
"""



