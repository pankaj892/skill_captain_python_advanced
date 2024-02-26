import mysql.connector

# Connect to the MySQL database
def connect_to_mysql():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="new_user",
            password="secret_pass",
            database="mytestdb"
        )
        return conn
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None

# Retrieve and display data from a table
def retrieve_data_from_table(conn):
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM person")
        rows = cursor.fetchall()

        # Display the retrieved data
        for row in rows:
            print(row)

        cursor.close()
    except mysql.connector.Error as error:
        print("Error executing query:", error)

# Main function
def main():
    conn = connect_to_mysql()
    retrieve_data_from_table(conn)

    # Close the database connection
    if conn is not None:
        conn.close()

if __name__ == "__main__":
    main()