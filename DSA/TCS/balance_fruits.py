"""
You have a basket full of apples and mangoes, your job is to make the number of apples and 
given a function that accepts three integers 'a', 'm' and 'rs' as its argument where 'a' and a 
basket respectively and 'rs' is the rupees that you have. Implement the function to balance the 
basket.
"""
def BalanceFruits( a, m, rs):
    if(a>m):
        p=a-m
        print(rs-p)
    elif(a<m):
        p=m-a
        print(rs+p)
    elif(a==m):
        print(rs)

        
BalanceFruits(8,4,6)
BalanceFruits(7,4,6)





