from manim import *
from theme import Theme


def num_color(value: int):
    if value >= 7:
        return Theme().teal
    elif value > 3:
        return Theme().apricot
    else:
        return Theme().rose


class CountDown(Scene):
    def construct(self):

        theme = Theme()
        self.camera.background_color = theme.background_primary

        value = ValueTracker(10)
        number = Integer().set_color(theme.white).scale(5)

        def num_upd(number):
            num_val = int(value.get_value())
            number.set_value(num_val).set_color(num_color(num_val))

        number.add_updater(num_upd, call_updater=True)

        self.add(number)
        self.wait()

        self.play(
            value.animate.set_value(0), run_time=10, rate_func=rate_functions.linear
        )
        self.wait()
