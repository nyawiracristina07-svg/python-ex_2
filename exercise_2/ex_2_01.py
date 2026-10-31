grade = input("Give me a grade from 0-100: ")

num_grade = int(grade)

if 90 <= num_grade <= 100:
    print('A')
elif 80 <= num_grade < 90:
    print('B')
elif 70 <= num_grade < 80:
    print('C')
elif 60 <= num_grade < 70:
    print('D')
elif 0 <= num_grade < 60:
    print('F')
else:
    print('Invalid grade')

