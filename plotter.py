import time
from itertools import combinations
import random
import numpy as np
from scipy.optimize import curve_fit
from manim import *

def generate_random_numbers(n):
    return [random.random() for _ in range(n)]

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

def get_sums(combos, target):
    good_list= []
    for combo in combos:
        if sum(combo) == target:
            good_list.append(combo)

class expPlot(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 17, 2],
            y_range=[0, 2.3, 1],
            axis_config={"color": BLUE, "include_numbers": True},
            tips=True,
        )
        x_label_text = Text("Size of Multiset", font_size = 14).next_to(axes.x_axis.get_midpoint(), DOWN*1.3, buff=0.5)
        y_label_text = Text("Run Time(seconds)",font_size = 14).next_to(axes.y_axis.get_midpoint(), LEFT, buff=0)
        y_label_text.rotate(90*DEGREES)
        title = Text('Running Time vs. Multiset size', font_size=16).to_edge(UP)
        self.play(FadeIn(axes),run_time = 2)
        self.play(Write(x_label_text), Write(y_label_text),Write(title))

        # Add axes and points to scene
        self.wait(1)
        for j in range(15):
            points = []
            x = []
            y = []
            for i in range(14):
                toAdd = generate_random_numbers(i+2)
                
                start_time = time.time()

                combos = make_combos(toAdd)               
                result = get_sums(combos,5)

                end_time = time.time()        

                runTime = end_time - start_time
                x.append(i+2)
                y.append(runTime)
                points.append((i+2,runTime))
            
            dots = VGroup(*[Dot(axes.c2p(x, y),color=ORANGE,radius = 0.08) for x, y in points])
            self.play(Create(dots), run_time = 1)

            # Plot fitted line
            x_data = np.array(x)
            y_data = np.array(y)
            popt, _ = curve_fit(self.fit_function, x_data, y_data)
            fitted_function_str = f'f(x) = {popt[0]:.4e} * \\cdot 2^{{({popt[1]:.2f}x)}}'
            equation_label = MathTex(fitted_function_str,font_size=16)

            fitted_line_points = [(x_val, self.fit_function(x_val, *popt)) for x_val in np.linspace(0, 20, 100)]
            fitted_line = VMobject()
            fitted_line.set_points_smoothly([axes.c2p(x_val, y_val) for x_val, y_val in fitted_line_points])
            equation_label.move_to(fitted_line.get_bottom() + [0,1,0])

            self.play(Create(fitted_line),runtime=8)
            self.play(Write(equation_label))
            self.wait(3)
            if j!=15:
                self.play(FadeOut(fitted_line,dots,equation_label))
            else:
                self.wait(40)

    def fit_function(self, x, a, b):
        return a * (2**(b * x))  # This is just an example function, replace it with the desired function

    def generate_random_numbers(self,n):
        return [random.random() for _ in range(n)]

    def make_combos(self,my_set):
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

    def get_sums(self,combos, target):
        good_list= []
        for combo in combos:
            if sum(combo) == target:
                good_list.append(combo)
