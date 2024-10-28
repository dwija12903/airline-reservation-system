import mysql.connector as sqlcon

def connect_to_db():
    """Establish a connection to the database."""
    return sqlcon.connect(host='localhost', user='root', passwd='12345', database='project_cs')

def a6_weight():
    """Fetch and display the allowed weight for a passenger and calculate fines if necessary."""
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    # Check database connection
    if mydb.is_connected():
        print("Connected to the database.")

    passenger_name = input("Enter passenger name: ")

    # Using parameterized query to prevent SQL injection
    query = "SELECT weight_allowed FROM airlines6 WHERE passenger_name = %s"
    mycursor.execute(query, (passenger_name,))

    # Fetch the result
    weight_info = mycursor.fetchone()

    if weight_info:
        weight_allowed = weight_info[0]
        print("Weight that passenger is carrying:", weight_allowed, 'kg', '\t')

        if weight_allowed > 25:
            print("Passenger is not allowed to carry this much weight.")
            fine = (weight_allowed - 25) * 500
            print("Please pay the fine for extra weights carried:", fine)
        else:
            print("Weight is allowed.")
    else:
        print("No weight information found for the given passenger name.")

    mydb.close()