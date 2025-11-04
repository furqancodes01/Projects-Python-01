item_1 = input()
item_2 = input()
item_3 = input()
item_4 = input()

price_1 = '30'
price_2 = '40'
price_3 = '50'
price_4 = '60'

dash_1 = 20 - len(item_1) - len(price_1)
dash_2 = 20 - len(item_2) - len(price_2)
dash_3 = 20 - len(item_3) - len(price_3)
dash_4 = 20 - len(item_4) - len(price_4)

print(item_1 + '-'*dash_1 + price_1 )
print(item_2 + '-'*dash_2 + price_2 )
print(item_3 + '-'*dash_3 + price_3 )
print(item_4 + '-'*dash_4 + price_4 )
