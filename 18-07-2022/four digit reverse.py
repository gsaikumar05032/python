print('enter the four digit')
n=int(input())
a=n//1000
b=(n//100)%10
c=(n/10)%10
d=n%10
rev=d*1000+c*100+b*10+a
print('reverse of the number',rev)

