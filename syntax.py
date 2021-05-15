from manim import *

class EnglishSyntaxTree(Scene):
    def construct(self):
        #####################################################
        # Title of animation                                #
        #####################################################
        title = Text("Syntax: X-bar Theory")
        self.add(title)
        self.wait()
        self.play(Unwrite(title))
        self.wait()

        #####################################################
        # Animate writing of sentence                       #
        #####################################################
        sentence = Tex("Colorless", "green", "ideas", "sleep", "furiously", arg_separator=" ")
        self.play(Write(sentence))
        self.play(sentence.animate.shift(DOWN * 3.5))

        #####################################################
        # Animate tree root layer (S)                       #
        #####################################################
        brace_1S = Brace(sentence, UP)
        label_1S = brace_1S.get_text("S")
        label_1S.add_updater(lambda m: m.set(coord=label_1S.get_coord(2)))
        self.play(
            GrowFromCenter(brace_1S),
            FadeIn(label_1S),
            sentence.animate.set_color(color=TEAL_C)
        )
        self.wait(0.5)
        self.play(
            label_1S.animate.shift(UP),
            ShrinkToCenter(brace_1S)
        )
        node_1S = Dot(point=label_1S.get_center(), radius=0.35, color=BLACK)
        node_1S.add(label_1S)
        tree = Group(node_1S)
        self.wait(0.25)

        #####################################################
        # Animate 2nd tree layer (NP, VP)                   #
        #####################################################
        np2 = Group(sentence[0], sentence[1], sentence[2])
        vp2 = Group(sentence[3], sentence[4])
        brace_2NP = Brace(np2, UP)
        brace_2VP = Brace(vp2, UP)
        label_2NP = brace_2NP.get_text("NP")
        label_2VP = brace_2VP.get_text("VP")
        label_2NP.add_updater(lambda m: m.set(coord=label_2NP.get_coord(2)))
        label_2VP.add_updater(lambda m: m.set(coord=label_2VP.get_coord(2)))
        self.play(
            GrowFromCenter(brace_2NP),
            GrowFromCenter(brace_2VP),
            FadeIn(label_2NP),
            FadeIn(label_2VP),
            np2.animate.set_color(color=RED_C),
            vp2.animate.set_color(color=BLUE_C),
        )
        self.wait(0.25)
        self.play(
            tree.animate.shift(UP),
            label_2NP.animate.shift(UP),
            label_2VP.animate.shift(UP),
            ShrinkToCenter(brace_2NP),
            ShrinkToCenter(brace_2VP)
        )
        node_2NP = Dot(point=label_2NP.get_center(), radius=0.35, color=BLACK)
        node_2VP = Dot(point=label_2VP.get_center(), radius=0.35, color=BLACK)
        node_2NP.add(label_2NP)
        node_2VP.add(label_2VP)
        line_1S_2NP = Line(node_1S.point_at_angle(210 * DEGREES), node_2NP.point_at_angle(90 * DEGREES))
        line_1S_2VP = Line(node_1S.point_at_angle(330 * DEGREES), node_2VP.point_at_angle(90 * DEGREES))
        line_1S_2NP.add_updater(lambda m: m.set(coord=line_1S_2NP.get_coord(2)))
        line_1S_2VP.add_updater(lambda m: m.set(coord=line_1S_2VP.get_coord(2)))
        tree.add(node_2NP, node_2VP, line_1S_2NP, line_1S_2VP)
        self.play(
            Create(line_1S_2NP),
            Create(line_1S_2VP),
        )
        self.wait(0.25)

        #####################################################
        # Animate 3rd tree layer (N', V')                   #
        #####################################################
        np3 = np2
        vp3 = vp2
        brace_3NP = Brace(np3, UP)
        brace_3VP = Brace(vp3, UP)
        label_3NP = brace_3NP.get_text("N'")
        label_3VP = brace_3VP.get_text("V'")
        label_3NP.add_updater(lambda m: m.set(coord=label_3NP.get_coord(2)))
        label_3VP.add_updater(lambda m: m.set(coord=label_3VP.get_coord(2)))
        self.play(
            GrowFromCenter(brace_3NP),
            GrowFromCenter(brace_3VP),
            FadeIn(label_3NP),
            FadeIn(label_3VP),
        )
        self.wait(0.25)
        self.play(
            tree.animate.shift(UP),
            label_3NP.animate.shift(UP),
            label_3VP.animate.shift(UP),
            ShrinkToCenter(brace_3NP),
            ShrinkToCenter(brace_3VP),
        )
        node_3NP = Dot(point=label_3NP.get_center(), radius=0.35, color=BLACK)
        node_3VP = Dot(point=label_3VP.get_center(), radius=0.35, color=BLACK)
        node_3NP.add(label_3NP)
        node_3VP.add(label_3VP)
        line_2NP_3NP = Line(node_2NP.point_at_angle(270 * DEGREES), node_3NP.point_at_angle(90 * DEGREES))
        line_2VP_3VP = Line(node_2VP.point_at_angle(270 * DEGREES), node_3VP.point_at_angle(90 * DEGREES))
        line_2NP_3NP.add_updater(lambda m: m.set(coord=line_2NP_3NP.get_coord(2)))
        line_2VP_3VP.add_updater(lambda m: m.set(coord=line_2VP_3VP.get_coord(2)))
        tree.add(node_3NP, node_3VP, line_2NP_3NP, line_2VP_3VP)
        self.play(
            Create(line_2NP_3NP),
            Create(line_2VP_3VP),
        )
        self.wait(0.25)

        #####################################################
        # Animate 4th tree layer (AdjP, N', V', AdvP)       #
        #####################################################
        # Split N' to AdjP and N'
        brace_4AdjP = Brace(sentence[0], UP)
        brace_4NP = Brace(Group(sentence[1], sentence[2]), UP)
        label_4AdjP = brace_4AdjP.get_text("AdjP")
        label_4NP = brace_4NP.get_text("N'")
        label_4AdjP.add_updater(lambda m: m.set(coord=label_4AdjP.get_coord(2)))
        label_4NP.add_updater(lambda m: m.set(coord=label_4NP.get_coord(2)))
        # Split V' to V' and AdvP
        brace_4VP = Brace(sentence[3], UP)
        brace_4AdvP = Brace(sentence[4], UP)
        label_4VP = brace_4VP.get_text("V'")
        label_4AdvP = brace_4AdvP.get_text("AdvP")
        label_4VP.add_updater(lambda m: m.set(coords=label_4VP.get_coord(2)))
        label_4AdvP.add_updater(lambda m: m.set(coords=label_4AdvP.get_coord(2)))
        self.play(
            # Left branch
            GrowFromCenter(brace_4AdjP),
            GrowFromCenter(brace_4NP),
            FadeIn(label_4AdjP),
            FadeIn(label_4NP),
            sentence[0].animate.set_color(color=GOLD_C),
            # Right branch
            GrowFromCenter(brace_4VP),
            GrowFromCenter(brace_4AdvP),
            FadeIn(label_4VP),
            FadeIn(label_4AdvP),
            sentence[4].animate.set_color(color=PURPLE_C)
        )
        self.wait(0.25)
        self.play(
            tree.animate.shift(UP),
            # Left branch
            label_4AdjP.animate.shift(UP),
            label_4NP.animate.shift(UP),
            ShrinkToCenter(brace_4AdjP),
            ShrinkToCenter(brace_4NP),
            # Right branch
            label_4VP.animate.shift(UP),
            label_4AdvP.animate.shift(UP),
            ShrinkToCenter(brace_4VP),
            ShrinkToCenter(brace_4AdvP),
        )
        # Left branch
        node_4AdjP = Dot(point=label_4AdjP.get_center(), radius=0.35, color=BLACK)
        node_4NP = Dot(point=label_4NP.get_center(), radius=0.35, color=BLACK)
        node_4AdjP.add(label_4AdjP)
        node_4NP.add(label_4NP)
        line_3NP_4AdjP = Line(node_3NP.point_at_angle(210 * DEGREES), node_4AdjP.point_at_angle(90 * DEGREES))
        line_3NP_4NP = Line(node_3NP.point_at_angle(330 * DEGREES), node_4NP.point_at_angle(90 * DEGREES))
        line_3NP_4AdjP.add_updater(lambda m: m.set(coord=line_3NP_4AdjP.get_coord(2)))
        line_3NP_4NP.add_updater(lambda m: m.set(coord=line_3NP_4NP.get_coord(2)))
        # Right branch
        node_4VP = Dot(point=label_4VP.get_center(), radius=0.35, color=BLACK)
        node_4AdvP = Dot(point=label_4AdvP.get_center(), radius=0.35, color=BLACK)
        node_4VP.add(label_4VP)
        node_4AdvP.add(label_4AdvP)
        line_3VP_4VP = Line(node_3VP.point_at_angle(210 * DEGREES), node_4VP.point_at_angle(90 * DEGREES))
        line_3VP_4AdvP = Line(node_3VP.point_at_angle(330 * DEGREES), node_4AdvP.point_at_angle(90 * DEGREES))
        line_3VP_4VP.add_updater(lambda m: m.set(coord=line_3VP_4VP.get_coord(2)))
        line_3VP_4AdvP.add_updater(lambda m: m.set(coord=line_3VP_4AdvP.get_coord(2)))
        tree.add(
            node_4AdjP, node_4NP, line_3NP_4AdjP, line_3NP_4NP,
            node_4VP, node_4AdvP, line_3VP_4VP, line_3VP_4AdvP
        )
        self.play(
            Create(line_3NP_4AdjP),
            Create(line_3NP_4NP),
            Create(line_3VP_4VP),
            Create(line_3VP_4AdvP),
        )
        self.wait(0.25)

        #####################################################
        # Animate 5th tree layer (Adj', AdjP, N', V, Adv')  #
        #####################################################
        brace_5AdjP = Brace(sentence[0], UP)
        brace_5NP_AdjP = Brace(sentence[1], UP)
        brace_5NP = Brace(sentence[2], UP)
        brace_5V = Brace(sentence[3], UP)
        brace_5AdvP = Brace(sentence[4], UP)
        label_5AdjP = brace_5AdjP.get_text("Adj'")
        label_5NP_AdjP = brace_5NP_AdjP.get_text("AdjP")
        label_5NP = brace_5NP.get_text("N'")
        label_5V = brace_5V.get_text("V")
        label_5AdvP = brace_5AdvP.get_text("Adv'")
        label_5AdjP.add_updater(lambda m: m.set(coord=label_5AdjP.get_coord(2)))
        label_5NP_AdjP.add_updater(lambda m: m.set(coord=label_5NP_AdjP.get_coord(2)))
        label_5NP.add_updater(lambda m: m.set(coord=label_5NP.get_coord(2)))
        label_5V.add_updater(lambda m: m.set(coord=label_5V.get_coord(2)))
        label_5AdvP.add_updater(lambda m: m.set(coord=label_5AdvP.get_coord(2)))
        self.play(
            GrowFromCenter(brace_5AdjP),
            GrowFromCenter(brace_5NP_AdjP),
            GrowFromCenter(brace_5NP),
            GrowFromCenter(brace_5V),
            GrowFromCenter(brace_5AdvP),
            FadeIn(label_5AdjP),
            FadeIn(label_5NP_AdjP),
            FadeIn(label_5NP),
            FadeIn(label_5V),
            FadeIn(label_5AdvP),
            sentence[1].animate.set_color(color=GREEN_C)
        )
        self.wait(0.25)
        self.play(
            tree.animate.shift(UP),
            label_5AdjP.animate.shift(UP),
            label_5NP_AdjP.animate.shift(UP),
            label_5NP.animate.shift(UP),
            label_5V.animate.shift(UP),
            sentence[3].animate.shift(UP),
            label_5AdvP.animate.shift(UP),
            ShrinkToCenter(brace_5AdjP),
            ShrinkToCenter(brace_5NP_AdjP),
            ShrinkToCenter(brace_5NP),
            brace_5V.animate.shift(UP),
            ShrinkToCenter(brace_5AdvP),
        )
        node_5AdjP = Dot(point=label_5AdjP.get_center(), radius=0.35, color=BLACK)
        node_5NP_AdjP = Dot(point=label_5NP_AdjP.get_center(), radius=0.35, color=BLACK)
        node_5NP = Dot(point=label_5NP.get_center(), radius=0.35, color=BLACK)
        node_5V = Dot(point=label_5V.get_center(), radius=0.35, color=BLACK)
        node_5AdvP = Dot(point=label_5AdvP.get_center(), radius=0.35, color=BLACK)
        node_5AdjP.add(label_5AdjP)
        node_5NP_AdjP.add(label_5NP_AdjP)
        node_5NP.add(label_5NP)
        node_5V.add(label_5V)
        node_5AdvP.add(label_5AdvP)
        line_4AdjP_5AdjP = Line(node_4AdjP.point_at_angle(270 * DEGREES), node_5AdjP.point_at_angle(90 * DEGREES))
        line_4NP_5NP_AdjP = Line(node_4NP.point_at_angle(210 * DEGREES), node_5NP_AdjP.point_at_angle(90 * DEGREES))
        line_4NP_5NP = Line(node_4NP.point_at_angle(330 * DEGREES), node_5NP.point_at_angle(90 * DEGREES))
        line_4VP_5V = Line(node_4VP.point_at_angle(270 * DEGREES), node_5V.point_at_angle(90 * DEGREES))
        line_4AdvP_5AdvP = Line(node_4AdvP.point_at_angle(270 * DEGREES), node_5AdvP.point_at_angle(90 * DEGREES))
        tree.add(
            node_5AdjP, node_5NP_AdjP, node_5NP, node_5V, node_5AdvP, sentence[3], brace_5V,
            line_4AdjP_5AdjP, line_4NP_5NP_AdjP, line_4NP_5NP, line_4VP_5V, line_4AdvP_5AdvP
        )
        self.play(
            Create(line_4AdjP_5AdjP),
            Create(line_4NP_5NP_AdjP),
            Create(line_4NP_5NP),
            Create(line_4VP_5V),
            Create(line_4AdvP_5AdvP)
        )
        self.wait(0.25)

        #####################################################
        # Animate 6th tree layer (Adj, Adj', N, Adv)        #
        #####################################################
        brace_6Adj = Brace(sentence[0], UP)
        brace_6AdjP = Brace(sentence[1], UP)
        brace_6N = Brace(sentence[2], UP)
        brace_6Adv = Brace(sentence[4], UP)
        label_6Adj = brace_6Adj.get_text("Adj")
        label_6AdjP = brace_6AdjP.get_text("Adj'")
        label_6N = brace_6N.get_text("N")
        label_6Adv = brace_6Adv.get_text("Adv")
        label_6Adj.add_updater(lambda m: m.set(coord=label_6Adj.get_coord(2)))
        label_6AdjP.add_updater(lambda m: m.set(coord=label_6AdjP.get_coord(2)))
        label_6N.add_updater(lambda m: m.set(coord=label_6N.get_coord(2)))
        label_6Adv.add_updater(lambda m: m.set(coord=label_6Adv.get_coord(2)))
        self.play(
            GrowFromCenter(brace_6Adj),
            GrowFromCenter(brace_6AdjP),
            GrowFromCenter(brace_6N),
            GrowFromCenter(brace_6Adv),
            FadeIn(label_6Adj),
            FadeIn(label_6AdjP),
            FadeIn(label_6N),
            FadeIn(label_6Adv)
        )
        self.wait(0.25)
        self.play(
            tree.animate.shift(UP),
            label_6Adj.animate.shift(UP),
            sentence[0].animate.shift(UP),
            label_6AdjP.animate.shift(UP),
            label_6N.animate.shift(UP),
            sentence[2].animate.shift(UP),
            label_6Adv.animate.shift(UP),
            sentence[4].animate.shift(UP),
            brace_6Adj.animate.shift(UP),
            ShrinkToCenter(brace_6AdjP),
            brace_6N.animate.shift(UP),
            brace_6Adv.animate.shift(UP)
        )
        node_6Adj = Dot(point=label_6Adj.get_center(), radius=0.35, color=BLACK)
        node_6AdjP = Dot(point=label_6AdjP.get_center(), radius=0.35, color=BLACK)
        node_6N = Dot(point=label_6N.get_center(), radius=0.35, color=BLACK)
        node_6Adv = Dot(point=label_6Adv.get_center(), radius=0.35, color=BLACK)
        node_6Adj.add(label_6Adj)
        node_6AdjP.add(label_6AdjP)
        node_6N.add(label_6N)
        node_6Adv.add(label_6Adv)
        line_5AdjP_6Adj = Line(node_5AdjP.point_at_angle(270 * DEGREES), node_6Adj.point_at_angle(90 * DEGREES))
        line_5NP_AdjP_6AdjP = Line(node_5NP_AdjP.point_at_angle(270 * DEGREES), node_6AdjP.point_at_angle(90 * DEGREES))
        line_5NP_6N = Line(node_5NP.point_at_angle(270 * DEGREES), node_6N.point_at_angle(90 * DEGREES))
        line_5AdvP_6Adv = Line(node_5AdvP.point_at_angle(270 * DEGREES), node_6Adv.point_at_angle(90 * DEGREES))
        tree.add(
            node_6Adj, node_6AdjP, node_6N, node_6Adv, sentence[0], sentence[2], sentence[4], brace_6Adj,
            brace_6N, brace_6Adv, line_5AdjP_6Adj, line_5NP_AdjP_6AdjP, line_5NP_6N, line_5AdvP_6Adv
        )
        self.play(
            Create(line_5AdjP_6Adj),
            Create(line_5NP_AdjP_6AdjP),
            Create(line_5NP_6N),
            Create(line_5AdvP_6Adv)
        )
        self.wait(0.25)

        #####################################################
        # Animate 7th tree layer (Adj)                      #
        #####################################################
        brace_7Adj = Brace(sentence[1], UP)
        label_7Adj = brace_7Adj.get_text("Adj")
        self.play(
            GrowFromCenter(brace_7Adj),
            FadeIn(label_7Adj)
        )
        self.wait(0.25)
        node_7Adj = Dot(point=label_7Adj.get_center(), radius=0.35, color=BLACK)
        node_7Adj.add(label_7Adj)
        line_6AdjP_7Adj = Line(node_6AdjP.point_at_angle(270 * DEGREES), node_7Adj.point_at_angle(90 * DEGREES))
        tree.add(node_7Adj, line_6AdjP_7Adj, sentence[1], brace_7Adj)
        self.play(Create(line_6AdjP_7Adj))
        self.wait()