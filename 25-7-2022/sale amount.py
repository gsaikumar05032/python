sa=float(input('enter the sale amount'))
if sa>=5000:
    com=sa*7/100
else:
    com=sa*3/100
net=sa-com
print('sa={sa}')
print('comission={com}')
print('net sales={net}')
