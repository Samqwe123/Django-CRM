import mysql.connector

# Connect to MySQL server (without specifying a database)
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin"
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a new database
cursorObject.execute("CREATE DATABASE samdb")

print("Database samdb has been recreated successfully!")

# Close the connection
cursorObject.close()
dataBase.close()

#Test123
#Test for Fork and Pull request