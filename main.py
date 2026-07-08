from functions import (
    add_student,
    calculate_average,
    find_student,
    display_report,
)


def main():
     print (" Have a nice week, this is a system to access student's grades", " to show our menu enter y")
    response = input() 
    if response == 'y': 
        list_options() 
    
    students = []
    while response == 'y':
        print(" Enter your operation no: ")
        x = input()
        
        if x == '1':
            while True:
                name = input(" Type a student name: (0 to stop)")
                if name == '0': 
                    break
                    
                grade = input(" Type a student grade:  ")
                add_student(name,grade)
                
            response = option()    
            
        elif x == '2': 
            print( calculate_average(students))
            response = option()
                    
        elif x == '3': 
            print(" Type a student's same you want to find") 
            ename = input() 
            print( find_students(students, ename))
            response = option()
                
        elif x == '4': 
           print( display_report(students))
           response = option() 
        elif x == '5':
            print( " EXIT!, THANKS FOR USING THIS SYSTEM ")
