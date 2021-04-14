def splitnumber(str):
    num=""
    alpha=""
    special=""
    m=len(str)
    for i in range(0,m):
        if(str[i].isdigit()):
            num=num+str[i]
        elif((str[i]>='A' and str[i]<='Z') or (str[i]>='a' and str[i]<='z')):
            alpha=alpha+str[i]
        else:
            special=special+str[i]

    print(alpha)
    print(num)


str=input()        
splitnumber(str)




"""
There are two strings containing digits, alphabets, and special characters.
Generate a digit code by extracting the digits from the strings such that the digit code has a digit from the first string followed by the digit from the second string.
"""


