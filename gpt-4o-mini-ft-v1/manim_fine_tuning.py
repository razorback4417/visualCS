# ft:gpt-4o-mini-2024-07-
# 18:personal:manim-finetune-v1-
# 10:Ac3XpSam

from manim import *

class MergeSortExample(Scene):
    def construct(self):

        # Displaying the merge sort problem
        problem = MathTex(r"\text{Merge Sort: } [38, 27, 43, 3, 9, 82, 10]")
        problem.to_edge(UP)
        self.play(Write(problem))
        self.wait(1)

        # Setting vertical spacing for steps
        vertical_spacing = 0.8
        steps_display = []

        # Defining the steps of merge sort
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

        # Animating each step of the sorting process
        for i, step in enumerate(sorting_steps):
            new_step = MathTex(step)
            new_step.next_to(problem, DOWN, buff=vertical_spacing * (i + 1))

            # Adjusting the scale if the width exceeds the frame
            if new_step.width > config.frame_width - 1:
                new_step.scale(0.8)

            # Ensuring new step is properly positioned
            new_step.move_to([0, new_step.get_y(), 0])

            self.play(Write(new_step))
            steps_display.append(new_step)
            self.wait(0.5)

        # Displaying the final sorted result
        final_result = MathTex(r"\text{Sorted: } [3, 9, 10, 27, 38, 43, 82]")
        final_result.scale(1.2)
        final_result.to_edge(DOWN)

        # Fading out the steps and writing the final result
        self.play(
            *[FadeOut(step) for step in steps_display], # Fading out previous steps
            Write(final_result) # Wait before ending the scene
        )
        self.wait(2)