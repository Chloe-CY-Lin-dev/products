import os #operating system

products=[]

if os.path.isfile('products.csv'):
	print('Yes! 找到檔案了')
	# 讀取檔案
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續, 如果讀到商品、價格,跳過此次並進到下一個迴圈
			name, price = line.strip().split(',') #strip把換行符號去掉；spilt切割,split切割完的結果是清單
			products.append([name, price])
	print(products)

else:
	print('找不到檔案.....')


# 讓使用者輸入商品,價格
while True: #while loop適合用在不知道迴圈次數的情況下使用
	name = input('請輸入商品名稱：')
	if name == 'q': # quit
		break
	price = input('請輸入商品價格：')
	# p = []
	# p.append(name)
	# p.append(price)
	# 前3行可以用 p = [name, price]來代替
	# products.append(p) ## 把小清單p裝進大清單products
	products.append([name, price])
print(products)
# [['奶茶', '10'], ['珍珠奶茶', '60'], ['四季春', '40']] 這是一個二維清單

#印出所有商品紀錄
for p in products:
	print(p[0],'的價格是',p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: #write(w)寫入模式
	f.write('商品,價格\n') #加入欄位名稱
	for p in products:
		f.write(p[0]+','+p[1]+'\n') #f.write才是真正的寫入
