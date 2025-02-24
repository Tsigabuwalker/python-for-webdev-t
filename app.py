import sqlite3

connect = sqlite3.connect('data.db')

# Uncomment these lines if you want to drop the table and create it again
# connect.execute("DROP TABLE IF EXISTS Customer")
# connect.execute('''
# CREATE TABLE Customer(
#                 Id INT PRIMARY KEY,
#                 Name TEXT NOT NULL,
#                 Age INT NOT NULL
#                 );''')

# Insert a record into the CUSTOMER table
connect.execute("INSERT INTO Customer (Id, Name, Age) VALUES (4438, 'Tsigabu', 24)")
connect.commit()  # Remember to commit the changes

# Query to select all data from the Customer table
all_data = connect.execute("SELECT * FROM Customer")

# Print each row in the result
for row in all_data:
    print(row)

connect.close()  # Close the connection