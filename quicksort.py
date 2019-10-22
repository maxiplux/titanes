def quicksort(data_set):
    
    if len(data_set)==0:
        return []
    
    left=[]
    right=[]
    pivot=data_set[0]
    for index in  range(1,len(data_set)):
        element=data_set[index]
        if  element < pivot:
            left.append(element)
        else:
            right.append(element)
            
    return quicksort(left)+[pivot]+quicksort(right)

data_set= [9, 2, 5, 6, 4, 3, 7, 10, 1, 12, 8, 11]
print (quicksort(data_set),data_set)
