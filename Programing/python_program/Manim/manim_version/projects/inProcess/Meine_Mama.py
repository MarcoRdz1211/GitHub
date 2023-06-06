from big_ol_pile_of_manim_imports import *
import math 

#python -m manim projects\Meine_Mama.py --- -pl

e,pi = math.e,math.pi

class Imagen(Scene):
    def construct(self):
        Text = TextMobject("Fur meine lieber Mama:")
        Text1 = TextMobject("Meiene Mama ist die beste Person auf die Welt")
        Text2 = TextMobject("An jeden Tag weckt sie fruh fur uns auf")
        Text3 = TextMobject("Meine Mama helfen alles wer brauchen")
        Text4 = TextMobject("Alle wir mussen eine Mama als meine")

        Text.move_to([0,2,0])
        Text1.next_to(Text,2*DOWN)
        Text2.next_to(Text1,DOWN)
        Text3.next_to(Text2,DOWN)
        Text4.next_to(Text3,DOWN)

        Text.set_color(BLUE),Text1[0].set_color(GOLD),Text2[0].set_color(GOLD),Text3[0].set_color(GOLD),Text4[0].set_color(GOLD)
        self.add(Text,Text1,Text2,Text3,Text4)


class Video(Scene):
    def construct(self):
        Text = TextMobject("Fur meine lieber Mama:")
        Text1 = TextMobject("Meiene Mama ist die beste Person auf die Welt")
        Text2 = TextMobject("An jeden Tag weckt sie fruh fur uns auf")
        Text3 = TextMobject("Meine Mama helfen alles wer brauchen")
        Text4 = TextMobject("Alle wir mussen eine Mama als meine")

        Text.move_to([0,2,0])
        Text1.next_to(Text,2*DOWN)
        Text2.next_to(Text1,DOWN)
        Text3.next_to(Text2,DOWN)
        Text4.next_to(Text3,DOWN)

        Text.set_color(BLUE),Text1[0].set_color(GOLD),Text2[0].set_color(GOLD),Text3[0].set_color(GOLD),Text4[0].set_color(GOLD)

        self.play(ShowCreation(Text)),self.wait(1)
        self.play(FadeIn(Text1)),self.wait(1)
        self.play(FadeIn(Text2)),self.wait(1)
        self.play(FadeIn(Text3)),self.wait(1)
        self.play(FadeIn(Text4)),self.wait(1)

        self.wait(2)
