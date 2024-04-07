import mysql.connector
import hashlib

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flask_proj"
)

import mysql.connector

def register(username, password):
    c = mydb.cursor()
    sql = f"INSERT INTO uporabniki (user, passwd) VALUES ('{username}','{password}');"
    c.execute(sql)
    mydb.commit()

def registerIP(username, password,ip):
    c = mydb.cursor()
    sql = f"INSERT INTO uporabniki (user, passwd, IP, IPCheckLogin) VALUES ('{username}','{password}','{ip}','1');"
    c.execute(sql)
    mydb.commit()

def CheckUser(username):
    c = mydb.cursor()
    sql = f"SELECT * FROM uporabniki WHERE user = '{username}';"
    c.execute(sql)
    a=c.fetchone()
    if a == None:
        return True
    else:
        return False

def IdIp(IP):
    c = mydb.cursor()
    sql = f"SELECT ID FROM uporabniki WHERE IP = '{IP}';"
    c.execute(sql)
    a=c.fetchone()
    a=a[0]
    return a


def IdUser(username):
    c = mydb.cursor()
    sql = f"SELECT ID FROM uporabniki WHERE user = '{username}';"
    c.execute(sql)
    a=c.fetchone()
    a=a[0]
    return a

def HashPasswd(password):
    salt="?$2b$12$GG2dTVOVfUNawHK0Ttru7u"
    hashed = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return hashed

def login(username, password,ip):
    c = mydb.cursor()
    password=HashPasswd(password)
    sql = f"SELECT * FROM uporabniki WHERE user = '{username}' AND passwd = '{password}' AND (IP = '{ip}' OR IPCheckLogin=0);"
    c.execute(sql)
    a=c.fetchone()
    if a == None:
        return True
    else:
        return False

def TaskList(tasks):
    tasksList = []
    for task in tasks:
        tasksList.append(str(task[1]))     
    return tasksList

def TaskAdd(task, user_id):
    c = mydb.cursor()
    sql = f"INSERT INTO tasks (task, UserID) VALUES ('{task}','{user_id}');"
    c.execute(sql)
    mydb.commit()

def TaskGet(user_id):
    c = mydb.cursor()
    sql = f"SELECT * FROM tasks WHERE UserID = '{user_id}'"
    c.execute(sql)
    a=c.fetchall()
    return a

def TaskGetComplete(user_id):
    c = mydb.cursor()
    sql = f"SELECT * FROM tasks WHERE UserID = '{user_id}' AND complete = 1"
    c.execute(sql)
    a=c.fetchall()
    return a

def CheckMatchIP(IP):
    c = mydb.cursor()
    sql = f"SELECT * FROM uporabniki WHERE IP = '{IP}';"
    c.execute(sql)
    a=c.fetchone()
    if a == None:
        return False
    else:
        return True
    
def ValidID(ID):
    c = mydb.cursor()
    sql = f"SELECT * FROM uporabniki WHERE ID = '{ID}';"
    c.execute(sql)
    a=c.fetchone()
    if a == None:
        return False
    else:
        return True
    
