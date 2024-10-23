import sqlite3
from student import Student
from datetime import datetime

current_time = datetime.now()

conn = sqlite3.connect('database.db')

c = conn.cursor()

#c.execute("""CREATE TABLE student (
#     ID integer,
#     name text,
#   ishere integer  
#)""")
#c.execute("""CREATE TABLE time (
#     ID integer,
#    date text,
#     timein text,
#    timeout text  
#)""")


def insert_student(student):
    c.execute("INSERT INTO student VALUES (:ID,:name,:ishere)",{'ID': student.ID,'name':student.name,'ishere':student.ishere})

    
def signin(ID):
    c.execute("INSERT INTO time (ID, date, timein, timeout) VALUES (:ID, :date, :timein, :timeout)", 
              {'ID': ID, 'date': datetime.now().date().strftime("%Y-%m-%d"), 
               'timein': datetime.now().strftime("%H:%M:%S"), 'timeout': None})
    c.execute("UPDATE student SET ishere = :ishere WHERE ID = :ID", 
              {'ID': ID, 'ishere': 1})
    conn.commit()
    print("student signed in")



def signout(ID):
    c.execute("UPDATE time SET timeout = :timeout WHERE ID = :ID AND timeout IS NULL", 
              {'ID': ID, 'timeout': datetime.now().strftime("%H:%M:%S")})
    c.execute("UPDATE student SET ishere = :ishere WHERE ID = :ID", 
              {'ID': ID, 'ishere': 0})
    conn.commit() 
    print("student signed out")

def get_student_by_name(name):
    c.execute("SELECT * FROM student WHERE name =:name ",{'name':name})
    return  c.fetchall()
    

def get_ID_by_name(name):
    c.execute("SELECT ID FROM student WHERE name =:name ",{'name':name})
    number = c.fetchone()
    return number[0]

def signin_by_name(name):
    c.execute("SELECT ID FROM student WHERE name =:name ",{'name':name})
    number = c.fetchone()
    signin(number[0])



def signout_by_name(name):
    c.execute("SELECT ID FROM student WHERE name =:name ",{'name':name})
    number = c.fetchone()
    signout(number[0])



def get_time_by_date(date):
    c.execute("SELECT * FROM time WHERE date =:date ",{'date':date})
    return c.fetchall()

def get_student():
    c.execute("SELECT * FROM student")
    return c.fetchall()
def get_time():
    c.execute("SELECT * FROM time")
    return c.fetchall()

sonan = Student(1,'sonan gudina',0)
insert_student(sonan)
print(get_student())
print(get_ID_by_name("sonan gudina"))
signin(get_ID_by_name("sonan gudina"))
signout(get_ID_by_name("sonan gudina"))
signin_by_name("sonan gudina")
conn.close

