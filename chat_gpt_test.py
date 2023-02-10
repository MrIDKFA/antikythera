import csv
import sqlite3

# Create a CSV file with multiple rows and columns
with open("sample.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Country"])
    writer.writerow(["John Doe", 30, "USA"])
    writer.writerow(["Jane Doe", 25, "Canada"])

# Create a new SQLite database for the CSV file
conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

# Open the CSV file in Python and read its contents
with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    headers = next(reader)

    # Create a table in the database to store the data from the CSV file
    cursor.execute("CREATE TABLE sample ({} INT, {} INT, {} TEXT)".format(*headers))

    # Write the contents of the CSV file into the database
    for row in reader:
        cursor.execute("INSERT INTO sample ({}) VALUES (?, ?, ?)".format(", ".join(headers)), row)

# Commit the changes and close the connection
conn.commit()
conn.close()
