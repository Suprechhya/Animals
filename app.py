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
#loops through all results
print('Animal_id     Animal_Name     Scientific_Name    Species_Types')
for animals in results:
    print(f'Animal_ID   {animals[0]}   Animal_Name:   {animals[1]}    Scientific_Name:  {animals[2]}  Species_Types:  {animals[3]}')
#loop finised here
db.close()

#funtions
def print_all_animals_by_id():
    '''print all the animal id nicely'''
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

#funtions
def print_all_animals_by_name():
    '''print all the animal name nicely'''
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

#funtions
def print_all_animals_by_scientific_name():
    '''print all the scientific name nicely'''
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

#funtions
def print_all_animals_by_species_types():
    '''print all the animal species types nicely'''
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


#main code
user_input = input('\nWhich Animal Data Would You Like To See? \n1. Print all data \n2. Exit\n')
if user_input == '1':
    print_all_animals()
if user_input == '2':
    break
else:
    print('That is not a option')

