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