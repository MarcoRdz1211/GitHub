from big_ol_pile_of_manim_imports import *

#python -m manim projects\tarea-fisicamoderna.py --- -pl

class SimpleField(Scene):
    CONFIG = {
        "plane_kwargs" : {
        "color" : RED
            },
        }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels()) #add x and y label
        self.add(plane) #Place grid on screen
     
        points = [x*RIGHT+y*UP
        for x in np.arange(-5,10,1)
        for y in np.arange(-5,5,1)
        ] #List of vectors pointing to each grid point
        p = Dot([0,1.5,0],color=YELLOW)
        vector = Vector(direction=2*RIGHT)
        vector.move_to([1,1.5,0])
        vect_text = TextMobject(r"$\overrightarrow{v}$",color=GOLD)
        vect_text.move_to([1,1.85,0])
        campo = TextMobject(r"$\overrightarrow{E}$",color=GOLD)
        campo.move_to([5.5,-1.5,0])
        
        vec_field = [] #Empty list to use in for loop
        for point in points:
            field = 0.5*RIGHT #Constant field up and to right
            result = Vector(field).shift(point) #Create vector and shift it to grid point
            vec_field.append(result) #Append to list
     
            draw_field = VGroup(*vec_field) #Pass list of vectors to create a VGroup

        draw_field.set_color(BLUE)
        self.add(p,vector,draw_field,vect_text,campo) #Draw VGroup on screen

class MoveProton(Scene):
    CONFIG = {
        "plane_kwargs" : {
        "color" : RED
            },
        }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels()) #add x and y label
        self.play(FadeIn(plane)) #Place grid on screen
     
        points = [x*RIGHT+y*UP
        for x in np.arange(-5,10,1)
        for y in np.arange(-5,5,1)
        ] #List of vectors pointing to each grid point
        p = Dot([0,1.5,0],color=BLUE)
        vector = Vector(direction=2*RIGHT)
        vector.move_to([1,1.5,0])
        vect_text = TextMobject(r"$\overrightarrow{v}$",color=GOLD)
        vect_text.move_to([1,1.85,0])
        campo = TextMobject(r"$\overrightarrow{E}$",color=GOLD)
        campo.move_to([5.5,-1.5,0])
        
        vec_field = [] #Empty list to use in for loop
        for point in points:
            field = 0.5*RIGHT #Constant field up and to right
            result = Vector(field).shift(point) #Create vector and shift it to grid point
            vec_field.append(result) #Append to list
     
            draw_field = VGroup(*vec_field) #Pass list of vectors to create a VGroup

        draw_field.set_color(BLUE)
        self.play(FadeIn(draw_field),FadeIn(campo)) #Draw VGroup on screen

        proton = VGroup(p,vector,vect_text)
        path_proton_point = Line(p.get_center(),p.get_center()+4*RIGHT)
        path_proton_vector = Line(vector.get_center(),vector.get_center()+4*RIGHT)
        path_proton_name = Line(vect_text.get_center(),vect_text.get_center()+4*RIGHT)

        self.wait(2)
        self.play(FadeIn(proton))
        self.play(MoveAlongPath(proton[0],path_proton_point),
                  MoveAlongPath(proton[1],path_proton_vector),
                  MoveAlongPath(proton[2],path_proton_name))
        self.wait(2)
