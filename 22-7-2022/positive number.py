print('enter the positive number')
n=int(input())
if n>=0 and n<=10:
    print('single digit')
if n>=10 and n<=100:
    print('double digit')
if n>=100 and n<=1000:
    print ('three digit')
if n>=1000 and n<=10000:
    print('fourth digit')
if n>10000:
    print('large digit')
