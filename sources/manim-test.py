from manim import *
from theme import Theme

class TestingManim(Scene):
    def construct(self):

        theme=Theme()

        self.camera.background_color=theme.background_primary
        
        circle=Circle()
        circle.set_stroke(width=10,color=theme.background_secondary)
        circle.set_fill(color=theme.rose,opacity=1)


        self.play(Create(circle))
