#imports data
import sqlite3


#Contants and VariablesS
DATABASE = 'SQL.db'

#Funtion Code
def print_all_animals():
    '''print all the animals nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Animals"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loops through all results
    for animals in results:
        print(f'Animal_ID   {animals[0]}   Animal_Name:   {animals[1]}    Scientific_Name:  {animals[2]}  Species_Types:  {animals[3]}')
    #loop finised here
    db.close()

def print_all_animals_by_id():
    '''print all the animal name nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT animal_id FROM Animals"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loops through all results
    for animals in results:
        print(f'Animal_ID:   {animals[0]}')
    db.close()


def print_all_animals_by_name():
    '''print all the animal name nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT animal_name FROM Animals"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loops through all results
    for animals in results:
        print(f'Animal_Name:   {animals[0]}')
    db.close()


def print_all_animals_by_scientific_name():
    '''print all the scientific name nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT scientific_name FROM Animals"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loops through all results
    for animals in results:
        print(f'Scientific_Name:   {animals[0]}')
    db.close()

def print_all_animals_by_species_types():
    '''print all the species types nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT species_types FROM Animals"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loops through all results
    for animals in results:
        print(f'Species_Types:   {animals[0]}')
    db.close()


def print_all_animals_in_alphabetical_order():
    '''print all the animal data nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Animals ORDER BY scientific_name"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loops through all results
    for animals in results:
        print(f'Animal_ID   {animals[0]}   Animal_Name:   {animals[1]}    Scientific_Name:  {animals[2]}  Species_Types:  {animals[3]}')
    db.close()
 
   
#Main Code 
user_input = input(
"""
Which Data Would You Like To See?
1. Print All Animal Data
2. Print Only Animal ID
3. Print Only Animal Names
4. Print Only Scientific Names
5. Print Only Species Types
6. Print All Animal Data in Alphabetical Order by Scientific Name
7. Exit
""")


if user_input == '1':
    print_all_animals()
elif user_input == '2':
    print_all_animals_by_id()
elif user_input == '3':
    print_all_animals_by_name()
elif user_input == '4':
    print_all_animals_by_scientific_name()
elif user_input == '5':
    print_all_animals_by_species_types()
elif user_input == '6':
    print_all_animals_in_alphabetical_order()
else:
    print('That Is Not An Option, Please Choose The Numbers That Have Been Given!')




