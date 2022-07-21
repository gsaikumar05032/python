print('enter the compound interest')
p=int(input())
r=int(input())
n=float(input())
ci=p*(1+r/100)**n
total=p+ci
print('total amount',total)
print('ci amount',ci)

