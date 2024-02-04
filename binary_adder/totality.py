from manim import *
from itertools import combinations

class AllTogether(MovingCameraScene):
    def construct(self,original_list = [24,37],target = 61):
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

        if(C_in == 1):

            if(position == 0):
                 #if it is the last one
                c = Text(f"{C_out}", font_size = 18).next_to(sum, LEFT * 3)
                line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-0.486, -0.1, 0], color=BLUE_C, stroke_width=3)
                line_carry2 = Line(box.get_left() + [-0.486, -0.1, 0], c.get_top() + [0,0.1,0], color = BLUE_C, stroke_width = 3)

                C_dot = Dot(color=BLUE_C,radius = 0.04).move_to(c.get_top() + [0,0.1,0])
            
                self.add(box,A_dot,B_dot,S_dot,input_A, input_B, sum, c, line_A, line_B, line_sum, line_carry,line_carry2, C_dot)
            else:
                #if it's not the last one
                line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-1.2, -0.1, 0], color=BLUE_C, stroke_width=3)
                c = Text(f"C = {C_out}", font_size = 18).next_to(box,LEFT).shift(UP * .2)

                self.add(box,A_dot,B_dot,S_dot, input_A, input_B, sum, c, line_A, line_B, line_sum, line_carry)
        else:
            if(position == 0):
                 #if it is the last one
                c = Text(f"{C_out}", font_size = 18).next_to(sum, LEFT * 3.5)
                line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-0.486, -0.1, 0], color=WHITE, stroke_width=1)
                line_carry2 = Line(box.get_left() + [-0.486, -0.1, 0], c.get_top() + [0,0.1,0], color = WHITE, stroke_width = 1)

                C_dot = Dot(color=WHITE,radius = 0.03).move_to(c.get_top() + [0,0.1,0])
            
                self.add(box,A_dot,B_dot,S_dot, input_A, input_B, sum, c, line_A, line_B, line_sum, line_carry,line_carry2,C_dot)
            else:
                #if it's not the last one
                line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-1.2, -0.1, 0], color=WHITE, stroke_width=1)
                c = Text(f"{C_out}", font_size = 18).next_to(box,LEFT).shift(UP * .2)

                self.add(box,A_dot,B_dot,S_dot, input_A, input_B, sum, c, line_A, line_B, line_sum, line_carry)

