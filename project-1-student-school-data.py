import os, mysql.connector

datab = mysql.connector.connect(host='localhost', user='root', passwd='toor', database='mizpah', charset='utf8')
cursorx = datab.cursor()

def add_student():
    create_table = '''CREATE TABLE IF NOT EXISTS Student(
    roll_no  INTEGER(4),
    name VARCHAR(30),
    phone VARCHAR(12),
    address VARCHAR(50),
    admission_no VARCHAR(10) PRIMARY KEY)'''
    
    cursorx.execute(create_table)
    
    roll_no = int(input('Enter roll number : '))
    name = input('Enter name : ')
    phone = input('Enter phone number : ')
    address = input('Enter address : ')
    #std = input('Enter class : ')
    admission_no = input('Enter adminssion number : ')

    insert_data = f'''INSERT INTO Student(
    roll_no, name, phone, address, admission_no) VALUES(
    %s, %s, %s, %s, %s)'''
    values = (roll_no, name, phone, address, admission_no)
    
    cursorx.execute(insert_data, values)
    cursorx.execute('COMMIT')
                               
    cursorx.close()

def display_student():
    cursorx.execute('SELECT * FROM Student')
    data = cursorx.fetchall()
    for row in data:
        print(row)
        
def add_marks():
    create_table = '''CREATE TABLE IF NOT EXISTS Marks(
    admission_no  VARCHAR(10) PRIMARY KEY,
    maths INT,
    computer INT,
    science INT,
    total INT,
    average DECIMAL)
    '''
    cursorx.execute(create_table)
    admission_no = input('Enter admission_no of the student : ')
    maths = int(input('Enter Maths Marks : '))
    computer = int(input('Enter Computer Marks : '))
    science = int(input('Enter Science Marks : '))

    total = maths + computer + science
    average = total / 3
    query = '''INSERT INTO Marks(
    admission_no, maths, computer, science, total, average) VALUES (
    %s, %s, %s, %s, %s, %s)
    '''
    values = (admission_no, maths, computer, science, total, average)

    cursorx.execute(query, values)
    cursorx.execute('COMMIT')
    print('Marks entered successfully. ')

def display_student_marks():
    admission_no = input('Enter the admission_no of the student : ')
    print('==============================================')
    print('Name, Roll_no, admission_no')
    print('---------------------------')
    query = 'SELECT name, roll_no, admission_no FROM Student WHERE admission_no = %s'
    cursorx.execute(query, (admission_no,))
    data = cursorx.fetchall()
    if data:
        for i in data:
            print(i)
    else:
        print('Record not found')
    
    query = 'SELECT * FROM Marks WHERE admission_no = %s'
    cursorx.execute(query, (admission_no,))
    data = cursorx.fetchall()
    
    if data:
        print('Student report card')
        print('-------------------')
        print('Admission_no, Maths, Computer, Science, Total')
        for i in data:
            print(i)
    else:
        print('Record not found, try again')
    print('==============================================')
    
def main():
    while(True):   
        print('Press 1 for - Adding a student')
        print('Press 2 for - Displaying the student\'s data')
        print('Press 3 for - Adding Marks for the student')
        print('Press 4 for - Displaying the student\'s marks')
        choice = int(input('Enter your choice '))
        
        if choice == 1:
            add_student()
        elif choice == 2:
            print("roll_no, ", "name, ", "phone, ", "address, ", "admission_no")
            display_student()
            print()
        elif choice == 3:
            add_marks()
        elif choice == 4:
            display_student_marks()
        else:
            cursorx.close()
            return

if __name__ == '__main__':
    main()
