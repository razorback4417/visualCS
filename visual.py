from manim import *

class ArrayItem:
    def __init__(self, value):
        self.value = value
        self.square = Square(side_length=1)
        self.text = Integer(value)

class Thumbnail(Scene):
    def construct(self):

        title = Title("Sorting algorithms 2:")
        subtitle = Text("Selection sort", font_size=90)

        self.add(title)
        self.add(subtitle)

class Intro(Scene):
    def construct(self):

        title = Text("Selection sort")

        self.play(Write(title))
        self.wait(1)
        self.play(Unwrite(title, reverse=False))

class Sort(Scene):
    def construct(self):
        # initialize the array
        data = [2,3,1,4,7,6,5,9,8]

        # transform the array into ArrayItems
        dArray = []
        for el in data:
            dArray.append(ArrayItem(el))

        # create the VGroup for Manim rendering
        gArray = VGroup()
        # add the squares
        for el in dArray:
            gArray.add(VGroup().add_to_back(el.square).add(el.text))
        # arrange them
        gArray.arrange(buff=0)
        # add the texts
        #for el in range(len(dArray)):
            #gArray.add(dArray[el].text.align_to(dArray[el].square))

        self.play(Write(gArray, lag_ratio=0.1))
        self.wait(1)

        # sort
        for i in range(len(dArray)-1):
            self.play(dArray[i].square.animate(run_time=0.3).set_fill(GREEN, opacity=0.3))
            min_id = i
            for j in range(i+1,len(dArray)):
                self.play(dArray[j].square.animate(run_time=0.3).set_fill(BLUE, opacity=0.3))
                if dArray[j].value < dArray[min_id].value:
                    if min_id != i:
                        self.play(AnimationGroup(dArray[j].square.animate(run_time=0.3).set_fill(GREEN, opacity=0.3),
                                             dArray[min_id].square.animate(run_time=0.3).set_fill(GREEN, opacity=0)))
                    else:
                        self.play(dArray[j].square.animate(run_time=0.3).set_fill(GREEN, opacity=0.3))
                    min_id = j
                    continue
                self.play(dArray[j].square.animate(run_time=0.3).set_fill(BLUE, opacity=0))
            dArray[i].value, dArray[min_id].value = dArray[min_id].value, dArray[i].value
            if min_id != i:
                auxMin = gArray[min_id].copy()
                auxI = gArray[i].copy()
                self.play(AnimationGroup(Transform(gArray[i],auxMin.match_x(gArray[i]), run_time=0.3),
                                         Transform(gArray[min_id],auxI.match_x(gArray[min_id]), run_time=0.3)))
                self.play(AnimationGroup(dArray[i].square.animate(run_time=0.3).set_fill(GREEN, opacity=0),
                                             dArray[min_id].square.animate(run_time=0.3).set_fill(GREEN, opacity=0)))
            else:
                self.play(dArray[i].square.animate(run_time=0.3).set_fill(GREEN, opacity=0))

        self.wait(1)
        self.play(Unwrite(gArray, lag_ratio=0.1, reverse=False))

class SortWithDuplicates(Scene):
    def construct(self):
        # initialize the array
        data = [1,3,3,2,5]

        # transform the array into ArrayItems
        dArray = []
        for el in data:
            dArray.append(ArrayItem(el))

        # create the VGroup for Manim rendering
        gArray = VGroup()
        # add the squares
        for el in dArray:
            gArray.add(VGroup().add_to_back(el.square).add(el.text))
        # arrange them
        gArray.arrange(buff=0)
        # add the texts
        #for el in range(len(dArray)):
            #gArray.add(dArray[el].text.align_to(dArray[el].square))

        self.play(Write(gArray, lag_ratio=0.1))
        self.wait(1)

        # sort
        for i in range(len(dArray)-1):
            self.play(dArray[i].square.animate(run_time=0.3).set_fill(GREEN, opacity=0.3))
            min_id = i
            for j in range(i+1,len(dArray)):
                self.play(dArray[j].square.animate(run_time=0.3).set_fill(BLUE, opacity=0.3))
                if dArray[j].value < dArray[min_id].value:
                    if min_id != i:
                        self.play(AnimationGroup(dArray[j].square.animate(run_time=0.3).set_fill(GREEN, opacity=0.3),
                                             dArray[min_id].square.animate(run_time=0.3).set_fill(GREEN, opacity=0)))
                    else:
                        self.play(dArray[j].square.animate(run_time=0.3).set_fill(GREEN, opacity=0.3))
                    min_id = j
                    continue
                self.play(dArray[j].square.animate(run_time=0.3).set_fill(BLUE, opacity=0))
            dArray[i].value, dArray[min_id].value = dArray[min_id].value, dArray[i].value
            if min_id != i:
                auxMin = gArray[min_id].copy()
                auxI = gArray[i].copy()
                self.play(AnimationGroup(Transform(gArray[i],auxMin.match_x(gArray[i]), run_time=0.3),
                                         Transform(gArray[min_id],auxI.match_x(gArray[min_id]), run_time=0.3)))
                self.play(AnimationGroup(dArray[i].square.animate(run_time=0.3).set_fill(GREEN, opacity=0),
                                             dArray[min_id].square.animate(run_time=0.3).set_fill(GREEN, opacity=0)))
            else:
                self.play(dArray[i].square.animate(run_time=0.3).set_fill(GREEN, opacity=0))

        self.wait(1)
        self.play(Unwrite(gArray, lag_ratio=0.1, reverse=False))

class DrawCode(Scene):
    def construct(self):
        listing = Code(
            "code/selection_sort.py",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=False,
            style="github-dark",
            background="window",
            language="py",
            font_size=24,
        )

        self.play(Write(listing))
        self.wait(1)