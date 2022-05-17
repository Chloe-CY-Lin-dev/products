#while loop適合用在不知道迴圈次數的情況下使用

products=[]
while True:
	name = input('請輸入商品名稱：')
	if name == 'q': # quit
		break
	price = input('請輸入商品價格：')
	# p = []
	# p.append(name)
	# p.append(price)
	# 前3行可以用 p = [name, price]來代替
	# products.append(p) #把小清單p裝進大清單products
	products.append([name, price])
print(products)
# [['奶茶', '10'], ['珍珠奶茶', '60'], ['四季春', '40']] 這是二維清單

for p in products:
	print(p[0],'的價格是',p[1])
