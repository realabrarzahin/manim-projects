from manim import *


class Theme:
    def __init__(self):
        # Background and surface tones
        self.background_primary = "#191521"  # deep black-purple
        self.background_secondary = "#231E30"  # twilight shadow

        # Accent colors
        self.teal = "#53D69A"  # minty signal
        self.steel = "#626769"  # industrial gray
        self.sky = "#7EAEF2"  # clear sky blue
        self.violet = "#A277FF"  # classic Aura violet
        self.apricot = "#F1BF78"  # sun-washed gold
        self.rose = "#F27A7A"  # calm crimson
        self.pink = "#F694FF"  # soft magenta
        self.white = "#FFFFFF"  # pure white for contrast

    def to_dict(self):
        return self.__dict__


class CountDown(Animation):

    def __init__(self, number: Integer, start: float, end: float, **kwargs) -> None:
        super().__init__(number, **kwargs)

        self.start = start
        self.end = end

    def interpolate_mobject(self, alpha: float) -> None:
        value = self.start - ((self.start - self.end) * alpha)

        self.mobject.set_value(int(value))


class CountDownAnimation(Scene):
    def construct(self):

        theme = Theme()
        self.camera.background_color = theme.background_primary

        number = Integer().set_color(theme.white).scale(5).set_value(10)
        number.add_updater(lambda number: number.move_to(ORIGIN))

        self.add(number)
        self.wait()

        self.play(CountDown(number, 10, 0), run_time=10, rate_functions=linear)
        self.wait()
