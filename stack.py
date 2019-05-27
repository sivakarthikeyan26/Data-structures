class sta:
    def __init__(self):
        self.stack=[]
    def add(self):
        print("enter the value to add")
        val=input()
        if val not in self.stack:
            self.stack.append(val)
        else:
            print("already value is present in stack")
    def delete(self):
        if len(self.stack)<=0:
            print("stack is empty")
        else:
            print("enter how many elements you want to pop")
            n=int(input())
            for i in range(n):
                c=self.stack.pop()
                print(c)
            print("finished deleting")
    def display(self):
        lis=[]
        n=len(self.stack)
        if n<=0:
            print("stack is empty can't delete")
        else:
            for i in range(n):
                c=self.stack.pop()
                print(c)
                lis.append(c)
                
            while n>=1:
                self.stack.append(lis[n-1])
                n=n-1
            print("stack retrived")
    def delbyelement(self):
        arr=[]
        print("enter the element you want to delete")
        val=input()
        n=len(self.stack)
        if n<=0:
            print("stack is empty cant display")
        else:
            for i in range(n):
                c=self.stack.pop()
                if c!=val:
                    arr.append(c)
                else:
                    continue
            while (n-1)>=1:
                self.stack.append(arr[n-2])
                n=n-1
            print("stack retrived")
         
                    
            

ch=0
s=sta()
while ch!=5:
    print("1.add, 2.pop, 3.display")
    ch=int(input())
    if ch==1:
        s.add()
    elif ch==2:
        s.delete()
    elif ch==3:
        s.display()
    elif ch==4:
        s.delbyelement()
        
