import pandas as pd

class Student:
    def __init__(self, name, age, classroom):
        self.name = name
        self.age = age
        self.classroom = classroom

    def save(self):
        """
        Function to save the student data into a CSV file
        """
        studentfile = pd.read_csv('.\data\students.csv')
        studentinput = {"name":[self.name], "age":[self.age], "classroom":[self.classroom]}
        studentadd = pd.DataFrame(studentinput)
        studentfile = pd.concat([studentfile,studentadd], ignore_index=True)
        studentfile.to_csv('.\data\students.csv', index=False)
        pass