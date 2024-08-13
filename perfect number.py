num=int(input("enter a number: "))
sum=0
for i in range(1,num):
    n=num%i
    if(num==0):
     sum=sum+i
if(sum==num):
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")
