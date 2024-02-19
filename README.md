# MIPT-Group7

McGill IPT Group 7, working on the water-based computer
Using the Manim python package we're using the computing power of the n-bit ripple adder as a analogy for how you would scale up a computer to do large amounts of sums

## TO-DO

The AllTogether class is meant to do all of the computations for adding the sums. This is working but there are some quirks

- ~~I want to keep the frame the same size, possibly calculate the largest addition that we'd have to do to keep it that size~~
    * ~~Problem here is that I think the resizing is currently done in the function "makeAdders" going to have to migrate that out and keep it consistent.~~
- ~~Make the current combo we're summing over in the middle when the resizing of the frame happens and make keep it there. It currently gets cleared in the for loop that does the summing~~
- ~~Keep track of the sums on the screen somehow.~~
- ~~Add the target, possibly keeping it on the screen for comparisons.~~
- ~~ Got to make the final Carry point down or have it look more... terminal~~
- ~~Maybe show how the half and full adder work as well(Don't think we need this since we have the physical model)~~
- ~~Try to make the lines connected to the 1's turn red to make it more intuitive as to what the water would do.~~
- ~~Make the construction of the adders more sleek.~~
- ~~Make the numbers that we've already sequentially adder turn red or something ~~
- ~~Make the lines arrows in adder_anim.py, what if someone from Tunisia finds this?~~

- ~~Make is so that you don't clear it the next time and the output from one addition becomes the input to the next one, while all of the additions stay on the screen~~
   ~~i.e make the output of one addition flow into the input of the new sequence of adders~~

- make it run multiple at a time? RUN ALL AT THE SAME TIME

- Do the running time analysis, including explaing the logic behind sequentially adding the numbers

- ~~Make a plot of the algorithm running time to show the exponential nature of it. Plot running time vs. size of set~~

- make a plot showing the number of adders/gates needed to compute n-sized set

- recruit someone with fluid dynamics experience to make the analysis and explanation of the greedy siphon

- finish the presentation, practice presentation. WIN