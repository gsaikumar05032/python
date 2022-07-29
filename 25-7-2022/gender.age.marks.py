print('enter gender and age and marks of a person')
gender=input().lower
age=int(input())
marks=int(input())
if (gender=='male' and age>=21 and marks>=60):
    print('major')
else:
    print('minor')
