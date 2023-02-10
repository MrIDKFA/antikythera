import sqlite3
import csv

# Connect to the database (or create it if it doesn't exist)

conn = sqlite3.connect('sklad.db')


# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sklad (
	    line_id INT PRIMARY KEY,
	    sapItem TEXT,
	    skladNum INT,
	    ks INT,
	    atp INT
    ) 
    ''')

conn.commit()


counter = 0
#open csv and read from it
with open("ztp_all_utf.csv", "r", encoding="UTF-8") as file:
    reader = csv.reader(file, delimiter=";")
    header = next(reader)
    for row in reader:
        counter = counter + 1
        # command = f"INSERT INTO sklad (line_id, sapItem, skladNum, ks, atp) VALUES ({counter}, '{row[0]}', {row[2]}, {row[3]}, {row[4]});"
        # cursor.execute(command)

conn.commit
# Close the connection
conn.close()
