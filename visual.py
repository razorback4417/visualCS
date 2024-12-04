from manim import *

class MergeSortScene(Scene):
    def construct(self):
        # Configuration
        self.array = [3, 5, 4, 2, 6]
        self.square_size = 0.7
        self.square_spacing = 0.2
        self.level_spacing = 1.2  # Vertical space between levels
        self.split_spacing = 0.8  # Extra horizontal space between split groups

        # Initial setup
        self.camera.background_color = "#2D3436"
        title = Text("Merge Sort", color=WHITE).to_edge(UP, buff=0.5)
        self.add(title)

        # Create and show initial array
        initial_squares = self.create_array_group(self.array, 3)
        initial_text = Text("Initial Array:", color=WHITE).scale(0.7)
        initial_text.next_to(initial_squares, UP, buff=0.3)
        self.add(initial_text)
        self.play(Create(initial_squares))
        self.wait(0.5)

        # Perform merge sort visualization
        self.merge_sort_animate(self.array, 0, len(self.array)-1, 3, 0)
        self.wait(1)

        # Final text
        final_text = Text("Array Sorted", color=GREEN).scale(0.7)
        final_text.to_edge(DOWN, buff=0.5)
        self.add(final_text)
        self.wait(1)

    def create_array_group(self, arr, y_pos, x_offset=0):
        group = VGroup()
        total_width = len(arr) * (self.square_size + self.square_spacing)
        start_x = x_offset - total_width/2 + self.square_size/2

        for i, num in enumerate(arr):
            square = Square(
                side_length=self.square_size,
                color=BLUE,
                fill_opacity=0.3
            )
            x_pos = start_x + i * (self.square_size + self.square_spacing)
            square.move_to([x_pos, y_pos, 0])

            number = Text(str(num), color=WHITE).scale(0.6)
            number.move_to(square.get_center())

            group.add(VGroup(square, number))

        return group
    def merge_sort_animate(self, arr, left, right, y_pos, x_offset):
        if left == right:
            # Single element - just create and show it
            element = self.create_array_group([arr[left]], y_pos, x_offset)
            self.play(Create(element))
            return element, [arr[left]]

        # Calculate middle point
        mid = (left + right) // 2

        # Calculate positions for split arrays
        left_size = mid - left + 1
        right_size = right - mid

        # Calculate x_offsets for left and right subarrays
        left_offset = x_offset - (right_size * (self.square_size + self.square_spacing + self.split_spacing))/2
        right_offset = x_offset + (left_size * (self.square_size + self.square_spacing + self.split_spacing))/2

        # Create arrows to show splitting
        start_point = [x_offset, y_pos, 0]
        left_end = [left_offset, y_pos - self.level_spacing, 0]
        right_end = [right_offset, y_pos - self.level_spacing, 0]

        left_arrow = Arrow(start_point, left_end, color=GRAY)
        right_arrow = Arrow(start_point, right_end, color=GRAY)

        self.play(Create(left_arrow), Create(right_arrow))

        # Recursive calls with new positions
        left_group, left_sorted = self.merge_sort_animate(
            arr, left, mid,
            y_pos - self.level_spacing,
            left_offset
        )

        right_group, right_sorted = self.merge_sort_animate(
            arr, mid + 1, right,
            y_pos - self.level_spacing,
            right_offset
        )

        # Merge step
        merged = []
        i = j = 0
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] <= right_sorted[j]:
                merged.append(left_sorted[i])
                i += 1
            else:
                merged.append(right_sorted[j])
                j += 1

        while i < len(left_sorted):
            merged.append(left_sorted[i])
            i += 1

        while j < len(right_sorted):
            merged.append(right_sorted[j])
            j += 1

        # Create merged array visualization
        merged_group = self.create_array_group(merged, y_pos, x_offset)
        self.play(
            Create(merged_group),
            run_time=1
        )

        return merged_group, merged

class MergeSortVisualization(Scene):
    def construct(self):
        ms_scene = MergeSortScene()
        ms_scene.construct()

if __name__ == "__main__":
    config.frame_width = 16
    config.frame_height = 9
    config.pixel_width = 1920
    config.pixel_height = 1080
    with tempconfig({"quality": "production_quality"}):
        scene = MergeSortVisualization()
        scene.render()