from manim import *
from itertools import combinations

class AllTogether(MovingCameraScene):
    def construct(self,original_list = [31,36,24,37,0],target = 61):

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

        line1 = Line(input_A.get_bottom() + [0,-0.38,0], input_A.get_bottom() + [2.5,-0.38,0], color = WHITE, stroke_width = 1)
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
            
            GrowFromPoint(Arrow(input_A.get_right() + [-0.2,0,0], box.get_left() + [0,0.2,0] + [0.2,0,0], color=WHITE, stroke_width=1,tip_length = 0.1),input_A.get_right(),run_time = 2),
            GrowFromPoint(Arrow(input_B.get_right() + [-0.2,0,0], box.get_left() + [0,-0.2,0]+ [0.2,0,0], color=WHITE, stroke_width=1,tip_length = 0.1),input_B.get_right(),run_time = 2),
            GrowFromPoint(Arrow(box.get_right() + [0,0.2,0] + [-0.2,0,0], box2.get_left() + [0,0.2,0]+ [0.2,0,0], color=WHITE, stroke_width=1,tip_length = 0.1),box.get_right() + [0,0.2,0],run_time = 2),
            GrowFromPoint(Arrow(box2.get_right() + [0,0.2,0] + [-0.2,0,0], sum_label.get_left()+ [0.2,0,0], color=WHITE, stroke_width=1, tip_length = 0.1),box2.get_right() + [0,0.2,0],run_time = 2),
            GrowFromPoint(Line(carry_in.get_right(), carry_in.get_right() + [2,0,0], stroke_width = 1),carry_in.get_right(),run_time = 2),
            GrowFromPoint(Line(carry_in.get_right() + [2,0,0], carry_in.get_right() + [2,1.5,0], stroke_width = 1),carry_in.get_right(),run_time = 2),
            GrowFromPoint(Arrow(carry_in.get_right() + [2,1.5,0], box2.get_left() + [-0.05,-0.25,0], stroke_width = 1,tip_length = 0.1),carry_in.get_right() + [2.2,1.5,0],run_time = 2),
            GrowFromPoint(Arrow(or_gate.get_right()+ [-0.2,0,0], carry_label.get_left() + [0.2,0,0], stroke_width = 1,tip_length = 0.1),or_gate.get_right(),run_time = 2),

            GrowFromPoint(Line(box.get_right() + [0,-0.2,0], box.get_right() + [0.3,-0.2,0], stroke_width = 1),box.get_right() + [0,-0.2,0],run_time = 2),
            GrowFromPoint(Line(box.get_right() + [0.3,-0.2,0], or_gate.get_left() + [-2.46,-0.2,0], stroke_width = 1),box.get_right() + [0,-0.2,0],run_time = 2),
            GrowFromPoint(Arrow(or_gate.get_left() + [-2.36,-0.2,0]+ [-0.35,0,0], or_gate.get_left() + [0,-0.2,0] + [0.2,0,0], stroke_width = 1,tip_length = 0.1),box.get_right() + [-2.46,-0.2,0],run_time = 2),

            GrowFromPoint(Line(box2.get_right() + [0,-0.2,0], box2.get_right() + [0.3,-0.2,0], stroke_width = 1),box.get_right() + [0,-0.2,0],run_time = 2),
            GrowFromPoint(Line(box2.get_right() + [0.3,-0.2,0], box2.get_right() + [0.3,-1.8,0], stroke_width = 1),box.get_right() + [0.3,-0.2,0],run_time = 2),
            GrowFromPoint(Arrow(box2.get_right() + [0.3,-1.8,0], box2.get_right() + [0.732,-1.8,0], stroke_width = 1,tip_length = 0.1),box.get_right() + [0.75,-1.8,0],run_time = 2),

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

        dot_A0 = Dot(color=WHITE,radius = 0.03).move_to(input_A0.get_bottom()+ [0,-0.1,0])
        dot_A1 = Dot(color=WHITE,radius = 0.03).move_to(input_A1.get_bottom()+ [0,-0.1,0])
        dot_A2 = Dot(color=WHITE,radius = 0.03).move_to(input_A2.get_bottom()+ [0,-0.1,0])


        dot_B0 = Dot(color=WHITE,radius = 0.03).move_to(input_B0.get_bottom()+ [0,-0.1,0])
        dot_B1 = Dot(color=WHITE,radius = 0.03).move_to(input_B1.get_bottom()+ [0,-0.1,0])
        dot_B2 = Dot(color=WHITE,radius = 0.03).move_to(input_B2.get_bottom()+ [0,-0.1,0])

        dot_s0 = Dot(color=WHITE,radius = 0.03).move_to(sum0.get_top() + [0,0.1,0])
        dot_s1 = Dot(color=WHITE,radius = 0.03).move_to(sum1.get_top() + [0,0.1,0])
        dot_s2 = Dot(color=WHITE,radius = 0.03).move_to(sum2.get_top() + [0,0.1,0])

        dot_cout = Dot(color=WHITE,radius = 0.03).move_to(carry_out.get_top() + [0,0.1,0])


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

            Create(dot_A0),
            Create(dot_A1),
            Create(dot_A2),

            Create(dot_B0),
            Create(dot_B1),
            Create(dot_B2),

            Create(dot_s0),
            Create(dot_s1),
            Create(dot_s2),

            Create(dot_cout),

            GrowFromPoint(Line(input_A0.get_bottom() + [0,-0.1,0], box0.get_top(), color=WHITE, stroke_width=1),input_A0.get_bottom(),run_time = 2),
            GrowFromPoint(Line(input_B0.get_bottom()+ [0,-0.1,0], box0.get_top() + [0.37,0,0], color=WHITE, stroke_width=1),input_B0.get_bottom(),run_time = 2),
            GrowFromPoint(Line(input_A1.get_bottom()+ [0,-0.1,0], box1.get_top(), color=WHITE, stroke_width=1),input_A1.get_bottom(),run_time = 2),
            GrowFromPoint(Line(input_B1.get_bottom()+ [0,-0.1,0], box1.get_top() + [0.36,0,0], color=WHITE, stroke_width=1),input_B1.get_bottom(),run_time = 2),
            GrowFromPoint(Line(input_A2.get_bottom()+ [0,-0.1,0], box2.get_top(), color=WHITE, stroke_width=1),input_A2.get_bottom(),run_time = 2),
            GrowFromPoint(Line(input_B2.get_bottom()+ [0,-0.1,0], box2.get_top() + [0.37,0,0], color=WHITE, stroke_width=1),input_B2.get_bottom(),run_time = 2),

            GrowFromPoint(Line(box0.get_bottom(), sum0.get_top() + [0,0.1,0], color=WHITE, stroke_width=1),box0.get_bottom(),run_time = 2),
            GrowFromPoint(Line(box1.get_bottom(), sum1.get_top()+ [0,0.1,0], color=WHITE, stroke_width=1),box1.get_bottom(),run_time = 2),
            GrowFromPoint(Line(box2.get_bottom(), sum2.get_top()+ [0,0.1,0], color=WHITE, stroke_width=1),box2.get_bottom(),run_time = 2),

            GrowFromPoint(Line(box0.get_left() + [0,-0.1,0], box1.get_right() + [0,-0.1,0], color=WHITE, stroke_width=1),box0.get_left() + [0,-0.1,0],run_time = 2),
            GrowFromPoint(Line(box1.get_left() + [0,-0.1,0], box2.get_right() + [0,-0.1,0], color=WHITE, stroke_width=1),box1.get_left() + [0,-0.1,0],run_time = 2),

            GrowFromPoint(Line(box2.get_left() + [0,-0.1,0], carry_out.get_top() + [0,0.9,0], color=WHITE, stroke_width=1),box1.get_left() + [0,-0.1,0],run_time = 2),
            GrowFromPoint(Line(carry_out.get_top() + [0,0.1,0], carry_out.get_top() + [0,0.9,0], color=WHITE, stroke_width=1),carry_out.get_top(),run_time = 2),

            GrowFromPoint(Line(title.get_left() + [-0.5,-0.3,0], title.get_right() + [0.5,-0.3,0], stroke_width = 3,color = ORANGE),title.get_left() + [-0.5,-0.3,0],run_time = 8),
        )
        self.wait(5)

        self.clear()

         # Display the original list
        binary_target = bin(target)[2:]
        original_text = Text("Original List: " + str(original_list), font_size=24).to_edge(UP)
        self.play(Write(original_text), run_time = 2)
        self.wait(2)

        # Convert the list to binary
        binary_list = self.decimal_to_binary_list(original_list)
        binary_text = Text("Binary List: " + str(binary_list), font_size=24).next_to(original_text, DOWN)

        combo_list = self.make_combos(binary_list)
        combo = self.make_sublists(combo_list,4)

        shit = Text("Combinations", font_size = 18, color = ORANGE).next_to(binary_text,DOWN)
        
        # Transform the original list to binary
        self.play(Write(binary_text,run_time = 2),)
        self.wait(2)

        self.play(Write(shit, run_time = 2),)

        self.wait(1)
        for i in range(len(combo)):
            sublist_text = Text(f"{combo[i]}", font_size=18).next_to(shit, DOWN*(i+1))
            self.play(Write(sublist_text), run_time=1)
            self.wait(0.5)
        self.wait(5)

        original_length = len(combo_list)

        self.clear()

        target_text = Text(f"Target = {str(binary_target)}", font_size = 20).to_edge(DOWN)
        for i in range((original_length)):

            largest_combo = max(combo_list, key=len)
            combo_list.remove(largest_combo)

            num_units = len(max(largest_combo, key=len))

            combo_text = Text(f"Current Combo: {largest_combo}" , font_size = 24)

            centre = combo_text.get_center()
            self.camera.frame.set_width(2.5 * float(num_units) * 1.4)
            self.camera.frame.move_to(centre)

            combo_text.to_edge(UP)

            self.play(Write(target_text))
            self.play(Write(combo_text))
            sum_guy = largest_combo[0]

            for j in range(len(largest_combo)-1):

                center_of_screen = ORIGIN
                
                fucker = self.makeAdders(sum_guy,largest_combo[j+1])
                adder_units = fucker[0]
                sum_guy = self.add_binary_strings(sum_guy, largest_combo[j+1])

                sum_text = Text(f"Sum = {str(sum_guy)}", font_size = 20).next_to(target_text, UP)

                center_of_adder_units = adder_units.get_center()
                displacement_vector = center_of_screen - center_of_adder_units
                adder_units.shift(displacement_vector)

                self.play(Create(adder_units, run_time=(num_units)*1.5))

                self.wait(2)

                self.play(Write(sum_text), run_time = 2)
    
                self.wait(3)

                if (sum_guy == binary_target):
                    true_target = Text(f"Target = {str(binary_target)}", font_size = 20, color = ORANGE).to_edge(DOWN)
                    true_sum =  Text(f"Sum = {str(sum_guy)}", font_size = 20, color = ORANGE).next_to(true_target, UP)

                    self.play(Transform(sum_text,true_sum),
                              Transform(target_text,true_target))
                    self.wait(3)
                    self.play(Transform(true_target,target_text),
                              Transform(true_sum, sum_text))

                self.remove(*self.mobjects)
                self.add(combo_text)
                self.add(target_text)
            self.clear()
    def decimal_to_binary_list(self, decimal_list):
        return [bin(x)[2:] for x in decimal_list]
    #getting the different combinations of a list
    def add_binary_strings(self,binary_str1, binary_str2):
        # Convert binary strings to integers
        num1 = int(binary_str1, 2)
        num2 = int(binary_str2, 2)

        # Add the numbers
        sum_result = num1 + num2

        # Convert the sum back to binary and remove the '0b' prefix
        sum_binary = bin(sum_result)[2:]

        return sum_binary

#
    def make_combos(self, my_set):

        my_set = [x for x in my_set if x != 0]

        if len(my_set) < 2:
            raise ValueError("Size of the set must be greater than 1")

        combos = []
        for i in range(2, len(my_set) +1):
            combos.extend(combinations(my_set,i))
        combos_list = [list(comb) for comb in combos]
        unique_combo_list = []

        [unique_combo_list.append(x) for x in combos_list if x not in unique_combo_list]

        return unique_combo_list
    def make_sublists(self,list,n):
        i = 0
        big_list = []
        while i*n < len(list):
            big_list.append(list[i*n:(i+1)*n])
            i += 1

        return big_list
    def makeAdders(self, bit1,bit2):
        #b1 = Text(bit1,font_size = 18)
        #b2 = Text(bit2,font_size = 18)

        result = []

        max_len = max(len(bit1), len(bit2))
        bit1 = [0] * (max_len - len(bit1)) + [int(digit) for digit in bit1]
        bit2 = [0] * (max_len - len(bit2)) + [int(digit) for digit in bit2]

        carry = 0
        input_list = []

        for i in range(max_len - 1, -1, -1):
            for_adder = (bit1[i], bit2[i], carry,i)
            sum_bits = bit1[i] + bit2[i] + carry
            result.insert(0, sum_bits % 2)  # Insert the least significant bit to the front
            carry = sum_bits // 2  # Set the carry for the next iteration
            input_list.append(for_adder)

        if carry:
            result.insert(0, carry)  # If there's a carry after all iterations, add it to the front

        # Create AdderUnits with specified inputs
        adder_units = VGroup(*[AdderUnit(*inputs).shift((LEFT * 2.2) * i) for i, inputs in enumerate(input_list)])

        return(adder_units,result)


class AdderUnit(VGroup):
    def __init__(self, A, B, C_in,position, **kwargs):
        super().__init__(**kwargs)
        self.createUnit(A, B, C_in,position)
    def construct(self):
        # Create an instance of AdderUnit
        AdderUnit.width = self[0][0].get_width()

        adder_unit = AdderUnit()

        # Add it to the scene
        self.add(adder_unit)

        # Play animations
        self.play(
            Create(adder_unit,run_time = 5)
        )

        # Wait for a moment
        self.wait(1)

    def createUnit(self,A,B,C_in,position):

        total = A + B + C_in
        S = total % 2
        C_out = total // 2
        

        box = VGroup(Square(side_length=1, color = BLUE),Text("Full\nAdder", font_size = 20).move_to(Square())).shift(2*RIGHT)
        input_A = Text(f"{A}", font_size = 24).next_to(box,UP * 3)
        input_B = Text(f"{B}", font_size = 24).next_to(box,UP * 3).shift(RIGHT * 0.37)
        sum = Text(f"{S}", font_size = 24).next_to(box,3*DOWN)

        A_dot = Dot(color=WHITE,radius = 0.03).move_to(input_A.get_bottom()+ [0,-0.1,0])
        B_dot = Dot(color=WHITE,radius = 0.03).move_to(input_B.get_bottom()+ [0,-0.1,0])
        S_dot = Dot(color=WHITE,radius = 0.03).move_to(sum.get_top()+ [0,0.1,0])

        if (S == 1):
            line_sum = Line(box.get_bottom() , sum.get_top() + [0,0.1,0], color=BLUE_C, stroke_width=3)
            S_dot = Dot(color=BLUE_C,radius = 0.04).move_to(sum.get_top()+ [0,0.1,0])
        else:
            line_sum = Line(box.get_bottom() , sum.get_top() + [0,0.1,0], color=WHITE, stroke_width=1)
            S_dot = Dot(color=WHITE,radius = 0.03).move_to(sum.get_top()+ [0,0.1,0])


        if(A == 1):
            line_A = Line(input_A.get_bottom() + [0,-0.1,0], box.get_top(), color=BLUE_C, stroke_width=3)
            A_dot = Dot(color=BLUE_C,radius = 0.04).move_to(input_A.get_bottom()+ [0,-0.1,0])
        else:
            line_A = Line(input_A.get_bottom() + [0,-0.1,0], box.get_top(), color=WHITE, stroke_width=1)
            A_dot = Dot(color=WHITE,radius = 0.03).move_to(input_A.get_bottom()+ [0,-0.1,0])

        if(B == 1):
            line_B= Line(input_B.get_bottom() + [0,-0.1,0], box.get_top() + [0.37, 0, 0], color=BLUE_C, stroke_width=3)
            B_dot = Dot(color=BLUE_C,radius = 0.04).move_to(input_B.get_bottom()+ [0,-0.1,0])
        else:
            line_B = Line(input_B.get_bottom() + [0,-0.1,0], box.get_top() + [0.37, 0, 0], color=WHITE, stroke_width=1)
            B_dot = Dot(color=WHITE,radius = 0.03).move_to(input_B.get_bottom()+ [0,-0.1,0])

        if(C_out == 1):

            if(position == 0):
                 #if it is the last one
                c = Text(f"{C_out}", font_size = 18).next_to(sum, LEFT * 3.6)
                line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-0.496, -0.1, 0], color=BLUE_C, stroke_width=3)
                line_carry2 = Line(box.get_left() + [-0.496, -0.1, 0], c.get_top() + [0,0.1,0], color = BLUE_C, stroke_width = 3)

                C_dot = Dot(color=BLUE_C,radius = 0.04).move_to(c.get_top() + [0,0.1,0])
            
                self.add(box,A_dot,B_dot,S_dot,input_A, input_B, sum, c, line_A, line_B, line_sum, line_carry,line_carry2, C_dot)
            else:
                #if it's not the last one
                line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-1.2, -0.1, 0], color=BLUE_C, stroke_width=3)
                c = Text(f"{C_out}", font_size = 18).next_to(box,LEFT).shift(UP * .2)

                self.add(box,A_dot,B_dot,S_dot, input_A, input_B, sum, c, line_A, line_B, line_sum, line_carry)
        else:
            if(position == 0):
                 #if it is the last one
                c = Text(f"{C_out}", font_size = 18).next_to(sum, LEFT * 3.6)
                line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-0.493, -0.1, 0], color=WHITE, stroke_width=1)
                line_carry2 = Line(box.get_left() + [-0.493, -0.1, 0], c.get_top() + [0,0.1,0], color = WHITE, stroke_width = 1)

                C_dot = Dot(color=WHITE,radius = 0.03).move_to(c.get_top() + [0,0.1,0])
            
                self.add(box,A_dot,B_dot,S_dot, input_A, input_B, sum, c, line_A, line_B, line_sum, line_carry,line_carry2,C_dot)
            else:
                #if it's not the last one
                line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-1.2, -0.1, 0], color=WHITE, stroke_width=1)
                c = Text(f"{C_out}", font_size = 18).next_to(box,LEFT).shift(UP * .2)

                self.add(box,A_dot,B_dot,S_dot, input_A, input_B, sum, c, line_A, line_B, line_sum, line_carry)

