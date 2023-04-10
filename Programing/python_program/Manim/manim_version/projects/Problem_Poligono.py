from big_ol_pile_of_manim_imports import *
import math 

#python -m manim projects\Problem_Poligono.py --- -pl

e,pi = math.e,math.pi

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

        self.play(SC(circle)) , self.wait(0.5) , self.play(SC(square))
        self.play(ReplacementTransform(square,M)) , self.wait(1)
        self.play(Write(Loge_text),run_time=4) , self.wait(2)
        self.play(FadeOut(M)) , self.wait(0.5)
        self.play(FadeOut(circle)) , self.wait(0.5) 
        self.play(FadeOut(Loge_text))
        self.wait(2)

class first(Scene):
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
        Loge = VGroup(circle,M).move_to([6,-3,0]).scale(0.5)
        
        Poligono = [(-2.5,1.1,0), (-0.8,1.5,0), (0.65,1.15,0),
                    (1.8,0.6,0), (2.25,-0.5,0), (1.7,-1,0),
                    (0.25,-1.5,0), (-2.15,-1.3,0), (-3.9,-0.2,0),
                    (-2.5,1.1,0)]
        
        Poligono_new = Poligono.copy()
        Poligono_new[8] = (-3.7,-1.17,0)

        Vertexs,Vertexs_new = VGroup(),VGroup()

        for i in Poligono:
            Vertexs.add(Dot(point=i).set_color(YELLOW))

        for i in Poligono_new:
            if i!=(-2.15,-1.3,0):
                Vertexs_new.add(Dot(point=i).set_color(YELLOW))
                         
        Vertex_names,Vertex_names_new = VGroup(),VGroup()
        for i in range(0,8):
            if i<=4:            
                Vertex_names.add(TextMobject("A"+str(i+1)).next_to(Poligono[i],UP).scale(0.5))
            else:
                Vertex_names.add(TextMobject("A"+str(i+1)).next_to(Poligono[i],DOWN).scale(0.5))

        for i in range(0,7):
            if i<=4:            
                Vertex_names_new.add(TextMobject("A"+str(i+1)).next_to(Poligono_new[i],UP).scale(0.5))
            else:
                Vertex_names_new.add(TextMobject("A"+str(i+1)).next_to(Poligono_new[i],DOWN).scale(0.5))

        
        Vertex_names.add(TextMobject("A9").next_to(Poligono[8],LEFT).scale(0.5))
        Vertex_names_new.add(TextMobject("B8").next_to(Poligono_new[8],DOWN).scale(0.5))

        A1A7 = Line(start=Poligono[0],end=Poligono[7],color=GOLD)
        A1A7_new = Line(start=Poligono[-2],end=Poligono_new[8],color=GOLD)
        A8B8 = Line(start=Poligono_new[7],end=Poligono_new[8],color=GOLD)
        Dot_B8 = Dot(point=Poligono_new[8]).set_color(GREEN)
        arc = ArcBetweenPoints(start_point=LEFT+DOWN,
                               end_point=0.5*LEFT+1.5*DOWN).add_tip()

        P = VGroup(Polygon(*Poligono,color=BLUE,fill_color=DARK_BLUE,fill_opacity=1),Vertexs,Vertex_names)
        P_new = VGroup(Polygon(*Poligono_new,color=BLUE,fill_color=PINK,fill_opacity=0.5),Vertexs_new,Vertex_names_new)

        text1 = TextMobject(r"Area(Poligono 1)",color=DARK_BLUE).scale(0.75)
        text1.move_to([3,3.5,0])
        text2 = TextMobject(r"=",color=WHITE).scale(0.75)
        text2.next_to(text1,DOWN)
        text3 = TextMobject(r"Area(Poligono 2)",color=PINK).scale(0.75)
        text3.next_to(text2,DOWN)
        TextFinal = VGroup(text1,text2,text3)

        self.wait(2)
        self.play(FadeIn(Loge),run_time=1), self.wait(1)
        self.play(ShowCreation(P[0]),run_time=3), self.wait(1)
        self.play(FadeIn(P[1]),FadeIn(P[2]),run_time=3), self.wait(1)
        self.play(FadeIn(A1A7),run_time=1.5), self.wait(1)
        self.play(ReplacementTransform(A1A7.copy(),A1A7_new),run_time=1.5)
        self.play(Write(Dot_B8),FadeIn(A8B8),run_time=1.5), self.wait(1)
        self.play(Write(P_new),run_time=3), self.wait(1)

        P_final,P_final_new = P.copy().move_to([-3.5,1,0]),P_new.copy().move_to([3,-1,0])
        
        self.play(FadeOut(A1A7),FadeOut(A1A7_new),FadeOut(A8B8),
                  FadeOut(Dot_B8),ReplacementTransform(P,P_final),
                  ReplacementTransform(P_new,P_final_new),run_time=1.5)
        self.play(FadeIn(TextFinal),FadeIn(arc),run_time=1.5), self.wait(1)

#----------------------------------

        Poligono_new1 = [(-2.5,1.1,0), (-0.8,1.5,0), (0.65,1.15,0),
                        (1.8,0.6,0), (2.25,-0.5,0), (1.16,-1.65,0),
                        (-3.7,-1.17,0), (-2.5,1.1,0)]

        Vertexs_new1 = VGroup()

        for i in Poligono_new1:
            Vertexs_new1.add(Dot(point=i).set_color(YELLOW))

        text_new1 = TextMobject(r"Area(Poligono 3)",color=PINK).scale(0.75)
        text_new1.move_to(text3)

        P_new1 = VGroup(Polygon(*Poligono_new1,color=BLUE,fill_color=PINK,fill_opacity=0.5),Vertexs_new1)
        P_new1.move_to(P_final_new)
        self.play(FadeOut(P_final_new),ReplacementTransform(P_final_new,P_new1),
                  ReplacementTransform(TextFinal[2],text_new1),run_time=3)
        self.wait(1)

#----------------------------------

        Poligono_new2 = [(-2.5,1.1,0), (-0.8,1.5,0), (0.65,1.15,0),
                        (2.478,0.2756,0), (1.16,-1.65,0),
                        (-3.7,-1.17,0), (-2.5,1.1,0)]

        Vertexs_new2 = VGroup()

        for i in Poligono_new2:
            Vertexs_new2.add(Dot(point=i).set_color(YELLOW))

        text_new2 = TextMobject(r"Area(Poligono 4)",color=PINK).scale(0.75)
        text_new2.move_to(text_new1)
            
        P_new2 = VGroup(Polygon(*Poligono_new2,color=BLUE,fill_color=PINK,fill_opacity=0.5),Vertexs_new2)
        P_new2.move_to(P_final_new)
        
        self.play(ReplacementTransform(P_new1,P_new2),
                  ReplacementTransform(text_new1,text_new2),run_time=3)
        self.wait(1)
        
#----------------------------------

        Poligono_new3 = [(-2.5,1.1,0), (-0.8,1.5,0), (2.39345,1.4583,0),
                        (1.16,-1.65,0), (-3.7,-1.17,0), (-2.5,1.1,0)]

        Vertexs_new3 = VGroup()

        for i in Poligono_new3:
            Vertexs_new3.add(Dot(point=i).set_color(YELLOW))

        text_new3 = TextMobject(r"Area(Poligono 5)",color=PINK).scale(0.75)
        text_new3.move_to(text_new2)
            
        P_new3 = VGroup(Polygon(*Poligono_new3,color=BLUE,fill_color=PINK,fill_opacity=0.5),Vertexs_new3)
        P_new3.move_to(P_new2)
        
        self.play(ReplacementTransform(P_new2,P_new3),
                  ReplacementTransform(text_new2,text_new3),run_time=3)
        self.wait(1)

#----------------------------------

        Poligono_new4 = [(-1.807,1.7431,0), (2.39345,1.4583,0),
                        (1.16,-1.65,0), (-3.7,-1.17,0), (-1.807,1.7431,0)]

        Vertexs_new4 = VGroup()

        for i in Poligono_new4:
            Vertexs_new4.add(Dot(point=i).set_color(YELLOW))

        text_new4 = TextMobject(r"Area(Cuadrilatero)",color=PINK).scale(0.75)
        text_new4.move_to(text_new3)
            
        P_new4 = VGroup(Polygon(*Poligono_new4,color=BLUE,fill_color=PINK,fill_opacity=0.5),Vertexs_new4)
        P_new4.move_to(P_final_new)
        
        self.play(ReplacementTransform(P_new3,P_new4),
                  ReplacementTransform(text_new3,text_new4),run_time=3)
        self.wait(1)


#----------------------------------

        Poligono_new5 = [(3.8918,3.5281,0), (1.16,-1.65,0), (-3.7,-1.17,0), (3.8918,3.5281,0)]

        Vertexs_new5 = VGroup()

        for i in Poligono_new5:
            Vertexs_new5.add(Dot(point=i).set_color(YELLOW))

        Vertex_names_new5 = VGroup(TextMobject("C1").next_to(Poligono_new5[0],UP).scale(0.5),
                                   TextMobject("C2").next_to(Poligono_new5[1],RIGHT).scale(0.5),
                                   TextMobject("C3").next_to(Poligono_new5[2],LEFT).scale(0.5))
        
        text_new5 = TextMobject(r"Area(Triangulo)",color=PINK).scale(0.75)
        text_new5.move_to(text_new4)
            
        P_new5 = VGroup(Polygon(*Poligono_new5,color=BLUE,fill_color=PINK,fill_opacity=0.5),Vertexs_new5,Vertex_names_new5)
        P_new5.move_to([2.5,-0.8,0])
        
        self.play(ReplacementTransform(P_new4,P_new5),
                  ReplacementTransform(text_new4,text_new5),run_time=3)
        self.wait(1)

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
