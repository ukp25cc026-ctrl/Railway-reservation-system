# 🚂 Railway Reservation System

A Python-based command-line application for managing railway ticket bookings with ease.

---

## 📌 Features

| Feature | Description |
|---|---|
| ✅ Check Availability | View total, booked, and available seats |
| 🎟️ Book Ticket | Enter name & age, get assigned seat + unique Booking ID |
| 🔍 View Ticket | Retrieve full booking details using Booking ID |
| ❌ Cancel Ticket | Cancel an active booking and free up the seat |
| 📋 View All Bookings | Admin view of all reservations with status |

---

## 🛠️ How to Run

### Prerequisites
- Python 3.6 or higher

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/railway-reservation-system.git

# 2. Navigate into the project folder
cd railway-reservation-system

# 3. Run the program
python main.py
```

No external libraries required — uses only Python's built-in modules (`random`, `string`, `datetime`).

---

## 🗂️ Project Structure

```
railway-reservation-system/
│
├── main.py        # Main application file
└── README.md      # Project documentation
```

---

## 🖥️ Sample Usage

```
╔══════════════════════════════════════════════════════╗
║        🚂  RAILWAY RESERVATION SYSTEM  🚂            ║
║            Welcome! Your journey starts here.        ║
╚══════════════════════════════════════════════════════╝

  MAIN MENU
  [1]  Check Seat Availability
  [2]  Book a Ticket
  [3]  View Ticket Details
  [4]  Cancel a Ticket
  [5]  View All Bookings
  [6]  Exit
```

### Booking a Ticket
```
  Enter Passenger Name : Alice
  Enter Passenger Age  : 28

  ✅  Booking Successful!
  ───────────────────────────────────────────────────────
    Booking ID   : RLW-A3F9KZ
    Passenger    : Alice
    Age          : 28
    Seat Number  : 1
    Booked On    : 2026-04-27 10:30:00
    Status       : CONFIRMED
```

---

## ⚙️ System Configuration

- **Total Seats:** 50 (configurable via `TOTAL_SEATS` constant in `main.py`)
- **Data Storage:** In-memory dictionary (no database required)
- **Booking ID Format:** `RLW-XXXXXX` (e.g., `RLW-A3F9KZ`)

---

## 🧪 Test Scenarios

1. **Multiple Bookings** — Book several tickets and verify seat assignments are unique
2. **Full Capacity** — Fill all 50 seats and confirm no more bookings are accepted
3. **Cancellation** — Cancel a booking and verify the seat becomes available again
4. **Invalid Input** — Enter wrong Booking IDs or invalid ages to test error handling

---

## 👨‍💻 Author

Developed as part of a Python project challenge for learning GitHub workflows and building CLI applications.

---

## 📄 License

This project is open-source and available for educational use.
