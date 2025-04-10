from manim import *
from theme import Theme


class ImgOrVidInBG(MovingCameraScene):
    def construct(self):

        bg_img = ImageMobject(
            "../sources/external media/images/BG.png"
        ).scale_to_fit_height(config.frame_height)
        self.add(bg_img)

        theme = Theme()
        self.camera.background_color = theme.background_primary

        text = Text(
            "Assalamualykum!\nMy name is Antor.",
            font_size=48,
            font="Roboto Mono",
            weight=SEMIBOLD,
        )

        underline = Line(
            start=text[23].get_corner(UL) * RIGHT + 0.7 * DOWN,
            end=text[27].get_corner(UR) * RIGHT + 0.7 * DOWN,
            color=theme.sky,
        )

        elements = VGroup(text, underline)
        elements.move_to([-2.7, 2.5, 0])

        # SVG
        svg_path = "../sources/external media/images/example.svg"
        original = SVGMobject(svg_path).scale(2).move_to([2.9, -1.8, 0])

        fill_svg = original.copy()
        for submobject in fill_svg:
            submobject.set_stroke(opacity=0)
            submobject.set_fill(color=submobject.get_fill_color(), opacity=1)

        self.play(Create(fill_svg), run_time=1)
        self.wait()

        self.play(Write(text))
        self.wait()

        self.play(
            Create(underline),
            text.animate._set_color_by_t2c({"Antor": theme.sky}),
            run_time=0.15,
            rate_fun=rate_functions.double_smooth,
        )

        self.play(
            Uncreate(underline.reverse_direction()),
            run_time=0.15,
            rate_fun=rate_functions.double_smooth,
        )
        self.wait()
