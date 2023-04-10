from big_ol_pile_of_manim_imports import *
import math
import numpy as np

#python -m manim projects\graphing.py --- -pl

class Imagen(Scene):
    def construct(self):
        circle = Circle(fill_color=PURPLE_E,fill_opacity=1,color=DARK_GREY)
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
        
        self.add(circle,M,Loge_text)

def SC(a):
    return ShowCreation(a)

#class logo(Scene):
class graphics(Scene):
    def construct(self):
        circle = Circle(fill_color=PURPLE_E,fill_opacity=1,color=DARK_GREY)
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
        
        self.play(SC(circle)) , self.wait(0.5) , self.play(SC(square))
        self.play(Transform(square,M)) , self.wait(1)
        self.play(Write(Loge_text),run_time=4)
        self.wait(1)
        self.play(FadeOut(M),FadeOut(square)) , self.wait(0.5)
        self.play(FadeOut(circle)) , self.play(FadeOut(Loge_text))
        self.wait(1)
        
#class evgraph(ThreeDScene):
#    def construct(self):
        axes = Axes(x_min=-5 , x_max=5 , y_min=-4 , y_max=4)

        axes.set_color(BLUE)

        before_graph = ParametricFunction(lambda x: np.array([x,0,0]),
                                         t_min=-3 , t_max=3 , color=GOLD)

        text = TextMobject(r"$y=1$")
        text.to_corner(UR)
        
        self.play(Write(axes),Write(before_graph),Write(text))
        self.wait(1.5)

        for n in range(1,8):
            after_graph = ParametricFunction(lambda x: np.array([x,x**n,0]),
                                         t_min=-3 , t_max=3 , color=GOLD)

            text_new = TextMobject(r"$y=x^{}$".format(n))
            text_new.to_corner(UR)
            
            self.play(ReplacementTransform(before_graph,after_graph),
                      ReplacementTransform(text,text_new))

            before_graph,text = after_graph,text_new

            self.wait(1.5)

        self.remove(text_new)
        
        for n in range(0,8):
            after_graph = ParametricFunction(lambda x: np.array([3*np.cos(n*x)*np.cos(x),3*np.cos(n*x)*np.sin(x),0]),
                                             t_min=0 , t_max=2*math.pi , color=GOLD)

            text_new = TextMobject(r"$r=cos({} \theta)$".format(n))
            text_new.to_corner(UR)

            self.play(ReplacementTransform(before_graph,after_graph),
                      ReplacementTransform(text,text_new))

            before_graph,text = after_graph,text_new

            self.wait(1.5)

        self.wait(1.5)
        self.remove(after_graph,text_new,axes)
        self.wait(3)

#class end(Scene):
#    def construct(self):        
        square = Square(fill_color=BLUE_E,fill_opacity=1)
        heart1 = FunctionGraph(self.h1 , x_min=-1 , x_max=1 , color=WHITE)
        heart2 = FunctionGraph(self.h2 , x_min=-1 , x_max=1 , color= WHITE)
        Math_text = TextMobject("Math",color="BLACK")
        Final_text1 = TextMobject(r"Cooming soon!?",color="GOLD")
        Math_text.move_to(0.2*UP)
        Final_text1.next_to(square,DOWN)

        self.play(Write(square),run_time=1),self.wait(1)
        self.play(Write(heart1),run_time=1),self.play(Write(heart2),run_time=1)
        self.play(Write(Math_text)) , self.wait(1)
        self.play(Write(Final_text1))
        self.wait(2)

    def h1(self,x):
        return ((math.sqrt(abs(x))+math.sqrt(1-x**2))*(10/13)-0.225)

    def h2(self,x):
        return ((math.sqrt(abs(x))-math.sqrt(1-x**2))*(10/13)-0.225)

