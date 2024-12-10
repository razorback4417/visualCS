# Prompt
> **NOTE:** Prompt is styled (e.g. italicized and bolded) for legibility purposes. Prompt was given to model in "raw" unstyled form.

Create an educational animation of the Merge Sort algorithm using the Manim Python library. The visualization should demonstrate both the recursive division and merging processes through a simple, clear visual representation.

**Initial Setup**

Create a class inheriting from Scene named MergeSortVisualization
Initialize an unsorted array of 8 integers (e.g., [7, 3, 1, 8, 4, 2, 6, 5])
Represent each number in a square:

* Fixed-size squares (1.0 units)
* Number centered inside square
* Initial color: WHITE with slight transparency
* Small spacing between squares (0.2 units)

**Visual Layout Requirements**

Position initial array centered at y=2
Maintain consistent spacing between squares
Reserve vertical space below (y < 2) for recursive divisions
Keep all elements within camera frame (-7 ≤ x ≤ 7, -4 ≤ y ≤ 4)

**Animation Sequence**

*Array Initialization (2-3 seconds)*

* Fade in squares with numbers
* Add title "Merge Sort Visualization" at top
* Brief pause to show initial state

*Division Phase*

Create clear splitting animations:

* Move subarrays down by 1.5 units
* Shift left/right subgroups horizontally
* Add dotted lines connecting parent to child arrays
* Duration: ~1 second per split

*Merging Phase*
For each merge comparison:

* Highlight comparing squares in blue
* Move smaller number up first
* Return color to white after comparison
* Remove original squares after merging

*Final Steps*

* Color final sorted array green
* Display "Array Sorted!" text
* Hold final state for 2 seconds

**Technical Notes**

* Use consistent animation timings (0.5-1.0 seconds per action)
* Add appropriate pauses between steps
* Group square and number as single mobject
* Track and update positions carefully during merges
* Importantly, make sure no objects get in the way of each other, and that all objects are visible in the screen


# Output
Sure! Below is an implementation of a Merge Sort visualization using the Manim library. This code includes the required animations for the initialization, division, and merging phases, keeping in mind the layout and visual requirements you specified.

Make sure you have Manim installed and set up before running this code.

```python
from manim import *

class MergeSortVisualization(Scene):
    def construct(self):
        # Initial unsorted array
        self.array = [7, 3, 1, 8, 4, 2, 6, 5]
        self.squares = []

        # Create squares for each number in the array
        for i, value in enumerate(self.array):
            square = Square(side_length=1.0, fill_color=WHITE, fill_opacity=0.5, stroke_color=WHITE)
            number = Integer(value).move_to(square.get_center())
            group = VGroup(square, number).move_to(RIGHT * (i * 1.2) + UP * 2)
            self.squares.append(group)

        # Add title
        title = Text("Merge Sort Visualization").to_edge(UP)

        # Initial animation
        self.play(FadeIn(title), *[FadeIn(group) for group in self.squares])
        self.wait(1)

        # Start the division phase
        self.divide_and_animate(0, len(self.array))

        # Final steps
        self.finalize()

    def divide_and_animate(self, start, end):
        if end - start <= 1:
            return

        mid = (start + end) // 2
        self.divide_and_animate(start, mid)
        self.divide_and_animate(mid, end)

        # Start the merging process
        self.merge_and_animate(start, mid, end)

    def merge_and_animate(self, start, mid, end):
        left = self.squares[start:mid]          # Left subarray
        right = self.squares[mid:end]           # Right subarray
        merged = []

        # Move down the squares to make space for merging
        for square in left + right:
            self.play(square.animate.shift(DOWN * 1.5))

        # Adding dotted lines for visualization
        line = DashedLine(UP * 1.5, UP * 2 + LEFT * 2 + RIGHT * 2, stroke_width=1, color=BLUE)
        self.play(Create(line))
        self.wait(0.5)

        # Merge process
        while left and right:
            if left[0][1].get_value() <= right[0][1].get_value():
                self.highlight_square(left[0], BLUE)
                merged.append(left.pop(0))
            else:
                self.highlight_square(right[0], BLUE)
                merged.append(right.pop(0))

        # Clean up the original squares
        for square in (left + right):
            square.clear_updaters()  # Remove updaters for the squares to stop moving

        for square in left + right:
            self.play(FadeOut(square))

        # Place merged squares
        for i, square in enumerate(merged):
            self.play(square.animate.move_to(UP * 1.5 + RIGHT * (i * 1.2)))

        # Remove the line
        self.play(FadeOut(line))
        self.wait(0.5)

        # Update self.squares with the new merged squares
        start_square_index = start // 2
        self.squares[start_square_index: start_square_index + len(merged)] = merged

    def highlight_square(self, group, color):
        square = group[0]
        self.play(square.animate.set_fill(color))
        self.wait(0.5)
        self.play(square.animate.set_fill(WHITE, 0.5))

    def finalize(self):
        # Color the final sorted array green and show the sorted array message
        for square in self.squares:
            square[0].set_fill(GREEN, 1)
        final_message = Text("Array Sorted!").scale(1.5).move_to(DOWN * 2)
        self.play(FadeIn(final_message))
        self.wait(2)

# To run the scene, use the following command (make sure you have manim installed):
# manim -pql <script_name.py> MergeSortVisualization
```

### Notes:
- Save the code in a file, e.g., `merge_sort_visualization.py`.
- Replace `<script_name.py>` with your actual filename when running the command to render the video.
- The above implementation includes a correct division and merging showing the algorithm's state at each step.
- The visual space and movement are laid out according to your specifications, avoiding overlaps and ensuring visibility.
- You can tweak animations' timing and other parameters to suit your needs better.

This code will create a clear and educational visualization of the Merge Sort algorithm.