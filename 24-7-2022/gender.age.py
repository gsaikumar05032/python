print('Enter the gender,age of the person')
gender=input().lower()
age=int(input())
if(gender=='male' and age>=21 ):
    print('major')
else:
    print('minor')
