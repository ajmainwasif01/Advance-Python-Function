s1 = {3,4,6}
s2 = {'c','e','f'}

s3 = list(zip(s1,s2))

print(s3)

lst1 = [10,30,40,50]
lst2 = [100,300,400,500]

for x,y in zip(lst1,lst2[:: - 1]):
    print(x,y)

stocks = ['RFL', 'GP', 'BEXIMCO']
price = [144.5, 110, 307.4]

new_dic = {stocks: price for stocks, price in zip(stocks,price)}

print('\n{}'.format(new_dic))
