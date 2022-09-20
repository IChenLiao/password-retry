#密碼重試程式

#先在程式碼中 設定好密碼 password = 'a123456'
#讓使用者[最多輸入3次密碼] while loop
#不對的話，就印出"密碼錯誤! 還有__次機會" else:
#對的話，就印出"登入成功!" if & break

password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break
	else:
		print('密碼錯誤!')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('沒機會嘗試! 要鎖帳號了!')