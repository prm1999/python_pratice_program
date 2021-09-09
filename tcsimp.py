"""
D1. Write a python program to print the following lines in the given format

"Hello, Thank you" Adam said.

"You're very welcome, Have a good day!" Ron responded.

D 2. Write a Python program to accept a number and check if its odd or even. Print appropriate messages.

D 3. Write a Python program to print the multiplication table of a number. The number is to taken as user input.

D4. Write a Python program to accept two strings as input and check if they are identical copy of each other or if the second string is a substring of the first string. If they are identical, print "Both the strings are same". If the 2nd string is substring of the 1st string, print " is a substring of . Please note that the value for String1 and String2 should be printed in place of the holders.

D 5. Create a menu driven Python program to operate on a list of numbers which is provided by the user. The different operations to be provided are :

         a. Add all numbers

         b. Find the highest number

         c. Find the average of all the numbers

         d. Find the numbered with highest frequency in the list.

6.  A school has many students studying in different standards. Each student has a roll number, name, marks in 4 subjects and standard. The school wants a system that can calculate his grade and promote him/her if his grade is greater than 'F'. The criteria for grade calculation is:

i. If percentage >=80,  grade  is  'A'
ii. if  60<=percentage<80, grade  is 'B'
iii. if 40<=percentage<60, grade is 'C'
iv. percentage<40, grade is 'F'

7. A bookshop has many books belonging to different categories like horror, romance, non-fiction etc. Each book has a name, ID,price, category and the author name. The bookshop wants an automated system with which it can get  the price of a particular book. 
Also, the bookshop wants the system to update the price of a given category of books if needed by a given price. Implement the scenario using OOP in Python.
"""


#1 solution
v="Hello, Thank you"
#2 3
x=int(input())
for i in range(0,10):
    p=x*i
    print( x,"*",i,"=",p) 
if(x%2==0):
    print("YES")
else:print("NO")
#4
str1=input()
str2=input()
p=(str1==str2)
print(p)



#5
p=int(input())
q=int(input())


