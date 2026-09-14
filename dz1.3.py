a=bool
x,y=float(input('x=')),float(input('y='))
if x**2+y**2<=4:
    if y>=(x+2) or y>=(-x+2):a=True
if x>=-2 and x<=2 and y<=0 and y>=-1: a=True
print(a)

