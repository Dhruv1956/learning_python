def  CreateList(count):
    aList = []
    i=0
    while(i<count):
        print("Enter a number: ")
        n= int(input())
        aList.append(n)
        i=i+1
    return aList

def PrintList(list):
    i=0
    while(i<len(list)):
        print(list[i])
        i=i+1

def FindBiggestNumber(alist):
    i=1
    big=alist[0]
    while(i<len(alist)):
        if(big<alist[i]):
            big=alist[i]
        i=i+1
    return big

def FindSmallestNumber(alist):
    i=1
    small=alist[0]
    while(i<len(alist)):
        if(small>alist[i]):
            small=alist[i]
        i=i+1
    return small

def FindAverage(alist):
    i=0
    sum=0
    while(i<len(alist)):
        sum=sum+alist[i]
        i=i+1
    average=sum/len(alist)
    return average

def primenumber (n):
    i=2 
    isprime=True
    loopCount = int(n / 2) +1

    while(i<=loopCount):
        r=n%i
        if(r==0):
            isprime=False
        i=i+1
    if(isprime==True):
        print("number [",n,"] is prime")
    else:
        print("number [",n,"] is not prime")

def FindPrimeNumbers(alist):
    i=0
    while(i<len(alist)):
        primenumber(alist[i])
        i=i+1  

print("Enter number of integers you want: ")
count = int(input())
alist = CreateList(count)
big = FindBiggestNumber(alist)
small = FindSmallestNumber(alist)
print("biggest number is", big) 
print("smallest number is", small) 
average=FindAverage(alist)
print("average of the numbers given is",average)
FindPrimeNumbers(alist)
