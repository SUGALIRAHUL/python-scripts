def extract_digits_reverse(num):
    digits = []
    while num > 0:
        digit = num % 10
        digits.append(digit)
        num //= 10
    return digits

num=int(input("enter a number: "))
reversed_digits=extract_digits_reverse(num)
print("the reverse order of integers is :",reversed_digits)
