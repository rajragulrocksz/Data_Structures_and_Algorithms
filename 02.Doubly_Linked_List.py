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
        self.tail=temp.prev
        self.tail.next = None
        temp.next=None
        temp.prev=None
        self.length-=1
        return temp.value

    def printlist(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

dll=Double_Linked_List(7)
dll.append(2)
dll.append(6)
dll.append(10)
dll.printlist()
dll.pop()
dll.printlist()


