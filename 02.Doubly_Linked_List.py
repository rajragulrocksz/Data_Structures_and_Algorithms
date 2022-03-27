
class Node:
    def __init__(self,value) :
        self.value =value
        self.next =None
        self.prev = None

class Double_Linked_List:
    def __init__(self):
        #new_node = Node(value)
        self.head=None
        self.tail=None
        self.length=0 

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
        return True
    def pop(self):
        if self.length ==0:
            return None
        temp = self.tail
        if self.length ==1:
            self.head =None
            self.tail =None
        else:
            self.tail=temp.prev
            self.tail.next = None
            temp.next=None
            temp.prev=None
        self.length-=1
        return temp.value
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
        self.length+=1
        return True
    def popfirst(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None

        else:
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
            self.length-=1
        return temp.value
    def get(self,index):
        if index < 0 or index >=self.length:
            return None
        if index < self.length/2:
            temp=self.head
            for i in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for i in range(self.length-1,index,-1):
                print("exec")
                temp=temp.prev
        return temp
    def set_value(self,index,value):
        temp=self.get(index)
        if temp is not None:
            temp.value=value
            return True
        return False
    def insert(self,index,value):
        if index < 0 or index>self.length:
            return None
        new_node = Node(value)
        if index==0:
            self.prepend(value)
            return True
        if index==self.length:
            self.append(value)
            return True
        before_node=self.get(index-1)
        after_node=before_node.next
        new_node.next=after_node
        new_node.prev=before_node
        before_node.next=new_node
        after_node.prev=new_node
        self.length+=1
        return True
    def remove(self,index):
        if index < 0 or index >=self.length:
            return None
        if index ==0:
            a=self.popfirst()
            return a
        if index ==self.length-1:
            a=self.pop()
            return a
        temp=self.get(index)
        before=temp.prev
        after =temp.next
        before.next=after
        after.prev=before
        temp.prev=None
        temp.next=None
        self.length-=1
        return temp.value



    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        

dll=Double_Linked_List()
while True:
    print("Doubly Linked List Operations:----------------------")
    print("\n1.Append\n2.Prepend\n3.pop\n4.popfirst\n5.GetValue\n6.SetValue\n7.Insert\n8.Remove\n9.Print_List\n10.List_Length\n11.Exit\nChoose an Operation:")
    n=int(input())
    if n==1:
        value=int(input("Enter value to Append : "))
        dll.append(value)
    elif n==2:
        value=int(input("Enter value to Prepend : "))
        dll.prepend(value)
    elif n==3:
        res=dll.pop()
        print("popped value",res)
    elif n==4:
        res=dll.popfirst()
        print("popfirst value",res)
    elif n==5:
        index=int(input("Enter index to get Value: "))
        res=dll.get(index)
        print("Element at index",index,"is : ",res.value)
    elif n==6:
        i,v=input("Enter index,value for Setting : ").split()
        dll.set_value(int(i),int(v))
    elif n==7:
        i,v=input("Enter index,value for Inserting : ").split()
        dll.insert(int(i),int(v))
    elif n==8:
        index=int(input("Enter index to remove Value: "))
        print("Removed Item :",dll.remove(index))
        
    elif n==9:
        print("Elements in the list are :-----------")
        dll.printlist()
        break
    elif n==10:
        print("Length of the List : ",dll.length)
        break
    elif n==11:
        break
    else:
        print("Enter a Valid Option")
        print("\n\n\n")
        break
    print("Elements in the list are :---------")
    dll.printlist()
   


