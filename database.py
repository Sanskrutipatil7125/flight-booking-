import sqlite3

def create_database():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS flights (
                        id INTEGER PRIMARY KEY,
                        airline TEXT,
                        origin TEXT,
                        destination TEXT,
                        price REAL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                        id INTEGER PRIMARY KEY,
                        flight_id INTEGER,
                        passenger_name TEXT,
                        FOREIGN KEY(flight_id) REFERENCES flights(id))''')

    # Insert sample flights
    cursor.execute("INSERT INTO flights (airline, origin, destination, price) VALUES ('Air India', 'Delhi', 'Mumbai', 7500)")
    cursor.execute("INSERT INTO flights (airline, origin, destination, price) VALUES ('Indigo', 'Bangalore', 'Chennai', 2500)")
    cursor.execute("INSERT INTO flights (airline, origin, destination, price) VALUES ('Indigo', 'Pune', 'Delhi', 6200)")
    cursor.execute("INSERT INTO flights (airline, origin, destination, price) VALUES ('Akasha', 'Bangalore', 'Goa', 1390)")
    cursor.execute("INSERT INTO flights (airline, origin, destination, price) VALUES ('Indigo', 'Delhi', 'Hydrabad',9500)")
    conn.commit()
    conn.close()

create_database()
