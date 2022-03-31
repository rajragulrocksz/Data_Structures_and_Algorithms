class Graph:
    def __init__(self):
        self.data ={}
    
    def add_vertex(self,vertex):
        if vertex not in self.data.keys():
            self.data[vertex]=[]
            return True
        return False
    
    def add_edge(self,v1,v2):
        if v1 in self.data.keys() and v2 in self.data.keys():
            if v2 not in self.data[v1]:
                self.data[v1].append(v2)
            if v1 not in self.data[v2]:
                self.data[v2].append(v1)
            return True
        return False

    def remove_edge(self,v1,v2):
        if v1 in self.data.keys() and v2 in self.data.keys():
            try:
                self.data[v1].remove(v2)
                self.data[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self,vertex):
        if vertex in self.data.keys():
            for i in self.data[vertex]:
                self.remove_edge(vertex,i)
            del self.data[vertex]
            return True
        return False
    
    def print_Graph(self):
        for i in self.data.keys():
            print(i,"-->",self.data[i])
        return True


gr=Graph()

while True:
    print("\n===================")
    print("\nGraph Operations")
    print("\n===================")
    print("1.Add Vertex\n2.Add Edge\n3.Remove Edge\n4.Remove Vertex\n5.Print Graph\n6.Exit")
    n=int(input("Choose any operation to perform : " ))
    if n==1:
        ver=input("Enter vertex to add : ")
        gr.add_vertex(ver)
        print("Vertex",ver,"added")
    elif n==2:
        v1,v2=input("Enter v1 and v2 for creating edge : ").split()
        gr.add_edge(v1,v2)
    elif n==3:
        v1,v2=input("Enter v1 and v2 for removing edge : ").split()
        gr.remove_edge(v1,v2)
    elif n==4:
        ver=input("Enter vertex to Remove : ")
        gr.remove_vertex(ver)
    elif n==5:
        True
    elif n==6:
        break
    else:
        print("Enter a valid Option")
        continue
    print("The Graph is as follows :\n")
    gr.print_Graph()