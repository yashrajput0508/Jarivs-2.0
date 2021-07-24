import sqlite3 as sql
import datetime


def database():
    conn = sql.connect("database.db")
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM datas")
        conn.commit()
        c.close()
    except sql.OperationalError:
        c.execute("CREATE TABLE datas(id INTEGER PRIMARY KEY AUTOINCREMENT,userinput varchar(255),userresponse varchar(255),date varchar(255))")
        conn.commit()
        c.close()

def updatedatabase(userinput,userresponse):
    conn=sql.connect("database.db")
    database()
    c=conn.cursor()
    c.execute("INSERT INTO datas(userinput,userresponse,date) VALUES(?,?,?);",(userinput,userresponse,datetime.date.today(),))
    conn.commit()
    c.close()

