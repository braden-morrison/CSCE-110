# File: grades.py
# Author: Braden Morrison
# Date: 08/09/2023
# Section: 700
# E-mail: bradenmorrison@tamu.edu 
# Description: user inputs txt file, program produces bar graphs of the data in file



import matplotlib.pyplot as drawing
import statistics


def get_grades(filename):
    """
    This function takes a file name as input and populates a dictionary containing the assignment types and grades.
    @param filename:
    @return: dictionary of grades
    """
    gradebook = dict()
    # todo
    with open(filename, 'r') as file:
        for line in file:
            activity, score = line.strip().split()
            score = float(score)

            if activity not in gradebook:
                gradebook[activity] = []
            gradebook[activity].append(score)

    return gradebook


def main():
    """
    This function prompts for the grades file name.
    Next, it calls the functions get_grades().
    Next, it draws the bar chart of the average grade for each assignment.
    @return:
    """
    filename = input("Enter the grade file name: ")
    gradebook = get_grades(filename)
    print(f'The dictionary of grades is: {gradebook}')
    # todo

    #AVERAGES
    
    dic = dict()
    for cat, grades in gradebook.items():
        dic[cat] = sum(grades) / len(grades)
    category = dic.keys()
    scores = dic.values()

    #BAR CHART
    drawing.bar(category, scores, width = 0.8, align='center')
    drawing.xlabel("Assignment")
    drawing.ylabel("Average grade")
    drawing.title(f"CSCE 110 assignment grades")
    drawing.legend(['grades'])
    drawing.show()
   

    



if __name__ == '__main__':
    main()