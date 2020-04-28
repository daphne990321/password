count = 0 
n = 2
while count <= 3:
	password = input('請輸入密碼')
	if password != 'a123456':
		m = n - count
		print('密碼錯誤！還有', m, '次機會')
		count = count + 1
		if m == 0:
			break
	else:
		print('登入成功')
		break
