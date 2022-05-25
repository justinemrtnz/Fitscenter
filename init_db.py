import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (lname, fname, mname , address , crop , area , livestock, noheads) VALUES (?, ?,?,?,?,?,?,?)",
            ('BERTHS', 'RONALD' , 'LAURIO', 'SILANGAN ILAYA', '','','','')
            )

cur.execute("INSERT INTO posts (lname, fname, mname , address , crop , area , livestock, noheads) VALUES (?, ?,?,?,?,?,?,?)",
            ('URRIZA', 'VIRGILIO' , 'GUITIERREZ', 'SILANGAN ILAYA', '','','','')
            )

connection.commit()
connection.close()
