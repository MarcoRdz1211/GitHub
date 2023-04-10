import matplotlib.pyplot as plt
import random
import numpy as np
import math
from matplotlib.animation import FuncAnimation
from big_ol_pile_of_manim_imports import *

#python -m manim projects\Fractal-Animation.py --- -pl

class Fractal(Scene):
    def sqrt(x):
        return math.sqrt(x)

    def f1(x0,y0,zx,zy):
        x,y =(1+x0*zx-y0*zy),(x0*zy+y0*zx)
        return [x,y]

    def f2(x0,y0,zx,zy):
        x,y =(-1-x0*zx+y0*zy),(-x0*zy-y0*zx)
        return [x,y]
    
    def construct(self):
        X = [[0,0]]
        
        k = 12 #if n>13. then it's gonna need a big time.
        zx,zy = random.uniform(-1,1),random.uniform(-1,1)

        n = len(X)
        for i in range(0,n):
            point=Dot([1+x0*zx-y0*zy,x0*zy+y0*zx,0])            
            self.add(point)
            point=Dot([-1-x0*zx+y0*zy,-x0*zy-y0*zx,0])            
            self.add(point)

        self.wait(3)
