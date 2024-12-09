from manim import *
import numpy as np

#Scene to illustrate gradient descent optimization
class GradientDescentExample(Scene):
    def construct(self):
        # Write the function
        func = MathTex(r"f(x) = x^4 - 3x^3 + 2")
        self.play(Write(func))
        self.wait(1)

        # Explanation for minimization
        explanation1 = Text("We want to find the minimum of the function", font_size=24).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(2)

        # Explanation for gradient descent
        explanation2 = Text("Using gradient descent to optimize", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation2))
        self.wait(2)

        # Gradient definition
        gradient_def = MathTex(r"\nabla f(x) = 4x^3 - 9x^2")
        self.play(ReplacementTransform(func.copy(), gradient_def))
        self.wait(2)

        # Write the update rule
        update_rule = MathTex(r"x_{n+1} = x_n - \alpha \nabla f(x_n)")
        self.play(Write(update_rule))
        self.wait(1)

        # Group for the animation
        optimization_elements = VGroup(func, gradient_def, update_rule)
        optimization_elements.move_to(ORIGIN)

        # Initial x value and learning rate
        init_x_value = MathTex(r"x_0 = 0.5")
        learning_rate = MathTex(r"\alpha = 0.01")
        self.play(Write(init_x_value))
        self.play(Write(learning_rate))
        self.wait(1)

        # Explanation for iterations
        explanation3 = Text("Performing iterations to minimize the function", font_size=24).to_edge(UP)
        self.play(Transform(explanation1, explanation3))
        self.wait(2)

        # Perform gradient descent iterations (simplified)
        for n in range(3):
            new_x = MathTex(r"x_{", str(n+1), r"} = ", r"x_{", str(n), r"} - 0.01 \cdot (4x_{", str(n), r"}^3 - 9x_{", str(n), r"}^2)")
            self.play(ReplacementTransform(init_x_value, new_x))
            self.wait(1)
            init_x_value = new_x

        # Clear the scene and show final result
        self.clear()

        # Final explanation for convergence
        final_explanation = Text("Converged to minimum after iterative updates", font_size=24).to_edge(UP)
        self.play(Write(final_explanation))
        self.wait(2)