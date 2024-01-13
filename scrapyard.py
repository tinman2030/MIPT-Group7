from manim import *
from itertools import combinations

class MakeAdder(Scene):
    def construct(self):
        boxes_group = BoxesGroup()
        self.play(Create(boxes_group), run_time = 5)
        self.wait(1)

class BoxesGroup(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_boxes()

    def create_boxes(self):
        for i in range(10):
            box = Square(side_length=1, color=BLUE)
            text = Text(f"Box {i}", font_size=12)
            group = VGroup(box, text).arrange(DOWN)
            self.add(group)

        # Align the boxes in a row
        self.arrange(RIGHT, buff=0.5)
class BinaryConversion(Scene):
    def construct(self, original_list = [1,2,3,4,5]):
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
            self.wait(0.8)

    def decimal_to_binary_list(self, decimal_list):
        return [bin(x)[2:] for x in decimal_list]
    #getting the different combinations of a list
    def make_combos(self, my_set):

        my_set = [x for x in my_set if x != 0]

        if len(my_set) < 2:
            raise ValueError("Size of the set must be greater than 2")

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
        big_list.append(list[i*n:])

        return big_list
