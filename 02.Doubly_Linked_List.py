class Node:
    def __init__(self,value) :
        self.value =value
        self.next =None
        self.prev = None

class Double_Linked_List:
    def __init__(self,value):
        new_node = Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

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
        return temp.value

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

dll=Double_Linked_List(7)
print("Appending Data")
dll.append(2)
dll.append(6)
dll.append(10)
print("Append Result")
dll.printlist()
s=dll.pop()
print("Pop Data & List : ",s)
dll.printlist()
dll.prepend('55')
dll.prepend('58')
dll.prepend(10)
print("Prepend Result")
dll.printlist() 
s=dll.popfirst()
print("pop-first_element:",s,"\nRemaining Elements")
dll.printlist()
s=dll.get(2)
print("Get Element at index 2",s)


