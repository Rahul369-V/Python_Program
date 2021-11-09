# find the odd occurrence in a list
#best time complexity


def getoddoccurrence(arr):
    res = 0
    for element in arr:
        res = res ^ element
        
        print(res)
  
    return res


        
#arr=[1,1,2,3,3,2,4,5,5,7]

arr=[1,1,2,2,3,3,4,4] # element repeated for even times

#arr=[11,2,2,3,4,3,4]   #one element is repeated for odd times

print("odd occurance number:",getoddoccurrence(arr))
