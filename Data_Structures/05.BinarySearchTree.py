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
            return True
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
           

    def BFS(self):
        current_node =self.root
        q=[]
        result=[]
        q.append(current_node)
        while len(q) > 0:
            current_node=q.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                q.append(current_node.left)
            if current_node.right is not None:
                q.append(current_node.right)

        return result
        
    def DFS_preorder(self):
        result=[]
        def preorder_traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                preorder_traverse(current_node.left)
            if current_node.right is not None:
                preorder_traverse(current_node.right)
        preorder_traverse(self.root)
        return result
    
    def DFS_postorder(self):
        result=[]
        def postorder_traverse(current_node):
            
            if current_node.left is not None:
                postorder_traverse(current_node.left)
            if current_node.right is not None:
                postorder_traverse(current_node.right)
            result.append(current_node.value)
        postorder_traverse(self.root)
        return result

    def DFS_inorder(self):
        result=[]
        def inorder_traverse(current_node):
            if current_node.left is not None:
                inorder_traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                inorder_traverse(current_node.right)
        inorder_traverse(self.root)
        return result


bst= BSTree()
bst.insert(47)
bst.insert(21) 
bst.insert(35)
bst.insert(76) 
bst.insert(18)
bst.insert(90) 
bst.insert(27)
bst.insert(52)
bst.insert(65)
bst.insert(82)

'''
BFS_Output :  [47, 21, 76, 18, 35, 52, 90, 27, 65, 82]
DFS_PreOrder Output :  [47, 21, 18, 35, 27, 76, 52, 65, 90, 82]
DFS_PostOrder Output :  [18, 27, 35, 21, 65, 52, 82, 90, 76, 47]
DFS_InOrder Output :  [18, 21, 27, 35, 47, 52, 65, 76, 82, 90]
'''

while True:
    print("\n\n================================\nBinary Search Tree Operations \n================================")
    print("\n1.Insert\n2.Check the Presence of Values\n3.Minimum Value in the Tree\n4.BFS_Output\n5.DFS_preOrder_Output\n6.DFS_PostOrder\n7.DFS_InOrder\n8.Exit\n")
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
    elif n==4:
        print("BFS_Output : ",bst.BFS())
    elif n==5:
        print("DFS_PreOrder Output : ",bst.DFS_preorder())
    elif n==6:
        print("DFS_PostOrder Output : ",bst.DFS_postorder())
    elif n==7:
        print("DFS_InOrder Output : ",bst.DFS_inorder())
    elif n==8:
        break
    else:
        print("Enter any valid operation")

