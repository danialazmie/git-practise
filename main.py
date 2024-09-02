from models import Student
from utils import print_title
import time

def main_menu():

    print_title('Student Management System')

    print('1. Add Student')
    print('2. View Student')
    print('3. Update Student')
    print('4. Delete Student')
    print('5. Exit')

    option = input('Enter your option: ')

    if option == '1':
        pass
    elif option == '2':
        pass

def add_student():
    
    print_title('Add a Student')

    name = input('Name: ')
    age = input('Age: ')
    classroom = input('Classroom: ')

    student = Student(name, age, classroom)

    student.save()

    print(f'Student {student.name} added successfully!')

    time.sleep(1)

    main_menu()

    

def view_student():
    pass

def update_student():
    pass

def delete_student():
    pass

def main():
    main_menu()

if __name__ == "__main__":
    main()