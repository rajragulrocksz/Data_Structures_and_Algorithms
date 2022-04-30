def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index=i
        for j in range(i+1,len(my_list)):
            
            if my_list[min_index] > my_list[j]:
                min_index=j
        print("Min_index:",min_index)
        if i!=min_index:
            my_list[i],my_list[min_index] =my_list[min_index],my_list[i]
        print(my_list)
    return my_list

my_list= list(map(lambda x: int(x) ,input("Enter a list : ").split() ))

print("Final Result of Selection_Sort : ",selection_sort(my_list))
