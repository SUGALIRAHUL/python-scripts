def calculate_difference(number):
    difference = abs(number - 17)
    if number > 17:
        return 2 * difference
    else:
        return difference

given_number = float(input("Enter a number: "))
difference_ between_numbers = calculate_difference(given_number)
print("the difference of number and 17 is:", difference_ between_numbers )
