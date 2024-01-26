# MIPT-Group7

McGill IPT Group 7, working on the water-based computer
Using the Manim python package we're using the computing power of the n-bit ripple adder as a analogy for how you would scale up a computer to do large amounts of sums

## TO-DO

The AllTogether class is meant to do all of the computations for adding the sums. This is working but there are some quirks

- I want to keep the frame the same size, possibly calculate the largest addition that we'd have to do to keep it that size
    * Problem here is that I think the resizing is currently done in the function "makeAdders" going to have to migrate that out and keep it consistent.
- Make the current combo we're summing over in the middle when the resizing of the frame happens and make keep it there. It currently gets cleared in the for loop that does the summing
- Keep track of the sums on the screen somehow.
- Add the target, possibly keeping it on the screen for comparisons. 
- Got to make the final Carry point down or have it look more... terminal
- Maybe show how the half and full adder work as well
- Try to make the lines connected to the 1's turn red to make it more intuitive as to what the water would do.
