# PROMPT

# Use the Manim Python library to create an animation of the Merge Sort algorithm. Break it into the following steps:

# 1. Setup the Scene: Display an unsorted array of numbers as a row of rectangles. Ensure spacing is even, and everything fits within the camera view.
# 2. Splitting Phase: Animate recursive splitting into subarrays. Move subarrays to distinct locations without overlapping or cluttering the scene.
# 3. Merging Phase: Animate merging two subarrays step by step. Highlight comparisons (e.g., with colors or arrows) and place merged elements logically into the new array.
# 4. Final Assembly: Gradually combine sorted subarrays back into the original array. Keep spacing consistent and ensure smooth transitions.
# 5. Enhancements: Add labels for each phase, use colors to highlight key actions, and conclude with the sorted array prominently displayed.

# Guidelines:
# - Avoid overlapping objects or animations.
# - Keep everything within the camera view at all times.
# - Ensure transitions are logical and not too fast or abrupt.

# Create this step by step, providing code and brief explanations as you progress.

#ERROR:
# (base) theol@T-Air-2 visualCS % manim merge.py
# Manim Community v0.18.1

# [12/07/24 02:52:34] INFO     Writing 5 to media/Tex/ade9425328175941.tex                                                                                                                              tex_file_writing.py:109
#                     ERROR    LaTeX compilation error: LaTeX Error: File `standalone.cls' not found.                                                                                                   tex_file_writing.py:314

#                     ERROR    Context of error:                                                                                                                                                        tex_file_writing.py:348
#                              -> \documentclass[preview]{standalone}
#                              \usepackage[english]{babel}
#                              \usepackage{amsmath}
#                              \usepackage{amssymb}

#                     INFO     You do not have package standalone.cls installed.                                                                                                                        tex_file_writing.py:358
#                     INFO     Install standalone.cls it using your LaTeX package manager, or check for typos.                                                                                          tex_file_writing.py:358
#                     ERROR    LaTeX compilation error: Emergency stop.                                                                                                                                 tex_file_writing.py:314

#                     ERROR    Context of error:                                                                                                                                                        tex_file_writing.py:348
#                              -> \documentclass[preview]{standalone}
#                              \usepackage[english]{babel}
#                              \usepackage{amsmath}
#                              \usepackage{amssymb}

# ╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
# │ /Users/theol/miniconda3/lib/python3.10/site-packages/manim/cli/render/commands.py:120 in render  │
# │                                                                                                  │
# │   117 │   │   │   try:                                                                           │
# │   118 │   │   │   │   with tempconfig({}):                                                       │
# │   119 │   │   │   │   │   scene = SceneClass()                                                   │
# │ ❱ 120 │   │   │   │   │   scene.render()                                                         │
# │   121 │   │   │   except Exception:                                                              │
# │   122 │   │   │   │   error_console.print_exception()                                            │
# │   123 │   │   │   │   sys.exit(1)                                                                │
# │                                                                                                  │
# │ /Users/theol/miniconda3/lib/python3.10/site-packages/manim/scene/scene.py:229 in render          │
# │                                                                                                  │
# │    226 │   │   """                                                                               │
# │    227 │   │   self.setup()                                                                      │
# │    228 │   │   try:                                                                              │
# │ ❱  229 │   │   │   self.construct()                                                              │
# │    230 │   │   except EndSceneEarlyException:                                                    │
# │    231 │   │   │   pass                                                                          │
# │    232 │   │   except RerunSceneException as e:                                                  │
# │                                                                                                  │
# │ /Users/theol/Documents/visualCS/merge.py:12 in construct                                         │
# │                                                                                                  │
# │     9 │   │   rectangles = VGroup()                                                              │
# │    10 │   │   for i, num in enumerate(unsorted_array):                                           │
# │    11 │   │   │   rect = Rectangle(width=0.8, height=1).shift(RIGHT * (i - len(unsorted_array)   │
# │ ❱  12 │   │   │   label = Tex(str(num)).move_to(rect.get_center())                               │
# │    13 │   │   │   rectangles.add(VGroup(rect, label))                                            │
# │    14 │   │                                                                                      │
# │    15 │   │   # Add "Unsorted Array" label                                                       │
# │                                                                                                  │
# │ /Users/theol/miniconda3/lib/python3.10/site-packages/manim/mobject/text/tex_mobject.py:443 in    │
# │ __init__                                                                                         │
# │                                                                                                  │
# │   440 │   def __init__(                                                                          │
# │   441 │   │   self, *tex_strings, arg_separator="", tex_environment="center", **kwargs           │
# │   442 │   ):                                                                                     │
# │ ❱ 443 │   │   super().__init__(                                                                  │
# │   444 │   │   │   *tex_strings,                                                                  │
# │   445 │   │   │   arg_separator=arg_separator,                                                   │
# │   446 │   │   │   tex_environment=tex_environment,                                               │
# │                                                                                                  │
# │ /Users/theol/miniconda3/lib/python3.10/site-packages/manim/mobject/text/tex_mobject.py:293 in    │
# │ __init__                                                                                         │
# │                                                                                                  │
# │   290 │   │   │   │   │   │   """,                                                               │
# │   291 │   │   │   │   │   ),                                                                     │
# │   292 │   │   │   │   )                                                                          │
# │ ❱ 293 │   │   │   raise compilation_error                                                        │
# │   294 │   │   self.set_color_by_tex_to_color_map(self.tex_to_color_map)                          │
# │   295 │   │                                                                                      │
# │   296 │   │   if self.organize_left_to_right:                                                    │
# │                                                                                                  │
# │ /Users/theol/miniconda3/lib/python3.10/site-packages/manim/mobject/text/tex_mobject.py:272 in    │
# │ __init__                                                                                         │
# │                                                                                                  │
# │   269 │   │   self.brace_notation_split_occurred = False                                         │
# │   270 │   │   self.tex_strings = self._break_up_tex_strings(tex_strings)                         │
# │   271 │   │   try:                                                                               │
# │ ❱ 272 │   │   │   super().__init__(                                                              │
# │   273 │   │   │   │   self.arg_separator.join(self.tex_strings),                                 │
# │   274 │   │   │   │   tex_environment=self.tex_environment,                                      │
# │   275 │   │   │   │   tex_template=self.tex_template,                                            │
# │                                                                                                  │
# │ /Users/theol/miniconda3/lib/python3.10/site-packages/manim/mobject/text/tex_mobject.py:81 in     │
# │ __init__                                                                                         │
# │                                                                                                  │
# │    78 │   │                                                                                      │
# │    79 │   │   assert isinstance(tex_string, str)                                                 │
# │    80 │   │   self.tex_string = tex_string                                                       │
# │ ❱  81 │   │   file_name = tex_to_svg_file(                                                       │
# │    82 │   │   │   self._get_modified_expression(tex_string),                                     │
# │    83 │   │   │   environment=self.tex_environment,                                              │
# │    84 │   │   │   tex_template=self.tex_template,                                                │
# │                                                                                                  │
# │ /Users/theol/miniconda3/lib/python3.10/site-packages/manim/utils/tex_file_writing.py:63 in       │
# │ tex_to_svg_file                                                                                  │
# │                                                                                                  │
# │    60 │   if svg_file.exists():                                                                  │
# │    61 │   │   return svg_file                                                                    │
# │    62 │                                                                                          │
# │ ❱  63 │   dvi_file = compile_tex(                                                                │
# │    64 │   │   tex_file,                                                                          │
# │    65 │   │   tex_template.tex_compiler,                                                         │
# │    66 │   │   tex_template.output_format,                                                        │
# │                                                                                                  │
# │ /Users/theol/miniconda3/lib/python3.10/site-packages/manim/utils/tex_file_writing.py:213 in      │
# │ compile_tex                                                                                      │
# │                                                                                                  │
# │   210 │   │   if exit_code != 0:                                                                 │
# │   211 │   │   │   log_file = tex_file.with_suffix(".log")                                        │
# │   212 │   │   │   print_all_tex_errors(log_file, tex_compiler, tex_file)                         │
# │ ❱ 213 │   │   │   raise ValueError(                                                              │
# │   214 │   │   │   │   f"{tex_compiler} error converting to"                                      │
# │   215 │   │   │   │   f" {output_format[1:]}. See log output above or"                           │
# │   216 │   │   │   │   f" the log file: {log_file}",                                              │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
# ValueError: latex error converting to dvi. See log output above or the log file: media/Tex/ade9425328175941.log


from manim import *

class MergeSortAnimation(Scene):
    def construct(self):
        # The unsorted array
        unsorted_array = [5, 3, 8, 4, 2, 7, 1, 6]

        # Setup: Create rectangles for each element
        rectangles = VGroup()
        for i, num in enumerate(unsorted_array):
            rect = Rectangle(width=0.8, height=1).shift(RIGHT * (i - len(unsorted_array) / 2) * 1.5)
            label = Tex(str(num)).move_to(rect.get_center())
            rectangles.add(VGroup(rect, label))

        # Add "Unsorted Array" label
        unsorted_label = Tex("Unsorted Array").to_edge(UP)
        self.play(FadeIn(rectangles), Write(unsorted_label))
        self.wait(1)

        # Step 1: Splitting Phase
        # Divide the array into halves recursively
        split_positions = [
            (LEFT * 3.5, RIGHT * 3.5),  # First split
            (LEFT * 5.5, LEFT * 1.5),  # Left half splits further
            (RIGHT * 1.5, RIGHT * 5.5),  # Right half splits further
        ]

        left_half = VGroup(rectangles[0], rectangles[1], rectangles[2], rectangles[3])
        right_half = VGroup(rectangles[4], rectangles[5], rectangles[6], rectangles[7])

        # Animate the first split
        self.play(
            left_half.animate.shift(split_positions[0][0]),
            right_half.animate.shift(split_positions[0][1])
        )
        self.wait(1)

        # Split the left and right halves further
        left_quarters = [
            VGroup(left_half[0], left_half[1]),
            VGroup(left_half[2], left_half[3]),
        ]
        right_quarters = [
            VGroup(right_half[0], right_half[1]),
            VGroup(right_half[2], right_half[3]),
        ]
        self.play(
            left_quarters[0].animate.shift(split_positions[1][0]),
            left_quarters[1].animate.shift(split_positions[1][1]),
            right_quarters[0].animate.shift(split_positions[2][0]),
            right_quarters[1].animate.shift(split_positions[2][1])
        )
        self.wait(1)

        # Step 2: Merging Phase
        # Merging two subarrays at a time with highlights
        def merge_subarrays(array1, array2, target_position):
            # Highlight the first comparison
            self.play(
                array1[0].animate.set_fill(YELLOW, opacity=0.5),
                array2[0].animate.set_fill(YELLOW, opacity=0.5),
            )
            self.wait(0.5)

            # Merge and place elements in target
            merged_array = sorted(
                [int(array1[0][1].text), int(array2[0][1].text)]
            )
            for i, num in enumerate(merged_array):
                rect = Rectangle(width=0.8, height=1).shift(target_position + RIGHT * i * 1.5)
                label = Tex(str(num)).move_to(rect.get_center())
                self.play(FadeIn(VGroup(rect, label)))
                self.wait(0.5)

        # Merge the first level subarrays
        merge_subarrays(left_quarters[0], left_quarters[1], LEFT * 3)
        merge_subarrays(right_quarters[0], right_quarters[1], RIGHT * 3)

        # Step 3: Final Assembly
        # Combine the sorted halves into the final array
        sorted_left = [1, 3, 5, 8]  # Example result of merge
        sorted_right = [2, 4, 6, 7]  # Example result of merge
        sorted_array = sorted_left + sorted_right

        final_rectangles = VGroup()
        for i, num in enumerate(sorted_array):
            rect = Rectangle(width=0.8, height=1).shift(RIGHT * (i - len(sorted_array) / 2) * 1.5)
            label = Tex(str(num)).move_to(rect.get_center())
            final_rectangles.add(VGroup(rect, label))

        self.play(
            left_half.animate.shift(ORIGIN),
            right_half.animate.shift(ORIGIN)
        )
        self.play(Transform(rectangles, final_rectangles))
        self.wait(1)

        # Step 4: Display Final Array
        final_label = Tex("Sorted Array").to_edge(UP)
        self.play(Transform(unsorted_label, final_label))
        self.wait(2)
