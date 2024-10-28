import mysql.connector as sqlcon

def connect_to_db():
    """Establish a connection to the database."""
    return sqlcon.connect(host='localhost', user='root', passwd='12345', database='project_cs')

def a5_class():
    """Fetch and display the flight class of a passenger."""
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    # Check database connection
    if mydb.is_connected():
        print("Connected to the database.")

    passenger_name = input("Enter passenger name: ")

    # Using parameterized query to prevent SQL injection
    query = "SELECT class FROM airlines5 WHERE passenger_name = %s"
    mycursor.execute(query, (passenger_name,))

    # Fetch the result
    class_info = mycursor.fetchone()

    if class_info:
        print("Class:", class_info[0])
    else:
        print("No class information found for the given passenger name.")

    mydb.close()
