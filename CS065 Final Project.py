# author: Chi (Alison) Dang
# date: November 12, 2020
# description: assignment 7 -- Information Literacy
# proposed points (out of 10): I beleive my assignment 6 points

# Part 1
# 1.1: Get the number of the total salary of gender differences when they work for private in difference race
# source: Kaggie: Fatakdawala, M. (2018). Income Dataset. Retrieved 9 December 2020, from https://www.kaggle.com/mastmustu/income?select=test.csv
import csv
import matplotlib.pyplot as plt
import numpy as np

def display_data(data):
    """
    parameter: data is a input data read in from csv.Dict
    display_fields prints out of all of the fields (columns) in the data set
    """
    for salary in data.fieldnames:
        print(salary)

def process_data(data, gender, workclass, race):
    """
    input: data: a data set of salary statistics
    prints out the total salary people can earn by age & gender
    """
    total = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    total7 = 0
    total8 = 0
    total9 = 0
    total10 = 0
    for row in data:
        if row["race"] == "White":
            if row['gender'] == "Male" and row['workclass'] == "Private":
                total += float(row["fnlwgt"])
            if row['gender'] == "Female" and row['workclass'] == "Private":
                total2 += float(row["fnlwgt"])
        elif row["race"] == "Amer-Indian-Eskimo":
            if row['gender'] == "Male" and row['workclass'] == "Private":
                total3 += float(row["fnlwgt"])
            if row['gender'] == "Female" and row['workclass'] == "Private":
                total4 += float(row["fnlwgt"])
        elif row["race"] == "Black":
            if row['gender'] == "Male" and row['workclass'] == "Private":
                total5 += float(row["fnlwgt"])
            if row['gender'] == "Female" and row['workclass'] == "Private":
                total6 += float(row["fnlwgt"])
        elif row["race"] == "Other":
            if row['gender'] == "Male" and row['workclass'] == "Private":
                total7 += float(row["fnlwgt"])
            if row['gender'] == "Female" and row['workclass'] == "Private":
                total8 += float(row["fnlwgt"])
        elif row["race"] == "Asian-Pac-Islander":
            if row['gender'] == "Male" and row['workclass'] == "Private":
                total9 += float(row["fnlwgt"])
            if row['gender'] == "Female" and row['workclass'] == "Private":
                total10 += float(row["fnlwgt"])
    
    print("The total salary of all White race male in Private workclass in the USA: ", total)
    print("The total salary of all White race female in Private workclass in the USA: ", total2)
    print("The total salary of all Amer-Indian-Eskimo race male in Private workclass in the USA: ", total3)
    print("The total salary of all Amer-Indian-Eskimo race female in Private workclass in the USA: ", total4)
    print("The total salary of all Black race male in Private workclass in the USA: ", total5)
    print("The total salary of all Black race female in Private workclass in the USA: ", total6)
    print("The total salary of all Other race male in Private workclass in the USA: ", total7)
    print("The total salary of all Other race female in Private workclass in the USA: ", total8)
    print("The total salary of all Asian-Pac-Islander race male in Private workclass in the USA: ", total9)
    print("The total salary of all Asian-Pac-Islander race female in Private workclass in the USA: ", total10)


def main():
    # open the data file
    infile = open("test.csv", "r")
    
    # create a variable to read through the data
    salary_data = csv.DictReader(infile)
    
    # display the column names in the data
    display_data(salary_data)

    # call process data -- process_data(covid_data)
    process_data(salary_data, "Female", "Private", "White")
     
main()



# 1.2: make a graph to show the difference in total salaray between two gender when they work for private in difference races
    #uses matplotlib to create a bar graph
#     Consulting and citing from this website:
#     Matplotlib Bar chart. (2020). Retrieved 9 December 2020, from https://pythonspot.com/matplotlib-bar-chart/
    
import numpy as np
import matplotlib.pyplot as plt

# data to plot
numbers = 5
male_salary = [70942842, 178332, 9570972, 409174, 1494387]
female_salary = [32873995, 1494387, 7380776, 198272, 697929]

# create plot
fig, ax = plt.subplots()
index = np.arange(numbers)
width = 0.40
opacity = 0.75

rects1 = plt.bar(index, male_salary, width, alpha=opacity, color= 'b', label='Male')
rects2 = plt.bar(index + width, female_salary, width, alpha=opacity, color='r', label='Female')
    
plt.xlabel("Race")
plt.ylabel("The total salary")
plt.title("Sex Differences in Salary were presented in the Private work class")
    
plt.xticks(index + width, ("W", "AIE", "B", "O", "API"))    
    
plt.legend()
plt.show()
