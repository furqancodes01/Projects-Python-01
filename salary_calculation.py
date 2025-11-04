work_hours = [int(x) for x in  input("Enter the hours per day in entire week: ").split()]
wage = int(input("Enter the hourly wage: "))

total = sum(work_hours)

salary = total * wage
print('SAlary is: ',salary)