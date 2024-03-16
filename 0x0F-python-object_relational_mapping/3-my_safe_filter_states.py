#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument, safely from SQL injection
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query to select states matching the input state name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
