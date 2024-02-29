from manim import *
from itertools import combinations

class AllTogether(MovingCameraScene):
    def construct(self,original_list = [31,36,34,24,9],target = 67):

        #display the original list
        binary_target = bin(target)[2:]
        original_text = Text("Original List: " + str(original_list), font_size=24).to_edge(UP)
        self.play(Write(original_text), run_time = 2)
        self.wait(2)

        # convert the list to binary
        binary_list = self.decimal_to_binary_list(original_list)
        binary_text = Text("Binary List: " + str(binary_list), font_size=24).next_to(original_text, DOWN)

        combo_list = self.make_combos(binary_list)
        combo = self.make_sublists(combo_list,4)

        shit = Text("Combinations", font_size = 18, color = ORANGE).next_to(binary_text,DOWN)
        
        # write the original list in binary
        self.play(Write(binary_text,run_time = 1))
        self.wait(1)
        #create all the combo
        self.play(Write(shit, run_time = 1))
        self.wait(1)

        #write each combo
        for i in range(len(combo)):
            sublist_text = Text(f"{combo[i]}", font_size=18).next_to(shit, DOWN*(i+1.5))
            self.play(Write(sublist_text), run_time=1)
            self.wait(0.5)
        self.wait(3)

        original_length = len(combo_list)
        # fade to the adders
        vmobjects = [obj for obj in self.mobjects if isinstance(obj, VMobject)]
        self.play(FadeOut(VGroup(*vmobjects), run_time=2))
        #write the target
        target_text = Text(f"Target = {str(binary_target)}", font_size = 20)

        for i in range((original_length)):
            #finding the largest combination and add from largest to smallest
            largest_combo = max(combo_list, key=len)
            combo_list.remove(largest_combo)

            sum_guy = largest_combo[0]
            sum_guy_list = []
            for j in range(len(largest_combo)-1):#need to change this to get keep items on the screen
                #update the sum
                sum_guy_list.append(sum_guy)
                sum_guy = self.add_binary_strings(sum_guy, largest_combo[j+1])
            #make the number of units based on the largest number
            num_units = len(sum_guy)

            combo_text = Text(f"Current Combo: {largest_combo}" , font_size = 24)
            #make the camera fit all of the units
            centre = combo_text.get_center()
            self.camera.frame.set_width(2.5 * float(num_units) * 1.4)
            self.camera.frame.move_to(centre)
            #write the combo were summing
            combo_text.to_edge(UP)

            self.play(Write(combo_text),run_time = 1)
            self.wait(2)
            self.play(FadeOut(combo_text, run_time=1))
            #keep track of the numbers that we're adding and have added

            summed_text = Text(f"Sum: {sum_guy}", font_size=20) 

            center_of_screen = ORIGIN
            ho = 0

            for j in range(len(largest_combo)-1):#need to change this to get keep items on the screen

                ho += 1
    
                #make the adders
                indicator = 0

                if (j==len(largest_combo)-2):
                    indicator = 1
                
                fucker = self.makeAdders(sum_guy_list[j],largest_combo[j+1],num_units,indicator)
                adder_units = fucker[0]
                #update the sum

                sum_text = Text(f"Sum = {str(sum_guy_list[j])}", font_size = 20).next_to(target_text, UP)
                #putting the centre of the adders in the centre of the screen
                center_of_adder_units = adder_units.get_center()
                displacement_vector = center_of_screen - center_of_adder_units
                
                #the centre of the camera changes since the size of the adders changes so have to account for that
                if j == len(largest_combo)-2:
                    y = ((j-1) * 4) + 3.5
                    adder_units.shift(displacement_vector + ([0,-y,0]))

                else:
                    adder_units.shift(displacement_vector + ([0,-4*j,0]))


                #move the camera down for a bit
                self.play(self.camera.frame.animate.move_to(adder_units))

                self.play(Create(adder_units, run_time=(num_units)))
    
                self.wait(2)
            # end of the combos
            target_text.move_to(center_of_screen + [0,-4*ho,0])
            summed_text.next_to(target_text,UP)
            combo_text.next_to(summed_text,UP)
            
            self.play(
                    Write(combo_text, run_time =1 ),
                    Write(target_text,run_time = 1),
                    Write(summed_text,run_time = 1)
                    )
            self.wait(1)

            if (sum_guy == binary_target):
                #if the sum is correct then make it turn orange and then turn back to normal
                true_target = Text(f"Target = {str(binary_target)}", font_size = 20, color = ORANGE).move_to(center_of_screen + [0,-4*ho,0])
                true_sum =  Text(f"Sum = Target = {str(sum_guy)}", font_size = 20, color = ORANGE).next_to(true_target, UP)

                self.play(
                        ReplacementTransform(summed_text,true_sum, run_time = 1),
                        ReplacementTransform(target_text,true_target, run_time = 1))
                    
                self.wait(2)

                target_text = Text(f"Target = {str(binary_target)}", font_size = 20).move_to(center_of_screen + [0,-4*ho,0])
                sum_text = Text(f"Sum = {str(sum_guy)}", font_size = 20).next_to(target_text, UP)

                self.play(
                    ReplacementTransform(true_sum, sum_text,run_time = 1.5),
                    ReplacementTransform(true_target, target_text, run_time = 1))
            self.wait(2)
            #get rid of all the shit
            vmobjects = [obj for obj in self.mobjects if isinstance(obj, VMobject)]
            self.play(FadeOut(VGroup(*vmobjects), run_time=2)) 
            
    def decimal_to_binary_list(self, decimal_list):
        return [bin(x)[2:] for x in decimal_list]
    #getting the different combinations of a list
    def add_binary_strings(self,binary_str1, binary_str2):
        # convert binary strings to integers
        num1 = int(binary_str1, 2)
        num2 = int(binary_str2, 2)

        # add the numbers
        sum_result = num1 + num2

        # convert the sum back to binary and remove the '0b' prefix
        sum_binary = bin(sum_result)[2:]

        return sum_binary

    def make_combos(self, my_set):
        #get rid of the 0's in the set
        my_set = [x for x in my_set if x != 0]
        #error if there is only 1 or no items in the set
        if len(my_set) < 2:
            raise ValueError("Size of the set must be greater than 1")
        #make the combinations
        combos = []
        for i in range(2, len(my_set) +1):
            combos.extend(combinations(my_set,i))
        combos_list = [list(comb) for comb in combos]
        unique_combo_list = []
        #make sure the items are unique
        [unique_combo_list.append(x) for x in combos_list if x not in unique_combo_list]

        return unique_combo_list
    
    def make_sublists(self,list,n):
        i = 0
        big_list = []
        while i*n < len(list):
            big_list.append(list[i*n:(i+1)*n])
            i += 1

        return big_list
    def makeAdders(self, bit1,bit2,n,ron):

        result = []

        max_len = n
        bit1 = [0] * (max_len - len(bit1)) + [int(digit) for digit in bit1]
        bit2 = [0] * (max_len - len(bit2)) + [int(digit) for digit in bit2]

        carry = 0
        input_list = []

        for i in range(n - 1, -1, -1):
            for_adder = (bit1[i], bit2[i], carry,i,ron)
            sum_bits = bit1[i] + bit2[i] + carry
            result.insert(0, sum_bits % 2)  
            # insert the least significant bit to the front
            carry = sum_bits // 2  
            # set the carry for the next iteration
            input_list.append(for_adder)

        if carry:
            result.insert(0, carry)  
            # if there's a carry after all iterations, add it to the front

        # create AdderUnits with specified inputs
        adder_units = VGroup(*[AdderUnit(*inputs).shift((LEFT * 2.2) * i) for i, inputs in enumerate(input_list)])

        return(adder_units,result)


class AdderUnit(VGroup):
    def __init__(self, A, B, C_in,position,sandwich, **kwargs):
        super().__init__(**kwargs)
        self.createUnit(A, B, C_in,position,sandwich)
    def construct(self):
        # create an instance of AdderUnit
        AdderUnit.width = self[0][0].get_width()

        adder_unit = AdderUnit()

        # add it to the scene
        self.add(adder_unit)

        # play creation animations
        self.play(
            Create(adder_unit,run_time = 3)
        )

        self.wait(1)

    def createUnit(self,A,B,C_in,position,sandwich):
        print(sandwich)
        #doing the binary calculations
        total = A + B + C_in
        S = total % 2
        C_out = total // 2

        #creating all of the objects
        box = VGroup(Square(side_length=1, color = BLUE),Text("Full\nAdder", font_size = 20).move_to(Square())).shift(2*RIGHT)
        input_A = Text(f"{A}", font_size = 24).next_to(box,UP * 3)
        input_B = Text(f"{B}", font_size = 24).next_to(box,UP * 3).shift(RIGHT * 0.37)
        sum = Text(f"{S}", font_size = 24).next_to(box,3*DOWN)

        A_dot = Dot(color=WHITE,radius = 0.03).move_to(input_A.get_bottom()+ [0,-0.1,0])
        B_dot = Dot(color=WHITE,radius = 0.03).move_to(input_B.get_bottom()+ [0,-0.1,0])
        S_dot = Dot(color=WHITE,radius = 0.03).move_to(sum.get_top()+ [0,0.1,0])


        #make it blue if the input is 1, signifying water present
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
                line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-0.495, -0.1, 0], color=BLUE_C, stroke_width=3)
                line_carry2 = Line(box.get_left() + [-0.495, -0.1, 0], c.get_top() + [0,0.1,0], color = BLUE_C, stroke_width = 3)

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
                line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-0.495, -0.1, 0], color=WHITE, stroke_width=1)
                line_carry2 = Line(box.get_left() + [-0.495, -0.1, 0], c.get_top() + [0,0.1,0], color = WHITE, stroke_width = 1)

                C_dot = Dot(color=WHITE,radius = 0.03).move_to(c.get_top() + [0,0.1,0])
            
                self.add(box,A_dot,B_dot,S_dot, input_A, input_B, sum, c, line_A, line_B, line_sum, line_carry,line_carry2,C_dot)
            else:
                #if it's not the last one
                line_carry = Line(box.get_left() + [0, -0.1, 0], box.get_left() + [-1.2, -0.1, 0], color=WHITE, stroke_width=1)
                c = Text(f"{C_out}", font_size = 18).next_to(box,LEFT).shift(UP * .2)

                self.add(box,A_dot,B_dot,S_dot, input_A, input_B, sum, c, line_A, line_B, line_sum, line_carry)
        
        if sandwich == 0:
            if (S==1):
                S_outdot = Dot(color=BLUE_C,radius = 0.04).move_to(sum.get_bottom()+ [0,-0.1,0])
                S_outdot1 = Dot(color=BLUE_C,radius = 0.04).move_to(sum.get_bottom()+ [0,-0.9,0])
                sum_outline = Line(sum.get_bottom() + [0,-0.1,0], sum.get_bottom() + [0,-0.9,0], color = BLUE_C, stroke_width = 3)
            else:
                S_outdot = Dot(color=WHITE,radius = 0.03).move_to(sum.get_bottom()+ [0,-0.1,0])
                S_outdot1 = Dot(color=WHITE,radius = 0.03).move_to(sum.get_bottom()+ [0,-0.9,0])
                sum_outline = Line(sum.get_bottom() + [0,-0.1,0], sum.get_bottom() + [0,-0.9,0], color = WHITE, stroke_width = 1)
            self.add(S_outdot,S_outdot1,sum_outline)
