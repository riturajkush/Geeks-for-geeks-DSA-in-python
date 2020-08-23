#User function Template for python3
'''
	Your task is to use KMP search algorithm
	to check if given pat exits in the txt.

	Function Arguments: pat (given pattern), txt(string to search into), q=101.
	Return Type:boolean
'''
def Rabin_Karp(pat, txt, q):
    d = 256
    M = len(pat) 
    N = len(txt) 
    i = 0
    j = 0
    p = 0 # hash value for pattern 
    t = 0 # hash value for txt 
    h = 1

	# The value of h would be "pow(d, M-1)%q" 
    for i in range(M-1): 
        h = (h*d)%q 

	# Calculate the hash value of pattern and first window 
	# of text 
    for i in range(M): 
	    p = (d*p + ord(pat[i]))%q 
	    t = (d*t + ord(txt[i]))%q 

	# Slide the pattern over text one by one 
    for i in range(N-M+1):
		# Check the hash values of current window of text and 
		# pattern if the hash values match then only check 
		# for characters on by one 
	    if p==t: 
			# Check for characters one by one 
		    for j in range(M): 
			    if txt[i+j] != pat[j]: 
				    break

		    j+=1
			# if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1] 
		    if j==M: 
			    return True 

		# Calculate hash value for next window of text: Remove 
		# leading digit, add trailing digit 
	    if i < N-M: 
		    t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q 

			# We might get negative values of t, converting it to 
			# positive 
		    if t < 0: 
			    t = t+q 
    return False

    
    
    
    
    '''if (len(pat)>len(txt)):
        return False
    hash_pat = 0
    hash_txt = 0
    flag = False
    window_size = len(pat)
    d = 256
    print(pow(d, window_size-1)%q)
    for i in range(0,len(pat)):
        hash_pat = (d*hash_pat + ord(pat[i]))%q 
	    hash_txt = (d*hash_txt + ord(txt[i]))%q 
        
    for i in range(len(txt)-window_size+1):
        print(i, hash_pat, hash_txt)
        if (hash_pat==hash_txt):
            flag = True
            for j in range(window_size):
                if (pat[j] != txt[i+j]):
                    flag = False
                    break
            if (flag==True):
                return True
        if (i<(len(txt)-window_size)):
            hash_txt = (d*(hash_txt - ord(txt[i])*((pow(d,window_size-1))%q)) + ord(txt[i + window_size]))%q
            if (hash_txt<0):
                hash_txt += hash_pat
    return False'''
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        txt=str(input())
        pat=str(input())
        q=101
        if(Rabin_Karp(pat,txt,q)):
            print("Yes")
        else:
            print("No")

# } Driver Code Ends
