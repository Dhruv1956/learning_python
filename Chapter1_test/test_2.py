def CreateGuestList():
    guestlist=[]
    while(True):
        print("please enter the name")
        name=str(input())
        if(name=='done'):
            break
        guestlist.append(name)
    return guestlist

def PrintList(list):
    i=0
    while(i<len(list)):
        print(list[i])
        i=i+1

guestlist=CreateGuestList()
print("List of Guests")
#this is a comment
PrintList(guestlist)





