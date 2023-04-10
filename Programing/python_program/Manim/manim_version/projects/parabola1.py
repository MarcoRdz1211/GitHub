from big_ol_pile_of_manim_imports import *
import math 

#python -m manim projects\Parabola1.py --- -pl

e,pi = math.e,math.pi

def SC(a):
    return ShowCreation(a)

def FO(a):
    return FadeOut(a)

class Imagen(Scene):
    def construct(self):
        g,v0_x,v0_y = 9.8,4,6
        y0,x0 = -0.5,-(v0_x)*(v0_y)/g
        xf = -x0
        a = 1/5
        
        Ground = Line([x0-1,y0,0],[xf+1,y0,0])
        Velocityline = Arrow([x0,y0,0],[4*a*x0,-a*(v0_y)*(x0)/(v0_x)+y0,0],color=RED)
        path = FunctionGraph(self.parabola , x_min=x0 , x_max=xf)
        text1 = TextMobject(r"Tiro Parabolico",color=GOLD)
        text2 = TextMobject(r"Formulacion de Newton",color=GOLD)
        x_dot = (xf+x0)/0.1
        y_dot = (-g/2)*(((x_dot-x0)/v0_x))**2+v0_y*(x_dot-x0)/v0_x+y0
        dot = Dot([x_dot,y_dot,0],color=BLUE)

        Velocityline.move_to([x0+0.1,y0+0.15,0])
        text1.move_to([0,3,0]) , text2.move_to([0,-2,0]) 
        initial = VGroup(Ground,path)

        self.add(initial,Ground,text1,text2,dot,Velocityline)

    def parabola(self,x):
        g,v0_x,v0_y = 9.8,4,6
        y0,x0 = -0.5,-(v0_x)*(v0_y)/g
        xf = -x0
        t = (x-x0)/v0_x
        return (-g/2)*t**2+v0_y*t+y0

class Video(Scene):
#class intro(Scene):
    def parabola(self,x):
        g,v0_x,v0_y = 9.8,4,6
        y0,x0 = -0.5,-(v0_x)*(v0_y)/g
        t = (x-x0)/v0_x
        return (-g/2)*t**2+v0_y*t+y0   

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

#--------------------------------Playin begin--------------------------------

#        self.add_sound("Background.mp3") 
        self.play(SC(circle)) , self.wait(0.5) , self.play(SC(square))
        self.play(ReplacementTransform(square,M)) , self.wait(1)
        self.play(Write(Loge_text),run_time=4) , self.wait(2)
        self.play(FadeOut(M)) , self.wait(0.5)
        self.play(FadeOut(circle)) , self.wait(0.5) 
        self.play(FadeOut(Loge_text))
        self.wait(2)

#--------------------------------First Scene--------------------------------

        escala1 = 0.25
        escala2 = 0.5
        escala3 = 0.75
        space = 0.5*DOWN

        g,v0_x,v0_y = 9.8,4,6
        y0,x0 = -0.5,-(v0_x)*(v0_y)/g
        xf = -x0
        a = 1/5

        Ground = Line([x0-1,y0,0],[xf+1,y0,0])
        Velocityline = Arrow([x0,y0,0],[4*a*x0,-a*(v0_y)*(x0)/(v0_x)+y0,0],color=RED)
        path = FunctionGraph(self.parabola , x_min=x0 , x_max=xf)
        text1 = TextMobject(r"Tiro Parabolico",color=GOLD)
        text2 = TextMobject(r"Formulacion de Newton",color=GOLD)
        x_dot = (xf+x0)/0.1
        y_dot = (-g/2)*(((x_dot-x0)/v0_x))**2+v0_y*(x_dot-x0)/v0_x+y0
        dot = Dot([x0,y0,0],color=BLUE)

        Velocityline.move_to([x0+0.1,y0+0.15,0])
        text1.move_to([0,3,0]) , text2.move_to([0,-2,0])
        Tiro = VGroup(Ground,path,Velocityline,dot)
        Tiro.save_state()

        self.play(Write(Tiro[0]),Write(text1)) , self.wait(1)
        self.play(Write(Velocityline),SC(dot))
        self.play(MoveAlongPath(dot,Tiro[1]),SC(Tiro[1]))
        self.play(FO(dot),FO(Velocityline)) , self.wait(1)
        self.play(Write(text2)) , self.wait(1)

        animation = ApplyMethod(Tiro.scale,escala2)

        self.play(FO(text2),animation)

        animation = ApplyMethod(Tiro.shift,[4.5,2.5,0])
        
        self.play(FO(text1),animation)
        self.wait(2)

#--------------------------------Second Scene--------------------------------

        text3 = TextMobject(r"Condiciones iniciales:",color=GOLD)
        eq1 = TextMobject(r"$\vec{r}=<x_0,y_0>$")
        eq2 = TextMobject(r"$\vec{v_0}=<v_{x_0},v_{y_0}>$")
        text4 = TextMobject(r"Ecuaciones diferenciales:",color=GOLD)
        eq3 = TextMobject(r"$\frac{d^2 x}{dt^2}=0$")
        eq4 = TextMobject(r"$\frac{d^2 y}{dt^2}=-g$")

        text3.to_corner(UL)
        eq1.next_to(text3,space) , eq2.next_to(eq1,space)
        text4.next_to(eq3,0.5*UP) , eq4.next_to(eq3,space)

        initial_conditions = VGroup(text3,eq1,eq2)

        text3.scale(escala3) , eq1.scale(escala3)
        eq2.scale(escala3) , text4.scale(escala3)
        eq3.scale(escala3) , eq4.scale(escala3)

        self.play(Write(initial_conditions)) , self.wait(3)
        self.play(Write(text4),Write(eq3),Write(eq4)) , self.wait(3)

        text5 = TextMobject(r"Solucion a la ecuacion diferencial de segundo orden:",color=GOLD)
        eq5 = TextMobject(r"$\frac{d^2 r}{dt^2}=a_r$")
        eq5_new0 = TextMobject(r"$\frac{d}{dt}(\frac{dr}{dt})=a_r$")
        eq5_new1 = TextMobject(r"$d(\frac{dr}{dt})=a_r dt$")
        eq5_new2 = TextMobject(r"$\int d(\frac{dr}{dt})=\int a_r dt$")
        eq5_new3 = TextMobject(r"$\frac{dr}{dt}=a_r t+k_1$")

        text6 = TextMobject(r"De la definicion de velocidad:",color=GOLD)
        eq6 = TextMobject(r"$v_r=\frac{dr}{dt}$")
        eq5_new4 = TextMobject(r"$v(t)=a_r t+k_1$")
        eq5_new5 = TextMobject(r"$v(0)=a_r \cdot 0+k_1$")
        eq5_new6 = TextMobject(r"$v_{r_0}=k_1$")
        eq5_new7 = TextMobject(r"$v(t)=a_r t+v_{r_0}$")
        eq5_new8 = TextMobject(r"$\frac{dr}{dt}=a_r t+v_{r_0}$")
        eq5_new9 = TextMobject(r"$dr=[a_r t+v_{r_0}]dt$")
        eq5_new10 = TextMobject(r"$\int dr=\int [a_r t+v_{r_0}]dt$")
        eq5_new11 = TextMobject(r"$r(t)=\frac{a_r}{2}t^2+v_{r_0}t+k_2$")
        
        eq5_new12 = TextMobject(r"$r(0)=\frac{a_r}{2} \cdot 0 ^2+v_{r_0} \cdot 0+k_2$")
        eq5_new13 = TextMobject(r"$r_0=k_2$")
        eq5_new14 = TextMobject(r"$r(t)=\frac{a_r}{2}t^2+v_{r_0}t+r_0$")

        text5.scale(escala3) , eq5.scale(escala3) , eq5_new0.scale(escala3)
        eq5_new1.scale(escala3) , eq5_new2.scale(escala3) , eq5_new3.scale(escala3)
        eq5_new4.scale(escala3) , eq5_new5.scale(escala3) , eq5_new6.scale(escala3)
        eq5_new7.scale(escala3) , eq5_new8.scale(escala3) , eq5_new9.scale(escala3)
        eq5_new10.scale(escala3) , eq5_new11.scale(escala3) , eq5_new12.scale(escala3)
        eq5_new13.scale(escala3) , eq5_new14.scale(escala3) , text6.scale(escala3)

        text5.move_to(text4) , eq5.next_to(text5,space)
        eq5_new0.next_to(eq5,space) , eq5_new1.move_to(eq5_new0)
        eq5_new2.move_to(eq5_new1) , eq5_new3.move_to(eq5_new2)
        text6.to_corner(DL) , text6.next_to(text6,2*UP) , eq6.next_to(text6,space)

        eq5_new4.move_to(eq5_new3) , eq5_new5.next_to(eq5_new4,space)
        eq5_new6.move_to(eq5_new5) , eq5_new7.move_to(eq5_new4)
        eq5_new8.move_to(eq5_new7) , eq5_new9.move_to(eq5_new8)
        eq5_new10.move_to(eq5_new9) , eq5_new11.move_to(eq5_new10)
        eq5_new12.next_to(eq5_new11,space) , eq5_new13.move_to(eq5_new12)
        eq5_new14.move_to(eq5_new11) , self.wait(3)

        self.play(ReplacementTransform(text4,text5),FO(eq3),FO(eq4))
        self.play(Write(eq5)) , self.wait(3)
        self.play(ReplacementTransform(eq5.copy(),eq5_new0)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new0,eq5_new1)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new1,eq5_new2)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new2,eq5_new3)) , self.wait(3)

        self.play(Write(text6)) , self.wait(1) , self.play(Write(eq6))
        self.wait(3)
        self.play(ReplacementTransform(eq6.copy(),eq5_new4),FO(eq5_new3))
        self.wait(3)

        self.play(ReplacementTransform(eq5_new4.copy(),eq5_new5)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new5,eq5_new6)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new6,eq5_new7),FO(eq5_new4)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new7,eq5_new8)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new8,eq5_new9)
                  ,FO(text6),FO(eq6)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new9,eq5_new10)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new10,eq5_new11)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new11.copy(),eq5_new12)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new12,eq5_new13)) , self.wait(3)
        self.play(ReplacementTransform(eq5_new13,eq5_new14),
                  ReplacementTransform(eq5_new11,eq5_new14)) , self.wait(5)

#--------------------------------Third Scene--------------------------------

        text7 = TextMobject(r"Para nuestro problema:",color=GOLD)
        eq7 = TextMobject(r"$\frac{d^2 x}{dt^2}=0$",r"$x(t)=\frac{a_x}{2}t^2+v_{x_0}t+x_0$")
        eq8 = TextMobject(r"$\frac{d^2 y}{dt^2}=-g$",r"$y(t)=\frac{a_y}{2}t^2+v_{y_0}t+y_0$")
        eq7_new = TextMobject(r"$x(t)=v_{x_0}t+x_0$")
        eq8_new = TextMobject(r"$y(t)=-\frac{1}{2}gt^2+v_{y_0}t+y_0$")
        text8  = TextMobject(r"Ecuaciones de movimiento:",color=GOLD)

        text7.scale(escala3) , eq7.scale(escala3) , eq8.scale(escala3)
        eq7_new.scale(escala3) , eq8_new.scale(escala3) , text8.scale(escala3)

        text7.move_to(text5)
        eq7[0].next_to(text7,LEFT) , eq7[1].next_to(text7,RIGHT)
        eq7[0].next_to(eq7[0],DOWN) , eq7[1].next_to(eq7[1],DOWN)
        eq8[0].next_to(eq7[0],space) , eq8[1].next_to(eq7[1],space)
        eq7_new.move_to(eq7[1]) , eq8_new.move_to(eq8[1])
        text8.next_to(eq8_new,0.5*UP)

        self.play(FO(text5),FO(eq5),FO(eq5_new14)) , self.wait(3)
        self.play(Write(text7)) , self.wait(1) , self.play(Write(eq7),Write(eq8))
        self.wait(3) , self.play(ReplacementTransform(eq7[1],eq7_new),
                                 ReplacementTransform(eq8[1],eq8_new))
        self.wait(5)

        solution = VGroup(text8,eq7_new.copy(),eq8_new.copy())

        solution[0].move_to([0,3.5,0]) , solution[1].next_to(solution[0],space)
        solution[2].next_to(solution[1],space)

        self.play(Write(solution[0]),FO(eq7[0]),FO(eq8[0]),FO(text7),
                  ReplacementTransform(eq7_new,solution[1]),
                  ReplacementTransform(eq8_new,solution[2]),
                  Restore(Tiro),FO(initial_conditions))
        self.wait(1) , self.play(MoveAlongPath(dot,path),SC(Velocityline))
        self.wait(1) , self.play(Write(dot.move_to([x0,y0,0])))
        self.wait(5)

        self.play(FO(solution),FO(Tiro))

        self.wait(3)

#-------------------------PlayingEnding---------------        

#class end(Scene):
#    def construct(self):        
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
#        self.add_sound("ending.mp3")
        self.play(Write(Math_text)) , self.wait(1)
        self.play(Write(Final_text1)) , self.play(Write(Final_text2))
        self.wait(5)

    def h1(self,x):
            return ((math.sqrt(abs(x))+math.sqrt(1-x**2))*(10/13)-0.225)

    def h2(self,x):
        return ((math.sqrt(abs(x))-math.sqrt(1-x**2))*(10/13)-0.225)

