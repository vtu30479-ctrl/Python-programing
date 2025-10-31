def seat_details(seat_list, index):
    try:
        seat = seat_list[index]
        print("Seat Details:")
        print("Seat Number:", seat.get("number"))
        print("Section:", seat.get("section"))
        print("Availability:", "Booked" if seat.get("is_booked") else "Available")
    except IndexError:
        print("Invalid seat index. Please select a valid seat.")

seats = [
{"number": "A1", "section": "VIP", "is_booked": False},
{"number": "A2", "section": "VIP", "is_booked": True},
{"number": "B1", "section": "General", "is_booked": False},
{"number": "B2", "section": "General", "is_booked": False}
]

try:
    seat_index = int(input("Enter the index of the seat you want to view: "))
    seat_details(seats, seat_index)
except ValueError:
    print("Invalid input. Please enter a valid seat index (integer).")
