def Printlist(list):
    i=0
    while(i<len(list)):
        print(list[i])
        i=i+1
    return
def Createlist(n):
    alist=[]
    i=0
    even=254
    while(i<n):
        even=even+2
        alist.append(even)
        i=i+1     
    return alist
mylist = [11,22,33,44,55]


alist=Createlist(100)
Printlist(alist)

