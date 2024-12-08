from manim import *

class BasicDefiniteIntegral(Scene):
    def construct(self):
        # Displaying the problem
        problem = MathTex(r"\int_{0}^{2} x^3 \,dx")
        self.play(Write(problem))
        self.wait(1)

        # Explanation for the integration rule
        explanation1 = Text("Using the Power Rule for definite integrals:", font_size=24).to_edge(UP)
        self.play(Write(explanation1))
        self.wait(2)

        # Demonstrating the Power Rule for definite integrals
        power_rule = MathTex(r"\int_{a}^{b} x^n \,dx = \left[\frac{1}{n+1}x^{n+1}\right]_{a}^{b}")
        self.play(Write(power_rule))
        self.wait(2)

        # Performing the integration step
        solution1 = MathTex(r"= \left[\frac{1}{3+1}x^{3+1}\right]_{0}^{2}")
        self.play(ReplacementTransform(problem.copy(), solution1))
        self.wait(1)

        # Explanation for evaluating the definite integral
        explanation2 = Text("Evaluating at the boundaries:", font_size=22).to_edge(UP)
        self.play(Transform(explanation1, explanation2))
        self.wait(2)

        # Evaluating the solution
        evaluated_solution = MathTex(r"= \left[\frac{1}{4}x^{4}\right]_{0}^{2}", "=", r"\frac{1}{4}(2^4) - \frac{1}{4}(0^4)", "=", r"\frac{1}{4}(16)", "=", r"4")
        self.play(ReplacementTransform(solution1, evaluated_solution))
        self.wait(1)

        # Clear the scene
        self.clear()
        self.wait(1)

        # Conclude with the final answer
        final_answer = MathTex(r"\int_{0}^{2} x^3 \,dx = 4")
        self.play(Write(final_answer))
        self.wait(1)