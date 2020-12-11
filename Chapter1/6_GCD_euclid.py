n1=int(input())
n2=int(input())
i=0
j=0
if (n1>n2):
    i=n1
    j=n2
else:
    i=n2
    j=n1
while(True):
    r=i%j
    if(r!=0):
        i=j
        j=r
    else:
        break
print("GCD=",j)


