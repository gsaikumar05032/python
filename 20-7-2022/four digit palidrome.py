print('enter the four digit number')
n=int(input())
a=n//1000
b=(n//100)%10
c=(n//10)%10
d=n%10
rev=d*1000+c*100+b*10+a
if (n==rev):
    print('it is a palidrome')
if (n!=rev):
    print('it is a palidrome')
    
          
