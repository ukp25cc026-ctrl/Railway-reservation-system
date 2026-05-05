"""
╔══════════════════════════════════════════════════════════╗
║          RAILWAY RESERVATION SYSTEM                      ║
║          Python-Based Ticket Booking System              ║
╚══════════════════════════════════════════════════════════╝
"""

import random
import string
from datetime import datetime

# ──────────────────────────────────────────────
#  CONFIGURATION
# ──────────────────────────────────────────────
TOTAL_SEATS = 50

# Storage
reservations = {}          # booking_id -> booking details
booked_seats  = set()      # seat numbers that are taken

# ──────────────────────────────────────────────
#  HELPER UTILITIES
# ──────────────────────────────────────────────

def generate_booking_id():
    """Generate a unique 8-character alphanumeric booking ID."""
    while True:
        bid = "RLW-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
        if bid not in reservations:
            return bid

def get_available_seats():
    """Return a sorted list of available seat numbers."""
    all_seats = set(range(1, TOTAL_SEATS + 1))
    return sorted(all_seats - booked_seats)

def assign_seat():
    """Assign the next available seat."""
    available = get_available_seats()
    return available[0] if available else None

def print_divider(char="─", width=55):
    print(char * width)

def print_header(title):
    print_divider("═")
    print(f"  {title}")
    print_divider("═")

def print_ticket(booking):
    """Pretty-print a single ticket."""
    print_divider()
    print(f"  {'BOOKING CONFIRMATION':^51}")
    print_divider()
    print(f"  Booking ID   : {booking['booking_id']}")
    print(f"  Passenger    : {booking['name']}")
    print(f"  Age          : {booking['age']}")
    print(f"  Seat Number  : {booking['seat']}")
    print(f"  Booked On    : {booking['booked_on']}")
    print(f"  Status       : {booking['status']}")
    print_divider()

# ──────────────────────────────────────────────
#  FEATURE 1 – CHECK AVAILABILITY
# ──────────────────────────────────────────────

def check_availability():
    print_header("SEAT AVAILABILITY")
    available = get_available_seats()
    booked_count = len(booked_seats)
    available_count = len(available)

    print(f"  Total Seats     : {TOTAL_SEATS}")
    print(f"  Booked Seats    : {booked_count}")
    print(f"  Available Seats : {available_count}")
    print_divider()

    if available_count == 0:
        print("  ⚠  No seats available. The train is fully booked!")
    else:
        # Display available seats in rows of 10
        print("  Available Seat Numbers:")
        for i, seat in enumerate(available, 1):
            print(f"  {seat:>3}", end="")
            if i % 10 == 0:
                print()
        print()
    print_divider()

# ──────────────────────────────────────────────
#  FEATURE 2 – BOOK TICKET
# ──────────────────────────────────────────────

def book_ticket():
    print_header("BOOK A TICKET")

    if len(booked_seats) >= TOTAL_SEATS:
        print("  ⚠  Sorry! No seats are available. Train is fully booked.")
        print_divider()
        return

    # Collect passenger details
    while True:
        name = input("  Enter Passenger Name : ").strip()
        if name:
            break
        print("  ⚠  Name cannot be empty. Please try again.")

    while True:
        age_input = input("  Enter Passenger Age  : ").strip()
        if age_input.isdigit() and 1 <= int(age_input) <= 120:
            age = int(age_input)
            break
        print("  ⚠  Please enter a valid age (1–120).")

    # Assign seat and create booking
    seat = assign_seat()
    booking_id = generate_booking_id()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    booking = {
        "booking_id": booking_id,
        "name": name,
        "age": age,
        "seat": seat,
        "booked_on": timestamp,
        "status": "CONFIRMED",
    }

    reservations[booking_id] = booking
    booked_seats.add(seat)

    print()
    print("  ✅  Booking Successful!")
    print_ticket(booking)

# ──────────────────────────────────────────────
#  FEATURE 3 – VIEW TICKET
# ──────────────────────────────────────────────

def view_ticket():
    print_header("VIEW TICKET DETAILS")

    booking_id = input("  Enter Booking ID : ").strip().upper()

    if booking_id in reservations:
        print()
        print_ticket(reservations[booking_id])
    else:
        print(f"\n  ⚠  No booking found for ID: {booking_id}")
        print_divider()

# ──────────────────────────────────────────────
#  FEATURE 4 – CANCEL TICKET
# ──────────────────────────────────────────────

def cancel_ticket():
    print_header("CANCEL TICKET")

    booking_id = input("  Enter Booking ID to Cancel : ").strip().upper()

    if booking_id not in reservations:
        print(f"\n  ⚠  No booking found for ID: {booking_id}")
        print_divider()
        return

    booking = reservations[booking_id]

    if booking["status"] == "CANCELLED":
        print(f"\n  ⚠  Booking {booking_id} is already cancelled.")
        print_divider()
        return

    # Confirm cancellation
    print()
    print_ticket(booking)
    confirm = input("  Are you sure you want to cancel this booking? (yes/no): ").strip().lower()

    if confirm == "yes":
        booked_seats.discard(booking["seat"])
        reservations[booking_id]["status"] = "CANCELLED"
        print(f"\n  ✅  Booking {booking_id} has been successfully cancelled.")
        print(f"     Seat {booking['seat']} is now available.")
    else:
        print("\n  Cancellation aborted. Your booking remains active.")

    print_divider()

# ──────────────────────────────────────────────
#  BONUS – VIEW ALL BOOKINGS (admin helper)
# ──────────────────────────────────────────────

def view_all_bookings():
    print_header("ALL RESERVATIONS")

    if not reservations:
        print("  No reservations found.")
        print_divider()
        return

    active    = [b for b in reservations.values() if b["status"] == "CONFIRMED"]
    cancelled = [b for b in reservations.values() if b["status"] == "CANCELLED"]

    print(f"  Total Bookings   : {len(reservations)}")
    print(f"  Active Bookings  : {len(active)}")
    print(f"  Cancelled        : {len(cancelled)}")
    print_divider()

    for booking in reservations.values():
        status_icon = "✅" if booking["status"] == "CONFIRMED" else "❌"
        print(f"  {status_icon} {booking['booking_id']}  |  Seat {booking['seat']:>2}  |  "
              f"{booking['name']:<20}  |  Age {booking['age']:>3}  |  {booking['status']}")

    print_divider()

# ──────────────────────────────────────────────
#  MAIN MENU
# ──────────────────────────────────────────────

def main():
    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║        🚂  RAILWAY RESERVATION SYSTEM  🚂            ║")
    print("║            Welcome! Your journey starts here.        ║")
    print("╚══════════════════════════════════════════════════════╝")

    menu_options = {
        "1": ("Check Seat Availability",  check_availability),
        "2": ("Book a Ticket",            book_ticket),
        "3": ("View Ticket Details",      view_ticket),
        "4": ("Cancel a Ticket",          cancel_ticket),
        "5": ("View All Bookings",        view_all_bookings),
        "6": ("Exit",                     None),
    }

    while True:
        print()
        print_divider("─")
        print("  MAIN MENU")
        print_divider("─")
        for key, (label, _) in menu_options.items():
            print(f"  [{key}]  {label}")
        print_divider("─")

        choice = input("  Enter your choice (1–6): ").strip()

        if choice not in menu_options:
            print("  ⚠  Invalid choice. Please enter a number between 1 and 6.")
            continue

        label, action = menu_options[choice]

        if choice == "6":
            print()
            print("  Thank you for using the Railway Reservation System!")
            print("  Have a safe journey! 🚆")
            print_divider("═")
            break

        print()
        action()

# ──────────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────────

if __name__ == "__main__":
    main()