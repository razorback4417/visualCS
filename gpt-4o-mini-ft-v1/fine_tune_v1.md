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
```python
from manim import *

class MergeSortExample(Scene):
    def construct(self):

        problem = MathTex(r"\text{Merge Sort: } [38, 27, 43, 3, 9, 82, 10]")
        problem.to_edge(UP)
        self.play(Write(problem))
        self.wait(1)

        vertical_spacing = 0.8
        steps_display = []

        sorting_steps = [
            r"[38, 27, 43, 3] \quad [9, 82, 10]",
            r"[38, 27] \quad [43, 3] \quad [9, 82, 10]",
            r"[38] \quad [27] \quad [43] \quad [3] \quad [9] \quad [82] \quad [10]",
            r"[27, 38] \quad [3, 43] \quad [9, 82, 10]",
            r"[3, 27, 38, 43] \quad [9, 82, 10]",
            r"[3, 27, 38, 43] \quad [9] \quad [82, 10]",
            r"[3, 27, 38, 43] \quad [9] \quad [82] \quad [10]",
            r"[3, 27, 38, 43] \quad [9, 10, 82]",
            r"[3, 9, 10, 27, 38, 43, 82]"
        ]

        for i, step in enumerate(sorting_steps):
            new_step = MathTex(step)
            new_step.next_to(problem, DOWN, buff=vertical_spacing * (i + 1))

            if new_step.width > config.frame_width - 1:
                new_step.scale(0.8)

            new_step.move_to([0, new_step.get_y(), 0])

            self.play(Write(new_step))
            steps_display.append(new_step)
            self.wait(0.5)

        final_result = MathTex(r"\text{Sorted: } [3, 9, 10, 27, 38, 43, 82]")
        final_result.scale(1.2)
        final_result.to_edge(DOWN)

        self.play(
            *[FadeOut(step) for step in steps_display],
            Write(final_result)
        )
        self.wait(2)
```