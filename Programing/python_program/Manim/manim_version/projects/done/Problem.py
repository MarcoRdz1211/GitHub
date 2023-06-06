from big_ol_pile_of_manim_imports import *
import math 

#python -m manim projects\Problem.py --- -pl

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

#        self.add_sound("Background.mp3") 
        self.play(SC(circle)) , self.wait(0.5) , self.play(SC(square))
        self.play(ReplacementTransform(square,M)) , self.wait(1)
        self.play(Write(Loge_text),run_time=4) , self.wait(2)
        self.play(FadeOut(M)) , self.wait(0.5)
        self.play(FadeOut(circle)) , self.wait(0.5) 
        self.play(FadeOut(Loge_text))
        self.wait(2)

#class initial(Scene):
#    def construct(self):
        escala = 0.5

        axes = Axes(x_min=-5 , x_max=5 , y_min=-3 , y_max=3)
        circle = Circle(radius = math.sqrt(math.log(math.sqrt(2*e),e)),
                        fill_color=BLUE_D,fill_opacity=0.5,color="DARKGREY")
        exp1 = FunctionGraph(self.e1 , x_min=-5 , x_max=5)
        exp2 = FunctionGraph(self.e2 , x_min=-5 , x_max=5)

        text_e1 = TextMobject(r"$e^{-x^2}$")
        text_e2 = TextMobject(r"$-e^{-x^2}$")

        x0,y0 = math.sqrt(math.log(math.sqrt(2),e)),1/math.sqrt(2)
        dot1,dot2,dot3,dot4 = Dot([x0,y0,0]),Dot([-x0,y0,0]),Dot([-x0,-y0,0]),Dot([x0,-y0,0])
        dot1.set_color(BLUE),dot2.set_color(BLUE),dot3.set_color(BLUE),dot4.set_color(BLUE)
        text_dot = TextMobject(r"$P(a,e^{-a^2})$")
        tan_line = Line([0,math.log(2*e,e)/math.sqrt(2),0],
                        [math.log(2*e,e)/math.sqrt(math.log(4,e)),0,0],color="GREY")
        line = Line([0,0,0],[2,2/math.sqrt(math.log(2,e)),0],color=GREY)
        dot = Dot([x0,y0,0])

        tangent_square = [(math.sqrt(math.log(math.sqrt(2),e)),1/math.sqrt(2),0),
                          (0.5327582,0.6399078,0),(0.4655592,0.6958546,0),
                          (0.5215060,0.7630536,0)]

        tan_square = Polygon(*tangent_square,color=BLACK,fill_color=BLACK,fill_opacity=1)

        text_e1.move_to([4.5,1,0])
        text_e2.move_to([4.5,-1,0])
        text_dot.scale(escala)
        text_dot.next_to(dot)

#-------------------------Draw problem - First Scene---------------

        text1 = TextMobject(r"La pendinete de la curva f en a, dada por la deivada, es:",color=GOLD)
        eq1 = TextMobject(r"$f'(x)=-2xe^{-x^2}$",color=WHITE)
        eq1_new = TextMobject(r"$f'(a)=-2ae^{-a^2}$",color=WHITE)
        text2 = TextMobject(r"Ahora, determinando la pendiente de la recta que pasa por P:",color=GOLD)
        eq2 = TextMobject(r"$m_r=\frac{e^{-a^2}-0}{a-0}$",color=WHITE)
        eq2_new = TextMobject(r"$m_r=\frac{e^{-a^2}}{a}$",color=WHITE)

        text1.scale(escala) , eq1.scale(escala)
        eq1_new.scale(escala) , text2.scale(escala)
        eq2.scale(escala) , eq2_new.scale(escala)

        text1.to_corner(UL) , eq1.next_to(text1,DOWN)
        eq1_new.move_to(eq1) , text2.next_to(eq1,DOWN)
        eq2.next_to(text2,DOWN) , eq2_new.move_to(eq2)

#-------------------------Second Scene---------------
        text3 = TextMobject(r"De la propiedad de la recta tangente",color=GOLD)
        eq3 = TextMobject(r"$mm_T=-1$")
        eq4 = TextMobject(r"$m_rf'(a)=-1$")
        eq4_new = TextMobject(r"$\frac{e^{-a^2}}{a}(-2ae^{-a^2})=-1$")
        eq4_new2 = TextMobject(r"$e^{-2a^2}=1/2$")
        eq4_new3 = TextMobject(r"$-2a^2=ln(1/2)$")
        eq4_new4 = TextMobject(r"$-2a^2=-ln(2)$")
        eq4_new5 = TextMobject(r"$a^2=\frac{ln(2)}{2}$")

        save_equation1 = TextMobject(r"$e^{-2a^2}=1/2$",color=YELLOW)
        save_equation2 = TextMobject(r"$a^2=\frac{ln(2)}{2}$",color=YELLOW)

        text3.move_to([-4,-1.5,0]) , eq3.next_to(text3,0.5*DOWN)
        eq4.next_to(eq3,0.5*DOWN) , eq4_new.move_to(eq4)
        eq4_new2.move_to(eq4_new) , eq4_new3.move_to(eq4_new2)
        eq4_new4.move_to(eq4_new3) , eq4_new5.move_to(eq4_new4)

        save_equation1.to_corner(UR),save_equation2.next_to(save_equation1,DOWN)

        text3.scale(escala) , eq3.scale(escala)
        eq4.scale(escala) , eq4_new.scale(escala)
        eq4_new2.scale(escala) , eq4_new3.scale(escala)
        eq4_new4.scale(escala) , eq4_new5.scale(escala)
        save_equation1.scale(escala) , save_equation2.scale(escala)

#-------------------------Third Scene---------------

        text4 = TextMobject(r"De la definicion del area de un circulo de radio r:",color=GOLD)
        eq5 = TextMobject(r"$A=\pi r^2$")
        text6 = TextMobject(r"donde:",r"$r=\sqrt{a^2+(e^{-a^2})^2}$")
        eq6 = TextMobject(r"$A=\pi r^2$")
        eq6_new = TextMobject(r"$A=\pi [\sqrt{a^2+(e^{-a^2})^2}]^2$")
        eq6_new2 = TextMobject(r"$A=\pi (a^2+e^{-2a^2})$")
        eq6_new3 = TextMobject(r"$A=\pi (\frac{ln(2)}{2}+\frac{1}{2})$")
        eq6_new4 = TextMobject(r"$A=\pi (\frac{ln(2)+1}{2})$")
        eq6_new5 = TextMobject(r"$A=\pi (\frac{ln(2)+ln(e)}{2})$")
        eq6_new6 = TextMobject(r"$A=\pi (\frac{ln(2e)}{2})$")
        eq6_new7 = TextMobject(r"$A=\pi ln(\sqrt{2e})$")

        text6[0].set_color(GOLD)

        text4.move_to(text1) , eq5.next_to(text4,0.5*DOWN)
        text6.next_to(eq5,0.5*DOWN) , eq6.next_to(text6,0.5*DOWN)
        eq6_new.move_to(eq6) , eq6_new2.move_to(eq6_new)
        eq6_new3.move_to(eq6_new2) , eq6_new4.move_to(eq6_new3)
        eq6_new5.move_to(eq6_new4) , eq6_new6.move_to(eq6_new5)
        eq6_new7.move_to(eq6_new6)

        text4.scale(escala) , eq5.scale(escala) , text6.scale(escala)
        eq6.scale(escala) , eq6_new.scale(escala) , eq6_new2.scale(escala)
        eq6_new3.scale(escala) , eq6_new4.scale(escala) , eq6_new5.scale(escala)
        eq6_new6.scale(escala) , eq6_new7.scale(escala)

        eq_final = TextMobject(r"$\pi ln(\sqrt{2e})$",color=BLACK)

        eq_final.scale(escala)
        
#-------------------------Playing first---------------        
        self.play(Write(axes))
        self.add_sound("1.mp3")
        self.play(Write(exp1),Write(exp2),run_time=1.5)
        self.play(Write(text_e1) , Write(text_e2),run_time=3)
        self.wait(5) , self.add_sound("2.mp3")
        self.play(Write(circle))
        self.wait(5) , self.add_sound("3.mp3") , self.play(Write(dot1))
        self.play(FadeOut(dot1),Write(dot2))
        self.play(FadeOut(dot2),Write(dot3))
        self.play(FadeOut(dot3),Write(dot4))
        self.play(FadeOut(dot4)) , self.wait(1.5)
        self.play(Write(dot),runt_time=2)
        self.wait(3) , self.play(Write(text_dot),runt_time=0.5)
        self.wait(5) , self.add_sound("4.mp3") , self.wait(3)
        self.play(Write(tan_line))
        self.wait(7) , self.add_sound("5.mp3") , self.wait(1)
        self.play(Write(text1))
        self.wait(2) , self.play(Write(eq1))
        self.wait(2) , self.play(ReplacementTransform(eq1,eq1_new))
        self.wait(4) , self.add_sound("6.mp3")
        self.play(Write(line),Write(tan_square))
        self.wait(3) , self.play(Write(text2))
        self.wait(3) , self.play(Write(eq2))
        self.wait(2) , self.play(ReplacementTransform(eq2,eq2_new))
        self.wait(4) , self.add_sound("7.mp3")

#-------------------------Playing second---------------        
        self.play(Write(text3)) , self.wait(1) , self.play(Write(eq3))
        self.wait(2) , self.add_sound("8.mp3") , self.wait(1)
        self.play(Write(eq4),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq4,eq4_new),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq4_new,eq4_new2),Write(save_equation1),run_time=2)
        self.wait(5) , self.play(ReplacementTransform(eq4_new2,eq4_new3))
        self.add_sound("9.mp3") 
        self.wait(2) , self.play(ReplacementTransform(eq4_new3,eq4_new4))
        self.wait(2) , self.play(ReplacementTransform(eq4_new4,eq4_new5),
                                 Write(save_equation2)) , self.wait(4)

        self.play(FadeOut(text1),FadeOut(eq1_new),FadeOut(text2),
                  FadeOut(eq2_new),FadeOut(text3),FadeOut(eq3),FadeOut(eq4_new5),
                  FadeOut(line),FadeOut(tan_line),FadeOut(tan_square))
        self.wait(2)

#-------------------------Playing third---------------

        self.add_sound("10.mp3") , self.play(Write(text4),run_time=2)
        self.wait(2) , self.play(Write(eq5))
        self.wait(5) , self.add_sound("11.mp3") 
        self.play(Write(text6)) , self.wait(8)
        self.play(Write(eq6)) , self.wait(3)
        self.add_sound("12.mp3")
        self.play(ReplacementTransform(eq6,eq6_new)) , self.wait(2)
        self.play(ReplacementTransform(eq6_new,eq6_new2)) , self.wait(2)
        self.play(ReplacementTransform(eq6_new2,eq6_new3),
                  ReplacementTransform(save_equation1,eq6_new3),
                  ReplacementTransform(save_equation2,eq6_new3))
        self.wait(2) , self.play(ReplacementTransform(eq6_new3,eq6_new4))
        self.wait(2) , self.add_sound("13.mp3")
        self.play(ReplacementTransform(eq6_new3,eq6_new4))
        self.play(ReplacementTransform(eq6_new4,eq6_new5))
        self.wait(2) , self.play(ReplacementTransform(eq6_new5,eq6_new6))
        self.wait(2) , self.play(ReplacementTransform(eq6_new6,eq6_new7)) , self.wait(7)

        self.play(FadeOut(text4),FadeOut(eq5),FadeOut(text6),FadeOut(dot),
                  FadeOut(text_dot),ReplacementTransform(eq6_new7,eq_final))

        self.wait(5)

        self.play(FadeOut(axes),FadeOut(circle),FadeOut(exp1),FadeOut(exp2),
                  FadeOut(text_e1),FadeOut(text_e2),FadeOut(eq_final))

        self.wait(2)

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
