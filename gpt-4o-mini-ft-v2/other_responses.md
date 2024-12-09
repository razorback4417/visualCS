# EXAMPLE 1
## INPUT

Create an educational video about the Merge Sort algorithm.

## OUTPUT
 from manim import *

class RecursionExample(Scene):
    def construct(self):
        # Display the initial problem
        initial_problem = Text("Solve: 5 * (x + 3)", font_size=36)
        self.play(Write(initial_problem))
        self.wait(1)

        # Show the first step (distribute)
        distribute_step = Text("Distribute 5 to both terms inside the parentheses", font_size=24)
        self.play(Transform(initial_problem, distribute_step))
        self.wait(2)

        # Display the distributed equation
        distributed_equation = Text("5x + 15", font_size=36)
        self.play(ReplacementTransform(initial_problem, distributed_equation))
        self.wait(1)

        # Show the final answer
        final_answer = Text("Final answer: 5x + 15", font_size=36, color=GREEN)
        self.play(Transform(distributed_equation, final_answer))
        self.wait(1)

        # Clear the scene and conclude
        self.clear()
        self.wait(1)
        self.play(Write(final_answer))
        self.wait(2)

# EXAMPLE 2
## INPUT
Create an educational video about the Merge Sort algorithm. Lets think this through step by step

## OUTPUT
        self.wait(1)
        self.play(FadeIn(array, shift=UP), run_time=1)