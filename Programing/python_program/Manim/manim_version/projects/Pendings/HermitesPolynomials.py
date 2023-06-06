from big_ol_pile_of_manim_imports import *
import math
import numpy

#python -m manim projects\HermitesPolynomials.py --- -pl

e,pi = math.e,math.pi



class Imagen(Scene):
    def construct(self):
        text1 = TextMobject(r"$H_{n}(x)=(-1)^{n}e^{x^2} \frac{d^{n}}{dx^{n}}(e^{-x^2})$")

        text1.move_to([0,0,0])

        self.add(text1)

def SC(a):
    return ShowCreation(a)


#class Video(Scene):
class intro(Scene):
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

#-------------------------Playin begin---------------        

        self.add_sound("Background.mp3") 
        self.play(SC(circle)) , self.wait(0.5) , self.play(SC(square))
        self.play(ReplacementTransform(square,M)) , self.wait(1)
        self.play(Write(Loge_text),run_time=4) , self.wait(2)
        self.play(FadeOut(M)) , self.wait(0.5)
        self.play(FadeOut(circle)) , self.wait(0.5) 
        self.play(FadeOut(Loge_text))
        self.wait(2)

class Initial(Scene):
    def construct(self):
        text1 = TextMobject("Sea "+r"$H_{n}(x)$"+" una funcion definida por: ").set_color(GOLD)
        eq1 = TextMobject(r"$H_{n}(x)=(-1)^{n}e^{x^2} \frac{d^{n}}{dx^{n}}(e^{-x^2})$")

        text1.next_to(text1,UP)

        self.play(FadeIn(text1),run_time=1) , self.wait(1)
        self.play(FadeIn(eq1),run_time=1) , self.wait(1)

        text1_new = TextMobject("Trabajando con:"+r"$h_{n}(x)$").set_color(GOLD)
        eq1_new = TextMobject(r"$h_{n}(x)=\frac{d^{n}}{dx^{n}}(e^{-x^2})$")

        text1_new.to_edge(UP) , eq1_new.next_to(text1_new,DOWN)

#------------------------------------

        self.play(ReplacementTransform(text1,text1_new),
                  ReplacementTransform(eq1,eq1_new),run_time=1) , self.wait(1)

        #Animations: 4
        
        text2 = TextMobject("Para el caso: "+r"$n=0$").set_color(GOLD)
        eq2 = TextMobject(r"$h_{n}(x)=\frac{d^{n}}{dx^{n}}(e^{-x^2})$")
        eq2_new1 = TextMobject(r"$h_{0}(x)=\frac{d^{0}}{dx^{0}}(e^{-x^2})$")
        eq2_new2 = TextMobject(r"$h_{0}(x)=e^{-x^2}$")

        text2.next_to(eq1_new,2*DOWN) , eq2.next_to(text2,DOWN)
        eq2_new1.move_to(eq2) , eq2_new2.move_to(eq2_new1)

#------------------------------------

        self.play(FadeIn(text2),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq1_new.copy(),eq2),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq2,eq2_new1),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq2_new1,eq2_new2),run_time=1) , self.wait(1)

        #Animations: 12

        text3 = TextMobject("Para el caso: "+r"$n=1$").set_color(GOLD)
        eq3 = TextMobject(r"$h_{n}(x)=\frac{d^{n}}{dx^{n}}(e^{-x^2})$")
        eq3_new1 = TextMobject(r"$h_{1}(x)=\frac{d^{1}}{dx^{1}}(e^{-x^2})$")
        eq3_new2 = TextMobject(r"$h_{1}(x)=-2xe^{-x^2}$")

        text3.next_to(eq2_new2,2*DOWN) , eq3.next_to(text3,DOWN)
        eq3_new1.move_to(eq3) , eq3_new2.move_to(eq3_new1)

#------------------------------------

        self.play(FadeIn(text3),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq1_new.copy(),eq3),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq3,eq3_new1),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq3_new1,eq3_new2),run_time=1) , self.wait(1)

        #Animations: 

        text4 = TextMobject("Para el caso: "+r"$n=2$").set_color(GOLD)
        eq4 = TextMobject(r"$h_{n}(x)=\frac{d^{n}}{dx^{n}}(e^{-x^2})$")
        eq4_new1 = TextMobject(r"$h_{2}(x)= \frac{d^{2}}{dx^{2}}(e^{-x^2})$")
        eq4_new2 = TextMobject(r"$h_{2}(x)=(-2(-2x)-2)e^{-x^2}$")
        eq4_new3 = TextMobject(r"$h_{2}(x)=(4x^{2}-2)e^{-x^2}$")

        text4.next_to(eq3_new2,2*DOWN) , eq4.next_to(text4,DOWN)
        eq4_new1.move_to(eq4) , eq4_new2.move_to(eq4_new1)
        eq4_new3.move_to(eq4_new2)

        self.play(FadeIn(text4),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq1_new.copy(),eq4),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq4,eq4_new1),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq4_new1,eq4_new2),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq4_new2,eq4_new3),run_time=1) , self.wait(2)

        #Animations: 

#------------------------------------

        hermit_equation = eq1.copy()
        hermit_region = Rectangle(height=1,widht=3).set_color(RED)
        eq_hermit = VGroup(hermit_equation,hermit_region)

        eq_aux0,eq_aux1,eq_aux2 = eq2_new2.copy(),eq3_new2.copy(),eq4_new3.copy()
        eq_aux0,eq_aux1,eq_aux2 = eq_aux0.scale(0.8),eq_aux1.scale(0.8),eq_aux2.scale(0.8)
        aux_region = Rectangle(height=3,widht=6).set_color(BLUE)

        eq_aux1.next_to(eq_aux0,DOWN),eq_aux2.next_to(eq_aux1,DOWN),aux_region.move_to(eq_aux1)
        aux_equations = VGroup(eq_aux0,eq_aux1,eq_aux2,aux_region).scale(0.75)
        aux_equations.to_corner(DOWN+RIGHT),hermit_equation.to_edge(UP)
        hermit_region.move_to(hermit_equation)

        self.play(FadeOut(text2),FadeOut(text3),FadeOut(text4),FadeOut(text1_new),
                  ReplacementTransform(eq1_new,hermit_equation),
                  ReplacementTransform(eq2_new2,aux_equations[0]),
                  ReplacementTransform(eq3_new2,aux_equations[1]),
                  ReplacementTransform(eq4_new3,aux_equations[2]),
                  FadeIn(aux_equations[3]),FadeIn(hermit_region),
                  run_time=1.5) , self.wait(1)
        
        #Animations: 

#------------------------------------

        text5 = TextMobject("Notese que: ").set_color(GOLD)
        eq5_0 = TextMobject(r"$h_{0}(x)=P_{0}(x)e^{-x^2}   P_{0} \in \mathbb{P}_{0}(\mathbb{R})$")
        eq5_1 = TextMobject(r"$h_{1}(x)=P_{1}(x)e^{-x^2}   P_{1} \in \mathbb{P}_{1}(\mathbb{R})$")
        eq5_2 = TextMobject(r"$h_{2}(x)=P_{2}(x)e^{-x^2}   P_{2} \in \mathbb{P}_{2}(\mathbb{R})$")

        text5.move_to([0,2,0])
        eq5_0.next_to(text5,DOWN),eq5_1.next_to(eq5_0,DOWN)
        eq5_2.next_to(eq5_1,DOWN)

        self.play(FadeIn(text5),run_time=2)
        self.play(FadeIn(eq5_0),FadeIn(eq5_1),
                  FadeIn(eq5_2),run_time=2)
        self.wait(2)

        self.play(FadeOut(text5),FadeOut(eq5_0),FadeOut(eq5_1),
                  FadeOut(eq5_1),FadeOut(eq5_2),run_time=2) , self.wait(2)

        #Animations: 39

#------------------------------------

        text6 = TextMobject("Considerese que: "+r"$h_{k}(x)=P_{k}(x)e^{-x^2}$").set_color(GOLD)
        eq6 = TextMobject(r"$P_{k}(x) \in \mathbb{P}_{k}(\mathbb{R})$").set_color(GOLD)

#        text6.next_to(eq_hermit,DOWN),eq6.next_to(text6,DOWN)

        eq6.next_to(text6,DOWN)

        text7 = TextMobject("Vease que, para el caso:").set_color(GOLD)
        eq7 = TextMobject(r"$n=k+1$")

        eq7.next_to(text7,RIGHT)

        equations7 = VGroup(text7,eq7).move_to([0,0,0])

        self.play(FadeIn(equations7),run_time=1) , self.wait(1)

#------------------------------------

        eq7_0 = TextMobject(r"$h_{k+1}(x)=\frac{d^{k+1}}{dx^{k+1}}(e^{-x^2})$")
        eq7_1 = TextMobject(r"$h_{k+1}(x)=\frac{d}{dx}(\frac{d^{k}}{dx^{k}}(e^{-x^2}))$")
        eq7_2 = TextMobject(r"$h_{k+1}(x)=\frac{d}{dx}(h_{k}(x))$")
        eq7_3 = TextMobject(r"$h_{k+1}(x)=\frac{d}{dx}(P_{k}(x)e^{-x^2})$")
        eq7_4 = TextMobject(r"$h_{k+1}(x)=P'_{k}(x)e^{-x^2}-2xP_{k}(x)e^{-x^2}$")
        eq7_5 = TextMobject(r"$h_{k+1}(x)=[P'_{k}(x)-2xP_{k}(x)]e^{-x^2}$")

        eq7_0.next_to(equations7,DOWN),eq7_1.move_to(eq7_0),eq7_2.move_to(eq7_0)
        eq7_3.move_to(eq7_0),eq7_4.move_to(eq7_0),eq7_5.move_to(eq7_0)

        self.play(FadeIn(eq7_0),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq7_0,eq7_1),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq7_1,eq7_2),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq7_2,eq7_3),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq7_3,eq7_4),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq7_4,eq7_5),run_time=1) , self.wait(1)
        self.play(FadeOut(equations7),FadeOut(eq7_5),run_time=1) , self.wait(1)
        
#------------------------------------

        text8 = TextMobject("Como:").set_color(GOLD)
        eq8 = TextMobject(r"$P_{k} \in \mathbb{P}_{k}(\mathbb{R})$",
                          r"$\Rightarrow P'_{k}\in \mathbb{P}_{k-1}(\mathbb{R})$")
        eq8_new1 = TextMobject(r"$P_{k} \in \mathbb{P}_{k}(\mathbb{R})$",
                          r"$\Rightarrow 2xP_{k}\in \mathbb{P}_{k+1}(\mathbb{R})$")
        eq8_new2 = TextMobject(r"$(P'_{k}(x)-2xP_{k}(x))\in \mathbb{P}_{k+1}(\mathbb{R})$")

        text8.next_to(eq8,UP),eq8_new1.next_to(eq8,DOWN),eq8_new2.next_to(eq8_new1,DOWN)

        self.play(FadeIn(text8),FadeIn(eq8),run_time=1) , self.wait(1)
        self.play(FadeIn(eq8_new1),run_time=1) , self.wait(1)
        self.play(FadeIn(eq8_new2),run_time=1) , self.wait(1)
        self.play(FadeOut(text8),FadeOut(eq8),FadeOut(eq8_new1),
                  FadeOut(eq8_new2),run_time=1) , self.wait(1)

#------------------------------------

        text9 = TextMobject("Considerando: ").set_color(GOLD)
        eq9 = TextMobject(r"$P_{k+1}(x)=P'_{k}(x)-2xP_{k}(x):$")
        eq9_new = TextMobject(r"$h_{k+1}(x)=P_{k+1}(x)e^{-x^2}$")

        text9.next_to(eq9,UP),eq9_new.next_to(eq9,DOWN)

        self.play(FadeIn(text9),FadeIn(eq9),FadeIn(eq9_new),run_time=1) , self.wait(1)
        self.play(FadeOut(text9),FadeOut(eq9),FadeOut(eq9_new),run_time=1) , self.wait(1)

#------------------------------------

        text10 = TextMobject("Entonces: ").set_color(GOLD)
        eq10 = TextMobject(r"$h_{n}(x)=\frac{d^{n}}{dx^{n}}(e^{-x^2})$")
        eq10_new = TextMobject(r"$h_{n}(x)=P_{n}(x)e^{-x^2}$")

        text10.next_to(eq10,UP),eq10_new.next_to(text10,RIGHT)

        self.play(FadeIn(text10),FadeIn(eq10),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq10,eq10_new),run_time=1) , self.wait(1)
        self.play(FadeOut(text10),FadeOut(eq10_new),run_time=1) , self.wait(1)

#------------------------------------

        text11 = TextMobject("Retomando las funciones de Hermit").set_color(GOLD)
        eq11 = TextMobject(r"$H_{n}(x)=(-1)^{n}e^{x^2} \frac{d^{n}}{dx^{n}}(e^{-x^2})$")
        eq11_new1 = TextMobject(r"$H_{n}(x)=(-1)^{n}e^{x^2}h_{n}(x)$")
        eq11_new2 = TextMobject(r"$H_{n}(x)=(-1)^{n}e^{x^2}h_{n}(x)$")
        eq11_new3 = TextMobject(r"$H_{n}(x)=(-1)^{n}e^{x^2}P_{n}(x)e^{-x^2}$")
        eq11_new4 = TextMobject(r"$H_{n}(x)=(-1)^{n}P_{n}(x)$")

        eq11.next_to(text11,DOWN),eq11_new1.move_to(eq11),eq11_new2.move_to(eq11)
        eq11_new3.move_to(eq11),eq11_new4.move_to(eq11)

        self.play(FadeIn(text11),FadeIn(eq11),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq11,eq11_new1),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq11_new1,eq11_new2),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq11_new2,eq11_new3),run_time=1) , self.wait(1)
        self.play(ReplacementTransform(eq11_new3,eq11_new4),run_time=1) , self.wait(1)
        self.play(FadeOut(text11),FadeOut(eq11_new4),FadeOut(eq_hermit),FadeOut(aux_equations),
                  run_time=1),self.wait(1)

#------------------------------------

        text12 = TextMobject("Entonces: ").set_color(GOLD)
        eq12 = TextMobject(r"$H_{n}$")
        text12_final = TextMobject("representa un polinomio de grado n").set_color(GOLD)
        
        eq12.next_to(text12,RIGHT),text12_final.next_to(text12,DOWN)
        
        self.play(FadeIn(text12),FadeIn(eq12),FadeIn(text12_final),run_time=1),self.wait(1)
        self.play(FadeOut(text12),FadeOut(eq12),FadeOut(text12_final),run_time=1),self.wait(1)
        
#-------------------------PlayingEnding---------------        

#class Graph(Scene):
#    def construct(self):
        a = 8
        
        text1 = TextMobject("Polinomios de Hermite "+r"$H_{n}(x)$").set_color(YELLOW)
        equation1 = TextMobject(r"$H_{n}(x)=(-1)^{n}e^{x^2} \frac{d^{n}}{dx^{n}}(e^{-x^2})$")

        x_axis = FunctionGraph(self.x0, color=WHITE, x_min=-a, x_max=a)
        y_axis = x_axis.copy()
        y_axis.rotate(PI/2)

        graph_0 = FunctionGraph(self.H0, color=DARK_BLUE, x_min=-a, x_max=a)
        graph_1 = FunctionGraph(self.H1, color=BLUE, x_min=-a, x_max=a)
        graph_2 = FunctionGraph(self.H2, color=GREEN, x_min=-a, x_max=a)
        graph_3 = FunctionGraph(self.H3, color=YELLOW, x_min=-a, x_max=a)
        graph_4 = FunctionGraph(self.H4, color=ORANGE, x_min=-a, x_max=a)

        eq0 = TextMobject(r"$H_{0}(x)$").set_color(DARK_BLUE).scale(0.9)
        eq1 = TextMobject(r"$H_{1}(x)$").set_color(BLUE).scale(0.9)
        eq2 = TextMobject(r"$H_{2}(x)$").set_color(GREEN).scale(0.9)
        eq3 = TextMobject(r"$H_{3}(x)$").set_color(YELLOW).scale(0.9)
        eq4 = TextMobject(r"$H_{4}(x)$").set_color(ORANGE).scale(0.9)

        text1.scale(0.75),equation1.scale(0.75)
        text1.to_corner(UP+LEFT),equation1.next_to(text1,DOWN)

        eq4.to_corner(DOWN+RIGHT)
        eq3.next_to(eq4,UP),eq2.next_to(eq3,UP)
        eq1.next_to(eq2,UP),eq0.next_to(eq1,UP)

        self.play(FadeIn(x_axis),FadeIn(y_axis),run_time=1), self.wait(1)
        self.play(FadeIn(text1),run_time=1) , self.wait(1)
        self.play(FadeIn(equation1),run_time=1) , self.wait(1)
        self.play(Write(graph_0),FadeIn(eq0),run_time=2) , self.wait(1)
        self.play(Write(graph_1),FadeIn(eq1),run_time=2) , self.wait(1)
        self.play(Write(graph_2),FadeIn(eq2),run_time=2) , self.wait(1)
        self.play(Write(graph_3),FadeIn(eq3),run_time=2) , self.wait(1)
        self.play(Write(graph_4),FadeIn(eq4),run_time=2) , self.wait(1)

    def x0(self,x):
        return 0

    def H0(self,x):
        n,g = 0,0

        for m in range(0,n//2+1):
            s = ((-1)**m)*math.factorial(n)/(math.factorial(m)*math.factorial(n-2*m))
            g += s*(2**(n-2*m))*x**(n-2*m)
        
        return g
    
    def H1(self,x):
        n,g = 1,0

        for m in range(0,n//2+1):
            s = ((-1)**m)*math.factorial(n)/(math.factorial(m)*math.factorial(n-2*m))
            g += s*(2**(n-2*m))*x**(n-2*m)
        
        return g
    def H2(self,x):
        n,g = 2,0

        for m in range(0,n//2+1):
            s = ((-1)**m)*math.factorial(n)/(math.factorial(m)*math.factorial(n-2*m))
            g += s*(2**(n-2*m))*x**(n-2*m)
        
        return g
    def H3(self,x):
        n,g = 3,0

        for m in range(0,n//2+1):
            s = ((-1)**m)*math.factorial(n)/(math.factorial(m)*math.factorial(n-2*m))
            g += s*(2**(n-2*m))*x**(n-2*m)
        
        return g
    
    def H4(self,x):
        n,g = 4,0

        for m in range(0,n//2+1):
            s = ((-1)**m)*math.factorial(n)/(math.factorial(m)*math.factorial(n-2*m))
            g += s*(2**(n-2*m))*x**(n-2*m)
        
        return g
    
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

    def e1(self,x):
        return (math.e)**(-x**2)

    def e2(self,x):
        return -(math.e)**(-x**2)

    def h1(self,x):
        return ((math.sqrt(abs(x))+math.sqrt(1-x**2))*(10/13)-0.225)

    def h2(self,x):
        return ((math.sqrt(abs(x))-math.sqrt(1-x**2))*(10/13)-0.225)
