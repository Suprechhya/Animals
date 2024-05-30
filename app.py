import sqlite3

DATABASE = "SQL.db"

#funtions
def print_all_animals():
    '''print all the animals nicely'''
db = sqlite3.connect('SQL.db')
cursor= db.cursor()
sql = "SELECT * FROM Animals"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()

#main code
print_all_animals()

