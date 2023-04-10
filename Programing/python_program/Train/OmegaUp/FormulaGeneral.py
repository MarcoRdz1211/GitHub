a,b,c = map(int, input().split())

x1,x2 = (-b+(b**2-4*a*c)**(1/2))/(2*a),(-b-(b**2-4*a*c)**(1/2))/(2*a)

print(x1,x2)
