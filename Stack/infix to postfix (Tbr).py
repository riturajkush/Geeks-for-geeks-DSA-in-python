#User function Template for python3
'''
Function Arguments :
		@param  : exp (given infix expression)
		@return : string
'''
def InfixtoPostfix(exp):
    dic = {'^': 1, '*': 2, '/': 2, '+':3, '-':3, '(':4, ')':4}
    stk = []
    postfix = []
    count = 0
    top = -1
    for i in exp:
        if (top==-1) and (i in dic):
            stk.append(i)
            top += 1
        else:
            #print('!!!')
            if (i not in dic):
                postfix.append(i)
            elif (i == '('):
                #count += 1
                stk.append(i)
                top += 1
            elif (i == ')'):
                while(stk[top]!='('):
                    postfix.append(stk.pop())
                    top -= 1
                stk.pop()
                top -= 1
                #count -= 1
            else:
                if (stk[top] in dic) and (dic[i]>=dic[stk[top]]):
                    postfix.append(stk.pop())
                    stk.append(i)
                else:
                    stk.append(i)
                    top += 1
    print(stk)
    return postfix
            
            



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        print(InfixtoPostfix(exp))
# } Driver Code Ends
