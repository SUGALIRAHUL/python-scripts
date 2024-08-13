def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("enter the start of the range: "))
end = int(input("enter the end of the range: "))

print("primr numbers between",start, "and", end,"are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)
