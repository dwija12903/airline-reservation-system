# ✈️ Airline Reservation System

Welcome to the **Airline Reservation System** project! This system allows users to manage flight reservations efficiently through a user-friendly interface.

## 📋 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Database Structure](#database-structure)
- [SQL Connectivity](#sql-connectivity)
- [Installation](#installation)
- [Usage](#usage)
- [Functions Overview](#functions-overview)
- [Flowchart](#flowchart)

## 🚀 Features
- **Reservation Management**: Users can make and manage reservations.
- **Flight Information**: Retrieve details about available flights.
- **Ticket Booking**: Book tickets based on user preference.
- **Weight and Class Information**: Check allowed weight and class of passengers.

## 🛠️ Technologies Used
- Python
- MySQL Connector
- MySQL Database
- Basic SQL Queries

## 🗂️ Database Structure
The system consists of the following tables:

- **`airlines2`**: Contains passenger reservation details.
- **`airlines3`**: Stores information about flights.
- **`airlines5`**: Holds class information for passengers.
- **`airlines6`**: Contains weight restrictions for passengers.

## 🔗 SQL Connectivity
The following outlines how the tables in the database connect with one another:

- **Passenger Information**: The `airlines2` table connects to the `airlines3` table through the `flight_number` field, allowing retrieval of flight details for a given passenger.
- **Class Information**: The `airlines5` table connects to the `airlines2` table through the `passenger_name`, enabling the retrieval of class details associated with each passenger.
- **Weight Restrictions**: The `airlines6` table connects similarly, allowing us to check the weight allowed for each passenger.

This connectivity allows seamless interactions between different functionalities of the reservation system, ensuring that all relevant information can be accessed quickly and efficiently.

## 📥 Installation
To set up this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dwija12903/airline-reservation-system.git
   cd airline-reservation-system
   ```

2. **Install Dependencies**:
   Ensure you have Python installed and run:
   ```bash
   pip install mysql-connector-python
   ```

3. **Set Up MySQL Database**:
   - Create a database named `project_cs`.
   - Execute SQL scripts to create the necessary tables.
   ```bash
        CREATE TABLE IF NOT EXISTS airlines_3 (
            flight_number VARCHAR(10) PRIMARY KEY,
            aircraft_name VARCHAR(50),
            capacity INT,
            start_place VARCHAR(50),
            destination_place VARCHAR(50),
            arrival_time TIME,
            departure_time TIME,
            travel_expenses DECIMAL(10, 2)
        );

        CREATE TABLE IF NOT EXISTS airlines2 (
            pnr_number VARCHAR(20) PRIMARY KEY,
            name_of_the_passenger VARCHAR(100),
            status_of_reservation VARCHAR(20),
            seat_number VARCHAR(10),
            phone VARCHAR(15),
            amount_paid DECIMAL(10, 2),
            flight_number VARCHAR(10),
            age INT,
            sex CHAR(1),
            FOREIGN KEY (flight_number) REFERENCES airlines_3(flight_number)
        );

        CREATE TABLE IF NOT EXISTS airlines5 (
            passenger_name VARCHAR(100),
            class VARCHAR(20)
        );

        CREATE TABLE IF NOT EXISTS airlines6 (
            passenger_name VARCHAR(100),
            weight_allowed INT
        );

   ```

## 🔧 Usage
1. Run the application:
   ```bash
   python AirlineManagemetSystem.py
   ```

## 📊 Functions Overview
- **`a2_reservation()`**: Manage passenger reservations.
- **`a3_insertion()`**: Insert new flight details.
- **`a3_delete()`**: Remove flight records.
- **`a3_display()`**: Display all flights.
- **`a3_update()`**: Update flight expenses.
- **`a3_booking()`**: Book a ticket for a flight.
- **`a3_search()`**: Search for a specific flight.
- **`a5_class()`**: Fetch the class information for passengers.
- **`a6_weight()`**: Check allowed weight for passengers and calculate fines.
- **`a7_passengerticket()`**: Display ticket information for a passenger.
```bash 
                             +------------------------+
                             |   Start Program        |
                             +------------------------+
                                         |
                                         v
                             +------------------------+
                             |   Display Main Menu    |
                             +------------------------+
                                         |
                    +-------------------+-------------------+
                    |                   |                   |
                    v                   v                   v
             +------------+      +--------------+      +--------------+
             |   a3_booking|<---+   a3_display  |      |   a3_search  |
             +------------+      +--------------+      +--------------+
                    |                   |
                    |                   |
                    v                   v
              +-------------+     +---------------+
              | a3_insertion|     |  a3_update    |
              +-------------+     +---------------+
                    |
                    v
             +------------------+
             |  a3_delete       |
             +------------------+
                    |
                    v
          +--------------------+
          |   a2_reservation   |
          +--------------------+
                    |
                    v
          +---------------------+
          |    a7_passengerticket|
          +---------------------+
                    |
                    v
          +---------------------+
          |    a6_weight         |
          +---------------------+
                    |
                    v
          +---------------------+
          |     a5_class        |
          +---------------------+

```

## 📈 Flowchart
The following flowchart illustrates the overall functionality and flow of data within the Airline Reservation System:
```bash 
+------------------+      +------------------+
|    airlines2     |      |    airlines3     |
|------------------|      |------------------|
| pnr_number       |<-----| flight_number (PK)|
| status_of_resv.  |      | aircraft_name    |
| seat_number      |      | capacity         |
| name_of_pass.    |      | start_place      |
| phone            |      | destination_place |
| amount_paid      |      | arrival_time     |
| flight_number (FK)|----->| departure_time   |
| age              |      | travel_expenses  |
| sex              |      +------------------+
+------------------+         

         |
         |
         v

+------------------+
|     airlines5    |
|------------------|
| passenger_name   |
| class            |
+------------------+

         |
         |
         v

+------------------+
|     airlines6    |
|------------------|
| passenger_name   |
| weight_allowed    |
+------------------+
```
This flowchart showcases how user interactions lead to various operations in the database, ensuring a seamless user experience.

---

Thank you for checking out the Airline Reservation System! If you have any questions or suggestions, feel free to reach out. Happy coding! ✨