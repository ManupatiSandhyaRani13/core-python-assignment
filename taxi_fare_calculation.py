def calculate_fare(trips):
    if not trips:
        print("No trips are provided")
        return 0
    total_fare = 0
    for i, trip in enumerate(trips, 1):
        fare = 50 + (trip * 10)
        total_fare += fare
        print(f"Trip {i}: ${fare}")
    print(f"Total Fare: ${total_fare}")
trips = []
base_fare = 50
distance_fare = 10
while True:
    user_input = input("Enter the distance in km or type 'exit' to stop: ")
    if user_input.lower() == 'exit':
        break
    distance = int(user_input)
    if distance > 0:
        trips.append(distance)
    else:
        print("Invalid Distance! Distance should be a positive number.")
print("Trips:", trips)
calculate_fare(trips)
