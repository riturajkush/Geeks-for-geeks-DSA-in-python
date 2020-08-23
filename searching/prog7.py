# your task is to complete this function
# function should return index to the any valid peak element
def peakElement(arr, n):
    l = 0
    r = n-1
    return binarySearch(arr, l, r)
    
def binarySearch(arr, l, r):
    if (l<=r):
        mid = l + (r-l)//2
        if (mid==0) and (arr[mid]>=arr[mid+1]):
            return mid
        if (mid==n-1) and (arr[mid]>=arr[mid-1]):
            return int(mid)
        if (arr[mid]>=arr[mid+1]) and (arr[mid]>=arr[mid-1]):
            return mid
        else:
            return binarySearch(arr, mid+1, r)
            return binarySearch(arr, l, mid-1)




#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = peakElement(arr, n)
        #print(type(index))
        flag = False
        if index == 0 and n==1:
            flag = True
        elif index==0 and arr[index]>=arr[index+1]:
            flag = True
        elif index==n-1 and arr[index]>=arr[index-1]:
            flag = True
        elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
            flag = True
        else:
            flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
