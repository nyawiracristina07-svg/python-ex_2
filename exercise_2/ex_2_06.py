temp = input("display temp: ")

float_temp = float(temp)

if  float_temp < 19:
    print('heating on')
elif 19 <= float_temp <= 24:
    print('comfort')
else:
    print ('cooling on')