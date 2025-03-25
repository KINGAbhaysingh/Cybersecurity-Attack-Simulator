# phishing_animation.py
from manim import *

class PhishingAnimation(Scene):
    def construct(self):
        # User device
        user = Rectangle(width=2, height=1, color=BLUE, fill_opacity=0.5).shift(2 * LEFT)
        user_label = Text("User").next_to(user, DOWN)
        self.play(Create(user), Write(user_label))
        
        # Data
        data = Text("Credentials").move_to(user.get_center())
        self.play(Write(data))
        self.wait(1)
        
        # Phishing hook
        hook = Arc(radius=1, start_angle=PI/2, angle=-PI, color=RED).shift(UP + RIGHT)
        hook_tip = Dot(color=RED).move_to(hook.get_end())
        self.play(Create(hook), Create(hook_tip))
        
        # Hook steals data
        self.play(data.animate.move_to(hook_tip.get_center()), run_time=2)
        self.play(hook.animate.shift(3 * RIGHT), data.animate.shift(3 * RIGHT))
        self.wait(1)
        
        # Clean up
        self.play(FadeOut(user), FadeOut(hook), FadeOut(data), FadeOut(user_label))
        self.wait(1)