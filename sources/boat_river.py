from manim import *
from theme import Theme


class BoatAndRiver(Scene):
    # Adding vector field arrows to represent waves of water.

    def field_arrows_func(self, pos):
        x, y = pos[:2]
        return np.array([x, y, 0])

    def construct(self):

        # Adding Background Image
        bg_image = (
            ImageMobject("./external media/images/BG.png")
            .scale_to_fit_height(config.frame_height)
            .set_z_index(-10)
        )

        self.add(bg_image)

        # Boat SVG Initialization
        boat = (
            SVGMobject("./external media/images/boat.svg")
            .move_to(ORIGIN + 1.2 * DOWN)
            .scale_to_fit_width(1 / 2)
        )

        # Importing Theme Class. It helps maintaining consistency in colors and design utilities
        theme = Theme()
        self.camera.background_color = theme.background_primary

        # Creating the two sides of a river.
        line_down_left = (
            Line(end=LEFT * 5 + 1.5 * DOWN, start=ORIGIN + 1.5 * DOWN)
            .set_color(theme.sky)
            .set_opacity([1 for _ in range(7)] + [0 for _ in range(2)])
            .set_sheen_direction(LEFT)
            .set_stroke(width=5)
        )
        line_down_right = (
            Line(end=RIGHT * 5 + 1.5 * DOWN, start=ORIGIN + 1.5 * DOWN)
            .set_color(theme.sky)
            .set_opacity([1 for _ in range(7)] + [0 for _ in range(2)])
            .set_sheen_direction(RIGHT)
            .set_stroke(width=5)
        )
        line_up_left = (
            Line(end=LEFT * 5 + 1.5 * UP, start=ORIGIN + 1.5 * UP)
            .set_color(theme.sky)
            .set_opacity([1 for _ in range(7)] + [0 for _ in range(2)])
            .set_sheen_direction(LEFT)
            .set_stroke(width=5)
        )
        line_up_right = (
            Line(end=RIGHT * 5 + 1.5 * UP, start=ORIGIN + 1.5 * UP)
            .set_color(theme.sky)
            .set_opacity([1 for _ in range(7)] + [0 for _ in range(2)])
            .set_sheen_direction(RIGHT)
            .set_stroke(width=5)
        )

        # Putting curly-braces enclosing two sides of the river.
        line_to_brace = Line(start=[4.5, -1.5, 0], end=[4.5, 1.5, 0])

        river_width = Brace(
            line_to_brace,
            direction=line_to_brace.copy().rotate(3 * PI / 2).get_unit_vector(),
        )

        # Labeling the length of the difference between two sides of the river as d.
        d = river_width.get_tex("d")

        # A dash line will follow the path of the boat.
        boat_follow_line = DashedLine(
            start=ORIGIN + 1.5 * DOWN, end=boat.get_corner(DOWN)
        )

        def updater(mob):
            if (boat.get_corner(DOWN) + DOWN * 0.1)[1] >= (ORIGIN + 1.5 * DOWN)[1]:
                mob.become(
                    DashedLine(
                        start=ORIGIN + 1.5 * DOWN,
                        end=boat.get_corner(DOWN) + DOWN * 0.1,
                    )
                )

        boat_follow_line.add_updater(updater)

        # Adding vector field arrows to represent waves of water.

        field_arrows = ArrowVectorField(
            func=self.field_arrows_func,
            x_range=[-5, 5],
            y_range=[-1.5, 1.5],
            length_func=lambda _: 0.25,
        )

        # Adding mobjects to the scene.
        # self.play(
        #     Create(line_down_left),
        #     Create(line_down_right),
        #     Create(line_up_left),
        #     Create(line_up_right),
        # )
        # self.wait()

        # self.play(FadeIn(river_width))
        # self.play(Write(d), run_time=0.5)
        # self.wait()

        # self.play(DrawBorderThenFill(boat), run_time=1, rate_func=rate_functions.smooth)
        # self.wait()

        # self.add(boat_follow_line)
        # self.play(
        #     boat.animate.move_to([0, 1.8, 0]),
        #     rate_fun=rate_functions.smooth,
        # )
        # self.wait(2)

        # self.play(boat.animate.move_to(ORIGIN + 1.2 * DOWN))
        # self.remove(boat_follow_line)
        # self.wait()

        self.add(field_arrows)
