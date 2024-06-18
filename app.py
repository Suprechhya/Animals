#imports data
import sqlite3

#Contants and Variables
DATABASE = 'SQL.db'

#Funtion Code
def print_all_animals():
    '''print all the animals nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Animals"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Animal_ID       Animal_Name                  Scientific_Name                   Species_Types")
    #loops through all results
    for animals in results:
        print(f'{animals[0]:<17}{animals[1]:<27}{animals[2]:<37}{animals[3]:<30}')
    #loop ends
    db.close()


def print_all_animals_by_id():
    '''print all the animals by id nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT animal_id FROM Animals"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Animal_ID:")
    #loops through all results
    for animals in results:
        print(f'{animals[0]}')
    #loop ends
    db.close()


def print_all_animals_by_name():
    '''print all the animals by name nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT animal_name FROM Animals"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Animal_Name:")
    #loops through all results
    for animals in results:
        print(f'{animals[0]}')
    #loop ends
    db.close()


def print_all_animals_by_scientific_name():
    '''print all animals by scientific name nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT scientific_name FROM Animals"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Scientific_Name:")
    #loops through all results
    for animals in results:
        print(f'{animals[0]}')
    #loop ends
    db.close()


def print_all_animals_by_species_types():
    '''print all animals by species types nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT species_types FROM Animals"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Species_Types:")
    #loops through all results
    for animals in results:
        print(f'{animals[0]}')
    #loop ends
    db.close()


def print_all_animals_in_alphabetical_order():
    '''print all the animal data in alphabetical order nicely'''
    db = sqlite3.connect('SQL.db')
    cursor = db.cursor()
    sql = "SELECT * FROM Animals ORDER BY scientific_name"
    cursor.execute(sql)
    results = cursor.fetchall()
    print("Animal_ID       Animal_Name                  Scientific_Name                   Species_Types")
    #loops through all results
    for animals in results:
        print(f'{animals[0]:<17}{animals[1]:<27}{animals[2]:<37}{animals[3]:<30}')
    #loop ends
    db.close()



#Main Code/Main Menu
while True:
#Enters a Loop
    user_input = input(
    """
    Which Animal Data Would You Like To See?
    1. Print All Animal Data
    2. Print Only Animal ID
    3. Print Only Animal Names
    4. Print Only Scientific Names
    5. Print Only Species Types
    6. Print All Animal Data in Alphabetical Order by Scientific Name
    7. Exit
    """)


#Input Codes
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
    elif user_input == '7':
    #checks for break
        break
    #breaks from the loop
    else:
        print('That Is Not An Option, Please Choose The Numbers That Has Been Given!')
    #repeats the loop