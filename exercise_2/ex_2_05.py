number_1 = input("display the first number: ")
number_2 = input("display the second number: ")

if (int(number_1) < 0 and int(number_2) < 0) or (int(number_1) > 0 and int(number_2) > 0):
    print(' positive')

elif (int(number_1) > 0 and int(number_2) < 0) or int(number_1) < 0 and int(number_2) > 0:
    print('negative') 
else:
    print('zero')

