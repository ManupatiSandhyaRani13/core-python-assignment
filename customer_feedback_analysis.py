def calculate_percentage(ratings):
    if not ratings:
        print("No ratings provided")
        return 0
    positive_rating_count = sum(1 for rating in ratings if rating >= 4)
    percentage = (positive_rating_count * 100) / len(ratings)
    return percentage
ratings = []
while True:
    user_input = input("Enter rating between 1-5 or type 'exit' to stop: ")
    if user_input.lower() == 'exit':
        break
    else:
        try:
            n = int(user_input)
            if 1 <= n <= 5:
                ratings.append(n)
            else:
                print("Invalid rating! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 5.")
print("ratings: ", ratings)
positive_percentage = calculate_percentage(ratings)
if positive_percentage != 0:
    print(f"Positive Feedback: {positive_percentage:.1f}%")
