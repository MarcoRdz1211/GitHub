from big_ol_pile_of_manim_imports import *
import math 

#python -m manim projects\Gamma.py --- -pl

e,pi = math.e,math.pi

def SC(a):
    return ShowCreation(a)

def FO(a):
    return FadeOut(a)

class Imagen(Scene):
    def construct(self):
        escala = 0.5

        axes = Axes(x_min=-5 , x_max=5 , y_min=-3 , y_max=3)
        exp1 = FunctionGraph(self.e1 , x_min=-1 , x_max=5)
        text_e1 = TextMobject(r"$\int_{0}^{\infty} x^2e^{-x}dx$")

        text_e1.move_to([0,3,0])
        initial = VGroup(axes,exp1)

        initial.scale(escala)

        self.add(axes,exp1,text_e1)

    def e1(self,x):
        return (x**2)*(e)**(-x)

class Video(Scene):
#class intro(Scene):
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

#-------------------------Begin---------------

#        self.add_sound("Background.mp3") 
        self.play(SC(circle)) , self.wait(0.5) , self.play(SC(square))
        self.play(ReplacementTransform(square,M)) , self.wait(1)
        self.play(Write(Loge_text),run_time=4) , self.wait(2)
        self.play(FadeOut(M)) , self.wait(0.5)
        self.play(FadeOut(circle)) , self.wait(0.5) 
        self.play(FadeOut(Loge_text))
        self.wait(2)

#-------------------------Gamma---------------
        Text = TextMobject(r"Gamma function: $\Gamma(\alpha)$",color=BLUE)
        Initial_eq = TextMobject(r"$\Gamma(\alpha):=\int_{0}^{\infty} x^{\alpha-1}e^{-x}dx$")

        Text.move_to(3*UP)
        
        self.play(Write(Text)),self.wait(0.5)
        self.play(Write(Initial_text)) , self.wait(2)
        self.play(FO(Text),FO(Initial_eq)) , self.wait(5)        

#-------------------------PlayingEnding---------------        

class end(Scene):
    def construct(self):        
        square = Square(fill_color=BLUE_E,fill_opacity=1)
        heart1 = FunctionGraph(self.h1 , x_min=-1 , x_max=1 , color=WHITE)
        heart2 = FunctionGraph(self.h2 , x_min=-1 , x_max=1 , color= WHITE)
        Math_text = TextMobject("Math",color=BLACK)
        Final_text1 = TextMobject(r"Gracias por ver!",color=GOLD)
        Final_text2 = TextMobject(r"Subscribete para mas",color=GOLD)
        Math_text.move_to(0.2*UP)
        Final_text1.next_to(square,DOWN)
        Final_text2.next_to(Final_text1,DOWN)

        self.play(Write(square),run_time=1),self.wait(1)
        self.play(Write(heart1),run_time=1),self.play(Write(heart2),run_time=1)
        self.add_sound("ending.mp3")
        self.play(Write(Math_text)) , self.wait(1)
        self.play(Write(Final_text1)) , self.play(Write(Final_text2))
        self.wait(5)

    def h1(self,x):
        return ((math.sqrt(abs(x))+math.sqrt(1-x**2))*(10/13)-0.225)

    def h2(self,x):
        return ((math.sqrt(abs(x))-math.sqrt(1-x**2))*(10/13)-0.225)
