import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

cur.execute("insert into maintainer (username,password) values (?,?)", ('admin', 'password'))

con.commit()
con.close()