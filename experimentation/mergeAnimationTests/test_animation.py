from manim import *

class MergeSortAnimation(Scene):
    def construct(self):
        # Initial array to sort
        array = [38, 27, 43, 3, 9, 82, 10]
        # Move origin up to allow space for downward splits
        self.origin = UP * 2

        # Create and display the array
        array_mob = self.create_array_mob(array)
        # Scale down the entire visualization to ensure it fits
        array_mob.scale(0.7)
        self.play(FadeIn(array_mob))
        self.wait(1)

        # Start the merge sort animation
        self.merge_sort(array, array_mob, self.origin)

    def create_array_mob(self, array):
        """Creates a VGroup of squares with numbers."""
        array_mob = VGroup()
        for i, value in enumerate(array):
            square = Square(side_length=1)
            num = Text(str(value), font_size=36)
            num.move_to(square.get_center())
            square_group = VGroup(square, num)
            # Center the array horizontally
            square_group.move_to(self.origin + RIGHT * (i - len(array)/2 + 0.5))
            array_mob.add(square_group)
        return array_mob

    def merge_sort(self, array, array_mob, position):
        if len(array) > 1:
            mid = len(array) // 2
            left_array = array[:mid]
            right_array = array[mid:]

            left_mob = array_mob[:mid]
            right_mob = array_mob[mid:]

            # Highlight the left and right subarrays
            self.play(left_mob.animate.set_color(BLUE))
            self.play(right_mob.animate.set_color(GREEN))
            self.wait(0.5)

            # Recursively sort the left half - moving DOWN instead of UP
            left_target_pos = position + DOWN*1.5 - RIGHT*(len(left_array)/2)
            self.play(left_mob.animate.move_to(left_target_pos))
            self.merge_sort(left_array, left_mob, left_target_pos)

            # Recursively sort the right half - moving DOWN instead of UP
            right_target_pos = position + DOWN*1.5 + RIGHT*(len(right_array)/2)
            self.play(right_mob.animate.move_to(right_target_pos))
            self.merge_sort(right_array, right_mob, right_target_pos)

            # Merge the sorted halves
            self.play(left_mob.animate.set_color(WHITE))
            self.play(right_mob.animate.set_color(WHITE))
            self.merge(array, left_array, right_array, array_mob, left_mob, right_mob, position)
        else:
            # Base case: single element is already sorted
            self.play(array_mob.animate.move_to(position))
            self.wait(0.5)

    def merge(self, array, left_array, right_array, array_mob, left_mob, right_mob, position):
        i = j = k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                array_mob[k] = left_mob[i]
                i += 1
            else:
                array[k] = right_array[j]
                array_mob[k] = right_mob[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(left_array):
            array[k] = left_array[i]
            array_mob[k] = left_mob[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            array_mob[k] = right_mob[j]
            j += 1
            k += 1

        # Animate merging arrays back together
        for idx, mob in enumerate(array_mob):
            # Center the merged array horizontally
            target_pos = position + RIGHT * (idx - len(array_mob)/2 + 0.5)
            self.play(mob.animate.move_to(target_pos), run_time=0.5)
        self.wait(0.5)