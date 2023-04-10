from big_ol_pile_of_manim_imports import *

SPACE_UNIT_TO_PLANE_UNIT = 0.75

class SlopeOfCircleExample(ZoomedScene):
    CONFIG = {
        "plane_kwargs" : {
            "x_radius" : FRAME_X_RADIUS/SPACE_UNIT_TO_PLANE_UNIT,
            "y_radius" : FRAME_Y_RADIUS/SPACE_UNIT_TO_PLANE_UNIT,
            "space_unit_to_x_unit" : SPACE_UNIT_TO_PLANE_UNIT,
            "space_unit_to_y_unit" : SPACE_UNIT_TO_PLANE_UNIT,
        },
        "example_point" : (3, 4),
        "circle_radius" : 5,
        "circle_color" : YELLOW,
        "example_color" : MAROON_B,
        "zoom_factor" : 20,
        "zoomed_canvas_corner" : UP+LEFT,
        "zoomed_canvas_corner_buff" : MED_SMALL_BUFF,
    }
    def construct(self):
        self.setup_plane()
        self.introduce_circle()
        self.talk_through_pythagorean_theorem()
        self.draw_example_slope()
        self.show_perpendicular_radius()
        self.show_dx_and_dy()
        self.write_slope_as_dy_dx()
        self.point_out_this_is_not_a_graph()
        self.perform_implicit_derivative()
        self.show_final_slope()

    def setup_plane(self):
        self.plane = NumberPlane(**self.plane_kwargs)
        self.plane.main_lines.fade()
        self.plane.add(self.plane.get_axis_labels())
        self.plane.add_coordinates()

        self.add(self.plane)

    def introduce_circle(self):
        circle = Circle(
            radius = self.circle_radius*SPACE_UNIT_TO_PLANE_UNIT,
            color = self.circle_color,
        )
        equation = TexMobject("x^2 + y^2 = 5^2")
        equation.add_background_rectangle()
        equation.next_to(
            circle.point_from_proportion(1./8), 
            UP+RIGHT
        )
        equation.to_edge(RIGHT)

        self.play(ShowCreation(circle, run_time = 2))
        self.play(Write(equation))
        self.wait()

        self.circle = circle
        self.circle_equation = equation

    def talk_through_pythagorean_theorem(self):
        point = self.plane.num_pair_to_point(self.example_point)
        x_axis_point = point[0]*RIGHT
        dot = Dot(point, color = self.example_color)

        x_line = Line(ORIGIN, x_axis_point, color = GREEN)
        y_line = Line(x_axis_point, point, color = RED)
        radial_line = Line(ORIGIN, point, color = self.example_color)
        lines = VGroup(radial_line, x_line, y_line)
        labels = VGroup()

        self.play(ShowCreation(dot))
        for line, tex in zip(lines, "5xy"):
            label = TexMobject(tex)
            label.set_color(line.get_color())
            label.add_background_rectangle()
            label.next_to(
                line.get_center(), 
                rotate_vector(UP, line.get_angle()),
                buff = SMALL_BUFF
            )
            self.play(
                ShowCreation(line),
                Write(label)
            )
            labels.add(label)

        full_group = VGroup(dot, lines, labels)
        start_angle = angle_of_vector(point)
        end_angle = np.pi/12
        spatial_radius = get_norm(point)
        def update_full_group(group, alpha):
            dot, lines, labels = group
            angle = interpolate(start_angle, end_angle, alpha)
            new_point = spatial_radius*rotate_vector(RIGHT, angle)
            new_x_axis_point = new_point[0]*RIGHT
            dot.move_to(new_point)

            radial_line, x_line, y_line = lines
            x_line.put_start_and_end_on(ORIGIN, new_x_axis_point)
            y_line.put_start_and_end_on(new_x_axis_point, new_point)
            radial_line.put_start_and_end_on(ORIGIN, new_point)
            for line, label in zip(lines, labels):
                label.next_to(
                    line.get_center(), 
                    rotate_vector(UP, line.get_angle()),
                    buff = SMALL_BUFF
                )
            return group

        self.play(UpdateFromAlphaFunc(
            full_group, update_full_group,
            rate_func = there_and_back,
            run_time = 5,
        ))
        self.wait(2)

        #Move labels to equation
        movers = labels.copy()
        pairs = list(zip(
            [movers[1], movers[2], movers[0]],
            self.circle_equation[1][0:-1:3]
        ))
        self.play(*[
            ApplyMethod(m1.replace, m2)
            for m1, m2 in pairs
        ])
        self.wait()

        self.play(*list(map(FadeOut, [lines, labels, movers])))
        self.remove(full_group)
        self.add(dot)
        self.wait()

        self.example_point_dot = dot
