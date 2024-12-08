from manim import *

class MergeSort(Scene):
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(self, lst):
        if len(lst) > 1:
            mid = len(lst) // 2
            left_half = self.merge_sort(lst[:mid])
            right_half = self.merge_sort(lst[mid:])
            return self.merge(left_half, right_half)
        return lst

    def construct(self):
        initial_array = [5, 2, 9, 1, 5, 6]
        merge_sort_animation = self.create_merge_sort_animation(initial_array)
        self.play(AnimationGroup(*merge_sort_animation, lag_ratio=1))

    def create_merge_sort_animation(self, array):
        animations = []
        text_group = VGroup(*[Text(str(num)) for num in array]).arrange(RIGHT)
        self.add(text_group)

        def animate_merge_sort(array, text_group):
            if len(array) <= 1:
                return array
            mid = len(array) // 2
            left_half = animate_merge_sort(array[:mid], text_group[:mid])
            right_half = animate_merge_sort(array[mid:], text_group[mid:])
            animations.append(Transform(text_group, VGroup(*left_half, *right_half).arrange(RIGHT)))
            return left_half + right_half

        animate_merge_sort(array, text_group)

        return animations