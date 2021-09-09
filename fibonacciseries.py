"""def fib(n):
    if(n==0):return 0
    elif(n==1):return 1
    else :return fib(n-2)+fib(n-1)

n=int(input())
c=[]
for i in range(0,n):
    f=fib(i)
    c.append(f)
print(c)






Given the consecutive scores of a cricket match,
 calculate the total runs scored, the number of wickets, the extras,
 the runs scored by each batsman, the number of overs bowled.
 Notes: wkt - wicket, wd - wide ball, add one run to the scoreboard,
  bowl again, lb - leg bye, and nb - no-ball, add one run to the scoreboard, bowl again.
   The sample input is - 1 0 1wd 0 3 2 0 0 2nb 0wkt 6 1 0 4 and sample output is - total runs scored: 20,
 number of wickets: 1, extras: 2, scores by batsmen: 1st batsmen: 3 runs; 2nd batsmen: 8 runs; 3rd batsmen: 7 runs.
"""
#input_run=input().split()
input_run=[ '1', '0' ,'1wd', '0','3', '2', '0', '0', '2nb', '0wkt', '6', '1', '0', '4']
n=len(input_run)
print(n)
ball =0
wicket=0
run=0
wkt=0
for i in range (0,n):
    if(input_run[i]=='1'):
        run+=1
    elif
