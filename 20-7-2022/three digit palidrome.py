print('enter the three digit number')
n=int(input())
a=n//100
b=(n//10)%10
c=n%10
rev=c*100+b*10+a
if(n==rev):
    print('it is palidrome')
if(n!=rev):
    print('it is not palidrome')
    
          
