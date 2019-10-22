def merge(array):
    if len(array)>1:
        len_array=len(array)
        left_array=array[:len_array//2]
        right_array=array[len_array//2:]
        
        merge(left_array)
        merge(right_array)

        
        

        array_index=0
        left_index=0
        right_index=0

        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] < right_array[right_index]:
                array[array_index]=left_array[left_index]
                left_index+=1
            else:
                array[array_index]=right_array[right_index]
                right_index+=1
                
            array_index=array_index+1
            
         
        while  left_index < len(left_array): 
            array[array_index] = left_array[left_index] 
            left_index+=1
            array_index+=1
          
        while right_index < len(right_array): 
            array[array_index] = right_array[right_index] 
            right_index+=1
            array_index+=1
            
t1=list(range(10,0,-1))            
merge(t1)
print (t1)
