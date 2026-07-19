"""Episode 1.2 — What Is Cosmochrony Trying to Explain? (redesigned).

Programme-level overview: the research question, the three levels of consequence,
and an honest epistemic map.  Drop-in replacement for
``what_is_cosmochrony_trying_to_explain.py``.  Requires ``cosmochrony_style.py``
alongside it, plus ``narration.py`` and ``edge_tts_service.py``.

Scientific guardrails preserved from the brief: this is a research programme, not a
finished theory; spectral admissibility is a *selection* principle; downstream
identifications remain conditional or open; no claim of a common experimental origin.
"""

from __future__ import annotations

import numpy as np
from manim import (
    Arrow,
    Circle,
    Create,
    DashedLine,
    Dot,
    DOWN,
    FadeIn,
    FadeOut,
    GrowFromCenter,
    LaggedStart,
    LEFT,
    Line,
    MathTex,
    ORIGIN,
    Rectangle,
    RIGHT,
    RoundedRectangle,
    UP,
    VGroup,
    Write,
)
from manim_voiceover import VoiceoverScene

from cosmochrony_style import (
    AMBER,
    CORAL,
    CYAN,
    FOREGROUND,
    GREEN,
    MUTED,
    STRUCTURE,
    VIOLET,
    kicker,
    reveal_words,
    serif,
    theory_vignette,
    type_on,
    type_sentence,
)
from edge_tts_service import EdgeTTSService
from narration import NARRATION

DOMAINS = (
    ("psi", CYAN, r"\psi", "quantum states"),
    ("grid", VIOLET, r"g_{\mu\nu}", "curved spacetime"),
    ("gauge", CORAL, r"A_\mu", "gauge forces"),
    ("matter", GREEN, r"\bar{\psi}\psi", "matter"),
)


def make_card(title: str, detail: str, colour: str, width: float = 2.9, height: float = 1.3) -> VGroup:
    box = RoundedRectangle(corner_radius=0.16, width=width, height=height, color=colour,
                           stroke_width=2.0, fill_color=colour, fill_opacity=0.08)
    heading = serif(title, size=27, bold=True).scale_to_fit_width(min(width - 0.5, max(0.1, len(title) * 0.22)))
    caption = serif(detail, size=18, color=MUTED)
    if caption.width > width - 0.5:
        caption.scale_to_fit_width(width - 0.5)
    content = VGroup(heading, caption).arrange(DOWN, buff=0.14).move_to(box)
    return VGroup(box, content)


def make_heading(kick: str, title: str) -> VGroup:
    top = kicker(kick, size=22)
    main = serif(title, size=43, bold=True)
    if main.width > 12.0:
        main.scale_to_fit_width(12.0)
    return VGroup(top, main).arrange(DOWN, buff=0.14).to_edge(UP, buff=0.4)


def make_network(center: np.ndarray, scale: float = 1.0, colour: str = CYAN) -> VGroup:
    coords = ((-1.30, 0.80), (-0.35, 1.32), (0.75, 1.02), (1.35, 0.10),
              (0.68, -0.85), (-0.42, -1.05), (-1.38, -0.35), (0.00, 0.18))
    edges = ((0, 1), (0, 6), (0, 7), (1, 2), (1, 7), (2, 3), (2, 7), (3, 4), (3, 7),
             (4, 5), (4, 7), (5, 6), (5, 7), (6, 7))
    positions = [center + scale * np.array([x, y, 0.0]) for x, y in coords]
    lines = VGroup(*[Line(positions[a], positions[b], color=STRUCTURE, stroke_width=2.0,
                          stroke_opacity=0.78) for a, b in edges])
    nodes = VGroup(*[Dot(p, radius=0.075 * scale, color=colour).set_stroke(FOREGROUND, width=1.0)
                     for p in positions])
    return VGroup(lines, nodes)


class WhatIsCosmochronyTryingToExplain(VoiceoverScene):
    """Question, layers, scope, and epistemic status of the programme — redesigned."""

    def construct(self) -> None:
        self.set_speech_service(EdgeTTSService(voice="en-GB-RyanNeural"))
        self.scene_domains()
        self.scene_question()
        self.scene_projection()
        self.scene_foundations()
        self.scene_spectra()
        self.scene_physics()
        self.scene_status()
        self.scene_closing()

    # ------------------------------------------------------------------ domains
    def scene_domains(self) -> None:
        badge = kicker("Modern physics", size=24)
        subtitle = serif("Powerful theories, separate foundations", size=44, bold=True)
        head = VGroup(badge, subtitle).arrange(DOWN, buff=0.14).to_edge(UP, buff=0.5)

        columns = []
        for kind, colour, formula, label in DOMAINS:
            column, graphic, formula_mob, label_mob = theory_vignette(kind, colour, formula, label)
            columns.append((column, graphic, formula_mob, label_mob))
        row = VGroup(*[c[0] for c in columns]).arrange(RIGHT, buff=0.9).shift(0.35 * DOWN)

        with self.voiceover(text=NARRATION["opening"]) as tracker:
            self.play(FadeIn(badge, shift=0.15 * DOWN), run_time=tracker.duration * 0.10)
            type_on(self, subtitle, run_time=tracker.duration * 0.20)
            per = tracker.duration * 0.62 / len(columns)
            for _column, graphic, formula_mob, label_mob in columns:
                # a theory graphic appears as ONE unit, then its formula, then its label
                self.play(FadeIn(graphic), run_time=per * 0.5)
                self.play(FadeIn(formula_mob, shift=0.08 * UP), run_time=per * 0.22)
                type_on(self, label_mob, run_time=per * 0.28)
            self.wait(tracker.duration * 0.08)
        self.play(FadeOut(VGroup(head, row)), run_time=0.55)

    # ----------------------------------------------------------------- question
    def scene_question(self) -> None:
        head = make_heading("The programme question", "Could one deeper description underlie them?")

        positions = (3.9 * LEFT + 1.5 * UP, 3.9 * RIGHT + 1.5 * UP,
                     3.9 * LEFT + 1.6 * DOWN, 3.9 * RIGHT + 1.6 * DOWN)
        minis = []
        for (kind, colour, formula, label), pos in zip(DOMAINS, positions):
            column, graphic, formula_mob, label_mob = theory_vignette(kind, colour, formula, label)
            column.scale(0.62).move_to(pos)
            minis.append((column, colour))

        centre = 0.15 * DOWN
        ring_a = Circle(radius=1.05, color=CYAN, stroke_width=2.2, stroke_opacity=0.6).move_to(centre)
        ring_b = Circle(radius=0.72, color=VIOLET, stroke_width=1.6, stroke_opacity=0.5).move_to(centre)
        mark = serif("?", size=120, bold=True).move_to(centre)

        connectors = VGroup(
            *[DashedLine(column.get_center(), centre, color=STRUCTURE, stroke_opacity=0.55,
                         dash_length=0.09) for column, _ in minis]
        )

        with self.voiceover(text=NARRATION["question"]) as tracker:
            self.play(FadeIn(head, shift=0.12 * UP), run_time=tracker.duration * 0.16)
            per = tracker.duration * 0.44 / len(minis)
            for column, _ in minis:
                self.play(FadeIn(column), run_time=per)
            self.play(
                LaggedStart(*[Create(c) for c in connectors], lag_ratio=0.12),
                run_time=tracker.duration * 0.18,
            )
            self.play(Create(ring_a), Create(ring_b), FadeIn(mark, scale=0.6),
                      run_time=tracker.duration * 0.16)
            self.wait(tracker.duration * 0.06)
        self.play(FadeOut(VGroup(head, *[m[0] for m in minis], connectors, ring_a, ring_b, mark)),
                  run_time=0.55)

    # ---------------------------------------------------------------- projection
    def scene_projection(self) -> None:
        head = make_heading("After Episode 1.1", "From a foundational result to a research programme")
        established = make_card("Established input", "genuine emergence needs non-injectivity",
                                CYAN, width=4.3, height=1.6).move_to(3.5 * LEFT + 0.3 * UP)
        nxt = make_card("Next question", "what else follows, and under which hypotheses?",
                        VIOLET, width=4.3, height=1.6).move_to(3.5 * RIGHT + 0.3 * UP)
        arrow = Arrow(established.get_right(), nxt.get_left(), buff=0.18, color=FOREGROUND, stroke_width=4)
        take = kicker("Take as given", size=16)
        if take.width > arrow.get_length() * 0.85:
            take.scale_to_fit_width(arrow.get_length() * 0.85)
        take.next_to(arrow, UP, buff=0.22)

        chips = VGroup()
        for text, colour in (("FORCED", GREEN), ("CONDITIONAL", AMBER), ("OPEN", CORAL)):
            box = RoundedRectangle(corner_radius=0.14, width=2.6, height=0.8, color=colour,
                                   stroke_width=2.0, fill_color=colour, fill_opacity=0.08)
            chips.add(VGroup(box, serif(text, size=22, bold=True).move_to(box)))
        chips.arrange(RIGHT, buff=0.55).to_edge(DOWN, buff=0.7)
        chip_caption = serif("The programme separates these three outcomes", size=22,
                             color=MUTED).next_to(chips, UP, buff=0.26)

        with self.voiceover(text=NARRATION["projection"]) as tracker:
            self.play(FadeIn(head, shift=0.12 * UP), run_time=tracker.duration * 0.14)
            self.play(FadeIn(established, shift=0.14 * UP), run_time=tracker.duration * 0.18)
            self.play(Create(arrow), FadeIn(take), run_time=tracker.duration * 0.14)
            self.play(FadeIn(nxt, shift=0.14 * RIGHT), run_time=tracker.duration * 0.18)
            self.play(FadeIn(chip_caption), run_time=tracker.duration * 0.10)
            self.play(LaggedStart(*[FadeIn(c, shift=0.1 * UP) for c in chips], lag_ratio=0.2),
                      run_time=tracker.duration * 0.20)
            self.wait(tracker.duration * 0.06)
        self.play(FadeOut(VGroup(head, established, nxt, arrow, take, chips, chip_caption)),
                  run_time=0.55)

    # --------------------------------------------------------------- foundations
    def scene_foundations(self) -> None:
        head = make_heading("Level I · Structural foundations", "What does unresolved distinction force?")
        cards = VGroup(
            make_card("Admissible transitions", "explicit axioms", CYAN, width=3.1),
            make_card("Non-commuting generators", "unresolved fibres", VIOLET, width=3.1),
            make_card("Finite Heisenberg structure", "proved in stated settings", GREEN, width=3.1),
        ).arrange(RIGHT, buff=0.65).shift(0.2 * UP)
        arrows = VGroup(
            Arrow(cards[0].get_right(), cards[1].get_left(), buff=0.1, color=MUTED, stroke_width=3),
            Arrow(cards[1].get_right(), cards[2].get_left(), buff=0.1, color=MUTED, stroke_width=3),
        )
        bridge = make_card("Continuum & physical identification",
                           "a separate bridge, not part of the proved chain", AMBER,
                           width=4.9, height=1.2).to_edge(DOWN, buff=0.55)
        bridge_line = DashedLine(cards[2].get_bottom(), bridge.get_top(), color=AMBER, stroke_opacity=0.75)

        with self.voiceover(text=NARRATION["foundations"]) as tracker:
            self.play(FadeIn(head, shift=0.12 * UP), run_time=tracker.duration * 0.14)
            self.play(FadeIn(cards[0], shift=0.12 * UP), run_time=tracker.duration * 0.16)
            self.play(Create(arrows[0]), FadeIn(cards[1], shift=0.12 * RIGHT), run_time=tracker.duration * 0.18)
            self.play(Create(arrows[1]), FadeIn(cards[2], shift=0.12 * RIGHT), run_time=tracker.duration * 0.18)
            self.play(Create(bridge_line), FadeIn(bridge), run_time=tracker.duration * 0.16)
            self.wait(tracker.duration * 0.1)
        self.play(FadeOut(VGroup(head, cards, arrows, bridge, bridge_line)), run_time=0.55)

    # ------------------------------------------------------------------ spectra
    def scene_spectra(self) -> None:
        head = make_heading("Level II · Spectral admissibility", "Which structures remain distinguishable?")
        network = make_network(3.8 * LEFT + 0.35 * DOWN, scale=0.95)
        graph_label = serif("relational graph", size=21, color=MUTED).next_to(network, DOWN, buff=0.35)
        arrow = Arrow(1.4 * LEFT, 0.3 * RIGHT, color=FOREGROUND, stroke_width=4).shift(0.25 * DOWN)

        bars = VGroup()
        heights = (0.45, 0.75, 1.15, 1.62, 1.05, 0.65)
        colours = (STRUCTURE, STRUCTURE, CYAN, VIOLET, CYAN, STRUCTURE)
        for index, (height, colour) in enumerate(zip(heights, colours)):
            bar = Rectangle(width=0.42, height=height, stroke_width=0, fill_color=colour, fill_opacity=0.92)
            bar.move_to(np.array([2.35 + index * 0.6, -1.15 + height / 2, 0.0]))
            bars.add(bar)
        baseline = Line(np.array([2.05, -1.15, 0]), np.array([5.6, -1.15, 0]), color=MUTED)
        spectrum_label = serif("spectral selection", size=21, color=MUTED).next_to(baseline, DOWN, buff=0.35)
        capacity = VGroup(kicker("Projective capacity", size=21),
                          serif("how much new distinction survives", size=21)).arrange(DOWN, buff=0.12)
        capacity.move_to(3.85 * RIGHT + 1.3 * UP)

        with self.voiceover(text=NARRATION["spectra"]) as tracker:
            self.play(FadeIn(head, shift=0.12 * UP), run_time=tracker.duration * 0.16)
            self.play(
                LaggedStart(*[Create(l) for l in network[0]], lag_ratio=0.04),
                LaggedStart(*[GrowFromCenter(n) for n in network[1]], lag_ratio=0.06),
                FadeIn(graph_label),
                run_time=tracker.duration * 0.26,
            )
            self.play(Create(arrow), run_time=tracker.duration * 0.10)
            self.play(Create(baseline),
                      LaggedStart(*[GrowFromCenter(b) for b in bars], lag_ratio=0.08),
                      FadeIn(spectrum_label), run_time=tracker.duration * 0.26)
            self.play(FadeIn(capacity, shift=0.12 * UP), run_time=tracker.duration * 0.14)
            self.wait(tracker.duration * 0.05)
        self.play(FadeOut(VGroup(head, network, graph_label, arrow, bars, baseline,
                                 spectrum_label, capacity)), run_time=0.55)

    # ------------------------------------------------------------------ physics
    def scene_physics(self) -> None:
        head = make_heading("Level III · Effective physics", "Possible consequences under further hypotheses")
        centre = make_card("Selected structures", "from admissibility", CYAN, width=2.9, height=1.2).shift(0.25 * DOWN)
        specs = (
            ("Quantum", CYAN, np.array([-4.3, 1.1, 0.0])),
            ("Geometry", VIOLET, np.array([0.0, 1.6, 0.0])),
            ("Gauge", CORAL, np.array([4.3, 1.1, 0.0])),
            ("Gravity", AMBER, np.array([-4.3, -1.55, 0.0])),
            ("Matter", GREEN, np.array([0.0, -2.05, 0.0])),
            ("Cosmology", VIOLET, np.array([4.3, -1.55, 0.0])),
        )
        branches = VGroup(*[make_card(title, "research branch", colour, width=2.5, height=0.95).move_to(pos)
                            for title, colour, pos in specs])
        links = VGroup()
        for index, branch in enumerate(branches):
            direction = branch.get_center() - centre.get_center()
            links.add(DashedLine(centre.get_boundary_point(direction),
                                 branch.get_boundary_point(-direction),
                                 color=specs[index][1], stroke_opacity=0.62))
        qualifier = serif("Derived links · structural proposals · open bridges", size=23,
                          color=MUTED).to_edge(DOWN, buff=0.22)

        with self.voiceover(text=NARRATION["physics"]) as tracker:
            self.play(FadeIn(head, shift=0.12 * UP), run_time=tracker.duration * 0.15)
            self.play(GrowFromCenter(centre), run_time=tracker.duration * 0.15)
            self.play(LaggedStart(*[Create(l) for l in links], lag_ratio=0.08),
                      LaggedStart(*[FadeIn(b) for b in branches], lag_ratio=0.08),
                      run_time=tracker.duration * 0.40)
            self.play(FadeIn(qualifier), run_time=tracker.duration * 0.14)
            self.wait(tracker.duration * 0.08)
        self.play(FadeOut(VGroup(head, centre, branches, links, qualifier)), run_time=0.55)

    # ------------------------------------------------------------------- status
    def scene_status(self) -> None:
        head = make_heading("An honest map", "Different claims carry different status")
        columns = VGroup(
            make_card("Proved", "in stated mathematical settings", GREEN, width=3.5, height=1.8),
            make_card("Conditional", "given explicit bridge hypotheses", AMBER, width=3.5, height=1.8),
            make_card("Open", "physical identification or completion", CORAL, width=3.5, height=1.8),
        ).arrange(RIGHT, buff=0.48).shift(0.2 * DOWN)
        footer = serif("A research programme — not a finished theory", size=29, bold=True).to_edge(DOWN, buff=0.58)

        with self.voiceover(text=NARRATION["status"]) as tracker:
            self.play(FadeIn(head, shift=0.12 * UP), run_time=tracker.duration * 0.16)
            per = tracker.duration * 0.5 / len(columns)
            for column in columns:
                self.play(FadeIn(column, shift=0.15 * UP), run_time=per)
            self.play(FadeIn(footer, shift=0.12 * UP), run_time=tracker.duration * 0.18)
            self.wait(tracker.duration * 0.1)
        self.play(FadeOut(VGroup(head, columns, footer)), run_time=0.55)

    # ------------------------------------------------------------------ closing
    def scene_closing(self) -> None:
        network = make_network(ORIGIN + 0.65 * UP, scale=0.78)
        ring = Circle(radius=1.52, color=CYAN, stroke_width=2.2, stroke_opacity=0.72).move_to(network)
        line_a = serif("Which structures of observable physics", size=38, bold=True)
        line_b = serif("become unavoidable under non-injective projection?", size=34, color=CYAN)
        question = VGroup(line_a, line_b).arrange(DOWN, buff=0.16).to_edge(DOWN, buff=0.8)
        if question.width > 12.2:
            question.scale_to_fit_width(12.2)
        wordmark = serif("Cosmochrony", size=25, color=MUTED, bold=True).to_edge(DOWN, buff=0.22)

        with self.voiceover(text=NARRATION["closing"]) as tracker:
            self.play(Create(ring),
                      LaggedStart(*[Create(l) for l in network[0]], lag_ratio=0.04),
                      LaggedStart(*[GrowFromCenter(n) for n in network[1]], lag_ratio=0.07),
                      run_time=tracker.duration * 0.32)
            type_on(self, line_a, run_time=tracker.duration * 0.24)
            type_on(self, line_b, run_time=tracker.duration * 0.24)
            self.play(FadeIn(wordmark), run_time=tracker.duration * 0.10)
            self.wait(tracker.duration * 0.10)
        self.play(FadeOut(VGroup(network, ring, question, wordmark)), run_time=0.85)
