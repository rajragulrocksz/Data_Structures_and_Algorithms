class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    
class queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1

    def enqueue(self,value):
        new_node=Node(value)
        if self.length ==0:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node
        self.length+=1
        return True
    
    def dequeue(self):
        if self.length ==0:
            return None
        temp=self.first
        if self.length==1:
            self.first=None
            self.last=None   
        else:
            self.first=temp.next
            temp.next=None
        self.length-=1
        return temp


    def printqueue(self):
        temp=self.first
        
        while temp is not None:
            print(temp.value, end=' ')
            temp=temp.next

q=queue(4)
while True:
    print("\n\nQueue Operations:----------------------")
    print("\n1.EnQueue\n2.Dequeue\n3.Print_List\n4.Queue_Length\n5.Exit\nChoose an Operation:")
    n=int(input())
    if n==1:
        value=int(input("Enter value to add : "))
        q.enqueue(value)
    elif n==2:
        res=q.dequeue()
        print("Dequeued Item : ",res.value)
    elif n==3:
        True
    elif n==4:
        print("No Of Elements in the Queue : ",q.length)
    elif n==5:
        break
    else:
        print("Enter a valid operation")
    print("The Elements in the queue are as follows : ")
    q.printqueue()
