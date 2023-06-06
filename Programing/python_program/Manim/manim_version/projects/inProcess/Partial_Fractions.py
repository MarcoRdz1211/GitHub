from big_ol_pile_of_manim_imports import *
import math

#python -m manim projects\Partial_Fractions.py --- -pl
e,pi = math.e,math.pi

class imagen(Scene):
    def construct(self):
        text = TextMobject(r"Descomposicion en fracciones parciales",color=GOLD)
        equation = TextMobject(r"\frac{A}{(x-\alpha_1)(x-\alpha_2) \cdots (x-\alpha_n)}$",
                               r"$\{ a_i \neq a_j \forall i \neq j\}$",color=BLUE)

        text.move_to(2*UP) , equation[0].move_to([0,0,0])
        equation[1].next_to(equation[0],DOWN)

        self.add(text,equation)

class partial(Scene):
    def construct(self):
        escala1 = 0.5
        escala2 = 0.75
        
        text = TextMobject(r"Descomposicion en fracciones parciales",color=GOLD)
        equation = TextMobject(r"$\frac{A}{(x-\alpha_1)(x-\alpha_2) \cdots (x-\alpha_n)}$",
                               r"$\{ a_i \neq a_j \forall i \neq j\}$",color=BLUE)

        text.move_to(2*UP) , equation[0].move_to([0,0,0])
        equation[1].next_to(equation[0],DOWN)


        text1 = TextMobject(r"Del teorema de descomposicion en fraccion parciales simples:",color=GOLD)
        eq1 = TextMobject(r"$\frac{A}{(x-\alpha_1)(x-\alpha_2) \cdots (x-\alpha_n)} = \frac{b_1}{x-\alpha_1}+\frac{b_2}{x-\alpha_2}+\cdots+\frac{b_n}{x-\alpha_n}$",
                          r"$\{ a_i \neq a_j \forall i \neq j \}$")
        eq2 = TextMobject(r"$\frac{A}{(x-\alpha_1)(x-\alpha_2) \cdots (x-\alpha_n)} = \sum_{i=1}^{n} (\frac{b_1}{x-\alpha_i})$")
        text2 = TextMobject(r"Multiplicando por: ",r"$(x-\alpha_1)(x-\alpha_2) \cdots (x-\alpha_n)$",r"se obtiene que:")
        eq3 = TextMobject(r"$A=b_1 (x-\alpha_2)(x-\alpha_3) \cdots (x-\alpha_n) +$",
                          r"$+ b_2 (x-\alpha_1)(x-\alpha_3) \cdots (x-\alpha_n) +\cdots$",
                          r"$\cdots + b_n (x-\alpha_1)(x-\alpha_2) \cdots (x-\alpha_{n-1})$")
        eq3_new = TextMobject(r"$A=b_1 (x-\alpha_2)(x-\alpha_3) \cdots (x-\alpha_n) +$",
                          r"$+ \sum_{i=2}^{n} b_i (x-\alpha_1) \cdots (x-\alpha_{i-1}) (x-\alpha_{i+1}) \cdots (x-\alpha_n) +$",
                          r"$+ b_n (x-\alpha_1)(x-\alpha_2) \cdots (x-\alpha_{n-1})$")

        text1.to_edge(UP) , eq1[0].next_to(text1,DOWN)
        eq1[1].next_to(eq1[0],DOWN) , eq2.move_to(eq1[0])
        text2.next_to(eq2,DOWN) , eq3[0].next_to(text2,DOWN)
        eq3[1].next_to(eq3[0],DOWN) , eq3[2].next_to(eq3[1],DOWN)
        eq3_new[0].move_to(eq3[0]) , eq3_new[1].move_to(eq3[1])
        eq3_new[2].move_to(eq3[2])

        text2[0].set_color(GOLD) , text2[2].set_color(GOLD)

        text1.scale(escala2) , eq1.scale(escala2) , eq2.scale(escala2)
        text2.scale(escala2) , text2.scale(escala2) , eq3.scale(escala2)
        eq3_new.scale(escala2)


        text3 = TextMobject(r"Evaluandose en: ",r"$x=\alpha_1$",r" entonces:")
        eq4 = TextMobject(r"$A=b_1 (\alpha_1-\alpha_2)(\alpha_1-\alpha_3) \cdots (\alpha_1-\alpha_n) +$",
                          r"$+ \sum_{i=2}^{n} b_i (\alpha_1-\alpha_1) \cdots (\alpha_1-\alpha_{i-1}) (\alpha_1-\alpha_{i+1}) \cdots (\alpha_1-\alpha_n) +$",
                          r"$+ b_n (\alpha_1-\alpha_1)(\alpha_1-\alpha_2) \cdots (\alpha_1-\alpha_{n-1})$")
        eq4_new1 = TextMobject(r"$A=b_1 (\alpha_1-\alpha_2)(\alpha_1-\alpha_3) \cdots (\alpha_1-\alpha_n) +$",
                          r"$+ \sum_{i=2}^{n} b_i (0) \cdots (\alpha_1-\alpha_{i-1}) (\alpha_1-\alpha_{i+1}) \cdots (\alpha_1-\alpha_n) +$",
                          r"$+ b_n (0)(\alpha_1-\alpha_2) \cdots (\alpha_1-\alpha_{n-1})$")
        eq4_new2 = TextMobject(r"$A=b_1 (\alpha_1-\alpha_2)(\alpha_1-\alpha_3) \cdots (\alpha_1-\alpha_n)$")
        eq4_new3 = TextMobject(r"$b_1=\frac{A}{ (\alpha_1-\alpha_2)(\alpha_1-\alpha_3) \cdots (\alpha_1-\alpha_n)}$")
        eq4_final = eq4_new3.copy()

        text3.move_to(text2)
        eq4[0].next_to(text3,DOWN) , eq4[1].next_to(eq4[0],DOWN)
        eq4[2].next_to(eq4[1],DOWN) , eq4_new1[0].next_to(text3,DOWN)
        eq4_new1[1].next_to(eq4_new1[0],DOWN) , eq4_new1[2].next_to(eq4_new1[1],DOWN)
        eq4_new2.next_to(text3,DOWN) , eq4_new3.next_to(text3,DOWN)
        eq4_final.to_corner(DL) , eq4_final.next_to(eq4_final,UP)

        text3[0].set_color(GOLD) , text3[2].set_color(GOLD)

        text3.scale(escala2) , eq4.scale(escala2) , eq4_new1.scale(escala2)
        eq4_new2.scale(escala2) , eq4_new3.scale(escala2)
        eq4_final.scale(escala2)

        
        text4 = TextMobject(r"Evaluandose en: ",r"$x=\alpha_r$",r"$\forall r\in[2,n-1]$",r"entonces:")
        eq5 = TextMobject(r"$A=b_1 (\alpha_r-\alpha_2)(\alpha_r-\alpha_3) \cdots (\alpha_r-\alpha_r) \cdots (\alpha_r-\alpha_n) +$",
                          r"$+ \sum_{i=2}^{n} b_i (\alpha_r-\alpha_1) \cdots (\alpha_r-\alpha_{i-1}) (\alpha_r-\alpha_{i+1}) \cdots (\alpha_r-\alpha_n) +$",
                          r"$+ b_n (\alpha_r-\alpha_1)(\alpha_r-\alpha_2) \cdots (\alpha_r-\alpha_r) \cdots (\alpha_r-\alpha_{n-1})$")
        eq5_new1 = TextMobject(r"$A=b_1 (\alpha_r-\alpha_2)(\alpha_r-\alpha_3) \cdots (0) \cdots (\alpha_r-\alpha_n) +$",
                          r"$+ \sum_{i=2}^{n} b_i (\alpha_r-\alpha_1) \cdots (\alpha_r-\alpha_{i-1}) (\alpha_r-\alpha_{i+1}) \cdots (\alpha_r-\alpha_n) +$",
                          r"$+ b_n (\alpha_r-\alpha_1)(\alpha_r-\alpha_2) \cdots (0) \cdots (\alpha_r-\alpha_{n-1})$")
        eq5_new2 = TextMobject(r"$A=b_r (\alpha_r-\alpha_1) \cdots (\alpha_r-\alpha_{r-1}) (\alpha_r-\alpha_{r+1}) \cdots (\alpha_r-\alpha_n)$")
        eq5_new3 = TextMobject(r"$b_r=\frac{A}{ (\alpha_r-\alpha_1) \cdots (\alpha_r-\alpha_{r-1}) (\alpha_r-\alpha_{r+1}) \cdots (\alpha_r-\alpha_n)}$",r"$ \forall r\in[2,n-1]$")
        eq5_final = TextMobject(r"$b_r=\frac{A}{ (\alpha_r-\alpha_1) \cdots (\alpha_r-\alpha_{r-1}) (\alpha_r-\alpha_{r+1}) \cdots (\alpha_r-\alpha_n)}$",r"$ \forall r\in[2,n-1]$")
        
        text4.move_to(text2)
        eq5[0].next_to(text4,DOWN) , eq5[1].next_to(eq5[0],DOWN)
        eq5[2].next_to(eq5[1],DOWN) , eq5_new1[0].next_to(text4,DOWN)
        eq5_new1[1].next_to(eq5_new1[0],DOWN) , eq5_new1[2].next_to(eq5_new1[1],DOWN)
        eq5_new2.next_to(text4,DOWN) , eq5_new3.next_to(text4,DOWN)
        eq5_final.to_corner(DL)

        text4[0].set_color(GOLD) , text4[3].set_color(GOLD) , eq5_final[1].set_color(BLUE)

        text4.scale(escala2) , eq5.scale(escala2) , eq5_new1.scale(escala2)
        eq5_new2.scale(escala2) , eq5_new3.scale(escala2)
        eq5_final.scale(escala2)


        text5 = TextMobject(r"Evaluandose en: ",r"$x=\alpha_n$",r"entonces:")
        eq6 = TextMobject(r"$A=b_1 (\alpha_n-\alpha_2)(\alpha_n-\alpha_3) \cdots (\alpha_n-\alpha_n) +$",
                          r"$+ \sum_{i=2}^{n} b_i (\alpha_n-\alpha_1) \cdots (\alpha_n-\alpha_{i-1}) (\alpha_n-\alpha_{i+1}) \cdots (\alpha_n-\alpha_n) +$",
                          r"$+ b_n (\alpha_n-\alpha_1)(\alpha_n-\alpha_2) \cdots (\alpha_n-\alpha_{n-1})$")
        eq6_new1 = TextMobject(r"$A=b_1 (\alpha_n-\alpha_2)(\alpha_n-\alpha_3) \cdots (0) +$",
                          r"$+ \sum_{i=2}^{n} b_i (\alpha_n-\alpha_1) \cdots (\alpha_n-\alpha_{i-1}) (\alpha_n-\alpha_{i+1}) \cdots (0) +$",
                          r"$+ b_n (\alpha_n-\alpha_1)(\alpha_n-\alpha_2) \cdots (\alpha_n-\alpha_{n-1})$")
        eq6_new2 = TextMobject(r"$A=b_n (\alpha_n-\alpha_1)(\alpha_n-\alpha_2) \cdots (\alpha_n-\alpha_{n-1})$")
        eq6_new3 = TextMobject(r"$b_n=\frac{A}{ (\alpha_n-\alpha_1)(\alpha_n-\alpha_2) \cdots (\alpha_n-\alpha_{n-1})}$")


        text5.move_to(text2)
        eq6[0].next_to(text5,DOWN) , eq6[1].next_to(eq6[0],DOWN)
        eq6[2].next_to(eq6[1],DOWN) , eq6_new1[0].next_to(text5,DOWN)
        eq6_new1[1].next_to(eq6_new1[0],DOWN) , eq6_new1[2].next_to(eq6_new1[1],DOWN)
        eq6_new2.next_to(text5,DOWN) , eq6_new3.next_to(text5,DOWN)


        text5[0].set_color(GOLD) , text5[2].set_color(GOLD)

        text5.scale(escala2) , eq6.scale(escala2) , eq6_new1.scale(escala2)
        eq6_new2.scale(escala2) , eq6_new3.scale(escala2)
    
        Solution = TextMobject(r"Solucion:",color=GOLD).scale(escala2)
        con = TextMobject(r"con:",color=GOLD).scale(escala2)
        final_solution = VGroup(Solution,eq2.copy(),con,eq4_final.copy(),eq5_final.copy(),eq6_new3.copy())

        final_solution[0].move_to([0,2,0]) , final_solution[1].next_to(final_solution[0],DOWN)
        final_solution[2].next_to(final_solution[1],DOWN)
        final_solution[3].next_to(final_solution[2],DOWN)
        final_solution[4].next_to(final_solution[3],DOWN)
        final_solution[5].next_to(final_solution[4],DOWN)

        self.play(Write(text)) , self.wait(2)
        self.play(Write(equation),run_time=3) , self.wait(2)

        self.play(FadeOut(equation),FadeOut(text),run_time=2)
        self.wait(2)


        self.play(Write(text1),run_time=2) , self.wait(2)
        self.play(Write(eq1),run_time=4) , self.wait(2)
        self.play(ReplacementTransform(eq1[0],eq2),FadeOut(eq1[1]),run_time=2)
        self.wait(2) , self.play(Write(text2),run_time=2)
        self.wait(2) , self.play(Write(eq3)) , self.wait(2)
        self.play(ReplacementTransform(eq3,eq3_new),run_time=2) , self.wait(2)


        self.play(ReplacementTransform(text2,text3),run_time=3)
        self.play(ReplacementTransform(eq3_new,eq4),
                  ReplacementTransform(text3[1].copy(),eq4),run_time=3) , self.wait(2)
        self.play(ReplacementTransform(eq4,eq4_new1),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq4_new1,eq4_new2),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq4_new2,eq4_new3),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq4_new3,eq4_final),FadeOut(text3),run_time=2) , self.wait(4)


        self.play(Write(text4),Write(eq3_new),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq3_new,eq5),
                  ReplacementTransform(text4[1].copy(),eq5),run_time=3) , self.wait(2)
        self.play(ReplacementTransform(eq5,eq5_new1),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq5_new1,eq5_new2),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq5_new2,eq5_new3),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq5_new3,eq5_final),FadeOut(text4),run_time=2) , self.wait(2)


        self.play(Write(text5),Write(eq3_new),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq3_new,eq6),
                  ReplacementTransform(text5[1].copy(),eq6),run_time=3) , self.wait(2)
        self.play(ReplacementTransform(eq6,eq6_new1),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq6_new1,eq6_new2),run_time=2) , self.wait(2)
        self.play(ReplacementTransform(eq6_new2,eq6_new3),run_time=2) , self.wait(2)


        self.play(FadeOut(text1),Write(final_solution[0]),
                  ReplacementTransform(eq2,final_solution[1]),
                  FadeOut(text5),FadeIn(final_solution[2]),
                  ReplacementTransform(eq4_final,final_solution[3]),
                  ReplacementTransform(eq5_final,final_solution[4]),
                  ReplacementTransform(eq6_new3,final_solution[5]))

        self.wait(3)
