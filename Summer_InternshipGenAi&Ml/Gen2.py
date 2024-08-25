import sqlite3

def search_database(query):
    # Connect to the database
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Execute the query
    try:
        cursor.execute(query)
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)
    except sqlite3.OperationalError as e:
        print(f"Error executing query: {e}")
        print("Check if the table 'users' exists in your database.")

    # Close the connection
    conn.close()

# Example usage - Adjust the query if needed
search_database("SELECT name FROM sqlite_master WHERE type='table';") # Check existing tables
# search_database("SELECT * FROM users WHERE name LIKE '%John%'")