from big_ol_pile_of_manim_imports import *
import os
import pyclbr
import numpy as np
 
#python -m manim projects\delete.py --- -pl

alpha = 1.25
  
class IntegralTest(GraphScene):
    CONFIG = {"x_min" : -8,
              "x_max" : 8,
              "y_min" : -8,
              "y_max" : 8,
              "graph_origin" : [0,0,0],
              "function_color" : WHITE ,
              "axes_color" : GREEN,
              "x_axis_label": "",
              "y_axis_label": "",
              "y_axis_height": 16,
              "x_axis_width": 16} 
 
    def construct(self):
        self.setup_axes(animate=False)

        plane = NumberPlane(color=RED) #Create axes and grid
        plane.add(plane.get_axis_labels()) #add x and y label
        self.play(Write(plane)) #Place grid on screen
        
        func_graph=self.get_graph(lambda x: alpha, color=WHITE, x_min = 0)
        func_graph_shift=self.get_graph(lambda x: alpha/x, color=WHITE, x_min = 1.0)
        
 
        riemannRectangles = self.get_riemann_rectangles(func_graph, x_min = 1,
                                                        x_max = 10, dx = .01,
                                                        stroke_width = 0.01,
                                                        stroke_color = WHITE,
                                                        start_color = WHITE,
                                                        end_color = WHITE)
 
        self.bring_to_front(func_graph)
        self.play(ShowCreation(func_graph)) 
 
 
        self.play(ShowCreation(riemannRectangles))
        self.wait() 
        self.wait()

class Integral(GraphScene):
    def get_region(self):
        x_vals = np.arange(-7,7)
        curve1 = self.get_curve(lambda x: alpha, color=WHITE, x_min = 0)
        curve2 = self.get_curve(lambda x: 0, color=WHITE, x_min = 0)
        c1_points = [curve1.get_point_from_function(x) for x in x_vals]
        c2_points = [curve2.get_point_from_function(x) for x in x_vals]
        c2_points.reverse()
        points = c1_points+c2_points
        region = Polygon(*points,stroke_width=0,fill_color=PINK,fill_opacity=0.5)

        R = TextMobject(r"R").set_color(PINK).scale(2).rotate(180*DEGREES , OUT)
        R.move_to(region,IN+RIGHT)
        
        self.play(ShowCreation(curve1),ShowCreation(curve2))
        self.wait(2)
        self.play(ShowCreation(region))
        self.add(R)
