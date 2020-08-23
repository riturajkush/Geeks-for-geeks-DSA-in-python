#User function Template for python3

#Complete this function
def stockBuySell(A,n):
    min_val = 10000
    profit = 0
    profit1 = 0
    for i in range(0,n):
        if (i>0):
            if (A[i]>A[i-1]):
                val = A[i]-min_val
                profit1 = max_val(val, profit1)
                '''print(i, "profit1", profit1)
                print("val", val)'''
                if (i==(n-1)):
                    print("(",end="")
                    print(start,i,end="")
                    print(")",end=" ")
            else:
                min_val = A[i]
                end = i-1
                if(start!=end):
                    print("(",end="")
                    print(start,end,end="")
                    print(")",end=" ")
                start = i
                #print("start", start)
                profit = profit + profit1
                #print("profit", profit)
                profit1 = 0
                #print("min_val", min_val)
        else:
            if (A[i]<min_val):
                start = i
                min_val = A[i]
                profit = profit + profit1
                #print("profit", profit)
                profit1 = 0
                #print("min_val", min_val)

    profit = profit + profit1
    if (profit==0):
        print("No Profit")
    #else:
        #print("final profit", profit)
    #print(profit1)


def max_val(a,b):
    if (a>b):
        return a
    else:
        return b



#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            stockBuySell(arr,n)
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
