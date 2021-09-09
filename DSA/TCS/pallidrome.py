"""Create a function with the name check_palindrome which takes a list of strings as input. The function checks each string of the list whether it is a palindrome or not and returns another list containing the palindrome from the input string.

Note:

i. A palindrome is a a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam
ii. The check for the string to be palindrome should be case-insensitive , e.g. madam and Madam both should be considered as palindrome.
You can use the below sample input and output to verify your solution."""


# Define the check_palindrome function here
def check_palindrome(inp_str):
    n=len(inp_str)
    c=[]
    for i in range(n):
        p=inp_str[i]
        p_l=p.lower()
        x="".join(reversed(p_l))
        if x==p_l:
            c.append(p)
        else :pass
    ans="".join(c)
    return c
#Do not remove the below portion of code.
if __name__=='__main__':
    count=int(input())
    inp_str=[]
    for i in range(count):
        inp_str.append(input())
        output=check_palindrome(inp_str)
        if len(output)!=0:
            for i in output:
                print(i)
            else:print('No palindrome found')
