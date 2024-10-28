import mysql.connector as sqlcon
import menu

def connect_to_db():
    """Establish a connection to the database."""
    return sqlcon.connect(host='localhost', user='root', passwd='12345', database='project_cs')

def main():
    """Main function to run the Airlines Reservation System."""
    mydb = connect_to_db()
    mycursor = mydb.cursor()

    while True:
        print("=" * 75)
        print(" " * 25 + "Airlines Reservation System")
        print("=" * 75)
        print("1: AIRLINES MANAGEMENT")
        print("2: RESERVATION SLIP")
        print("3: CLASS OF TRAVEL")
        print("4: WEIGHTS ALLOWED")
        print("5: PASSENGER TICKET")
        print("6: EXIT")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue  # Go to the next iteration of the loop

        if choice == 1:
            menu.menuairlines3()
        elif choice == 2:
            menu.menuairlines2()
        elif choice == 3:
            menu.menuairlines5()
        elif choice == 4:
            menu.menuairlines6()
        elif choice == 5:
            menu.menuairlines7()
        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    mydb.close()  # Close the database connection when done

if __name__ == "__main__":
    main()
