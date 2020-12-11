n1=int(input())
n2=int(input())

n1t=int(n1/10)
n1u=n1%10

n2t=int(n2/10)
n2u=n2%10

sum=n1u+n2u

if(sum<10):
    st=n1t+n2t
    sum=st*10+sum
    print("sum without carry=", sum)
else:
    sum_u=sum%10
    sum_t=sum/10
    st=n1t+n2t+sum_t
    sum=st*10+sum_u
    print("sum with carry=",sum)
print("Done")    
