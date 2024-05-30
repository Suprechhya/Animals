import sqlite3

DATABASE = 'SQL.db'

#open the database
def print_all_animals():
db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT * FROM Animals;"
cursor.execute(sql)
results = cursor.fetchall()

def print_all_animal_id():
db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT animal_id FROM Animals;"
cursor.execute(sql)
results = cursor.fetchall()


def print_all_animal_name():
db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT animal_name FROM Animals;"
cursor.execute(sql)
results = cursor.fetchall()

def print_all_scientific_name():
db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT scientific_name FROM Animals;"
cursor.execute(sql)
results = cursor.fetchall()

def print_all_species_types():
db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT species_types FROM Animals;"
cursor.execute(sql)
results = cursor.fetchall()

#print all the results
print(f"animal_id      animal_name       scientific_name         species_types")
for animals in results:
#creates list
    print(f"animal_id: {animals[0]}  animal_name: {animals[1]}   scientific_name: {animals[2]}    species_types: {animals[3]}")
#loop finish here
db.close()

#main code
user_input = input(
"""
Which Animal Data Would You Like To See? 
1. Print all Animal data
2. Prints the ID of the Animal
3. Prints the name of the Animal
4. Prints the scientific name of the Animal
5. Prints the species types of the Animal
6. Exit
"""
)

if user_input == '1':
    print_all_animals()
elif user_input == '2':
    print_all_animal_id()
elif user_input =='3':
    print_all_animal_name()
elif user_input == '4':
    print_all_scientific_name()
elif user_input == '5':
    print_all_species_types()
elif user_input == '6':
    exit
else:
    print('That is not a option')
