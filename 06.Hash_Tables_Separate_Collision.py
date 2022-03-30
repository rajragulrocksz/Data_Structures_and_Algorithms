class HashTable:

    def __init__(self,size=7):
        self.map_data= [None] * size
    
    def __hash(self,key):
        hash_init=0 #initialising hash value
        for i in key:
            hash_init = (hash_init + ord(i) *29 ) % len(self.map_data)
            #Ord -->ASCII of a letter
            # %len(self.map_data) is used to get only the remainders between 0 and 6 bcz hash size is 7 (0 to 6)
        return hash_init
    
    def set_ht(self,key,value):
        index=self.__hash(key)
        if self.map_data[index] is  None:
            self.map_data[index]=[]
        self.map_data[index].append([key,value])
        return True

    def get_value(self,key):
        index=self.__hash(key)
        for i in self.map_data[index] :
            if i is not None and  i[0]==key:
                return i[1]
        return None
    
    def get_allkeys(self):
        allkeys=[]
        for i in self.map_data:
            if i is not None:
                for j in i:
                    allkeys.append(j[0])
        return allkeys



    def print_hashtable(self):
        for i,value in enumerate(self.map_data):
            print(i,"-->",value)

hash_table=HashTable()

while True:
    print("\n================================")
    print("\nHash Table Separate Collisions")
    print("\n================================")
    print("\n1.Insert\n2.Get value for a key\n3.Print All Keys\n4.Print Hash Table\n5.Exit")
    n=int(input("\nEnter any Operation : "))
    if n==1:
        key,val=input("Enter Key and Value to Insert : ").split()
        hash_table.set_ht(key,int(val))
    elif n==2:
        key=input("Enter key to get its value : ")
        print(key," --> ",hash_table.get_value(key))
        continue
    elif n==3:
        print("Keys present in the hash table are : ",hash_table.get_allkeys())
        continue
    elif n==4:
        pass
    elif n==5:
        break
    else:
        print("\nEnter a valid operation")
    hash_table.print_hashtable()
    
