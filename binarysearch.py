def binary_search_simple( datasource, goal):
    
    start=0
    end=len(datasource)-1

    while (start <= end):
        midelement = start + (end - start) // 2

        if datasource[midelement] == goal:
            return midelement
        
        if datasource[midelement] < goal:
            start=midelement+1
        else:
            end=midelement-1

    return -1
def binary_search_simple_recursive( datasource, goal):

    def aux_binary_search_simple_recursive( datasource, goal,start,end):
        
        if start > end:
            return -1
        
        midelement = start + (end - start) // 2
        
        if (datasource[midelement]==goal):
            return midelement

        if datasource[midelement]< goal:
            return aux_binary_search_simple_recursive(datasource,goal,midelement+1,end)
    
        return aux_binary_search_simple_recursive(datasource,goal,start,midelement+1)

    return aux_binary_search_simple_recursive( datasource, goal,0,len(datasource)-1)

datasource = list( range(0,100))


print ( binary_search_simple_recursive( datasource, 2))
