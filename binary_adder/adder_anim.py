from manim import *
import os

class BinaryConversion(Scene):
    def construct(self):
        # Input numbers
        num1 = 42
        num2 = 17

        # Display the original numbers
        decimal1 = Text(f"Number 1: {num1}", font_size=24)
        decimal2 = Text(f"Number 2: {num2}", font_size=24).next_to(decimal1, DOWN)

        self.play(Write(decimal1), Write(decimal2))
        self.wait(1)

        # Convert numbers to binary
        binary_num1 = bin(num1)[2:].zfill(max(len(bin(num1)), len(bin(num2))))
        binary_num2 = bin(num2)[2:].zfill(max(len(bin(num1)), len(bin(num2))))

        # Display the binary representations
        binary_text1 = Text(f"Binary 1: {binary_num1}", font_size=24)
        binary_text2 = Text(f"Binary 2: {binary_num2}", font_size=24).next_to(binary_text1, DOWN)

        self.play(
            Transform(decimal1, binary_text1),
            Transform(decimal2, binary_text2),
            run_time=2
        )

        self.wait(1)

class HalfAdder(Scene):
    def construct(self):
        Title = Text("Half Adder", font_size = 36).shift(3*UP + .2 * RIGHT)
        # Inputs
        input_A = Text("A", font_size = 24).shift(1.2 * LEFT + 2 * UP)
        input_B = Text("B", font_size = 24).shift(0.8 * LEFT + 2 * UP)

        # XOR gate
        xor_gate = VGroup(
            Circle(radius=0.43, color = BLUE),
            Text("XOR", font_size=18).move_to(Circle())
        ).shift(LEFT)

        # AND gate
        and_gate = VGroup(
            Square(side_length = 0.666, color = BLUE),
            Text("AND", font_size=18).move_to(Square())
        ).shift(1.5*RIGHT)
        or_gate = VGroup(
            RoundedRectangle(corner_radius=0.1, width=0.5, height=0.7, color=BLUE),
            Text("OR", font_size=18).move_to(RoundedRectangle())
        )

        # Output labels
        sum_label = Text("Sum", font_size= 24).shift(LEFT + 2 * DOWN)
        carry_label = Text("Carry", font_size= 24).shift(1.5 * RIGHT + 2 * DOWN)

        line1 = Line(input_A.get_bottom() + [0,-0.4,0], input_A.get_bottom() + [2.5,-0.4,0], color = WHITE, stroke_width = 1)
        line2 = Line(input_B.get_bottom() + [0,-0.8,0], input_B.get_bottom() + [2.5,-0.8,0], color = WHITE, stroke_width = 1)
        
        # Connections
        self.play(
            Create(Title),
            Create(input_A,run_time = 2),
            Create(input_B,run_time = 2),
            Create(xor_gate,run_time = 2),
            Create(and_gate,run_time = 2),
            Create(sum_label,run_time = 2),
            Create(carry_label,run_time = 2),
            # from inputs to XOR
            GrowArrow(Arrow(input_A.get_bottom(), xor_gate.get_top() + [-0.2,0,0], color=WHITE,stroke_width = 1,tip_length = 0.1)),
            GrowArrow(Arrow(input_B.get_bottom(), xor_gate.get_top() + [0.2,0,0], color=WHITE,stroke_width = 1,tip_length = 0.1)),
            #XOR to sum
            GrowArrow(Arrow(xor_gate.get_bottom(), sum_label.get_top(), color=WHITE,stroke_width = 1,tip_length = 0.1)),
            #inputs to AND
            GrowFromPoint(line1,input_A.get_bottom() + [0,-0.4,0]),
            GrowFromPoint(line2,input_B.get_bottom() + [0,-0.8,0]),
            GrowArrow(Arrow(input_A.get_bottom() + [2.5,-0.132,0], and_gate.get_top() + [-.2,0,0], color=WHITE,stroke_width = 1,tip_length = 0.1)),
            GrowArrow(Arrow(input_B.get_bottom() + [2.5,-0.55,0], and_gate.get_top() + [0.2,0,0], color=WHITE,stroke_width = 1,tip_length = 0.1)),
            GrowArrow(Arrow(and_gate.get_bottom(), carry_label.get_top(), color=WHITE,stroke_width = 1,tip_length = 0.1)),
        )

        # transform the whole scene into a box
        box = VGroup(Rectangle(width = 1, height = 0.66, color = BLUE),Text("Half Adder", font_size = 16).move_to(Rectangle())).shift(UP + LEFT)
        box2 = box.copy().next_to(box, RIGHT, buff = 1)

        Title = Text("Full Adder", font_size = 36).shift(3*UP)
        input_A = Text("A", font_size = 24).shift(2.5 * LEFT + 1.2 * UP)
        input_B = Text("B", font_size = 24).shift(2.5 * LEFT + 0.8 * UP)
        carry_in = Text("Carry In", font_size = 24).shift(2.5*LEFT + 0.75 * DOWN)

        sum_label = Text("Sum", font_size= 24).shift(4 * RIGHT + 1.2 * UP)
        carry_label = Text("Carry", font_size= 24).shift(4 * RIGHT + 1 * DOWN)

        self.play(
            Wait(5),
            ReplacementTransform(VGroup(*self.mobjects), box, run_time = 2),
            Write(box2, run_time = 1),

            Create(or_gate.shift(DOWN + 2.5*RIGHT)),

            Create(input_A),
            Create(input_B),
            Create(carry_in),
            Create(Title),

            Create(sum_label),
            Create(carry_label),
            
            GrowFromPoint(Line(input_A.get_right(), box.get_left() + [0,0.2,0], color=WHITE, stroke_width=1),input_A.get_right()),
            GrowFromPoint(Line(input_B.get_right(), box.get_left() + [0,-0.2,0], color=WHITE, stroke_width=1),input_B.get_right()),
            GrowFromPoint(Line(box.get_right() + [0,0.2,0], box2.get_left() + [0,0.2,0], color=WHITE, stroke_width=1),box.get_right() + [0,0.2,0]),
            GrowFromPoint(Line(box2.get_right() + [0,0.2,0], sum_label.get_left(), color=WHITE, stroke_width=1),box2.get_right() + [0,0.2,0]),
        )
        