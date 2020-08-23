# Python 3 program to find the smallest  
# positive missing number  
  
# Function to find smallest positive 
# missing number. 
def findMissingNo(arr, n): 
  
    # to store current array element 
  
    # to store next array element in 
    # current traversal 
    for i in range(n) : 
  
        # if value is negative or greater 
        # than array size, then it cannot 
        # be marked in array. So move to 
        # next element. 
        if (arr[i] <= 0 or arr[i] > n): 
            continue
  
        val = arr[i] 
  
        # traverse the array until we 
        # reach at an element which 
        # is already marked or which 
        # could not be marked. 
        while (arr[val - 1] != val): 
            nextval = arr[val - 1] 
            arr[val - 1] = val 
            val = nextval 
            if (val <= 0 or val > n): 
                break
  
    # find first array index which is 
    # not marked which is also the 
    # smallest positive missing 
    # number. 
    for i in range(n): 
        if (arr[i] != i + 1) : 
            return i + 1
  
    # if all indices are marked, then 
    # smallest missing positive 
    # number is array_size + 1. 
    return n + 1
  
# Driver code 
if __name__ == "__main__": 
    arr = [ 1, 3, 2, 5 ] 
    arr_size = len(arr) 
    missing = findMissingNo(arr, arr_size) 
    print( "The smallest positive",  
           "missing number is ", missing) 
  
# This code is contributed  
# by ChitraNayal 
