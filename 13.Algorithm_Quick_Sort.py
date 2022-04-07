def swap_ids(my_list,ind1,ind2):
    my_list[ind1], my_list[ind2] =my_list[ind2], my_list[ind1]


def pivot(my_list,pivot,end_ind):
    swap=pivot
    print("Level====")
    print(my_list)
    for i in range(pivot+1,end_ind+1):
        if my_list[i] < my_list[pivot] :
            swap+=1
            swap_ids(my_list,swap,i)
    
    swap_ids(my_list,swap,pivot)
    print(my_list)
    return swap
    
    
def quick_sort(my_list,left,right):
    if left < right :
        pivot_ind = pivot(my_list,left,right)
        quick_sort(my_list,left,pivot_ind-1)
        quick_sort(my_list,pivot_ind+1,right)

    return my_list


my_list = [4,6,1,7,3,2,5]

print("Result of QuickSort: ", quick_sort(my_list,0,len(my_list)-1))

            

