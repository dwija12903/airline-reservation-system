import mysql.connector as sqlcon

def connect_to_db():
    """Establish a connection to the database."""
    return sqlcon.connect(host='localhost', user='root', passwd='12345', database='project_cs')

# Inserting Details
def a3_insertion():
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    flight_number = input("Flight Number: ")
    aircraft_name = input("Aircraft Name: ")
    capacity = int(input("Capacity: "))
    start_place = input("Start Place: ")
    destination_place = input("Destination Place: ")
    arrival_time = input("Arrival Time (HH:MM:SS): ")
    departure_time = input("Departure Time (HH:MM:SS): ")
    travel_expenses = int(input("Travel Expenses: "))

    query = """
    INSERT INTO airlines_3 
    (flight_number, aircraft_name, capacity, start_place, destination_place, arrival_time, departure_time, travel_expenses) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (flight_number, aircraft_name, capacity, start_place, destination_place, arrival_time, departure_time, travel_expenses)
    
    mycursor.execute(query, values)
    mydb.commit()
    mydb.close()

# Deleting Details
def a3_delete():
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    flight_number = input("Enter flight number whose data is to be deleted: ")
    query = "DELETE FROM airlines_3 WHERE flight_number = %s"
    
    mycursor.execute(query, (flight_number,))
    mydb.commit()
    mydb.close()

# Display Details
def a3_display():
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    query = "SELECT * FROM airlines_3"
    mycursor.execute(query)

    for row in mycursor.fetchall():
        print("\t".join(map(str, row)))

    mydb.close()

# Update Details
def a3_update():
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    new_expense = int(input("Enter travel expenses you want to update: "))
    query = "UPDATE airlines_3 SET travel_expenses = %s WHERE travel_expenses > 4000"

    mycursor.execute(query, (new_expense,))
    mydb.commit()
    mydb.close()

# Booking a Ticket
def a3_booking():
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    print("Details of the table are as follows:")
    a3_display()  # Reusing display function to show available flights

    flight_number = input("Enter the flight number you want to travel: ")
    query = "SELECT * FROM airlines_3 WHERE flight_number = %s"
    mycursor.execute(query, (flight_number,))
    
    flight_details = mycursor.fetchone()
    if flight_details is None:
        print("Sorry, no such flight found.")
    else:
        print("Flight found. Details of flight:")
        print("\t".join(map(str, flight_details)))
        choice = input("Do you want to book a ticket? (yes/no): ").strip().lower()
        if choice == 'yes':
            print("Ticket booked.")
        else:
            print("Ticket not booked.")

    mydb.close()

# Searching a Flight
def a3_search():
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    flight_number = input("Enter a flight number to be searched: ")
    query = "SELECT * FROM airlines_3 WHERE flight_number = %s"
    mycursor.execute(query, (flight_number,))

    flight_details = mycursor.fetchone()
    if flight_details is None:
        print("Sorry, no such flight found.")
    else:
        print("Flight found. Details of flight:")
        print("\t".join(map(str, flight_details)))

    mydb.close()
