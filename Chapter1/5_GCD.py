def FindDivisors(n):
    alist=[]
   
    i=1
    loopcount=int(n/2)+1
    while(i<=loopcount):
        r=n%i
        if(r==0):
            alist.append(i)
        i=i+1
    if(n!=1):
        alist.append(n)
    return alist

def PrintList(list):
    i=0
    while(i<len(list)):
        print(list[i])
        i=i+1

def FindElement(alist,n):
   i=0
   while(i<len(alist)):
       if (n==alist[i]):
           return True
       i=i+1
   return False

def FindCommonElements(alist1,alist2):
    i=0
    newlist=[]

    while(i<len(alist2)):
        found=FindElement(alist1,alist2[i])
        if(found):
            newlist.append(alist2[i])
        i=i+1
    return newlist

def FindBiggestNumber(alist):
    i=1
    big=alist[0]
    while(i<len(alist)):
        if(big<alist[i]):
            big=alist[i]
        i=i+1
    return big


print("Enter two numbers for GCD")
n1=int(input())
n2=int(input())
alist1=FindDivisors(n1)
print("divisors of n1")
PrintList(alist1)
alist2=FindDivisors(n2)
print("divisors of n2")
PrintList(alist2)
print("common divisors")
newlist=FindCommonElements(alist1,alist2)
PrintList(newlist)
GCD=FindBiggestNumber(newlist)
print("GCD=",GCD)




