num=int(input("enter a number: "))
sum=0
temp=num
while num>0:
    rem=num%10
    sum=sum+(rem*rem*rem)
    num=num//10
    if(num==temp):
        print("number is armstrong")

    else:
        print("number is not a ARMSTRONG")
    
