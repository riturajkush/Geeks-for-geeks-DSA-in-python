def keypad(string):
    res=''
    for item in string:
        if item in 'abc':
            res+='2'
        elif item in 'def':
            res+='3'
        elif item in 'ghi':
            res+='4'
        elif item in 'jkl':
            res+='5'
        elif item in 'mno':
            res+='6'
        elif item in 'pqrs':
            res+='7'
        elif item in 'tuv':
            res+='8'
        elif item in 'wxyz':
            res+='9'
    print(res)
    
    
    #Below gives TLE
    '''dic = {
    2 : ("a","b","c"),
    3 : ("d","e","f"),
    4 : ("g","h","i"),
    5 : ("j","k","l"),
    6 : ("m","n","o"),
    7 : ("p","q","r","s"),
    8 : ("t","u","v"),
    9 : ("w","x","y","z")}
    for k in s:
        for i in range(2,10):
            for j in dic[i]:
                if(k==j):
                    print(i,end="")
                    break
    print()'''


t = int(input())
for i in range(t):
    s = input()
    keypad(s)
