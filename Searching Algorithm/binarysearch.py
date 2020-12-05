#Binary search method.
def binary_search(values, l, r, searched):
    #The fucntion takes four parameters.
    #'Values' is the list in which a value is being searched.
    #'Searched' is the element being looked for.
    #r is the lenght of the list.
    #The lenght of the list keeps on changing every time we split the list
    values.sort()
    #We sort the list since the function needs the list to be sorted.
    if r >= 1:
        #For as long as the lenght of the list is not less than one.
        mid = l + (r - 1) // 2
        #The above line splits the list.
        if values[mid] == searched:
            #We check if the value is the element being searched for.
            return "Element " + str(searched) + " is at " + str(mid+1)
        elif values[mid] > searched:
            #We check if the middle value is bigger than the element being searched.
            return binary_search(values, l, mid-1, searched)
            #We recall the function over the second half.
        else:
            #If the mid value is smaller that the element being searched
            #We recall the fucntion over the first half.
            return binary_search(values, mid+1, r, searched)
    else:
        #If we searched through the list after spliting it several times and failed to get the element, we return an 'absent statement'.
        return "Element is not present in the array"