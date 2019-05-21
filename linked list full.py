class node:
    def __init__(self,d):
        self.data=d
        self.addr=None
class s:
    def __init__(self):
        self.head=None
        self.prev=None
    def insert(self):
            print("enter a value to insert")
            val=input()
            newnode=node(val)
            newnode.addr=self.head
            self.head=newnode
            
            
    def display(self):
        
        temp=self.head
        while temp!=None:
            print(end=" ")
            print(temp.data,end="--->")
            temp=temp.addr
    def delete(self):
        print("enter the node to delete")
        get=input()
        
        
        if self.head.data==get:
           self.head.addr=None
           self.head=n2
           print("node deleted")
        

        else:
            temp=self.head
            prev=temp
            while temp.data!=get:
                prev=temp
                temp=temp.addr
            prev.addr=temp.addr
            temp.addr=None
            print("node deleted")
    def insertmiddle(self):
        print("enter the node to insert after")
        get1=input()
        print("enter the new node")
        get2=input()
        new=node(get2)
        temp=self.head
        while temp.data!=None:
            prev=temp
            temp=temp.addr
            if temp.data==get1:
                new.addr=temp.addr
                temp.addr=new
                print("node inserted")
                break
    def delend(self):
        temp=self.head
        while temp!=None:
            if temp.addr==None:
                break
            prev=temp
            temp=temp.addr
        prev.addr=None    
        print("node deleted")
    def insertend(self):
        print("enter the node to insert at end")
        val=input()
        new=node(val)
        temp=self.head
        while temp!=None:
            if temp.addr==None:
                break
            prev=temp
            temp=temp.addr
        temp.addr=new
        print("node added at end")
            

s1=s()
s1.head=node("siva")
n2=node("karthikeyan")
n3=node("sarath")
n4=node("saran")
s1.head.addr=n2
n2.addr=n3
n3.addr=n4

print(s1.head.data,end=" ")
print(n2.data,end=" ")
print(n3.data,end=" ")
print(n4.data)

ch=0
while ch!=7:
    print("1.insert, 2.delete, 3.display, 4.add in middle, 5.delete at end, 6.add at end")
    ch=int(input())
    if ch==1:
       s1.insert()
       s1.display()
    elif ch==3:
        s1.display()
    elif ch==2:
        s1.delete()
    elif ch==4:
        s1.insertmiddle()
    elif ch==5:
        s1.delend()
    elif ch==6:
        s1.insertend()
        
