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
    conn.commit()

    
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

def get_ishere_by_name(name):
    c.execute("SELECT ishere FROM student WHERE name =:name ",{'name':name})
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

#s = Student(1,"Maximilian Buzza",0)
#s = Student(2,"Taylor CarrHeuer",0)
#s = Student(3,"Louis Cekay",0)
#s = Student(4,"Jacoby Chamberlin",0)
#s = Student(5,"Parker Cox",0)
#s = Student(6,"Ronin Coxwell",0)
#s = Student(7,"Andrew Dagostino",0)
#s = Student(8,"Olin Dawson",0)
#s = Student(9,"Kallan Debney",0)
#s = Student(10,"Ruby Deng",0)
#s = Student(11,"Aaden Dobelstein",0)
#s = Student(12,"Duncan Duffield",0)
#s = Student(13,"Henry Erickson",0)
#s = Student(14,"Henry Felsted",0)
#s = Student(15,"Lauren Gault",0)
#s = Student(16,"sonan gudina",0)
#s = Student(17,"Beatrice Gilfix",0)
#s = Student(18,"Jackson Harris",0)
#s = Student(19,"Cynthia Hsu",0)
#s = Student(20,"Anders Huberty",0)
#s = Student(21,"Meri Hunanyan",0)
#s = Student(22,"Aaryan Ilanchelian",0)
#s = Student(23,"Ananya Ilanchelian",0)
#s = Student(24,"Kyle Kilpatrick",0)
#s = Student(25,"Veraina Langley",0)
#s = Student(26,"Henrik Lee",0)
#s = Student(27,"Leanna Li",0)
#s = Student(28,"Alivia Marshall",0)
#s = Student(29,"Luke Morgan",0)
#s = Student(30,"Jack Morozov",0)
#s = Student(31,"Eshaan Rana",0)
#s = Student(32,"Henry Reagan",0)
#s = Student(33,"Caleb Rubow",0)
#s = Student(34,"Maxx Rudzek",0)
#s = Student(35,"Gavin Seidel",0)
#s = Student(36,"Gianluca Simi",0)
#s = Student(37,"Ravenna Talaga",0)
#s = Student(38,"Nathan Van Gordon",0)
#s = Student(39,"Weston Weissert",0)
#s = Student(40,"Darby Wheatley",0)
#s = Student(41,"Louis Cekay",0)
s = Student(42,"Alexander Zuniga",0)



insert_student(s)

print(get_student())


conn.close

