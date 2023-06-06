from big_ol_pile_of_manim_imports import *
import math 

#python -m manim projects\Problem.py --- -pl

e,pi = EXP,PI

class Imagen(Scene):
    def construct(self):
        escala = 0.5

        axes = Axes(x_min=-5 , x_max=5 , y_min=-3 , y_max=3)
        circle = Circle(radius = math.sqrt(math.log(math.sqrt(2*e),e)),
                        fill_color=BLUE_D,fill_opacity=0.5,color="DARKGREY")
        exp1 = FunctionGraph(self.e1 , x_min=-5 , x_max=5)
        exp2 = FunctionGraph(self.e2 , x_min=-5 , x_max=5)

        text_e1 = TextMobject(r"$e^{-x^2}$")
        text_e2 = TextMobject(r"$-e^{-x^2}$")

        text_e1.move_to([4.5,1,0])
        text_e2.move_to([4.5,-1,0])

        self.add(axes,circle,exp1,exp2,text_e1,text_e2)

    def e1(self,x):
        return (math.e)**(-x**2)

    def e2(self,x):
        return -(math.e)**(-x**2)

def SC(a):
    return ShowCreation(a)


class Video(Scene):
#class intro(Scene):
    def construct(self):
        circle = Circle(fill_color=PURPLE_E,fill_opacity=1,color="DARKGREY")
        square = Square(color=BLUE_D)
        M_coordinates = [(0,0,0) , (0.5,math.sqrt(0.75),0),
                         (0.6,0.8,0) , (0.6,-0.8,0),
                         (0.5,-math.sqrt(0.75),0),
                         (0.5,0.65847,0) , (0,-0.20755,0),
                         (-0.5,0.65847,0) , (-0.5,-math.sqrt(0.75),0),
                         (-0.6,-0.8,0) , (-0.6,0.8,0),
                         (-0.5,math.sqrt(0.75),0)]
        M = Polygon(*M_coordinates,color=BLACK,fill_color=WHITE,fill_opacity=1)
        Loge_text = TextMobject(r"That simple math guy",color=WHITE)
        Loge_text.next_to(circle,DOWN)

#class initial(Scene):
#    def construct(self):
        escala = 0.5

        func1 = FunctionGraph(self.e1 , x_min=-5 , x_max=5)
        func2 = FunctionGraph(self.e2 , x_min=-5 , x_max=5)

#-------------------------Playing first---------------        
        a         = 3
        colorLine = RED
        dots = [Dot([-a,-a,0]),
                Dot([-a,a,0]),
                Dot([a,a,0]),
                Dot([a,-a,0])]
        lines = [Line(dots[0],dots[1],color=colorLine),
                 Line(dots[1],dots[2],color=colorLine),
                 Line(dots[2],dots[3],color=colorLine),
                 Line(dots[3],dots[0],color=colorLine)
                 ]
        for dot in dots:
                i = dots.index(dot)
                self.play(Write(dots[i].set_color(BLUE),run_time=0.1))
                self.play(Write(lines[i]),run_time=0.1)

        dots = []
        i,x0 = 0.5,0.5
        while i<2*a:
            dots.append(Dot([-a+i,a,0]))
            dots.append(Dot([a,a-i,0]))
            dots.append(Dot([a-i,-a,0]))
            dots.append(Dot([-a,-a+i,0]))
            i += x0

        for i in range(0,len(dots)):
                self.play(Write(dots[i].set_color(BLUE)),run_time=0.1)

        lines = []
        for i in range(0,len(dots)):
            x,y,z = dots[i].get_center()
            lines.append(Line(dots[i],Dot([y,-x,z]),color=WHITE))
            #lines.append(Line(dots[i],Dot([-x,-y,z]),color=WHITE))
            #lines.append(Line(dots[i],Dot([-y,x,z]),color=WHITE))
            #lines.append(Line(dots[i],Dot([x,y,z]),color=WHITE))

        for line in lines:
                self.play(Write(line),run_time=0.1)

        self.wait(10)

    def e1(self,x):
        return e**(-x**2)

    def e2(self,x):
        return -e**(-x**2)

    def h1(self,x):
        return ((math.sqrt(abs(x))+math.sqrt(1-x**2))*(10/13)-0.225)

    def h2(self,x):
        return ((math.sqrt(abs(x))-math.sqrt(1-x**2))*(10/13)-0.225)
