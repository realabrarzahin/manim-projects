from manim import *

class TestingManim(Scene):
    def construct(self):
        
        circle=Circle()
        self.play(Create(circle))
