class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
    def append(self,value):
        new_node =Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            
        else:
            self.tail.next=new_node
            self.tail=new_node
            
        self.length+=1
    def pop(self):
        if self.length==0:
            return None

        elif self.length==1:
            temp=self.head
            self.head=None
            self.tail=None
            
        else:
            temp=self.head
            while temp.next is not None:
                pre=temp
                temp=temp.next
            self.tail=pre
            self.tail.next=None
        self.length-=1
        return temp
    def prepend(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
            
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1
    def popfirst(self):
        if self.length==0:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp.value
    def get(self,index):
        if index < 0 or index >= self.length:
            print("Enter valid Index")
        else:
            temp=self.head
            for i in  range(index)  :
                temp=temp.next
               
            return temp
    
    def set(self,index,value):
        if index < 0 or index > self.length:
            print("Enter valid Index")
            return None
        temp=self.get(index)
        temp.value=value
        return True



    def insert(self,index,value):
        if index < 0 or index > self.length:
            print("Enter valid Index")
            return None
        new_node=Node(value)
        #temp=self.head
        if index==0:
            self.prepend(value)
        else:
            temp=self.get(index-1)
            new_node.next=temp.next
            temp.next=new_node
        self.length+=1
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index==0:
            return self.popfirst()
        if index==self.length-1:
            return self.pop()
        
        pre=self.get(index-1)
        temp=pre.next
        pre.next=temp.next
        temp.next=None
        self.length-=1
        return temp
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        before =None
        #after=temp.next
        for i in range(self.length):
            after=temp.next
            temp.next=before
            before =temp
            temp=after
        return True

    def printList(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    


my_list = LinkedList(1)
my_list.printList()
print("Adding Items")
my_list.append(5)
my_list.append(7)
my_list.append(9)
my_list.printList()
print("Popping Items")
print("popped Item",my_list.pop().value)
my_list.printList()
print("popped Item",my_list.pop().value)
my_list.printList()
print("popped Item",my_list.pop().value)

my_list.printList()
print("Prepending Item")
my_list.prepend(4555)
my_list.printList()

print("prepopping")
print("Prepopping",my_list.popfirst())
my_list.printList()
print("Prepopping",my_list.popfirst())
my_list.printList()
print("Prepopping",my_list.popfirst())
my_list.printList()
my_list.append(5)
my_list.append(7)
my_list.append(9)
my_list.printList()
print("use Get Method")
print(my_list.get(0).value)
print(my_list.get(1).value)

print(my_list.get(2).value)
print(my_list.get(-9))
print(my_list.get(9))
my_list.set(2,90)
my_list.printList()
print("Insertion")
my_list.insert(1,99)
my_list.printList()
print("Removal")
print('Removed Item',my_list.remove(2).value)
my_list.printList()
print("Reversal",my_list.reverse())
my_list.printList()
