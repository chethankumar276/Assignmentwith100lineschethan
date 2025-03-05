from datetime import datetime

class HotelBooking:
    def __init__(self, total_rooms=10):
        self.total_rooms = total_rooms
        self.booked_rooms = {}
        self.room_prices = {i: 1000 + (i * 100) for i in range(1, total_rooms + 1)}
        self.total_revenue = 0

    def show_available_rooms(self):
        print("\nAvailable Rooms:", [i for i in range(1, self.total_rooms + 1) if i not in self.booked_rooms])

    def book_room(self, name, room_no):
        if room_no in self.booked_rooms:
            print(f"Room {room_no} is already booked!")
        elif room_no < 1 or room_no > self.total_rooms:
            print("Invalid room number!")
        else:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.booked_rooms[room_no] = {"name": name, "date": date, "price": self.room_prices[room_no]}
            self.total_revenue += self.room_prices[room_no]
            print(f"Room {room_no} booked for {name} on {date} at ₹{self.room_prices[room_no]}.")

    def cancel_booking(self, room_no):
        if room_no in self.booked_rooms:
            refund = self.booked_rooms[room_no]["price"]
            self.total_revenue -= refund
            del self.booked_rooms[room_no]
            print(f"Booking for room {room_no} canceled. ₹{refund} refunded.")
        else:
            print(f"No booking found for room {room_no}.")

    def show_booked_rooms(self):
        if not self.booked_rooms:
            print("No rooms are booked yet.")
        else:
            print("\nBooked Rooms:")
            for room, details in self.booked_rooms.items():
                print(f"Room {room}: {details['name']} | Booked on: {details['date']} | Price: ₹{details['price']}")

    def check_in(self, room_no):
        if room_no in self.booked_rooms:
            print(f"{self.booked_rooms[room_no]['name']} has checked into Room {room_no}. Enjoy your stay!")
        else:
            print("Room not booked yet!")

    def check_out(self, room_no):
        if room_no in self.booked_rooms:
            print(f"{self.booked_rooms[room_no]['name']} has checked out from Room {room_no}. Thank you!")
            del self.booked_rooms[room_no]
        else:
            print("No check-in record found for this room.")

    def total_earnings(self):
        print(f"\nTotal Revenue Earned: ₹{self.total_revenue}")

def main():
    hotel = HotelBooking(total_rooms=10)

    while True:
        print("\n1. View Available Rooms")
        print("2. Book a Room")
        print("3. Cancel Booking")
        print("4. Show Booked Rooms")
        print("5. Check-in")
        print("6. Check-out")
        print("7. Show Total Earnings")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            hotel.show_available_rooms()
        elif choice == '2':
            name = input("Enter your name: ")
            room_no = int(input("Enter room number to book: "))
            hotel.book_room(name, room_no)
        elif choice == '3':
            room_no = int(input("Enter room number to cancel: "))
            hotel.cancel_booking(room_no)
        elif choice == '4':
            hotel.show_booked_rooms()
        elif choice == '5':
            room_no = int(input("Enter room number for check-in: "))
            hotel.check_in(room_no)
        elif choice == '6':
            room_no = int(input("Enter room number for check-out: "))
            hotel.check_out(room_no)
        elif choice == '7':
            hotel.total_earnings()
        elif choice == '8':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
    print(hotel)
    print(HotelBooking)