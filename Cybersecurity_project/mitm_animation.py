# mitm_animation.py
from manim import *

class MITMAnimation(Scene):
    def construct(self):
        # Victim and gateway
        victim = Circle(radius=0.5, color=BLUE, fill_opacity=0.5).shift(3 * LEFT)
        victim_label = Text("Victim").next_to(victim, DOWN)
        gateway = Circle(radius=0.5, color=GREEN, fill_opacity=0.5).shift(3 * RIGHT)
        gateway_label = Text("Gateway").next_to(gateway, DOWN)
        self.play(Create(victim), Write(victim_label), Create(gateway), Write(gateway_label))
        
        # Normal communication
        msg = Arrow(victim.get_center(), gateway.get_center(), color=YELLOW)
        self.play(Create(msg))
        self.wait(1)
        
        # Attacker intercepts
        attacker = Circle(radius=0.5, color=RED, fill_opacity=0.5).shift(UP)
        attacker_label = Text("Attacker").next_to(attacker, UP)
        self.play(FadeOut(msg), Create(attacker), Write(attacker_label))
        
        # Redirected traffic
        msg1 = Arrow(victim.get_center(), attacker.get_center(), color=RED)
        msg2 = Arrow(attacker.get_center(), gateway.get_center(), color=RED)
        self.play(Create(msg1), Create(msg2))
        self.wait(2)
        
        # Clean up
        self.play(FadeOut(victim), FadeOut(gateway), FadeOut(attacker), 
                  FadeOut(msg1), FadeOut(msg2), FadeOut(victim_label), 
                  FadeOut(gateway_label), FadeOut(attacker_label))
        self.wait(1)