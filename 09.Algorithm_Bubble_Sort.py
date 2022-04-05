def bubble_sort(my_list):
    for i in range(len(my_list)-1,0,-1):
        print("Level",i)
        for j in range(i):
            if my_list[j+1] < my_list[j] :
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
                
            else:
                continue
            print(my_list)
    return my_list

my_list= list(map(lambda x: int(x) ,input("Enter a list : ").split() ))

print(bubble_sort(my_list))
