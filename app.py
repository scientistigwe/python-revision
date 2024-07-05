# """
# Life Management System
# """

# Track monthly expenses and categorize them.
def budget_tracker():
    """
    Description:
    
    Args:
    
    Return:
    """
    # Initialize an empty dictionary to store expenses
    expenses = {}

    # Loop to gather expense data from the user
    while True:
        category = input("Enter expense category here or done to exit: ")
        if category.lower() == 'done':
            print("Thank you for entering all expense categories and amounts.")
            break
        try:
            amount = float(input(f"Enter expense amount for {category}: "))
            expenses[category] = amount
        except ValueError as e:
            print(f"Error: You entered wrong value, please enter the correct amount in numbers only!")

    for category, values in expenses.items():
        print(f"{category}: {values}")

    # Calculate total expenses
    total_expenses = sum(expenses.values())
    print(f"Total monthly expense: {total_expenses}")

budget_tracker()
#     CALCULATE total_expenses as the sum of all values in expenses

#     // Display total expenses
#     PRINT "Total monthly expenses: $" + total_expenses

#     // Display each expense category and amount
#     FOR each category, amount in expenses:
#         PRINT category + ": $" + amount

# # Calculate the average grade of students and determine their grade.
# def grade_calculation():
#     """
#     Description:

#     Args:

#     Return:
#     """
#     pass


# # Manage a shopping list where she can add, remove, and view items.
# def shopping_list_manager():
#     """
#     Description:

#     Args:

#     Return:
#     """
#     pass


# def main():
#     track_expenses()
#     grade_calculation()
#     shopping_list_manager()


# if __name__ == '__main__':
#     main()

# Addition function
# def add_numbers(a,b):
#     """
#     Description: This function adds two numbers together.

#     Args: a and b.

#     return: sum of a and b
#     """
#     num_sum = a + b
#     return num_sum

# # Multiplication function
# def mult_numbers(a,b):
#     """
#     Description: This function multiplies two numbers.

#     Args: a and b.

#     Return: product of a and b.
#     """
#     num_mult = a * b
#     return num_mult

# # Subtraction function by Ikenna
# def substr_num(a,b):
#     """
#     Description: Substract a from b
#     Args: a nd b
#     returns: difference between a and b
#     """
#     num_sub = a - b
#     return num_sub


# # Modulo function by Ernest
# def modular(a, b):
#     """
#     Description: This function finds modular of 2 numbers

#     args: a and b

#     return: modular of a and be
#     """
#     num_mod = a % b
#     return num_mod

# # Division function by Henry
# def div_num(a,b):
#     """
#     Description: This function gives us the division between two number

#     args: a and b

#     returns: the division between a and b
#     """
#     num_div = a / b
#     return num_div


# def main():
#     """
#     Description:

#     Args:

#     Return: None 
#     """
#     num1 = 10
#     num2 = 5
#     print(add_numbers(num1, num2))
#     print(substr_num(num1, num2))
#     print(mult_numbers(num1, num2))
#     print(div_num(num1, num2))
#     print(modular(num1, num2))

# if __name__ == '__main__':
#     main()





# #def grade_calculation():
#     #create data structure:

#     #create loop to collect user input

#     #calculate kpis

#     #output/print
# #try:
# #    numbers1 = int(input('Enter number here: '))
# #except ValueError as e:
#     #print(e)
# #    print(f'error:', str(e).split(':')[1])
#     #numbers1 = int(numbers1)
# #    print(numbers1)
#  #   if type(numbers1) != int:
#         #converted_number = int(numbers1)
#         #if type(converted_number) != int:
#   #      print('please enter correct amount in numbers only')

# #    print(type(numbers1))

#     #numbers2 = '123456'

#     #for num in numbers1:
#     #   print(f'Numbers1: {num}')
#     #  print(f'Data type: {type(numbers1)}')

#     #for num in numbers2:
#     #   print(f'Numbers2: {num}')
#     #  print(f'Data type: {type(numbers2)}')
# #numbers2 = int(input('Enter number here: '))

# dtype = [12345, 'abc']
# dictx = {'name': 'Ikenna', 'class': 'codeinstitute'}
# #print(type(dictx))
# dtype2 = tuple(dtype)
# #print(type(dtype2))

# # groceries = 'orange', 'mango', 'spinarch', 'sent leaf'
# # fruits = 'orange', 'mango'
# # vegetables = 'spinarch', 'sent leaf'
# #list(dict)

# expense_per_store = [{'Aldi': ['item1', 'item2', 'item3']}, {'Asda': ['itemA', 'itemB', 'itemC']}, {'Tesco': ['itemX', 'itemY', 'itemZ']}]
# expenses = [{'fruits': ['orange', 'mango'], 'vegetables': ['spinarch', 'sent leaf']}, ['tv', 'radio', 'pillow']]
# print(type(expenses[1]))

# Data ETL