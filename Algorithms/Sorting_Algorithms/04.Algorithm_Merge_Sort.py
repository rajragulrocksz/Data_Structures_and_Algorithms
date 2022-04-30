def merge(list1,list2):
    combined = []
    i=0
    j=0
    print(list1,"=====",list2)
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:
            combined.append(list2[j])
            j+=1
    while i<len(list1):
        combined.append(list1[i])
        i+=1
    while j < len(list2):
        combined.append(list2[j])
        j+=1
    return combined

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid=int(len(my_list)/2)
    left=my_list[:mid]
    right=my_list[mid:]
    a=merge_sort(left)
    b=merge_sort(right)

    return merge(a,b)
my_list =input("Enter a list of Elements : ").split()
print(merge_sort(my_list))