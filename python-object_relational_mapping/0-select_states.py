#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db_name
    )

    # Create cursor
    cursor = db.cursor()

    # Execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    # Close connections
    cursor.close()
    db.close()
