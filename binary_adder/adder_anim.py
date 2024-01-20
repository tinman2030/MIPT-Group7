from manim import *
import os

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
            Create(Title, run_time = 2),
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

            GrowFromPoint(Line(Title.get_left() + [-0.5,-0.3,0], Title.get_right() + [0.5,-0.3,0], stroke_width = 3,color = ORANGE),Title.get_left() + [-0.5,-0.3,0],run_time = 8),
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
            ReplacementTransform(VGroup(*self.mobjects), box, run_time = 2),
            Write(box2, run_time = 2),

            Create(or_gate.shift(DOWN + 2.5*RIGHT),run_time = 2),

            Create(input_A,run_time = 2),
            Create(input_B,run_time = 2),
            Create(carry_in,run_time = 2),
            Create(Title,run_time = 2),

            Create(sum_label,run_time = 2),
            Create(carry_label,run_time = 2),
            
            GrowFromPoint(Line(input_A.get_right(), box.get_left() + [0,0.2,0], color=WHITE, stroke_width=1),input_A.get_right(),run_time = 2),
            GrowFromPoint(Line(input_B.get_right(), box.get_left() + [0,-0.2,0], color=WHITE, stroke_width=1),input_B.get_right(),run_time = 2),
            GrowFromPoint(Line(box.get_right() + [0,0.2,0], box2.get_left() + [0,0.2,0], color=WHITE, stroke_width=1),box.get_right() + [0,0.2,0],run_time = 2),
            GrowFromPoint(Line(box2.get_right() + [0,0.2,0], sum_label.get_left(), color=WHITE, stroke_width=1),box2.get_right() + [0,0.2,0],run_time = 2),
            GrowFromPoint(Line(carry_in.get_right(), carry_in.get_right() + [2.2,0,0], stroke_width = 1),carry_in.get_right(),run_time = 2),
            GrowFromPoint(Line(carry_in.get_right() + [2.2,0,0], carry_in.get_right() + [2.2,1.5,0], stroke_width = 1),carry_in.get_right(),run_time = 2),
            GrowFromPoint(Line(carry_in.get_right() + [2.2,1.5,0], box2.get_left() + [0,-0.25,0], stroke_width = 1),carry_in.get_right() + [2.2,1.5,0],run_time = 2),
            GrowFromPoint(Line(or_gate.get_right(), carry_label.get_left() + [0,-0,0], stroke_width = 1),or_gate.get_right(),run_time = 2),

            GrowFromPoint(Line(box.get_right() + [0,-0.2,0], box.get_right() + [0.3,-0.2,0], stroke_width = 1),box.get_right() + [0,-0.2,0],run_time = 2),
            GrowFromPoint(Line(box.get_right() + [0.3,-0.2,0], or_gate.get_left() + [-2.46,-0.2,0], stroke_width = 1),box.get_right() + [0,-0.2,0],run_time = 2),
            GrowFromPoint(Line(or_gate.get_left() + [-2.46,-0.2,0], or_gate.get_left() + [0,-0.2,0], stroke_width = 1),box.get_right() + [-2.46,-0.2,0],run_time = 2),

            GrowFromPoint(Line(box2.get_right() + [0,-0.2,0], box2.get_right() + [0.3,-0.2,0], stroke_width = 1),box.get_right() + [0,-0.2,0],run_time = 2),
            GrowFromPoint(Line(box2.get_right() + [0.3,-0.2,0], box2.get_right() + [0.3,-1.8,0], stroke_width = 1),box.get_right() + [0.3,-0.2,0],run_time = 2),
            GrowFromPoint(Line(box2.get_right() + [0.3,-1.8,0], box2.get_right() + [0.75,-1.8,0], stroke_width = 1),box.get_right() + [0.75,-1.8,0],run_time = 2),

            GrowFromPoint(Line(Title.get_left() + [-0.5,-0.3,0], Title.get_right() + [0.5,-0.3,0], stroke_width = 3,color = ORANGE),Title.get_left() + [-0.5,-0.3,0],run_time = 8),

        )
        title = Text("3-Bit Ripple Adder", font_size = 30).shift(3*UP)
        box0 = VGroup(Square(side_length=1, color = BLUE),Text("Full\nAdder", font_size = 20).move_to(Square())).shift(2*RIGHT)
        box1 = box0.copy().next_to(box0, 1.2 * LEFT, buff = 1)
        box2 = box0.copy().next_to(box1, 1.2 * LEFT, buff = 1)

        input_A0 = Text("A0", font_size = 18).next_to(box0,UP * 3)
        input_B0 = Text("B0", font_size = 18).next_to(input_A0,RIGHT * 0.35)

        input_A1 = Text("A1", font_size = 18).next_to(box1,UP * 3)
        input_B1 = Text("B1", font_size = 18).next_to(input_A1,RIGHT * 0.35)

        input_A2 = Text("A2", font_size = 18).next_to(box2,UP * 3)
        input_B2 = Text("B2", font_size = 18).next_to(input_A2,RIGHT * 0.35)

        sum0 = Text("Sum0", font_size = 18).next_to(box0,2.5*DOWN)
        sum1 = Text("Sum1", font_size = 18).next_to(box1,2.5*DOWN)
        sum2 = Text("Sum2", font_size = 18).next_to(box2,2.5*DOWN)

        c0 = Text("Carry0", font_size = 16).next_to(box0,LEFT)
        c1 = Text("Carry1", font_size = 16).next_to(box1,LEFT)

        carry_out = Text("Carry\nOut", font_size = 18).next_to(sum2,3 * LEFT)

        self.play(
            Create(title, run_time = 2),

            ReplacementTransform(VGroup(*self.mobjects), box0, run_time = 2),
            Write(box1, run_time = 2),
            Write(box2, run_time = 2),

            Create(input_A0),
            Create(input_B0),

            Create(input_A1),
            Create(input_B1),

            Create(input_A2),
            Create(input_B2),

            Create(sum0),
            Create(sum1),
            Create(sum2),

            Create(c0),
            Create(c1),
            Create(carry_out),

            GrowFromPoint(Line(input_A0.get_bottom(), box0.get_top(), color=WHITE, stroke_width=1),input_A0.get_bottom(),run_time = 2),
            GrowFromPoint(Line(input_B0.get_bottom(), box0.get_top() + [0.37,0,0], color=WHITE, stroke_width=1),input_B0.get_bottom(),run_time = 2),
            GrowFromPoint(Line(input_A1.get_bottom(), box1.get_top(), color=WHITE, stroke_width=1),input_A1.get_bottom(),run_time = 2),
            GrowFromPoint(Line(input_B1.get_bottom(), box1.get_top() + [0.37,0,0], color=WHITE, stroke_width=1),input_B1.get_bottom(),run_time = 2),
            GrowFromPoint(Line(input_A2.get_bottom(), box2.get_top(), color=WHITE, stroke_width=1),input_A2.get_bottom(),run_time = 2),
            GrowFromPoint(Line(input_B2.get_bottom(), box2.get_top() + [0.37,0,0], color=WHITE, stroke_width=1),input_B2.get_bottom(),run_time = 2),

            GrowFromPoint(Line(box0.get_bottom(), sum0.get_top(), color=WHITE, stroke_width=1),box0.get_bottom(),run_time = 2),
            GrowFromPoint(Line(box1.get_bottom(), sum1.get_top(), color=WHITE, stroke_width=1),box1.get_bottom(),run_time = 2),
            GrowFromPoint(Line(box2.get_bottom(), sum2.get_top(), color=WHITE, stroke_width=1),box2.get_bottom(),run_time = 2),

            GrowFromPoint(Line(box0.get_left() + [0,-0.1,0], box1.get_right() + [0,-0.1,0], color=WHITE, stroke_width=1),box0.get_left() + [0,-0.1,0],run_time = 2),
            GrowFromPoint(Line(box1.get_left() + [0,-0.1,0], box2.get_right() + [0,-0.1,0], color=WHITE, stroke_width=1),box1.get_left() + [0,-0.1,0],run_time = 2),

            GrowFromPoint(Line(box2.get_left() + [0,-0.1,0], carry_out.get_top() + [0,0.9,0], color=WHITE, stroke_width=1),box1.get_left() + [0,-0.1,0],run_time = 2),
            GrowFromPoint(Line(carry_out.get_top(), carry_out.get_top() + [0,0.9,0], color=WHITE, stroke_width=1),carry_out.get_top(),run_time = 2),

            GrowFromPoint(Line(title.get_left() + [-0.5,-0.3,0], title.get_right() + [0.5,-0.3,0], stroke_width = 3,color = ORANGE),title.get_left() + [-0.5,-0.3,0],run_time = 8),
        )
        self.wait(3)
