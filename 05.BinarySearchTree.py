class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    
class BSTree:
    def __init__(self):
        self.root=None
        self.length=0
    
    def insert(self,value):
        new_node=Node(value)
        
        if self.root is None:
            self.root=new_node
        temp=self.root
        while True:
            if new_node.value==temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
    def contain(self,value):
        temp=self.root
        while temp is not None:
            if  value == temp.value:
                return True
            elif value < temp.value:
                temp=temp.left
            else:
                temp=temp.right

        return False
    def min(self):
        temp=self.root
        while temp.left is not None:
                 temp=temp.left
        return temp.value
           

    '''def printTree(self):
        if self.root is None:
            return None
        else:
            temp=self.root
            while temp is not None:
                print(temp.value)
                if temp.left is not None:
                    temp=temp.left 
                '''
bst= BSTree()

while True:
    print("\n\n================================\nBinary Search Tree Operations \n================================ \n1.Insert\n2.Check the Presence of Values\n3.Minimum Value in the Tree")
    n=int(input("Choose an Operation: "))
    if n==1:
        value=int(input("Enter value to insert : "))
        bst.insert(value)
        print("Value ",value, "is successfully inserted")
    elif n==2:
        value=int(input("Enter value to search : "))
        if bst.contain(value)==True:
            print( "Value ",value,"is present in the Tree")
        else:
            print("Value ",value,"is not present in the Tree")

    elif n==3:
        print("Minimum Value in the Tree :",end= ' ')
        a=bst.min()
        if a is not None:
            print(a)
        else:
            print("Tree is Empty")
    else:
        print("Enter any valid operation")

