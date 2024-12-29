n = int(input("Enter a number: "))
for num in range(1,n+1):
    ctr=0
    for i in range(1,num+1):
        if num%i==0:
            ctr=ctr+1
    if ctr==2:
        print(num,end=" ")


                