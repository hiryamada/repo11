import psycopg2
from psycopg2 import Error

def main():
    """
    Basic PostgreSQL SELECT query example
    """
    try:
        # Connect to PostgreSQL database
        connection = psycopg2.connect(
            host="localhost",
            database="your_database",
            user="your_username",
            password="your_password",
            port="5432"
        )
        
        # Create a cursor object
        cursor = connection.cursor()
        
        # Execute a simple SELECT query
        cursor.execute("SELECT version();")
        
        # Fetch the result
        db_version = cursor.fetchone()
        print("PostgreSQL database version:")
        print(db_version)
        
        # Example: SELECT query from a table
        # Uncomment and modify the following lines to query your own table
        # cursor.execute("SELECT * FROM your_table LIMIT 10;")
        # records = cursor.fetchall()
        # for row in records:
        #     print(row)
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        
    finally:
        # Close database connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    main()
