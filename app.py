import sqlite3
#hello
DATABASE = 'SQL.db'

with sqlite3.connect(DATABASE) as db:
    cursor = db.cursor()
    sql = "SELECT * FROM Animals;"
    cursor.execute(sql)
    results = cursor.fetchall()

for animals in results:
    #creates list
    print(f"animal_id: {animals[0]}  animal_name: {animals[1]}  scientific_name:  {animals[2]}  species_types:  {animals[3]}")

db.close()