import mysql.connector as sqlcon

def a2_reservation():
    # Connecting to MySQL
    mydb = sqlcon.connect(host='localhost', user='root', passwd='12345', database='project_cs')
    if mydb.is_connected():
        print("Connected to database")
    mycursor = mydb.cursor()

    name = input("Enter name: ")

    # Display reservation details
    print("Reservation Details:")
    query = "SELECT * FROM airlines2 WHERE name_of_the_passenger = %s"
    mycursor.execute(query, (name,))
    result = mycursor.fetchall()
    
    if result:
        for row in result:
            print("\t".join(map(str, row)))

        # Reservation Slip
        print("\nYour reservation slip:")
        print("--------------------------------------------------------------------")

        # Retrieve and display individual fields from airlines2
        fields = {
            "PNR Number": "pnr_number",
            "Status": "status_of_reservation",
            "Seat Number": "seat_number",
            "Name": "name_of_the_passenger",
            "Phone Number": "phone",
            "Amount Paid": "amount_paid",
            "Flight Number": "flight_number",
            "Age": "age",
            "Sex": "sex"
        }
        
        for label, column in fields.items():
            query = f"SELECT {column} FROM airlines2 WHERE name_of_the_passenger = %s"
            mycursor.execute(query, (name,))
            for row in mycursor:
                print(f"{label}: {row[0]}")

        print("--------------------------------------------------------------------")
    else:
        print("No reservation found for this name.")
    
    mydb.commit()
    mydb.close()
