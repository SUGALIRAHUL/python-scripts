def calculate_sum(num1, num2, num3):
    if num1 == num2 == num3:
        return 3 * (num1 + num2 + num3)
    else:
        return num1 + num2 + num3

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))
sum_of_three_numbers = calculate_sum(number1, number2, number3)
print("The sum of three numbers:", sum_of_three_numbers)
