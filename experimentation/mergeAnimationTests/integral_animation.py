from manim import *

class IntegralAnimation(Scene):
    def construct(self):
        # Step 1: Display the integral problem
        integral_problem = Text(r"\int_0^2 x^2 \, dx")
        self.play(Write(integral_problem))
        self.wait(1)

        # Step 2: Explanation of the integral concept
        explanation1 = Text("Using the power rule of integration:", font_size=24)
        self.play(Write(explanation1))
        self.wait(2)

        # Step 3: Demonstration of the integration rule
        integral_rule = Text(r"\int x^n \,dx = \frac{x^{n+1}}{n+1} + C")
        self.play(Write(integral_rule))
        self.wait(2)

        # Step 4: Calculate the antiderivative
        antiderivative = Text(r"= \frac{x^{2+1}}{2+1} \bigg|_0^2")
        self.play(ReplacementTransform(integral_problem, antiderivative))
        self.wait(1)

        # Step 5: Evaluating the definite integral
        solution = Text(r"= \left[\frac{x^3}{3}\right]_0^2")
        self.play(ReplacementTransform(antiderivative, solution))
        self.wait(1)

        solution_evaluation = MathTex(r"= \frac{2^3}{3} - \frac{0^3}{3}")
        self.play(Transform(solution, solution_evaluation))
        self.wait(2)

        # Step 6: Final solution
        final_solution = Text(r"= \frac{8}{3}")
        self.play(ReplacementTransform(solution_evaluation, final_solution))
        self.wait(1)

        # Clear the scene
        self.clear()
        self.wait(1)

        # Show final solution before exiting
        self.play(Write(final_solution))
        self.wait(1)