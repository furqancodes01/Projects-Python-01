amt = float(input("enter the amount"))


if amt < 1000:
    tot = amt - amt*0.1
elif amt >= 1000 and amt < 5000:
    tot = amt -amt*0.15
elif amt >= 5000 and  amt < 10000:
    tot = amt - amt *0.2
else:
    tot = amt -amt* 0.25
print('pay',tot)