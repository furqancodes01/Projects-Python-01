n = int(input('Enter the digits: '))
sum = 0

while n>0:
    r= n % 10
    sum = sum + r
    n = n//10
print('the sum of the numbers is : ',sum) 