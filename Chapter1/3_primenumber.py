n=int(input())
i=2
isprime=True
while(i<=n/2):
    r=n%i
    if (r==0):
        isprime=False
    i=i+1
if(isprime==True):
    print (" it is a prime number")
else:
    print("it is not a prime number ")


