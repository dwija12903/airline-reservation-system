# Importing modules from libraries
import mysql.connector as sqlcon

# Connecting with MySQL
mydb = sqlcon.connect(host='localhost', user='root', passwd='12345', database='project_cs')
print("Connected:", mydb.is_connected())
mycursor = mydb.cursor()

# Main Program - Menu
print("====================================================================")
print("                        Airlines Management System                   ")
print("====================================================================")
print("Please select an option:")
print("1: INSERTION")
print("2: DELETION")
print("3: DISPLAY")
print("4: UPDATE")
print("5: SEE IF THE FLIGHT IS AVAILABLE")
print("6: BOOKING A TICKET")
print("7: RESERVATION SLIP")
print("8: CLASS OF TRAVEL")
print("9: WEIGHT ALLOWED")
choice = int(input("Select a choice (1-9): "))

# Inserting Details
if choice == 1:
    print("====================================================================")
    print("                          INSERTION                                ")
    print("====================================================================")
    a = input("Flight Number: ")
    b = input("Aircraft Name: ")
    c = int(input("Capacity: "))
    d = input("Start Place: ")
    e = input("Destination Place: ")
    f = input("Arrival Time: ")
    g = input("Departure Time: ")
    h = int(input("Travel Expenses: "))

    query = (
        "INSERT INTO airlines_3 "
        "(flight_number, aircraft_name, capacity, start_place, destination_place, "
        "arrival_time, departure_time, travel_expenses) "
        "VALUES ('{}', '{}', {}, '{}', '{}', '{}', '{}', {})"
    ).format(a, b, c, d, e, f, g, h)
    mycursor.execute(query)
    mydb.commit()

# Deleting Details
elif choice == 2:
    print("====================================================================")
    print("                           DELETION                                 ")
    print("====================================================================")
    numflight = input("Enter flight number to delete: ")
    query = "DELETE FROM airlines_3 WHERE flight_number='{}'".format(numflight)
    mycursor.execute(query)
    mydb.commit()

# Display Details
elif choice == 3:
    print("====================================================================")
    print("                   DETAILS OF ALL AVAILABLE FLIGHTS                 ")
    print("====================================================================")
    query = "SELECT * FROM airlines_3"
    mycursor.execute(query)
    for row in mycursor:
        print("\t".join(map(str, row)))
    mydb.commit()

# Update Details
elif choice == 4:
    print("====================================================================")
    print("                             UPDATE                                 ")
    print("====================================================================")
    query = "UPDATE airlines_3 SET travel_expenses = 6000 WHERE travel_expenses > 4000"
    mycursor.execute(query)
    mydb.commit()

# Booking a Ticket
elif choice == 6:
    print("====================================================================")
    print("                       BOOKING A TICKET                             ")
    print("====================================================================")
    query = "SELECT * FROM airlines_3"
    mycursor.execute(query)
    print("Details of the available flights:")
    for row in mycursor:
        print("\t".join(map(str, row)))
    mydb.commit()

    num = input("Enter the flight number you want to book: ")
    query = "SELECT * FROM airlines_3 WHERE flight_number='{}'".format(num)
    mycursor.execute(query)
    if not mycursor.fetchall():
        print("Sorry, no such flight found.")
    else:
        print("Flight found. Details:")
        mycursor.execute(query)
        for row in mycursor:
            print("\t".join(map(str, row)))

# Searching for a Flight
elif choice == 5:
    print("====================================================================")
    print("                           SEARCHING                                ")
    print("====================================================================")
    f = input("Enter flight number to search: ")
    query = "SELECT * FROM airlines_3 WHERE flight_number='{}'".format(f)
    mycursor.execute(query)
    if not mycursor.fetchall():
        print("Sorry, no such flight found.")
    else:
        print("Flight found. Details:")
        mycursor.execute(query)
        for row in mycursor:
            print("\t".join(map(str, row)))

# Reservation Slip
elif choice == 7:
    print("====================================================================")
    print("                         RESERVATION SLIP                           ")
    print("====================================================================")
    name = input("Enter name: ")
    query = "SELECT * FROM airlines2 WHERE name_of_the_passenger='{}'".format(name)
    mycursor.execute(query)
    for row in mycursor:
        print("\t".join(map(str, row)))

    print("--------------------------------------------------------------------")
    reservation_details = [
        ("PNR Number", "pnr_number"),
        ("Status", "status_of_reservation"),
        ("Seat Number", "seat_number"),
        ("Name", "name_of_the_passenger"),
        ("Phone", "phone"),
        ("Amount Paid", "amount_paid"),
        ("Flight Number", "flight_number"),
        ("Age", "age"),
        ("Sex", "sex")
    ]

    for label, col in reservation_details:
        query = f"SELECT {col} FROM airlines2 WHERE name_of_the_passenger='{name}'"
        mycursor.execute(query)
        for row in mycursor:
            print(f"{label}: {row[0]}")

# Class of Travel
elif choice == 8:
    print("====================================================================")
    print("                         CLASS OF TRAVEL                            ")
    print("====================================================================")
    name = input("Enter passenger name: ")
    query = "SELECT class FROM airlines5 WHERE passenger_name='{}'".format(name)
    mycursor.execute(query)
    for row in mycursor:
        print("Class:", row[0])

# Weight Allowed
elif choice == 9:
    print("====================================================================")
    print("                         WEIGHT ALLOWED                             ")
    print("====================================================================")
    name = input("Enter passenger name: ")
    query = "SELECT weight_allowed FROM airlines6 WHERE passenger_name='{}'".format(name)
    mycursor.execute(query)
    for row in mycursor:
        weight = row[0]
        print("Allowed weight:", weight, "kg")
        if weight > 25:
            fine = (weight - 25) * 500
            print(f"Excess weight fine: {fine}")
