leap_year = int(input('Enter the year: '))


if leap_year % 100 == 0 :
    if leap_year % 400 == 0 :
         print('Leap Year')
    else:
        print('Not a Leap Year')
elif leap_year % 4 == 0:
    print('Leap year')
else:
    print('Not a leap year')
    
            