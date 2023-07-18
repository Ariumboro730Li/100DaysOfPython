
import mysql.connector
from flask import jsonify

def fetchData():
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="100Jutaperbulan",
        database="ping_automate"
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Execute the MySQL query
    query = "SELECT * FROM content_ebr_to_gw LIMIT 57"
    cursor.execute(query)

    # Fetch all rows from the query result
    rows = cursor.fetchall()

    # Convert the query result to a list of dictionaries
    result = []
    for row in rows:
        result.append(dict(zip(cursor.column_names, row)))

    # Close the cursor and database connection
    cursor.close()
    connection.close()

    # Prepare the JSON response
    response = {
        "draw": 1,
        "recordsTotal": len(result),
        "recordsFiltered": len(result),
        "data": result
    }

    return jsonify(response)    
