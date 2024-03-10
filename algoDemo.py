from manim import *
from itertools import combinations

def make_combos(my_set):
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

class Demo(Scene):
    def construct(self, inputSet = [3,4,5,2], target = 6):

        original_text = Text("Multiset(S) = " + str(inputSet), font_size=24)
        target_text = Text("Target(T) = " + str(target), font_size = 24).next_to(original_text, DOWN)
        
        self.play(Write(original_text), run_time = 2)
        self.play(Write(target_text))
        self.wait(1.5)
        self.play(FadeOut(original_text))
        self.play(FadeOut(target_text))

        header = Text("Get All Combinations", font_size = 24).to_edge(UP)
        self.play(Write(header))

        combos = make_combos(inputSet)
        text_objects = []

        for i in range(len(combos)):
            sublist_text = Text(f"{combos[i]}", font_size=18).to_edge(UP)
            text_objects.append(sublist_text)
            sublist_text.shift(DOWN * i)
            
        text_group = VGroup(*text_objects)
       
        text_group.arrange(DOWN)
        text_group.move_to(ORIGIN)

        self.play(Write(text_group), run_time=2)
        self.wait(2)

        indicator = 0

        sumHeader = Text(f"Take Sums and Check if Sum == {target} ", font_size = 24).to_edge(UP)
        self.play(ReplacementTransform(header,sumHeader), run_time = 1)

        for i in range(len(combos)):

            sum_value = sum(combos[i])  # Calculate the sum
            new_text = Text(str(sum_value), font_size=18)
            new_text.move_to(text_objects[i].get_center())  # Set the position
            self.play(Transform(text_objects[i], new_text), run_time = 0.2)
            

            if(sum(combos[i]) == target):
                self.play(FadeToColor(text_objects[i], BLUE_D), run_time=0.2)
                indicator += 1
                break
            else:
                self.play(FadeToColor(text_objects[i], RED_E), run_time=0.2) 

            
        self.wait(2)

        returnText = Text("return", font_size = 24).to_edge(DOWN)
        returnText.shift([-0.35,0,0])

        if indicator > 0:
            resultText = Text("True", font_size = 24, color = BLUE_D).next_to(returnText,RIGHT, buff = 0.1)
            self.play(Write(returnText),
                      Wait(0.5),
                      Write(resultText))
        else: 
            resultText = Text("False", font_size = 24, color = RED_E).next_to(returnText,RIGHT,buff = 0.1)
            self.play(Write(returnText),
                      Wait(0.5),
                      Write(resultText))
        self.wait(5)
            