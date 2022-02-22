from math import* 
print('What would you like to evaluate? \n1.Sum \n2.Minus \n3.Multiplection \n4.Division \n5.Square Roor \n6.Factorial  ')
num = input('Enter a number: ')

if num=='1':
	print('Hi! You want to do Sum! ')
	num1=int(input('Enter your first number:'))
	num2=int(input('Enter your second number: '))
	result1=(num1+num2)
	print('Your sum`s answer is ' + str(result1))

elif num=='2':
	print('Hi! You want to do Minus! ')
	num3=int(input('Enter your first number:'))
	num4=int(input('Enter your second number: '))
	result2=(num3-num4)
	print('Your minus`s answer is ' + str(result2))

elif num=='3':
	print('Hi! You want to do Multiplection!')
	num5=int(input('Enter your first number:'))
	num6=int(input('Enter your second number: '))
	result3=(num5*num6)
	print('Your multiplection`s answer is ' + str(result3))

elif num=='4':
	print('Hi! You want to do Division!')
	num7=int(input('Enter your first number:'))
	num8=int(input('Enter your second number: '))
	result4=(num7/num8)
	print('Your Division`s answer is ' + str(result4))

elif num=='5':
	print('Hi! You want to do Squareroot')
	num9=int(input('Enter your number: '))
	result5=sqrt(num9)
	print('Your Squareroot`s answer is ' + str(result5) )

elif num=='6':
	print('Hi! You want to do Factorial')
	num10=int(input('Enter your number: '))
	result6=factorial(num10)
	print('your Factorial`s answer is ' + str(result6))
