import Reservations2
import FlightDetails3
import ClassOfTravel4
import Baggage5
import Tickets6

def menuairlines3():
    """Menu for Airlines Management System."""
    while True:
        print("=========================================================================")
        print("                     Airlines Management System")
        print("=========================================================================")
        print("1: INSERTION")
        print("2: DELETION")
        print("3: DISPLAY")
        print("4: UPDATE")
        print("5: SEE IF THE FLIGHT IS AVAILABLE")
        print("6: BOOKING A TICKET")
        print("Select a choice (1-6):")

        try:
            choice = int(input("Enter a choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue  # Go to the next iteration of the loop

        if choice == 1:
            FlightDetails3.a3_insertion()
        elif choice == 2:
            FlightDetails3.a3_delete()
        elif choice == 3:
            FlightDetails3.a3_display()
        elif choice == 4:
            FlightDetails3.a3_update()
        elif choice == 5:
            FlightDetails3.a3_search()
        elif choice == 6:
            FlightDetails3.a3_booking()
        else:
            print("Invalid choice. Please select a valid option.")

def menuairlines2():
    """Menu for Reservation Slip."""
    while True:
        print("=========================================================================")
        print("                          Reservation Slip")
        print("=========================================================================")
        print("7: RESERVATION SLIP")

        Reservations2.a2_reservation()
        # Option to continue or exit could be added here if necessary

def menuairlines5():
    """Menu for Class of Travel."""
    while True:
        print("=========================================================================")
        print("                           Class of Travel")
        print("=========================================================================")
        print("8: CLASS OF TRAVEL")

        ClassOfTravel4.a5_class()
        # Option to continue or exit could be added here if necessary

def menuairlines6():
    """Menu for Weights Allowed."""
    while True:
        print("=========================================================================")
        print("                           Weights Allowed")
        print("=========================================================================")
        print("9: WEIGHT ALLOWED")

        Baggage5.a6_weight()
        # Option to continue or exit could be added here if necessary

def menuairlines7():
    """Menu for Passenger Ticket."""
    while True:
        print("=========================================================================")
        print("                           Passenger Ticket")
        print("=========================================================================")

        Tickets6.a7_passengerticket()
        # Option to continue or exit could be added here if necessary
