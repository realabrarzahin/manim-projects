from manim import *


class GLTest(ThreeDScene):
    def construct(self):
        cube = Cube()
        self.play(Create(cube))
        self.wait()
