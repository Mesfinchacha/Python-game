n=int(input("Enter a number"))
fact=1
if n>=0:
    for i in range(1,n+1):
        if n==0 and n==1:
            print("fact=",1)
        else:
            fact*=i
    print("fact=",fact)
else:
    print("factorial is allowed only for posiives")