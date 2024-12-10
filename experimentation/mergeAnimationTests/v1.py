# from manim import *

# class MergeSortExample(Scene):
#     def construct(self):
#         # Displaying the problem
#         problem = Text("Sort the array: [38, 27, 43, 3, 9, 82, 10]", font_size=24)
#         self.play(Write(problem))
#         self.wait(2)

#         # Merge sort steps
#         steps = [
#             "Divide: [38, 27, 43, 3, 9, 82, 10] -> [38, 27, 43] and [3, 9, 82, 10]",
#             "Divide: [38, 27, 43] -> [38] and [27, 43]",
#             "Divide: [27, 43] -> [27] and [43]",
#             "Merge: [27] and [43] -> [27, 43]",
#             "Merge: [38] and [27, 43] -> [27, 38, 43]",
#             "Divide: [3, 9, 82, 10] -> [3, 9] and [82, 10]",
#             "Divide: [3, 9] -> [3] and [9]",
#             "Merge: [3] and [9] -> [3, 9]",
#             "Divide: [82, 10] -> [82] and [10]",
#             "Merge: [82] and [10] -> [10, 82]",
#             "Merge: [3, 9] and [10, 82] -> [3, 9, 10, 82]",
#             "Merge: [27, 38, 43] and [3, 9, 10, 82] -> [3, 9, 10, 27, 38, 43, 82]"
#         ]

#         for step in steps:
#             self.wait(1)
#             self.play(ReplacementTransform(problem.copy(), Text(step, font_size=24)))

#         self.wait(2)

from manim import *

class MergeSortScene(Scene):
    def construct(self):
        self.intro()
        self.split_phase()
        self.merge_phase()
        self.final_assembly()
        self.conclusion()

    def intro(self):
        title = Text("Merge Sort Animation", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

    def split_phase(self):
        title = Text("Splitting Phase", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Initial array - using Text instead of MathTex
        initial = Text("[38, 27, 43, 3, 9, 82, 10]", font_size=36)
        initial.next_to(title, DOWN, buff=1)
        self.play(Write(initial))
        self.wait(1)

        # First split
        split1_left = Text("[38, 27, 43]", font_size=36)
        split1_right = Text("[3, 9, 82, 10]", font_size=36)

        split1_left.shift(2 * LEFT + DOWN)
        split1_right.shift(2 * RIGHT + DOWN)

        self.play(
            TransformFromCopy(initial, split1_left),
            TransformFromCopy(initial, split1_right)
        )
        self.wait(1)

        # Second split (left side)
        split2_left = Text("[38]", font_size=36).shift(3 * LEFT + 2 * DOWN)
        split2_middle = Text("[27, 43]", font_size=36).shift(LEFT + 2 * DOWN)

        self.play(
            TransformFromCopy(split1_left, split2_left),
            TransformFromCopy(split1_left, split2_middle)
        )
        self.wait(1)

        # Clean up
        self.play(
            *[FadeOut(mob) for mob in [initial, split1_left, split1_right,
                                     split2_left, split2_middle, title]]
        )

    def merge_phase(self):
        title = Text("Merging Phase", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Show merging process
        left = Text("[27, 38]", font_size=36)
        right = Text("[3, 9]", font_size=36)
        merged = Text("[3, 9, 27, 38]", font_size=36)

        left.shift(2 * LEFT)
        right.shift(2 * RIGHT)

        self.play(Write(left), Write(right))
        self.wait(1)

        # Show comparison arrows
        arrow1 = Arrow(left.get_center(), merged.get_center(), buff=0.3)
        arrow2 = Arrow(right.get_center(), merged.get_center(), buff=0.3)

        merged.shift(DOWN)
        self.play(
            Create(arrow1),
            Create(arrow2)
        )
        self.play(
            Write(merged)
        )
        self.wait(1)

        # Clean up
        self.play(
            *[FadeOut(mob) for mob in [left, right, merged, arrow1, arrow2, title]]
        )

    def final_assembly(self):
        title = Text("Final Sorted Array", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        final_array = Text("[3, 9, 10, 27, 38, 43, 82]", font_size=48)
        final_array.set_color(BLUE)

        self.play(Write(final_array))
        self.wait(2)

        self.play(
            *[FadeOut(mob) for mob in [title, final_array]]
        )

    def conclusion(self):
        conclusion = Text("Merge Sort Complete!", font_size=48)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(FadeOut(conclusion))