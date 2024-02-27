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
points = []
x = []
y = []
for i in range(10):
    toAdd = generate_random_numbers(i+2)
    
    start_time = time.time()

    combos = make_combos(toAdd)               
    result = get_sums(combos,5)

    end_time = time.time()        

    runTime = end_time - start_time
    x.append(i+2)
    y.append(runTime)
    points.append((i+2,runTime))

    print(i)

# Convert lists to numpy arrays for curve fitting
x_data = np.array(x)
y_data = np.array(y)

# Define the function to fit (you need to define your function here)
def fit_function(x, a, b):
    return a * np.exp(b * x)  # This is just an example function, you should replace it with the function you want to fit

# Perform the curve fitting
popt, pcov = curve_fit(fit_function, x_data, y_data)

# Create a string representation of the fitted function
fitted_function_str = f'y = {popt[0]:.4e} * exp({popt[1]:.2f}x)'

class expPlot(Scene):
    def construct(self):
        points = []
        x = []
        y = []
        for i in range(10):
            toAdd = generate_random_numbers(i+2)
            
            start_time = time.time()

            combos = make_combos(toAdd)               
            result = get_sums(combos,5)

            end_time = time.time()        

            runTime = end_time - start_time
            x.append(i+2)
            y.append(runTime)
            points.append((i+2,runTime))

            print(i)
        axes = Axes(
            x_range=[0, 20, 1],
            y_range=[0, max(y), 1],
            axis_config={"color": BLUE},
        )
        dots = VGroup(*[Dot(axes.c2p(x, y)) for x, y in points])

        # Add axes and points to scene
        self.play(Create(axes),run_time = 2)
        self.wait(1)
        self.play(Create(dots), run_time = 2)

        self.wait(2)

        # Plot fitted line
        fitted_line_points = [(x_val, self.fit_function(x_val, *popt)) for x_val in np.linspace(0, 20, 100)]
        fitted_line = VMobject()
        fitted_line.set_points_smoothly([axes.c2p(x_val, y_val) for x_val, y_val in fitted_line_points])
        self.play(Create(fitted_line),runtime=4)
        self.wait()

    def fit_function(self, x, a, b):
        return a * np.exp(b * x)  # This is just an example function, replace it with the desired function

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
