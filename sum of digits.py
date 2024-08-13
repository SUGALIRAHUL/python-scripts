
def sum_of_digits(number):
    Total=0
    while number>0:
        Total += number%10
        number//=10
    return Total
number=int(input("enter a number: "))
print("sum of digits of a given number is: ",sum_of_digits(number))
                 
