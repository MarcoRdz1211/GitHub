from big_ol_pile_of_manim_imports import *
import math
import random

#python -m manim projects\Laplace_constant.py --- -pl
e,pi,alpha = math.e,math.pi,random.randint(1,2)+random.uniform(0.2,0.8)
delta = 0.05

class Imagen(GraphScene):
    def construct(self):

        text = TextMobject(r"Laplace Transform:",r"$\pounds \{ f(t) \} (s)$",
                           r"Visualization in Reals")

        text[0].move_to([0,1,0]),text[1].next_to(text[0],DOWN)
        text[2].next_to(text[1],2*DOWN)
        text[0].set_color(GOLD),text[1].set_color(WHITE)
        text[2].set_color(BLUE)

        self.add(text)

class Constant(GraphScene):
    CONFIG = {"x_min" : -8,
              "x_max" : 8,
              "y_min" : -8,
              "y_max" : 8,
              "graph_origin" : [0,0,0],
              "function_color" : BLUE,
              "opacity" : 0.5,
              "axes_color" : GREEN,
              "x_axis_label": "",
              "y_axis_label": "",
              "y_axis_height": 16,
              "x_axis_width": 16} 
 
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

#        self.add_sound("Background_video.mp3") 

#        self.play(ShowCreation(circle)) , self.wait(0.5) ,
#        self.play(ShowCreation(square)) , self.play(Transform(square,M))
#        self.wait(1) , self.play(Write(Loge_text),run_time=4)
#        self.wait(1)
#        self.play(FadeOut(M),FadeOut(square)) , self.wait(0.5)
#        self.play(FadeOut(circle)) , self.play(FadeOut(Loge_text))
#        self.wait(3)

#        self.play(Write(text),run_time = 3) , self.wait(3)

#        self.play(FadeOut(text),run_time = 3) , self.wait(3)


#------------------------------------ Plane and A(x) [constant function] ------------------

        self.setup_axes(animate=False)
        
        plane = NumberPlane(color=RED) #Create axes and grid
        plane.add(plane.get_axis_labels()) #add x and y label
        self.play(Write(plane)) #Place grid on screen

        text_a = TextMobject(r"$f(t)=\alpha$")
        graph_a = self.get_graph(lambda x: alpha, color=BLUE, x_min=-7, x_max=7)
        text_A = TextMobject(r"$\pounds \{ f(t) \} (s) = \frac{ \alpha }{s}$")
        graph_A = self.get_graph(lambda x: alpha/x, color=YELLOW, x_min=5*delta, x_max=7)

        area = self.get_riemann_rectangles(graph_a, x_min=0, x_max=7,
                                           dx = 0.01, stroke_width = 0.01,
                                           stroke_color = BLUE, start_color = BLUE,
                                           end_color = BLUE)
        
        text_a.move_to([-5,3.5,0]) , text_A.move_to([-5,2.5,0])


        self.play(Write(graph_a),Write(text_a)) , self.wait(pause_1)
        self.play(FadeIn(area)) , self.wait(pause_1)
        self.play(ReplacementTransform(area,graph_A),Write(text_A))
        self.wait(pause_2)

        self.play(FadeOut(graph_a),FadeOut(text_a),FadeOut(graph_A),
                  FadeOut(text_A),run_time = rt)
        self.wait(pause_3)


#------------------------------------ Final ------------------


        self.play(FadeOut(plane),FadeOut(self.axes))
        self.wait(pause_3)


        square = Square(fill_color=BLUE_E,fill_opacity=1)
        heart1 = FunctionGraph(self.h1 , x_min=-1 , x_max=1 , color=WHITE)
        heart2 = FunctionGraph(self.h2 , x_min=-1 , x_max=1 , color= WHITE)
        Math_text = TextMobject("Math",color=BLACK)
        Final_text1 = TextMobject(r"Proximamente!",color=GOLD)
        Math_text.move_to(0.2*UP)
        Final_text1.next_to(square,DOWN)

#        self.play(Write(square),run_time=1),self.wait(1)
#        self.play(Write(heart1),run_time=1),self.play(Write(heart2),run_time=1)
#        self.play(Write(Math_text)) , self.wait(1)
#        self.play(Write(Final_text1))
#        self.wait(5)


#------------------------------------ Graph's definition ------------------

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

