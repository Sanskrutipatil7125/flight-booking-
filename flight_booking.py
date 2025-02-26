import sqlite3
import tkinter as tk
from tkinter import messagebox

def fetch_flights():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flights")
    flights = cursor.fetchall()
    conn.close()
    
    flights_list.delete(0, tk.END)
    for flight in flights:
        flights_list.insert(tk.END, f"{flight[0]} - {flight[1]} ({flight[2]} to {flight[3]}) - ₹{flight[4]}")


def book_flight():
    selected = flights_list.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select a flight!")
        return
    
    flight_id = flights_list.get(selected[0]).split(" - ")[0]
    passenger_name = name_entry.get()

    if not passenger_name:
        messagebox.showerror("Error", "Please enter passenger name!")
        return

    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings (flight_id, passenger_name) VALUES (?, ?)", (flight_id, passenger_name))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", "Flight booked successfully!")
    name_entry.delete(0, tk.END)

# GUI Setup
app = tk.Tk()
app.title("Flight Booking System")

tk.Label(app, text="Available Flights:").pack()
flights_list = tk.Listbox(app, width=50, height=10)
flights_list.pack()

fetch_button = tk.Button(app, text="Load Flights", command=fetch_flights)
fetch_button.pack()

tk.Label(app, text="Passenger Name:").pack()
name_entry = tk.Entry(app)
name_entry.pack()

book_button = tk.Button(app, text="Book Flight", command=book_flight)
book_button.pack()

app.mainloop()
