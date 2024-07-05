#
import numpy as np
import pandas as pd

name = input("Enter name: ")
age = input("Enter age: ")

def validate_recieved_data(name, age):
    if not isinstance(name, str) or pd.isna(name):
        print('Please enter correct name.')
    elif not age.isdigit():
        print('Please enter correct age.')
    else:
        age = int(age)
        print("Entered name: %s and age: %d are of the right data types: %s & %s respectively" % (name, age, type(name), type(age)))

validate_recieved_data(name, age)

def write_js_file(name, age):
    with open(file_path, "w") as js_file:
        js_file.write("""
        document.addEventListener("DomContentLoaded", function(){
               
        })

""")
Project: Daily Life Organizer for ABC Inc.
Client: ABC Inc.

Project Overview: ABC Inc. wants to develop a Daily Life Organizer to help employees manage their daily tasks more efficiently. The solution should include functionalities for task management, expense tracking, fitness activity logging, and daily journal keeping. Each function should be simple to use and integrate seamlessly into the overall system.

Scenario and Tasks
1. Task Management

Scenario: Employees at ABC Inc. often have numerous tasks and deadlines to keep track of. A system is needed to help them organize and prioritize these tasks effectively.

Task:

Develop a function that allows employees to add tasks with a description and due date.
The function should store each task in a list and provide feedback to the user that the task has been added successfully.
2. Expense Tracking

Scenario: Employees frequently incur expenses for meals, transportation, and office supplies. Keeping track of these expenses is important for personal budgeting and reimbursement purposes.

Task:

Create a function to record expenses by capturing the description, amount, and category of each expense.
The function should store the expenses in a list and confirm to the user that the expense has been recorded.
3. Fitness Activity Logging

Scenario: ABC Inc. encourages employees to maintain a healthy lifestyle by engaging in regular fitness activities. Tracking these activities can help employees monitor their fitness progress and stay motivated.

Task:

Implement a function to log fitness activities, including the type of activity, duration, and calories burned.
The function should store the activities in a list and notify the user that the activity has been logged.
4. Daily Journal Keeping

Scenario: Reflecting on daily experiences can help employees manage stress and improve mental well-being. A daily journal can serve as a personal record of thoughts and events.

Task:

Design a function that allows employees to add journal entries by specifying the date and content.
The function should store the entries in a list and inform the user that the journal entry has been added.
Summary
ABC Inc. requires a Daily Life Organizer with the following functionalities:

Task Management:
Function to add tasks with a description and due date.
Expense Tracking:
Function to record expenses with a description, amount, and category.
Fitness Activity Logging:
Function to log fitness activities with type, duration, and calories burned.
Daily Journal Keeping:
Function to add journal entries with a date and content.
The solution should be user-friendly and integrate all functionalities into a cohesive system to help employees manage their daily activities efficiently.
