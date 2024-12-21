def seat_booking(booked_seats,n):
    if n < 1 or n > tot_seats:
        print(f"Invalid seat number! Please choose a seat between 1 and {tot_seats}.")
    elif n in booked_seats:
        print(f"The seat {n} is already booked")
    else:
        booked_seats.append(n)
        print(f"The seat {n} is  booked successfully")
    print("Booked seats:",sorted(booked_seats))
def cancel_seat(booked_seats,n1):
    if n1 in booked_seats:
        booked_seats.remove(n1)
        print(f"The seat {n1} is  cancelled")
    else:
        print("The seat is not booked yet.. can't cancel the seat")
def display(booked_seats, tot_seats):
    available_seats = []
    i=1
    for i in range(1,tot_seats+1):
        if i not in booked_seats:
            available_seats.append(i)
    print(f"Available seats:", sorted(available_seats))
booked_seats = []
tot_seats=int(input("Enter the total seats available: "))
value=input("Enter the booked seats  : ")
booked_seats=[int(value.strip()) for value in value.split(",")]
while True:
    print("1.Book Ticket\n2.Cancel Ticket\n3.Display\n4.1Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        n = int(input("Enter the seat to be booked :"))
        seat_booking(booked_seats, n)
        display(booked_seats, tot_seats)
    elif choice == 2:
        n1 = int(input("Enter the seat to be cancelled : "))
        cancel_seat(booked_seats, n1)
        display(booked_seats,tot_seats)
    elif choice == 3:
        display(booked_seats, tot_seats)
    else:
        exit(0)


