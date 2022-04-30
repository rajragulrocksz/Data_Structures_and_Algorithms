def insertion_sort(my_list):
    for i in range(1,len(my_list)):
        print("Level",i)
        temp=my_list[i]
        j=i-1
        while temp < my_list[j]   and j>-1:
            print(my_list[j],temp,my_list[j+1])
            my_list[j+1]=my_list[j]
            my_list[j]=temp
            j-=1
            
            print(my_list)
    return my_list


my_list= list(map(lambda x: int(x) ,input("Enter a list : ").split() ))

print("Final Result of Insertion_Sort : ",insertion_sort(my_list))

