pwd = 'a123456'
user = input('請輸入密碼:')
count = 3
while True:
	
	if user == pwd:
		print('登入成功')
		break
	else:
		count -= 1
		print(count)
		if count <= 0:
			print('登入失敗')
			break
		else:
			user = input('密碼錯誤,還有' + str(count) + '次機會,請輸入密碼:')