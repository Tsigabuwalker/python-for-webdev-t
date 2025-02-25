import sqlite3

# Connect to the database (or create it)
connect = sqlite3.connect('data.db')

# Uncomment these lines if you want to drop the table and create it again
# connect.execute("DROP TABLE IF EXISTS Customer")
# connect.execute('''
# CREATE TABLE Customer(
#                 Id INT PRIMARY KEY,
#                 Name TEXT NOT NULL,
#                 Age INT NOT NULL
#                 );''')

# Check existing data
existing_data = connect.execute("SELECT * FROM Customer").fetchall()
print("Existing Data:")
for row in existing_data:
    print(row)

# Insert only if the Id is unique
try:
    connect.execute('''
        INSERT INTO Customer (Id, Name, Age)
        VALUES 
            (44390, 'Tsigabu', 44),
            (44391, 'Abera', 66),  
            (44392, 'Hagos', 77);  
    ''')
    connect.commit()  # Remember to commit the changes
except sqlite3.IntegrityError:
    print("Error: One of the Ids already exists.")

# Query to select all data from the Customer table
all_data = connect.execute("SELECT * FROM Customer")

# Print each row in the result
print("All Data:")
for row in all_data:
    print(row)

connect.close()  # Close the connection