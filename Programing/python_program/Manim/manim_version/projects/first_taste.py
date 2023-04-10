from big_ol_pile_of_manim_imports import *
import math
import random

#python -m manim projects\first_taste.py --- -pl
e,pi,alpha = math.e,math.pi,random.randint(0,1)+random.uniform(0.2,0.8)
delta = 0.1

class first(Scene):
    def construct(self):
        wallpaper = TextMobject(r"$f(x)=e^{x^2}$")
        graph = FunctionGraph(self.exp)
        wallpaper.next_to(graph,UP)

        self.play(Write(graph),Write(wallpaper))

    def exp(self,x):
        return 10*(math.e)**(-x**2)

class hydrogen(Scene):
    def construct(self):
        rad = 0.1

        Title1 = TextMobject(r"Hidrogen",color=GOLD)

        path = Circle(radius=2,color=YELLOW)
        proton_circle = Circle(radius=rad,fill_color=RED,fill_opacity=1,color=RED)
        electron_circle1 = Circle(radius=rad,fill_color=BLUE,fill_opacity=1,color=BLUE)
        proton_name = TextMobject(r"+e",color=BLACK)
        electron_name1 = TextMobject(r"-e",color=BLACK)

        proton_name.scale(3*rad) , electron_name1.scale(3*rad)
        electron_circle1.move_to([2,0,0])
        proton_name.move_to(proton_circle) , electron_name1.move_to(electron_circle1)
        Title1.move_to(3*UP)

        nucleus = VGroup(proton_circle,proton_name)
        electron = VGroup(electron_circle1,electron_name1)

        self.play(Write(Title1),Write(nucleus),Write(path),Write(electron))
        self.wait(2)
        for i in range(0,3):
            self.play(MoveAlongPath(electron,path),run_time=5)

        self.wait(2)

        Title2 = TextMobject(r"Helio",color=GOLD)

        electron_circle2 = Circle(radius=rad,fill_color=BLUE,fill_opacity=1,color=BLUE)
        electron_name2 = TextMobject(r"-e",color=BLACK)

        electron_name2.scale(3*rad) , electron_circle2.move_to([-2,0,0])
        electron_name2.move_to(electron_circle2)
        Title2.move_to(Title1)

        electron.add(electron_circle2,electron_name2)

        self.play(ReplacementTransform(Title1,Title2),
                  Write(electron))
        self.wait(2)
    
class parabola(Scene):
    def construct(self):
        g,v0_x,v0_y = 9.81,3,5
        x0,y0 = -(v0_x)*(v0_y)/g,0
        xf = -x0
        dl = (abs(x0)+abs(xf))/10
        m = (v0_y)/(v0_x)

        path = FunctionGraph(self.func , x_min=x0, x_max = xf , color=YELLOW)
        ground = Line([x0-1,y0,0],[xf+1,y0,0],color=GOLD)
        dot = Dot([x0,y0,0],color=BLUE)
        height = FunctionGraph(self.line , x_min=x0, x_max = xf ,
                               y_min=y0 , color=GREEN)

        start_angle = self.get_pending(path,0)
        tanline = Arrow([(3/5)*x0,0,0],[0,0,0],color=DARK_BLUE)
        
        tanline.move_to([x0,y0,0])
        tanline.save_state()
        tanline.rotate(start_angle, about_point=tanline.get_center())

        def update_rotate_move(mob,alpha):
            tanline.restore()
            angle = self.get_pending(path,alpha)
            tanline.move_to(path.point_from_proportion(alpha))
            tanline.rotate(angle, about_point=tanline.get_center())

        curve = VGroup(path,ground)

        self.play(Write(curve),Write(dot),Write(tanline)) , self.wait(2)
        self.play(MoveAlongPath(dot,path),UpdateFromAlphaFunc(tanline,update_rotate_move))
        self.wait(2)
        self.play(ReplacementTransform(dot,dot.move_to([x0,y0,0])),
                  ReplacementTransform(tanline,tanline.move_to([x0,y0,0])))
        self.wait(4)
        self.play(MoveAlongPath(height,path)) , self.wait(4)
        

    def line(self,x):
        g,v0_x,v0_y = 9.81,3,5
        x0,y0 = -(v0_x)*(v0_y)/g,0
        xf = -x0
        t = (x-x0)/v0_x
        return (-(g/2)*t**2+(v0_y)*t)

    def func(self,x):
        g,v0_x,v0_y = 9.81,3,5
        x0,y0 = -(v0_x)*(v0_y)/g,0
        t = (x-x0)/v0_x
        return (-(g/2)*t**2+(v0_y)*t+y0)

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

class parabola2(Scene):
    def construct(self):
        g,v0_x,v0_y = 9.81,3,5
        x0,y0 = -(v0_x)*(v0_y)/g,0
        xf = -x0

        path = FunctionGraph(self.func , x_min=x0, x_max = xf , color=YELLOW)
        ground = Line([x0-1,y0,0],[xf+1,y0,0],color=GOLD)
        dot = Dot([x0,y0,0],color=BLUE)
        curve = VGroup(path,ground)

        self.play(Write(curve),Write(dot)) , self.wait(2)
        self.play(MoveAlongPath(dot,path),Write(path))
        self.wait(2)
        self.play(ReplacementTransform(dot,dot.move_to([x0,y0,0])))
        self.wait(4)
        self.introduce_graph(path, dot)

    def func(self,x):
        g,v0_x,v0_y = 9.81,3,5
        x0,y0 = -(v0_x)*(v0_y)/g,0
        t = (x-x0)/v0_x
        return (-(g/2)*t**2+(v0_y)*t+y0)

    def introduce_graph(self, graph, origin):
        h_line, v_line = [
            Line(origin, origin, color = color, stroke_width = 2)
            for color in (TIME_COLOR, DISTANCE_COLOR)
        ]
        def h_update(h_line, proportion = 1):
            end = graph.point_from_proportion(proportion)
            t_axis_point = end[0]*RIGHT + origin[1]*UP
            h_line.put_start_and_end_on(t_axis_point, end)
        def v_update(v_line, proportion = 1):
            end = graph.point_from_proportion(proportion)
            d_axis_point = origin[0]*RIGHT + end[1]*UP
            v_line.put_start_and_end_on(d_axis_point, end)

        car = Dot()
        car.rotate(np.pi/2)
        car.move_to(origin)
        car_target = origin*RIGHT + graph.point_from_proportion(1)*UP


        self.add(car)
        self.play(
            ShowCreation(
                graph,
                rate_func = None,
            ),
            MoveCar(
                car, car_target,
                rate_func = self.care_movement_rate_func
            ),
            UpdateFromFunc(h_line, h_update),
            UpdateFromFunc(v_line, v_update),
            run_time = self.time_of_journey,
        )
        self.wait()
        self.play(*list(map(FadeOut, [h_line, v_line, car])))

        #Show example vertical distance
        h_update(h_line, 0.6)
        t_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_dot.save_state()
        t_dot.move_to(self.x_axis_label_mob)
        t_dot.set_fill(opacity = 0)
        dashed_h = DashedLine(*h_line.get_start_and_end())
        dashed_h.set_color(h_line.get_color())
        brace = Brace(dashed_h, RIGHT)
        brace_text = brace.get_text("Distance traveled")
        self.play(t_dot.restore)
        self.wait()
        self.play(ShowCreation(dashed_h))
        self.play(
            GrowFromCenter(brace),
            Write(brace_text)
        )
        self.wait(2)
        self.play(*list(map(FadeOut, [t_dot, dashed_h, brace, brace_text])))

        #Name graph
        s_of_t = TexMobject("s(t)")
        s_of_t.next_to(
            graph.point_from_proportion(1), 
            DOWN+RIGHT,
            buff = SMALL_BUFF
        )
        s = s_of_t[0]
        d = TexMobject("d")
        d.move_to(s, DOWN)
        d.set_color(DISTANCE_COLOR)

        self.play(Write(s_of_t))
        self.wait()
        s.save_state()
        self.play(Transform(s, d))
        self.wait()
        self.play(s.restore)

class Hydrogen(Scene):
    def construct(self):
        hydrogen_atom = Mobject()
        title = TexMobject("Hydrogen Atom")
        point_A = (-2,2,0)
        point_B = (-2,-2,0)
        arrow = Arrow(ORIGIN+LEFT*0.9,ORIGIN+RIGHT*0.9)
        add_sign  = TexMobject("+", stroke_width=0.7)

        orbit = Circle(radius=1.3).scale(0.85)
        proton = Dot(radius=0.4, color="GREY").scale(0.85)
        elec = Dot(radius=0.2, color="RED").scale(0.85)
        p_charge = TexMobject("+", stroke_width=0.5)
        e_charge = TexMobject("-",stroke_width=0.5)


        title.move_to(title.get_center()+UP*2)
        elec.move_to(orbit.points[0])
        e_charge.move_to(elec.get_center())
        p_charge.move_to(proton.get_center())

        self.play(ShowCreation(title))
        self.play(ShowCreation(orbit))
        self.play(GrowFromCenter(proton), GrowFromCenter(p_charge))
        self.play(GrowFromCenter(elec), GrowFromCenter(e_charge))

        self.play(MoveAlongPath(elec, orbit),MaintainPositionRelativeTo(e_charge, elec), run_time=5,rate_func=None)

        hydrogen_atom.add(orbit,elec, proton, e_charge, p_charge)
        atom_copy = hydrogen_atom.copy()

        h1_text = TexMobject("H").move_to(point_A+LEFT*2)
        h2_text = TexMobject("H").move_to(point_B+LEFT*2)


        names = VGroup(h1_text, h2_text)
        self.play(ApplyMethod(atom_copy.shift, point_A),ApplyMethod(hydrogen_atom.shift, point_B),Transform(title, names))


        add_sign.move_to(atom_copy.get_center()+DOWN*2)
        self.play(ShowCreation(add_sign),ShowCreation(arrow))

        h1_atom = atom_copy.copy().move_to(arrow.get_end()+RIGHT*3.5)
        h2_atom = hydrogen_atom.copy().move_to(arrow.get_end()+RIGHT*1.5)
        self.remove(atom_copy, hydrogen_atom)

        h2_atom[1].move_to(h2_atom[0].points[2])
        h2_atom[3].move_to(h2_atom[1].get_center())
        h1_atom[1].move_to(h1_atom[0].points[14])
        h1_atom[3].move_to(h1_atom[1].get_center())

        h2_molecule = VGroup(h1_atom,h2_atom)
        two_atoms = VGroup(atom_copy,hydrogen_atom) #org.copy()

        self.play(Transform(two_atoms, h2_molecule), FadeOut(arrow.add(add_sign)))
        self.add(h2_molecule)
        self.remove(title,two_atoms)

class DrawAndGate(Scene):
    def construct(self):

        AND_GATE = VGroup()

        arc = Arc(start_angle=3*np.pi/2,angle=np.pi,radius=0.6)
        body = Mobject(Line(arc.points[-1], arc.get_top()+LEFT),
                        Line(arc.get_top()+LEFT, arc.get_top()+LEFT+DOWN*1.2),
                        Line(arc.get_top()+LEFT+DOWN*1.2, arc.points[0]),
                        )


        arc_center = len(arc.points)/2 
        out =   Line(arc.points[arc_center],arc.points[arc_center]+RIGHT)

        input_a = Line(body[1].get_center()+UP*0.3,body[1].get_center()+UP*0.3+LEFT)
        input_b = Line(body[1].get_center()+DOWN*0.3,body[1].get_center()+DOWN*0.3+LEFT)

        AND_GATE.add(arc,body)
        self.play(ShowCreation(AND_GATE))

        self.play(ShowCreation(input_a),ShowCreation(input_b),ShowCreation(out))

