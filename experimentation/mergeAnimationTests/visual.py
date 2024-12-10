from manim import *

class MergeSortScene(Scene):
    def construct(self):
        # Configuration
        self.array = [3, 5, 4, 2, 6]
        self.square_size = 0.7
        self.square_spacing = 0.2
        self.level_spacing = 1.5
        self.split_spacing = 1.0
        self.highlight_color = "#FFD700"  # Golden yellow for highlights

        # Track all elements at each level for merging animation
        self.levels = {0: [], 1: [], 2: [], 3: []}

        # Initial setup
        self.camera.background_color = "#2D3436"
        title = Text("Merge Sort", color=WHITE).to_edge(UP, buff=0.5)
        self.play(FadeIn(title))

        # Create initial array at top
        initial_group = self.create_array_group(self.array, 2.5)
        self.levels[0].append((initial_group, 0, len(self.array)-1))
        self.play(FadeIn(initial_group))

        # Phase 1: Split arrays recursively (top-down)
        self.split_phase(self.array, 0, len(self.array)-1, 0, 0)
        self.wait(0.5)

        # Phase 2: Merge arrays (bottom-up)
        self.merge_phase()
        self.wait(1)

    def create_square_number(self, number, position, highlighted=False):
        square = Square(
            side_length=self.square_size,
            color=self.highlight_color if highlighted else BLUE,
            fill_opacity=0.3
        ).move_to(position)

        number_text = Text(str(number), color=WHITE).scale(0.6)
        number_text.move_to(square.get_center())

        return VGroup(square, number_text)

    def create_array_group(self, arr, y_pos, x_offset=0):
        group = VGroup()
        total_width = len(arr) * (self.square_size + self.square_spacing)
        start_x = x_offset - total_width/2 + self.square_size/2

        for i, num in enumerate(arr):
            x_pos = start_x + i * (self.square_size + self.square_spacing)
            position = [x_pos, y_pos, 0]
            square_number = self.create_square_number(num, position)
            group.add(square_number)

        return group

    def split_phase(self, arr, left, right, level, x_offset):
        if left == right:
            # Leaf node
            element = self.create_array_group([arr[left]], 2.5 - level * self.level_spacing, x_offset)
            self.levels[level].append((element, left, right))
            self.play(FadeIn(element))
            return

        mid = (left + right) // 2
        curr_arr = arr[left:right + 1]

        # Create current level visualization
        curr_group = self.create_array_group(curr_arr, 2.5 - level * self.level_spacing, x_offset)
        self.levels[level].append((curr_group, left, right))

        if level > 0:  # Don't animate for the initial array
            self.play(FadeIn(curr_group))

        # Calculate offsets for children
        left_size = mid - left + 1
        right_size = right - mid
        left_offset = x_offset - (right_size * (self.square_size + self.square_spacing + self.split_spacing))/2
        right_offset = x_offset + (left_size * (self.square_size + self.square_spacing + self.split_spacing))/2

        # Draw arrows
        start_point = curr_group.get_center() + DOWN * 0.2
        left_end = [left_offset, 2.5 - (level + 1) * self.level_spacing + 0.2, 0]
        right_end = [right_offset, 2.5 - (level + 1) * self.level_spacing + 0.2, 0]

        left_arrow = Arrow(start_point, left_end, color=GRAY, buff=0.3)
        right_arrow = Arrow(start_point, right_end, color=GRAY, buff=0.3)

        self.play(FadeIn(left_arrow), FadeIn(right_arrow))

        # Recursive splits
        self.split_phase(arr, left, mid, level + 1, left_offset)
        self.split_phase(arr, mid + 1, right, level + 1, right_offset)

    def merge_phase(self):
        for level in range(3, -1, -1):
            level_groups = self.levels[level]

            for group, left, right in level_groups:
                if left == right:  # Skip leaf nodes
                    continue

                mid = (left + right) // 2
                left_arr = self.array[left:mid + 1]
                right_arr = self.array[mid + 1:right + 1]

                # Create positions for the merged array
                merged = []
                merged_group = VGroup()
                y_pos = 2.5 - level * self.level_spacing
                x_center = group.get_center()[0]

                # Calculate total width for positioning
                total_width = (right - left + 1) * (self.square_size + self.square_spacing)
                start_x = x_center - total_width/2 + self.square_size/2

                # Merge process
                i = j = merged_idx = 0
                while i < len(left_arr) and j < len(right_arr):
                    if left_arr[i] <= right_arr[j]:
                        number = left_arr[i]
                        i += 1
                    else:
                        number = right_arr[j]
                        j += 1

                    x_pos = start_x + merged_idx * (self.square_size + self.square_spacing)
                    position = [x_pos, y_pos, 0]

                    # Create highlighted square+number and then normal version
                    highlighted = self.create_square_number(number, position, highlighted=True)
                    normal = self.create_square_number(number, position, highlighted=False)

                    if merged_idx == 0:
                        self.play(FadeOut(group))

                    self.play(
                        FadeIn(highlighted),
                        run_time=0.5
                    )
                    self.play(
                        ReplacementTransform(highlighted, normal),
                        run_time=0.5
                    )

                    merged_group.add(normal)
                    merged.append(number)
                    merged_idx += 1

                # Handle remaining elements
                remaining_arr = left_arr[i:] + right_arr[j:]
                for number in remaining_arr:
                    x_pos = start_x + merged_idx * (self.square_size + self.square_spacing)
                    position = [x_pos, y_pos, 0]

                    highlighted = self.create_square_number(number, position, highlighted=True)
                    self.play(FadeIn(highlighted), run_time=0.5)
                    merged_group.add(highlighted)
                    merged.append(number)
                    merged_idx += 1
                # Update the array
                for i, val in enumerate(merged):
                    self.array[left + i] = val

# class MergeSortVisualization(Scene):
#     def construct(self):
#         ms_scene = MergeSortScene()
#         ms_scene.construct()

# if __name__ == "__main__":
#     config.frame_width = 16
#     config.frame_height = 9
#     config.pixel_width = 1920
#     config.pixel_height = 1080
#     with tempconfig({"quality": "production_quality"}):
#         scene = MergeSortVisualization()
#         scene.render()

# python visual.py -ql