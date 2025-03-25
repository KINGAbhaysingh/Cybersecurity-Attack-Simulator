# brute_force_animation.py
from manim import *

class BruteForceAnimation(Scene):
    def construct(self):
        # Lock
        lock = Circle(radius=1, color=YELLOW, fill_opacity=0.5)
        lock_label = Text("SSH Lock").next_to(lock, DOWN)
        self.play(Create(lock), Write(lock_label))
        
        # Password attempts
        for i in range(4):
            attempt = Text(f"Try {i+1}: 12345").shift(2 * LEFT + i * 0.5 * UP)
            self.play(Write(attempt), run_time=0.5)
            self.play(attempt.animate.move_to(lock), run_time=0.5)
            self.play(FadeOut(attempt))
        
        # Success
        success = Text("Success: test").shift(2 * LEFT + 2 * UP)
        self.play(Write(success), lock.animate.set_fill(GREEN))
        self.wait(1)
        
        # Clean up
        self.play(FadeOut(lock), FadeOut(success), FadeOut(lock_label))
        self.wait(1)