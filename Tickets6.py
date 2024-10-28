import mysql.connector as sqlcon

def connect_to_db():
    """Establish a connection to the database."""
    return sqlcon.connect(host='localhost', user='root', passwd='12345', database='project_cs')

def a7_passengerticket():
    """Fetch and display the ticket information for a passenger."""
    passenger_name = input("Enter your name: ")
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    # Check database connection
    if mydb.is_connected():
        print("Connected to the database.")

    # Flight Number
    query_flight = "SELECT flight_number FROM airlines2 WHERE name_of_the_passenger = %s"
    mycursor.execute(query_flight, (passenger_name,))
    flight_info = mycursor.fetchone()
    if flight_info:
        print("FLIGHT NUMBER:", flight_info[0], '\t')
    else:
        print("No flight number found for the passenger.")

    # Start Place
    query_start = """
    SELECT start_place FROM airlines_3
    JOIN airlines2 ON airlines2.flight_number = airlines_3.flight_number
    WHERE name_of_the_passenger = %s
    """
    mycursor.execute(query_start, (passenger_name,))
    start_info = mycursor.fetchone()
    if start_info:
        print("START PLACE:", start_info[0], '\t')
    else:
        print("No start place found for the passenger.")

    # Destination Place
    query_destination = """
    SELECT destination_place FROM airlines_3
    JOIN airlines2 ON airlines2.flight_number = airlines_3.flight_number
    WHERE name_of_the_passenger = %s
    """
    mycursor.execute(query_destination, (passenger_name,))
    destination_info = mycursor.fetchone()
    if destination_info:
        print("DESTINATION PLACE:", destination_info[0], '\t')
    else:
        print("No destination place found for the passenger.")

    # Passenger Name
    query_name = "SELECT name_of_the_passenger FROM airlines2 WHERE name_of_the_passenger = %s"
    mycursor.execute(query_name, (passenger_name,))
    name_info = mycursor.fetchone()
    if name_info:
        print("NAME:", name_info[0], '\t')
    else:
        print("No name information found for the passenger.")

    # Fare
    query_fare = """
    SELECT travel_expenses FROM airlines_3
    JOIN airlines2 ON airlines2.flight_number = airlines_3.flight_number
    WHERE name_of_the_passenger = %s
    """
    mycursor.execute(query_fare, (passenger_name,))
    fare_info = mycursor.fetchone()
    if fare_info:
        print("FARE:", fare_info[0], '\t')
    else:
        print("No fare information found for the passenger.")

    mydb.close()
