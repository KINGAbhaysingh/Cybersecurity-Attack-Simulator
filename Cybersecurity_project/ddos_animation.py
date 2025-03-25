# ddos_animation.py
from manim import *

class DDoSAnimation(Scene):
    def construct(self):
        # Server
        server = Circle(radius=1, color=BLUE, fill_opacity=0.5)
        server_label = Text("Server").next_to(server, DOWN)
        self.play(Create(server), Write(server_label))
        self.wait(1)

        # Packets flood the server
        packets = [Dot(color=RED, radius=0.1) for _ in range(30)]
        for i, packet in enumerate(packets):
            packet.move_to(3 * LEFT + i * 0.2 * UP)
            self.play(packet.animate.move_to(server), run_time=0.3)

        # Server overloads
        self.play(server.animate.scale(0.5), FadeToColor(server, RED), run_time=2)
        overload_text = Text("Overloaded!").next_to(server, UP)
        self.play(Write(overload_text))
        self.wait(1)

        # Clean up
        self.play(FadeOut(server), FadeOut(overload_text), *[FadeOut(p) for p in packets])
        self.wait(1)