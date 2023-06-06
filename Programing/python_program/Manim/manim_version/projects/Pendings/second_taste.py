from big_ol_pile_of_manim_imports import *
import math

#python -m manim projects\second_taste.py --- -pl
e,pi = math.e,math.pi

class parabola(Scene):
    def construct(self):
        g,v0_x,v0_y = 9.81,3,5
        x0,y0 = -(v0_x)*(v0_y)/g,0
        xf = -x0

        path = FunctionGraph(self.func , x_min=x0, x_max = xf , color=YELLOW)
        ground = Line([x0-1,y0,0],[xf+1,y0,0],color=GOLD)
        dot = Dot([x0,y0,0],color=BLUE)
        curve = VGroup(path,ground)

        self.play(Write(curve),Write(dot)) , self.wait(2)
        self.introduce_graph(path, dot)

    def func(self,x):
        g,v0_x,v0_y = 9.81,3,5
        x0,y0 = -(v0_x)*(v0_y)/g,0
        t = (x-x0)/v0_x
        return (-(g/2)*t**2+(v0_y)*t+y0)

    def introduce_graph(self, graph, origin):
        g,v0_x,v0_y = 9.81,3,5
        x0,y0 = -(v0_x)*(v0_y)/g,0
        xf = -x0

        v_line = Line([x0,y0,0],[x0,y0,0],color=BLUE,stroke_width = 2)

        def v_update(v_line, proportion = 1):
            origin = [x0,y0,0]
            end = graph.point_from_proportion(proportion)
            d_axis_point = origin[0]*RIGHT + end[1]*UP
            v_line.put_start_and_end_on(d_axis_point, end)

        dot = Dot()
        dot.move_to([x0,y0,0])

        self.add(dot)
        self.play(ShowCreation(graph,rate_func=None),
                  UpdateFromFunc(v_line,v_update),
                  MoveAlongPath(dot,graph),run_time=10)

        self.wait()
