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

        def update_rotate_move(mob,alpha):
            tanline.restore()
            angle = self.get_pending(path,alpha)
            tanline.move_to(path.point_from_proportion(alpha))
            tanline.rotate(angle, about_point=tanline.get_center())

        Ground = Line([x0-1,y0,0],[xf+1,y0,0])
        path = FunctionGraph(self.parabola , x_min=x0 , x_max=xf)
        text1 = TextMobject(r"Tiro Parabolico",color=GOLD)
        text2 = TextMobject(r"Formulacion de Newton",color=GOLD)
        x_dot = (xf+x0)/0.1
        y_dot = (-g/2)*(((x_dot-x0)/v0_x))**2+v0_y*(x_dot-x0)/v0_x+y0
        dot = Dot([x0,y0,0],color=BLUE)

        start_angle = self.get_pending(path,0)
        tanline = Arrow([(3/5)*x0,0,0],[0,0,0],color=DARK_BLUE)
        
        tanline.move_to([x0,y0,0])
        tanline.save_state()
        tanline.rotate(start_angle, about_point=tanline.get_center())

        text1.move_to([0,3,0]) , text2.move_to([0,-2,0])
        Tiro = VGroup(Ground,path)

        velocityline = tanline.copy()

        self.play(Write(Tiro[0]),Write(text1)) , self.wait(1)
        self.play(Write(dot),Write(tanline)) , self.wait(1)
        self.play(MoveAlongPath(dot,Tiro[1]),SC(Tiro[1]),
                  UpdateFromAlphaFunc(tanline,update_rotate_move),run_time=5)
        self.wait(3)
        self.play(ReplacementTransform(dot,dot.move_to([x0,y0,0])),
                  ReplacementTransform(tanline,velocityline))
        self.wait(2) , self.play(Write(text2)) , self.wait(1)

        Tiro.add(velocityline,dot)

        animation = ApplyMethod(Tiro.scale,escala2)

        self.play(FO(text2),animation)

        animation = ApplyMethod(Tiro.shift,[4.5,2.5,0])
        
        self.play(FO(text1),animation)
        self.wait(2)

    def parabola(self,x):
        g,v0_x,v0_y = 9.8,4,6
        y0,x0 = -0.5,-(v0_x)*(v0_y)/g
        t = (x-x0)/v0_x
        return (-g/2)*t**2+v0_y*t+y0      

    def get_pending(self,path,proportion,dx=0.01):
        if proportion<1:
            coord_i = path.point_from_proportion(proportion)
            coord_f = path.point_from_proportion(proportion+dx)
        else:
            coord_i = path.point_from_proportion(proportion-dx)
            coord_f = path.point_from_proportion(proportion)
        line = Line(coord_i,coord_f)
        angle = line.get_angle()
        return angle

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
