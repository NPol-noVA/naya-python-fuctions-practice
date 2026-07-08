#a-student-grade-management-system
## functions-of-grade-system




# a function for adding students' names and grades 
def add_student (name, grade): 
    students.append ({'names': name , 'grades': grade })



# function to calculate the average of grades
def calculate_average (students):
    c=0 ## counting students  
    s=0 
    for x in students: 
        s += float (x['grades'])
        c=c+1
    return float(s)/c 


# function to look for a student then return its grade  
def find_students ( students, name):
    k= " There's no student with this name"  
    for x in students: 
        if x['names']== name :
            print ( name," is exsited and its grade is : ")
            return x['grades']
    return k 



#  function to print a report of students' information and highest  grade 
def display_report (students):
    for x in students: 
        print ( x['names'],':' , x['grades']) 

    best_grade = 0 
    for x in students: 
        if best_grade <= float(x['grades']):
            best_grade = float(x['grades']) 
    print (" Highest grade = ")  
    return best_grade 


# function to ask users for either exit or continue   
def option():
    print(" Okey will you choose new option (y/n) ?") 
    response = input() 
    return response
# function to print list of options that user can choose
def list_options():
     print (' This is the menu:',
            "1. add a student","2. calculate average grade", "3. find a student's name","4. show report", "5.exit" ) 
