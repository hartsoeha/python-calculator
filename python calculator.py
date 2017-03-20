def calculator():
	operator = input('Which operation would you like to perform?: ')

	try:
		num1 = float(input('Input first number: '))
		num2 = float(input('Input second number: '))
	except(ValueError):
		print("Invalid Entry")
		calculator()
	if operator == '+':
		print('{} + {} = '.format(num1,num2))
		print(num1 + num2)
	
	elif operator == '-':
		print('{} - {} = '.format(num1,num2))
		print(num1 - num2)
		
	elif operator == '*':
		print('{} * {} = '.format(num1,num2))
		print(num1 * num2)
		
	elif operator == '/':
		print('{} / {} = '.format(num1,num2))
		try:
			print(num1 / num2)
		except(ZeroDivisionError):
			print("Cannot divide by zero.")
			
	elif operator == '**' or operator == '^':
		print('{} ^ {} = '.format(num1,num2))
		print(num1 ** num2)
		
	elif operator == '%':
		print('The remainder of {} / {} is '.format(num1,num2))
		print(num1 % num2)
		
	else:
		print('This operator is invalid.')

	def repeat():
		again = input("More Calculations? (Y or N): ")
		if again.upper() == "Y":
			calculator()
		elif again.upper() == "N":
			print("Thank you for testing this calculator.")
		else:
			print("Invalid Entry")
			repeat()
	repeat()
		
calculator()
		


