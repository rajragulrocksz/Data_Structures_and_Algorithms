class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1


    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1


    def pop(self):
        if self.height==0:
            return None
        if self.height==1:
            return self.top
        temp=self.top
        self.top=temp.next
        temp.next=None
        self.height-=1
        return temp

    def printStack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next


stck=Stack(10)

while True:
    print("\n\nStack Operations==============")
    print("\n1.Push\n2.Pop\n3.printStack\n4.Stackheight\n5.Exit ")
    n=int(input("Enter any Option : "))
    if n==1:
        value=int(input("Enter Value to Push : "))
        stck.push(value)
    elif n==2:
        print("Popped Item : ",stck.pop().value)
    elif n==4:
        print("No of Elements in Stack : ",stck.height)
        continue
    elif n==5:
        break
    else:
        print("Enter any Valid Option")
    
    print("Elements present in the stack are as follows: ")
    stck.printStack()