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

