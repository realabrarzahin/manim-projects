from manim import *


class Graph3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            x_length=6,
            y_length=6,
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            z_length=6,
            axis_config={"font_size": 30},
        )
        coordinates = axes.add_coordinates()
        labels = axes.get_axis_labels()
        graph = axes.plot(lambda x: x * x, color=BLUE, x_range=[-2, 2, 1])
        graph2 = axes.plot(lambda x: -x * x, color=BLUE, x_range=[-2, 2, 1])

        # USING PARAMETRIC FUNCTION
        graph3 = ParametricFunction(
            lambda t: np.array([t, t * 2, 0]), t_range=[-2, 2, 1], color=YELLOW
        )

        self.add(axes, labels)
        self.wait()

        self.move_camera(phi=45 * DEGREES, theta=45 * DEGREES, run_time=3)
        # self.play(Create(graph), rate_func=linear, run_time=3)
        # self.play(Create(graph2), rate_func=linear, run_time=3)
        # self.play(Create(graph3), rate_func=linear, run_time=3)
        self.add((graph))
        self.add((graph2))
        self.add((graph3))

        self.wait()
