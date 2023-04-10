import math

v,theta,direction = map(int, input().split(","))

if (direction==0):
    theta = 180-theta

theta = math.pi*theta/180
ans = v*math.cos(theta)

print(int(ans))
