import math


a=int(input('a='))
b=int(input('b='))
x=int(input('x='))
e=math.e
if 3*(b**2)>a:
	y=(e**math.sin(x))+b
else:
	y=(e**(-x))+a*(math.log10(x))
print(y)
