#imports data
import sqlite3


#Contants and VariablesS
DATABASE = 'SQL.db'


#funtions
def print_all_animals():
    '''print all the animals nicely'''
db = sqlite3.connect('SQL.db')
cursor= db.cursor()
sql = "SELECT * FROM Animals"
cursor.execute(sql)
results = cursor.fetchall()
#loops through all results
print('Animal_id     Animal_Name     Scientific_Name    Species_Types')
for animals in results:
    print(f'Animal_ID   {animals[0]}   Animal_Name:   {animals[1]}    Scientific_Name:  {animals[2]}  Species_Types:  {animals[3]}')
#loop finised here
db.close()







