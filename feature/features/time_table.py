import Speech
import sqlite3 as sql
from datetime import date
from datetime import datetime

# datetime object containing current date and time


class time_table:
    def __init__(self):
        self.sp=Speech.speech()
        self.today = date.today()
        self.now = datetime.now()
        try:
            self.create_table()
        except Exception:
            pass
    def create_table(self):
        # connecting to the database
        connection = sql.connect("time_table.db")

        # cursor
        crsr = connection.cursor()

        # SQL command to create a table in the database
        sql_command = "CREATE TABLE schedule(id INTEGER PRIMARY KEY AUTOINCREMENT,time TIME,date DATE,description VARCHAR(100))"

        # execute the statement
        crsr.execute(sql_command)

        # To save the changes in the files. Never skip this.
        # If we skip this, nothing will be saved in the database.
        connection.commit()

        # close the connection
        connection.close()

    def set_data(self):
        time=input("Enter the time:-")
        date=self.today.strftime("%d-%m-%Y")
        description=input("Enter the description:-")
        try:
            # creates a database in RAM
            con = sql.connect("time_table.db")
            cur = con.cursor()
            command="INSERT INTO schedule(time,date,description) values ('{}', '{}', '{}')" .format(time,date,description)
            cur.execute(command)
            con.commit()
            # And this is the named style:
            con.close()
        except Exception as e:
            print("An exception is occurs")
