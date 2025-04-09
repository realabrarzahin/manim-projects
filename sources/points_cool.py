from manim import *
from theme import Theme


class Points(Scene):
    def construct(self):
        theme = Theme()
        self.camera.background_color = theme.background_primary

        p1 = [-1, -1, 0]
        p2 = [1, -1, 0]
        p3 = [1, 1, 0]
        p4 = [-1, 1, 0]

        path = (
            Line(p1, p2)
            .append_points(Line(p2, p3).points)
            .append_points(Line(p3, p4).points)
        )

        point_start = path.get_start()
        point_end = path.get_end()
        point_center = path.get_center()

        text_start = (
            Text(
                f"get_start() = {np.round(point_start,2).tolist()}",
                font="Roboto Mono",
                font_size=24,
            )
            .to_edge(UR)
            .set_color(theme.teal)
        )

        text_end = (
            Text(
                f"get_end() = {np.round(point_end,2).tolist()}",
                font="Roboto Mono",
                font_size=24,
            )
            .next_to(text_start, DOWN, aligned_edge=LEFT)
            .set_color(theme.rose)
        )
        text_center = (
            Text(
                f"get_center() = {np.round(point_center,2).tolist()}",
                font="Roboto Mono",
                font_size=24,
            )
            .next_to(text_end, DOWN, aligned_edge=LEFT)
            .set_color(theme.apricot)
        )

        text_group = VGroup(text_center, text_start, text_end)

        dot_start = Dot(path.get_start()).scale(2).set_color(theme.teal)
        dot_end = Dot(path.get_end()).scale(2).set_color(theme.apricot)
        dot_center = Dot(path.get_center()).scale(2).set_color(theme.pink)
        dot_center_copy = Dot(path.get_center()).scale(2).set_color(theme.pink)
        dot_top = Dot(path.get_top()).scale(2).set_color(theme.violet)
        dot_bottom = Dot(path.get_bottom()).scale(2).set_color(theme.rose)

        dots = VGroup(dot_start, dot_end, dot_center, dot_top, dot_bottom)
        v_points = [Dot(x) for x in path.points]

        dot_to_transform = (
            Dot(path.get_center())
            .scale(2)
            .set_color([theme.apricot, theme.rose, theme.teal])
        )

        self.add(path)

        self.play(FadeIn(*v_points))
        self.play(FadeIn(dots))
        self.play(ReplacementTransform(dot_center, dot_to_transform))
        self.wait(1)

        self.play(ReplacementTransform(dot_to_transform, text_group))
        self.play(FadeIn(dot_center_copy))
        self.wait(2)
