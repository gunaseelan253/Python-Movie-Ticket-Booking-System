import random

movies = {
    1: ("Leo", 150),
    2: ("Jailer", 180),
    3: ("GOAT", 200),
    4: ("Vikram", 170)
}

bookings = {}

def show_movies():
    print("\n========== AVAILABLE MOVIES ==========")
    for number, details in movies.items():
        print(number, ".", details[0], "- Rs.", details[1])


def book_ticket():
    show_movies()

    try:
        movie_choice = int(input("\nEnter movie number: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if movie_choice not in movies:
        print("Invalid movie selection.")
        return

    movie_name, price = movies[movie_choice]

    name = input("Enter customer name: ")

    try:
        tickets = int(input("Enter number of tickets: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if tickets <= 0:
        print("Number of tickets must be greater than 0.")
        return

    print("\nAvailable Seats:")
    print("A1 A2 A3 A4 A5")
    print("B1 B2 B3 B4 B5")
    print("C1 C2 C3 C4 C5")

    seats = input("Enter seat numbers separated by comma: ")
    seat_list = [seat.strip().upper() for seat in seats.split(",")]

    if len(seat_list) != tickets:
        print("Number of seats must match number of tickets.")
        return

    booking_id = "BK" + str(random.randint(1000, 9999))
    total = price * tickets

    bookings[booking_id] = {
        "name": name,
        "movie": movie_name,
        "tickets": tickets,
        "seats": seat_list,
        "price": price,
        "total": total
    }

    print("\n======================================")
    print("          BOOKING CONFIRMED")
    print("======================================")
    print("Booking ID    :", booking_id)
    print("Customer Name :", name)
    print("Movie         :", movie_name)
    print("Tickets       :", tickets)
    print("Seats         :", ", ".join(seat_list))
    print("Ticket Price  : Rs.", price)
    print("Total Amount  : Rs.", total)
    print("======================================")


def view_booking():
    booking_id = input("\nEnter Booking ID: ").upper()

    if booking_id not in bookings:
        print("Booking not found.")
        return

    booking = bookings[booking_id]

    print("\n========== BOOKING DETAILS ==========")
    print("Booking ID    :", booking_id)
    print("Customer Name :", booking["name"])
    print("Movie         :", booking["movie"])
    print("Tickets       :", booking["tickets"])
    print("Seats         :", ", ".join(booking["seats"]))
    print("Total Amount  : Rs.", booking["total"])
    print("=====================================")


def cancel_booking():
    booking_id = input("\nEnter Booking ID to cancel: ").upper()

    if booking_id in bookings:
        del bookings[booking_id]
        print("Booking cancelled successfully.")
    else:
        print("Booking not found.")


while True:

    print("\n======================================")
    print("       MOVIE TICKET BOOKING SYSTEM")
    print("======================================")
    print("1. View Movies")
    print("2. Book Ticket")
    print("3. View Booking")
    print("4. Cancel Booking")
    print("5. Exit")
    print("======================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        show_movies()

    elif choice == 2:
        book_ticket()

    elif choice == 3:
        view_booking()

    elif choice == 4:
        cancel_booking()

    elif choice == 5:
        print("\nThank you for using Movie Ticket Booking System!")
        break

    else:
        print("Invalid choice. Please try again.")
