x,y,z = map(float, input().split())
s = ((2*x+y)*(y**3-z)/z)/((x+2*y+3*z)/(z-2*y-3*x)+x**2+z**2)
print("{:.6f}".format(s))
