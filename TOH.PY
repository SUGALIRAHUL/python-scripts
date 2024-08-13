def TowerofHanoi(n,source,destination,temp):
    if (n==1):
        print("move disk 1 from source",source,"to destination",destination)
    return
TowerofHanoi:(n-1,source,temp,destination)
print("move disk",n,"from source",source,"to destination",destination)
TowerofHanoi:(n-1,temp,destination,source)
n=int(input("enter no of disks in Tower: "))
TowerofHanoi(n,'A','B','C')
