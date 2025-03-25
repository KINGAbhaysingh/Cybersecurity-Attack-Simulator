# sql_injection_animation.py
from manim import *

class SQLInjectionAnimation(Scene):
    def construct(self):
        # Login gate and database
        gate = Rectangle(width=2, height=3, color=YELLOW, fill_opacity=0.3)
        gate_label = Text("Login Check").next_to(gate, UP)
        db = Circle(radius=1, color=GREEN, fill_opacity=0.5).shift(4 * RIGHT)
        db_label = Text("Database").next_to(db, DOWN)
        self.play(Create(gate), Write(gate_label), Create(db), Write(db_label))
        self.wait(1)

        # Malicious query
        query = Arrow(start=3 * LEFT, end=gate.get_center(), color=RED)
        query_label = Text("1' OR '1'='1").scale(0.5).next_to(query, LEFT)
        self.play(Create(query), Write(query_label))
        self.wait(1)

        # Query bypasses gate
        self.play(query.animate.move_to(db.get_center()), run_time=2)
        data = Text("User Data").next_to(db, UP)
        self.play(Write(data), FadeToColor(db, RED))
        self.wait(1)

        # Clean up
        self.play(FadeOut(gate), FadeOut(db), FadeOut(query), FadeOut(data),
                  FadeOut(gate_label), FadeOut(db_label), FadeOut(query_label))
        self.wait(1)