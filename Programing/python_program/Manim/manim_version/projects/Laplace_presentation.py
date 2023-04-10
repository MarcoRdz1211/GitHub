from big_ol_pile_of_manim_imports import *
import math
import random

#python -m manim projects\Laplace_presentation.py --- -pl
e,pi,alpha = math.e,math.pi,random.randint(0,1)+random.uniform(0.2,0.8)
delta = 0.05

class Imagen(Scene):
    def construct(self):

        text = TextMobject(r"Laplace Transform:",r"$\pounds \{ f(t) \} (s)$",
                           r"Visualization in Reals")

        text[0].move_to([0,1,0]),text[1].next_to(text[0],DOWN)
        text[2].next_to(text[1],2*DOWN)
        text[0].set_color(GOLD),text[1].set_color(WHITE)
        text[2].set_color(BLUE)

        self.add(text)

class Laplace(Scene):
    CONFIG = {
        "plane_kwargs" : {
        "color" : RED
            },
        }
    def construct(self):
        pause_1,pause_2,pause_3,rt = 3,4,2,2
        print(alpha)


#------------------------------------ Presentation ------------------


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

        text = TextMobject(r"Laplace Transform:",r"$\pounds \{ f(t) \} (s)$")

        text[0].move_to([0,1,0]),text[1].next_to(text[0],DOWN)
        text[0].set_color(GOLD),text[1].set_color(WHITE)

        self.add_sound("Background_video.mp3") 

        self.play(ShowCreation(circle)) , self.wait(0.5) ,
        self.play(ShowCreation(square)) , self.play(Transform(square,M))
        self.wait(1) , self.play(Write(Loge_text),run_time=4)
        self.wait(1)
        self.play(FadeOut(M),FadeOut(square)) , self.wait(0.5)
        self.play(FadeOut(circle)) , self.play(FadeOut(Loge_text))
        self.wait(3)

        self.play(Write(text),run_time = 3) , self.wait(3)

        self.play(FadeOut(text),run_time = 3) , self.wait(3)


#------------------------------------ Plane and A(x) [constant function] ------------------

        
        plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels()) #add x and y label
        self.play(Write(plane)) #Place grid on screen

        text_a = TextMobject(r"$f(t)=\alpha$")
        graph_a = FunctionGraph(self.a, color=BLUE, x_min=-7, x_max=7)
        text_A = TextMobject(r"$\pounds \{ f(t) \} (s) = \frac{ \alpha }{s}$")
        graph_A = FunctionGraph(self.A, color=YELLOW, x_min=delta, x_max=7)
        
        text_a.move_to([-5,3.5,0]) , text_A.move_to([-5,2.5,0])


        self.play(Write(graph_a),Write(text_a)) , self.wait(pause_1)
        self.play(ReplacementTransform(graph_a.copy(),graph_A),Write(text_A))
        self.wait(pause_2)

        self.play(FadeOut(graph_a),FadeOut(text_a),FadeOut(graph_A),
                  FadeOut(text_A),run_time = rt)
        self.wait(pause_3)


#------------------------------------ B(x) [exponential function] ------------------


        text_b = TextMobject(r"$f(t)=e^{ \alpha t}$")
        graph_b = FunctionGraph(self.b, color=BLUE, x_min=-7, x_max=7)
        text_B = TextMobject(r"$\pounds \{ f(t) \} (s) = \frac{1}{s-\alpha}$")
        graph_B = FunctionGraph(self.B, color=YELLOW, x_min=alpha+delta, x_max=7)
        
        text_b.move_to([-5,3.5,0]) , text_B.move_to([-5,2.5,0])

        
        self.play(Write(graph_b),Write(text_b)) , self.wait(pause_1)
        self.play(ReplacementTransform(graph_b.copy(),graph_B),Write(text_B))
        self.wait(pause_2)

        self.play(FadeOut(graph_b),FadeOut(text_b),FadeOut(graph_B),
                  FadeOut(text_B),run_time = rt)
        self.wait(pause_3)


#------------------------------------ C(x) [power function] ------------------


        text_c = TextMobject(r"$f(t)=t^{ \alpha }$")
        graph_c = FunctionGraph(self.c, color=BLUE, x_min=0, x_max=7)
        text_C = TextMobject(r"$\pounds \{ f(t) \} (s) = \frac{ \alpha !}{s^{ \alpha + 1 }}$")
        graph_C = FunctionGraph(self.C, color=YELLOW, x_min=2*delta, x_max=7)
        
        text_c.move_to([-5,3.5,0]) , text_C.move_to([-5,2.5,0])

        
        self.play(Write(graph_c),Write(text_c)) , self.wait(pause_1)
        self.play(ReplacementTransform(graph_c.copy(),graph_C),Write(text_C))
        self.wait(pause_2)

        self.play(FadeOut(graph_c),FadeOut(text_c),FadeOut(graph_C),
                  FadeOut(text_C),run_time = rt)
        self.wait(pause_3)

        
#------------------------------------ D(x) [sine function] ------------------


        text_d = TextMobject(r"$f(t)=sin( \alpha t)$")
        graph_d = FunctionGraph(self.d, color=BLUE, x_min=-7, x_max=7)
        text_D = TextMobject(r"$\pounds \{ f(t) \} (s) = \frac{ \alpha }{s^2 + \alpha^2}$")
        graph_D = FunctionGraph(self.D, color=YELLOW, x_min=delta, x_max=7)
        
        text_d.move_to([-5,3.5,0]) , text_D.move_to([-5,2.5,0])

        
        self.play(Write(graph_d),Write(text_d)) , self.wait(pause_1)
        self.play(ReplacementTransform(graph_d.copy(),graph_D),Write(text_D))
        self.wait(pause_2)

        self.play(FadeOut(graph_d),FadeOut(text_d),FadeOut(graph_D),
                  FadeOut(text_D),run_time = rt)
        self.wait(pause_3)
        

#------------------------------------ F(x) [cosine function] ------------------


        text_f = TextMobject(r"$f(t)=cos( \alpha t)$")
        graph_f = FunctionGraph(self.f, color=BLUE, x_min=-7, x_max=7)
        text_F = TextMobject(r"$\pounds \{ f(t) \} (s) = \frac{s}{s^2 + \alpha^2}$")
        graph_F = FunctionGraph(self.F, color=YELLOW, x_min=delta, x_max=7)
        
        text_f.move_to([-5,3.5,0]) , text_F.move_to([-5,2.5,0])

        
        self.play(Write(graph_f),Write(text_f)) , self.wait(pause_1)
        self.play(ReplacementTransform(graph_f.copy(),graph_F),Write(text_F))
        self.wait(pause_2)

        self.play(FadeOut(graph_f),FadeOut(text_f),FadeOut(graph_F),
                  FadeOut(text_F),run_time = rt)
        self.wait(pause_3)

        
#------------------------------------ G(x) [hiperbolic sine function] ------------------


        text_g = TextMobject(r"$f(t)=sinh( \alpha t)$")
        graph_g = FunctionGraph(self.g, color=BLUE, x_min=-7, x_max=7)
        text_G = TextMobject(r"$\pounds \{ f(t) \} (s) = \frac{ \alpha }{s^2 - \alpha^2}$")
        graph_G_1 = FunctionGraph(self.G, color=YELLOW, x_min=alpha+delta, x_max=7)
        graph_G_2 = FunctionGraph(self.G, color=YELLOW, x_min=-7, x_max=-alpha-delta)
        
        text_g.move_to([-5,3.5,0]) , text_G.move_to([-5,2.5,0])

        
        self.play(Write(graph_g),Write(text_g)) , self.wait(pause_1)
        self.play(ReplacementTransform(graph_g.copy(),graph_G_1),
                  ReplacementTransform(graph_g.copy(),graph_G_2),Write(text_G))
        self.wait(pause_2)

        self.play(FadeOut(graph_g),FadeOut(text_g),FadeOut(graph_G_1),
                  FadeOut(graph_G_2),FadeOut(text_G),run_time = rt)
        self.wait(pause_3)
        

#------------------------------------ H(x) [hiperbolic cosine function] ------------------


        text_h = TextMobject(r"$f(t)=cosh( \alpha t)$")
        graph_h = FunctionGraph(self.h, color=BLUE, x_min=-7, x_max=7)
        text_H = TextMobject(r"$\pounds \{ f(t) \} (s) = \frac{s}{s^2 - \alpha^2}$")
        graph_H_1 = FunctionGraph(self.H, color=YELLOW, x_min=alpha+delta, x_max=7)
        graph_H_2 = FunctionGraph(self.H, color=YELLOW, x_min=-7, x_max=-alpha-delta)
        
        text_h.move_to([-5,3.5,0]) , text_H.move_to([-5,2.5,0])

        
        self.play(Write(graph_h),Write(text_h)) , self.wait(pause_1)
        self.play(ReplacementTransform(graph_h.copy(),graph_H_1),
                  ReplacementTransform(graph_h.copy(),graph_H_2),Write(text_H))
        self.wait(pause_2)

        self.play(FadeOut(graph_h),FadeOut(text_h),FadeOut(graph_H_1),
                  FadeOut(graph_H_2),FadeOut(text_H),run_time = rt)
        self.wait(pause_3)


#------------------------------------ Final ------------------


        self.play(FadeOut(plane))

        square = Square(fill_color=BLUE_E,fill_opacity=1)
        heart1 = FunctionGraph(self.h1 , x_min=-1 , x_max=1 , color=WHITE)
        heart2 = FunctionGraph(self.h2 , x_min=-1 , x_max=1 , color= WHITE)
        Math_text = TextMobject("Math",color=BLACK)
        Final_text1 = TextMobject(r"Proximamente!",color=GOLD)
        Math_text.move_to(0.2*UP)
        Final_text1.next_to(square,DOWN)

        self.play(Write(square),run_time=1),self.wait(1)
        self.play(Write(heart1),run_time=1),self.play(Write(heart2),run_time=1)
        self.play(Write(Math_text)) , self.wait(1)
        self.play(Write(Final_text1))
        self.wait(5)


#------------------------------------ Graph's definition ------------------


    def a(self,x):
        return alpha

    def A(self,x):
        return alpha/x

    def b(self,x):
        return e**(alpha*x)

    def B(self,x):
        return 1/(x-alpha)

    def c(self,x):
        return x**alpha

    def C(self,x):
        n = alpha+1
        s = math.gamma(n)
        return s/(x**n)

    def d(self,x):
        return math.sin(alpha*x)

    def D(self,x):
        return (alpha)/(x**2+alpha**2)

    def f(self,x):
        return math.cos(alpha*x)

    def F(self,x):
        return x/(x**2+alpha**2)

    def g(self,x):
        return math.sinh(alpha*x)

    def G(self,x):
        return (alpha)/(x**2-alpha**2)

    def h(self,x):
        return math.cosh(alpha*x)

    def H(self,x):
        return x/(x**2-alpha**2)

    def FO(x):
        return FadeOut(x)

#------------------------------------ Final's graphs definition ------------------

    def e1(self,x):
        return (math.e)**(-x**2)

    def e2(self,x):
        return -(math.e)**(-x**2)

    def h1(self,x):
        return ((math.sqrt(abs(x))+math.sqrt(1-x**2))*(10/13)-0.225)

    def h2(self,x):
        return ((math.sqrt(abs(x))-math.sqrt(1-x**2))*(10/13)-0.225)

