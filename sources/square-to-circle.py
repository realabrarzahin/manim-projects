from manim import *
from theme import Theme

class SquareToCircle(Scene):
    def construct(self):
        theme=Theme()

        self.camera.background_color=theme.background_primary

        square=Square()
        square.round_corners(0.01)
        square.set_stroke(width=0,opacity=0,color=theme.background_secondary)

        circle=Circle()
        circle.set_stroke(width=10,opacity=1,color=theme.background_secondary)
        circle.set_fill(theme.rose,opacity=1)

        circle_around=Circle(radius=2)
        circle_around.set_stroke(width=20,opacity=1,color=theme.background_secondary)

        text=Text("Square transforming into Circle!",t2c={'Square':theme.apricot,'Circle!':theme.apricot},t2s={'Square':ITALIC,'Circle!':ITALIC},font="Montserrat",color=theme.pink,weight=SEMIBOLD,stroke_width=0) 
        text.shift(DOWN*2)
        text.font_size=36

        text_bangla=Text("কুল না?",font="Noto Serif Bengali",color=theme.teal,weight=SEMIBOLD,stroke_width=0)
        text_bangla.shift(DOWN*3)
        text.font_size=36

        
        
        self.play(square.animate.set_stroke(width=10,opacity=1,color=theme.background_secondary))
        self.play(square.animate.set_fill(theme.pink,opacity=1))
        self.play(Rotate(square,PI/4))
        self.play(Transform(square,circle),FadeIn(circle_around))
        self.remove(square)
        self.play(circle.animate.shift(UP),circle_around.animate.shift(UP))
        self.play(FadeIn(text))
        self.play(Write(text_bangla))

        self.wait(2)

        

        