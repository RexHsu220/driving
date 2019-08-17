country = input('Please enter your country:　')
age = input('Please enter your age: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18: 
		print('You are allowed to drive if you have a license.')
	else:
		print('You are not allowed to drive')	