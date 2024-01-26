from manim import *
from itertools import combinations

class AllTogether(MovingCameraScene):
    def construct(self,original_list = [62,24,37]):
         # Display the original list
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

        for i in range((original_length)):

            largest_combo = max(combo_list, key=len)
            combo_list.remove(largest_combo)

            combo_text = Text(f"Current Combo: {largest_combo}" , font_size = 18).to_edge(UP)
            self.play(Write(combo_text))
            sum = largest_combo[0]
            for i in range(len(largest_combo)-1):
                sum = self.makeAdders(sum,largest_combo[i+1])
                self.clear()


    def decimal_to_binary_list(self, decimal_list):
        return [bin(x)[2:] for x in decimal_list]
    #getting the different combinations of a list
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
            for_adder = (bit1[i], bit2[i], carry)
            sum_bits = bit1[i] + bit2[i] + carry
            result.insert(0, sum_bits % 2)  # Insert the least significant bit to the front
            carry = sum_bits // 2  # Set the carry for the next iteration
            input_list.append(for_adder)

        if carry:
            result.insert(0, carry)  # If there's a carry after all iterations, add it to the front

        num_units = max_len

        # Create AdderUnits with specified inputs
        adder_units = VGroup(*[AdderUnit(*inputs).shift((LEFT * 2.2) * i) for i, inputs in enumerate(input_list)])

        center_of_units = adder_units.get_center()

        # Set the camera to focus on the center of the units
        self.camera.frame.set_width(adder_units.width * 1.4)
        self.camera.frame.move_to(center_of_units)

        # Display the adder units
        self.play(Create(adder_units, run_time=num_units))
        self.wait(2) 

        return(result)


class AdderUnit(VGroup):
    def __init__(self, A, B, C_in, **kwargs):
        super().__init__(**kwargs)
        self.createUnit(A, B, C_in)
    def construct(self):
        # Create an instance of AdderUnit
        adder_unit = AdderUnit()

        # Add it to the scene
        self.add(adder_unit)

        # Play animations
        self.play(
            Create(adder_unit,run_time = 2),  # You can use your own animations here
            run_time=2
        )

        # Wait for a moment
        self.wait(1)

    def createUnit(self,A,B,C_in):

        total = A + B + C_in
        S = total % 2
        C_out = total // 2
        

        box = VGroup(Square(side_length=1, color = BLUE),Text("Full\nAdder", font_size = 20).move_to(Square())).shift(2*RIGHT)
        input_A = Text(f"{A}", font_size = 24).next_to(box,UP * 3)
        input_B = Text(f"{B}", font_size = 24).next_to(box,UP * 3).shift(RIGHT * 0.37)
        sum = Text(f"{S}", font_size = 24).next_to(box,2.5*DOWN)
        c = Text(f"C = {C_out}", font_size = 18).next_to(box,LEFT).shift(UP * .2)

        line_A = Line(input_A.get_bottom(), box.get_top(), color=WHITE, stroke_width=1)
        line_B = Line(input_B.get_bottom(), box.get_top() + [0.37, 0, 0], color=WHITE, stroke_width=1)
        line_sum = Line(box.get_bottom(), sum.get_top(), color=WHITE, stroke_width=1)
        line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-1.2, -0.1, 0], color=WHITE, stroke_width=1)

        self.add(box, input_A, input_B, sum, c, line_A, line_B, line_sum, line_carry)
        
        return C_out