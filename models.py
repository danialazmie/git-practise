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
        pass