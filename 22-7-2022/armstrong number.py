print('enter the three digit number')
n=int(input())
a=n//100
b=(n//10)%10
c=n%10
sum=a**3+b**3+c**c
if sum==n:
    print('armstrong number')
if sum!=n:
    print('armstrong number are not')
    
