import mysql.connector

# Connect to MySQL server
db_connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="salestracker"
)

# Create a cursor object
cursor = db_connection.cursor()

# Update mobile numbers for IDs 2 to 20
for i in range(22):
    new_mobile_number = f"987654320{i}"  # Example pattern for mobile numbers
    cursor.execute(
        "UPDATE leadlist SET mobileno = %s WHERE id = %s", (new_mobile_number, i)
    )

# Commit changes and close the database connection
db_connection.commit()
cursor.close()
db_connection.close()

print("Mobile numbers updated successfully!")
