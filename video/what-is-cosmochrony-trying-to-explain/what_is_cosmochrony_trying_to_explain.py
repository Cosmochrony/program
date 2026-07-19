"""Animate the research question and architecture of the Cosmochrony programme."""

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
    ORIGIN,
    Rectangle,
    RIGHT,
    RoundedRectangle,
    Text,
    Transform,
    UP,
    VGroup,
    WHITE,
    Write,
    config,
)
from manim_voiceover import VoiceoverScene

from edge_tts_service import EdgeTTSService
from narration import NARRATION


BACKGROUND = "#080D1B"
FOREGROUND = "#EFF4FF"
MUTED = "#9DACBC"
STRUCTURE = "#62789B"
CYAN = "#49D3DF"
VIOLET = "#996FFF"
CORAL = "#FF7D80"
GREEN = "#66D19E"
AMBER = "#F3BD58"
FONT = "Arial"

config.background_color = BACKGROUND


def stable_text(text: str, **kwargs) -> Text:
    """Render text with the native kerning of the selected font."""

    kwargs.setdefault("font", FONT)
    return Text(text, **kwargs)


def fit_width(mobject: Text | VGroup, width: float) -> Text | VGroup:
    """Scale an object down when it exceeds the requested width."""

    if mobject.width > width:
        mobject.scale_to_fit_width(width)
    return mobject


def make_text_block(
    text: str,
    font_size: float,
    color: str,
    max_width: float,
    weight: str = "NORMAL",
    expanded_spaces: bool = False,
) -> VGroup:
    """Create an explicitly wrapped text block without compressing spaces between words."""

    lines = VGroup(
        *[
            stable_text(
                line.replace(" ", "\N{THREE-PER-EM SPACE}") if expanded_spaces else line,
                font_size=font_size,
                weight=weight,
                color=color,
            )
            for line in text.split("\n")
        ]
    ).arrange(DOWN, buff=0.06)
    if lines.width > max_width:
        lines.scale_to_fit_width(max_width)
    return lines


def make_card(title: str, detail: str, colour: str, width: float = 2.75, height: float = 1.35) -> VGroup:
    """Create a compact labelled scientific-domain card."""

    box = RoundedRectangle(
        corner_radius=0.16,
        width=width,
        height=height,
        color=colour,
        stroke_width=2.2,
        fill_color=colour,
        fill_opacity=0.08,
    )
    heading = make_text_block(title, font_size=27, weight="BOLD", color=FOREGROUND, max_width=width - 0.42)
    caption = make_text_block(
        detail,
        font_size=18,
        color=MUTED,
        max_width=width - 0.48,
        expanded_spaces=True,
    )
    content = VGroup(heading, caption).arrange(DOWN, buff=0.13)
    content.move_to(box)
    return VGroup(box, content).set_z_index(2)


def make_network(center: np.ndarray, scale: float = 1.0, colour: str = CYAN) -> VGroup:
    """Create a small deterministic relational network."""

    coordinates = (
        (-1.30, 0.80),
        (-0.35, 1.32),
        (0.75, 1.02),
        (1.35, 0.10),
        (0.68, -0.85),
        (-0.42, -1.05),
        (-1.38, -0.35),
        (0.00, 0.18),
    )
    edges = ((0, 1), (0, 6), (0, 7), (1, 2), (1, 7), (2, 3), (2, 7), (3, 4), (3, 7),
             (4, 5), (4, 7), (5, 6), (5, 7), (6, 7))
    positions = [center + scale * np.array([x, y, 0.0]) for x, y in coordinates]
    lines = VGroup(
        *[
            Line(positions[start], positions[end], color=STRUCTURE, stroke_width=2.0, stroke_opacity=0.78)
            for start, end in edges
        ]
    )
    nodes = VGroup(
        *[
            Dot(position, radius=0.075 * scale, color=colour).set_stroke(WHITE, width=1.0)
            for position in positions
        ]
    )
    return VGroup(lines, nodes)


def make_heading(kicker: str, title: str) -> VGroup:
    """Create a scene heading with a small cyan kicker."""

    upper = stable_text(kicker, font=FONT, font_size=22, color=CYAN, weight="BOLD")
    main = fit_width(stable_text(title, font=FONT, font_size=43, color=FOREGROUND, weight="BOLD"), 12.0)
    return VGroup(upper, main).arrange(DOWN, buff=0.12).to_edge(UP, buff=0.38)


class WhatIsCosmochronyTryingToExplain(VoiceoverScene):
    """Present the programme's question, layers, scope, and epistemic status."""

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

    def scene_domains(self) -> None:
        """Introduce the successful but separately founded physical domains."""

        title = stable_text("MODERN PHYSICS", font=FONT, font_size=54, weight="BOLD", color=FOREGROUND)
        subtitle = stable_text("Powerful theories · separate foundations", font=FONT, font_size=27, color=CYAN)
        heading = VGroup(title, subtitle).arrange(DOWN, buff=0.16).to_edge(UP, buff=0.42)
        cards = VGroup(
            make_card("Quantum theory", "states and\nprobabilities", CYAN),
            make_card("Spacetime", "geometry and\ngravity", VIOLET),
            make_card("Gauge interactions", "forces and\nsymmetries", CORAL),
            make_card("Matter", "particles and\ngenerations", GREEN),
        ).arrange_in_grid(rows=2, cols=2, buff=(0.65, 0.48)).shift(0.52 * DOWN)

        with self.voiceover(text=NARRATION["opening"]) as tracker:
            self.play(Write(title), FadeIn(subtitle, shift=0.12 * UP), run_time=tracker.duration * 0.22)
            self.play(
                LaggedStart(*[FadeIn(card, shift=0.14 * UP) for card in cards], lag_ratio=0.14),
                run_time=tracker.duration * 0.55,
            )
            self.wait(tracker.duration * 0.15)
        self.play(FadeOut(VGroup(heading, cards)), run_time=0.55)

    def scene_question(self) -> None:
        """Pose the programme-wide emergence question without claiming its solution."""

        heading = make_heading("THE PROGRAMME QUESTION", "Could one deeper description underlie them?")
        network = make_network(ORIGIN + 0.25 * DOWN, scale=1.22)
        halo = Circle(radius=2.05, color=VIOLET, stroke_width=2.0, stroke_opacity=0.55)
        halo.move_to(network)
        labels = VGroup(
            stable_text("QUANTUM", font=FONT, font_size=19, color=CYAN).move_to(4.0 * LEFT + 0.8 * UP),
            stable_text("GEOMETRY", font=FONT, font_size=19, color=VIOLET).move_to(4.0 * RIGHT + 0.8 * UP),
            stable_text("FORCES", font=FONT, font_size=19, color=CORAL).move_to(4.0 * LEFT + 1.35 * DOWN),
            stable_text("MATTER", font=FONT, font_size=19, color=GREEN).move_to(4.0 * RIGHT + 1.35 * DOWN),
        )
        connectors = VGroup(
            *[
                DashedLine(label.get_center(), network.get_center(), color=STRUCTURE, stroke_opacity=0.5)
                for label in labels
            ]
        )
        question_mark = stable_text("?", font=FONT, font_size=78, color=FOREGROUND).move_to(network)

        with self.voiceover(text=NARRATION["question"]) as tracker:
            self.play(FadeIn(heading, shift=0.12 * UP), run_time=tracker.duration * 0.20)
            self.play(
                Create(halo),
                LaggedStart(*[Create(line) for line in network[0]], lag_ratio=0.04),
                LaggedStart(*[GrowFromCenter(node) for node in network[1]], lag_ratio=0.08),
                run_time=tracker.duration * 0.32,
            )
            self.play(
                LaggedStart(*[Create(line) for line in connectors], lag_ratio=0.10),
                LaggedStart(*[FadeIn(label) for label in labels], lag_ratio=0.10),
                FadeIn(question_mark),
                run_time=tracker.duration * 0.28,
            )
            self.wait(tracker.duration * 0.12)
        self.play(FadeOut(VGroup(heading, network, halo, labels, connectors, question_mark)), run_time=0.55)

    def scene_projection(self) -> None:
        """Use the ENI result as an input and move directly to the new research question."""

        heading = make_heading("AFTER EPISODE 1.1", "From a foundational result to a research programme")
        established = make_card(
            "Established input",
            "genuine emergence requires\nnon-injectivity",
            CYAN,
            width=4.25,
            height=1.65,
        ).move_to(3.55 * LEFT + 0.25 * UP)
        next_question = make_card(
            "Next question",
            "what else follows,\nand under which hypotheses?",
            VIOLET,
            width=4.25,
            height=1.65,
        ).move_to(3.55 * RIGHT + 0.25 * UP)
        arrow = Arrow(established.get_right(), next_question.get_left(), buff=0.18, color=FOREGROUND, stroke_width=4.0)
        handoff = stable_text("TAKE AS GIVEN", font_size=19, color=CYAN, weight="BOLD").next_to(
            arrow, UP, buff=0.12
        )

        status_specs = (("FORCED", GREEN), ("CONDITIONAL", AMBER), ("OPEN", CORAL))
        status_cards = VGroup()
        for label, colour in status_specs:
            box = RoundedRectangle(
                corner_radius=0.14,
                width=2.45,
                height=0.78,
                color=colour,
                stroke_width=2.0,
                fill_color=colour,
                fill_opacity=0.08,
            )
            text = stable_text(label, font_size=22, color=FOREGROUND, weight="BOLD").move_to(box)
            status_cards.add(VGroup(box, text))
        status_cards.arrange(RIGHT, buff=0.55).to_edge(DOWN, buff=0.68)
        status_caption = stable_text(
            "The programme separates these three outcomes",
            font_size=22,
            color=MUTED,
        ).next_to(status_cards, UP, buff=0.24)

        with self.voiceover(text=NARRATION["projection"]) as tracker:
            self.play(FadeIn(heading, shift=0.12 * UP), run_time=tracker.duration * 0.15)
            self.play(FadeIn(established, shift=0.14 * UP), run_time=tracker.duration * 0.18)
            self.play(Create(arrow), FadeIn(handoff), run_time=tracker.duration * 0.14)
            self.play(FadeIn(next_question, shift=0.14 * RIGHT), run_time=tracker.duration * 0.19)
            self.play(
                FadeIn(status_caption),
                LaggedStart(*[FadeIn(card, shift=0.10 * UP) for card in status_cards], lag_ratio=0.16),
                run_time=tracker.duration * 0.22,
            )
            self.wait(tracker.duration * 0.07)
        self.play(
            FadeOut(VGroup(heading, established, next_question, arrow, handoff, status_cards, status_caption)),
            run_time=0.55,
        )

    def scene_foundations(self) -> None:
        """Present the finite structural chain and separate its continuum bridge."""

        heading = make_heading("LEVEL 1 · STRUCTURAL FOUNDATIONS", "What does unresolved distinction force?")
        cards = VGroup(
            make_card("Admissible transitions", "explicit axioms", CYAN, width=3.05),
            make_card("Non-commuting\ngenerators", "unresolved fibres", VIOLET, width=3.05),
            make_card("Finite Heisenberg\nstructure", "proved in\nstated settings", GREEN, width=3.05),
        ).arrange(RIGHT, buff=0.65).shift(0.15 * UP)
        arrows = VGroup(
            Arrow(cards[0].get_right(), cards[1].get_left(), buff=0.10, color=MUTED, stroke_width=3.0),
            Arrow(cards[1].get_right(), cards[2].get_left(), buff=0.10, color=MUTED, stroke_width=3.0),
        )
        bridge = make_card(
            "Continuum and\nphysical identification",
            "a separate bridge",
            AMBER,
            width=4.55,
            height=1.25,
        )
        bridge.to_edge(DOWN, buff=0.52)
        bridge_line = DashedLine(cards[2].get_bottom(), bridge.get_top(), color=AMBER, stroke_opacity=0.75)

        with self.voiceover(text=NARRATION["foundations"]) as tracker:
            self.play(FadeIn(heading, shift=0.12 * UP), run_time=tracker.duration * 0.14)
            self.play(
                FadeIn(cards[0], shift=0.12 * UP),
                run_time=tracker.duration * 0.14,
            )
            self.play(
                Create(arrows[0]),
                FadeIn(cards[1], shift=0.12 * RIGHT),
                run_time=tracker.duration * 0.19,
            )
            self.play(
                Create(arrows[1]),
                FadeIn(cards[2], shift=0.12 * RIGHT),
                run_time=tracker.duration * 0.20,
            )
            self.play(Create(bridge_line), FadeIn(bridge), run_time=tracker.duration * 0.16)
            self.wait(tracker.duration * 0.09)
        self.play(FadeOut(VGroup(heading, cards, arrows, bridge, bridge_line)), run_time=0.55)

    def scene_spectra(self) -> None:
        """Visualize spectral admissibility as selection rather than substrate motion."""

        heading = make_heading("LEVEL 2 · SPECTRAL ADMISSIBILITY", "Which structures remain distinguishable?")
        network = make_network(3.75 * LEFT + 0.35 * DOWN, scale=0.95)
        graph_label = stable_text("RELATIONAL GRAPH", font=FONT, font_size=21, color=MUTED).next_to(network, DOWN, buff=0.35)
        spectral_arrow = Arrow(1.45 * LEFT, 0.25 * RIGHT, color=FOREGROUND, stroke_width=4.0)
        spectral_arrow.shift(0.25 * DOWN)
        spectrum_bars = VGroup()
        heights = (0.45, 0.75, 1.15, 1.62, 1.05, 0.65)
        bar_colours = (STRUCTURE, STRUCTURE, CYAN, VIOLET, CYAN, STRUCTURE)
        for index, (height, colour) in enumerate(zip(heights, bar_colours, strict=True)):
            bar = Rectangle(
                width=0.42,
                height=height,
                stroke_width=0,
                fill_color=colour,
                fill_opacity=0.92,
            )
            bar.move_to(np.array([2.35 + index * 0.60, -1.15 + height / 2, 0.0]))
            spectrum_bars.add(bar)
        baseline = Line(np.array([2.05, -1.15, 0.0]), np.array([5.60, -1.15, 0.0]), color=MUTED)
        spectrum_label = stable_text("SPECTRAL SELECTION", font=FONT, font_size=21, color=MUTED).next_to(
            baseline, DOWN, buff=0.35
        )
        capacity = VGroup(
            stable_text("PROJECTIVE CAPACITY", font=FONT, font_size=21, color=CYAN),
            stable_text("how much new distinction survives", font=FONT, font_size=21, color=FOREGROUND),
        ).arrange(DOWN, buff=0.10).move_to(3.82 * RIGHT + 1.25 * UP)

        with self.voiceover(text=NARRATION["spectra"]) as tracker:
            self.play(FadeIn(heading, shift=0.12 * UP), run_time=tracker.duration * 0.17)
            self.play(
                LaggedStart(*[Create(line) for line in network[0]], lag_ratio=0.04),
                LaggedStart(*[GrowFromCenter(node) for node in network[1]], lag_ratio=0.06),
                FadeIn(graph_label),
                run_time=tracker.duration * 0.25,
            )
            self.play(Create(spectral_arrow), run_time=tracker.duration * 0.10)
            self.play(
                Create(baseline),
                LaggedStart(*[GrowFromCenter(bar) for bar in spectrum_bars], lag_ratio=0.08),
                FadeIn(spectrum_label),
                run_time=tracker.duration * 0.25,
            )
            self.play(FadeIn(capacity, shift=0.12 * UP), run_time=tracker.duration * 0.13)
            self.wait(tracker.duration * 0.06)
        self.play(
            FadeOut(VGroup(heading, network, graph_label, spectral_arrow, spectrum_bars, baseline, spectrum_label, capacity)),
            run_time=0.55,
        )

    def scene_physics(self) -> None:
        """Map the selected structures to the programme's effective-physics branches."""

        heading = make_heading("LEVEL 3 · EFFECTIVE PHYSICS", "Possible consequences under additional hypotheses")
        centre = make_card("Selected structures", "from admissibility", CYAN, width=2.85, height=1.25).shift(0.25 * DOWN)
        branch_specs = (
            ("Quantum", CYAN, np.array([-4.25, 1.10, 0.0])),
            ("Geometry", VIOLET, np.array([0.0, 1.58, 0.0])),
            ("Gauge", CORAL, np.array([4.25, 1.10, 0.0])),
            ("Gravity", AMBER, np.array([-4.25, -1.55, 0.0])),
            ("Matter", GREEN, np.array([0.0, -2.05, 0.0])),
            ("Cosmology", VIOLET, np.array([4.25, -1.55, 0.0])),
        )
        branches = VGroup(
            *[make_card(title, "research branch", colour, width=2.45, height=0.95).move_to(position)
              for title, colour, position in branch_specs]
        )
        link_directions = [branch.get_center() - centre.get_center() for branch in branches]
        links = VGroup(
            *[
                DashedLine(
                    centre.get_boundary_point(link_directions[index]),
                    branch.get_boundary_point(-link_directions[index]),
                    color=branch_specs[index][1],
                    stroke_opacity=0.62,
                )
                for index, branch in enumerate(branches)
            ]
        )

        with self.voiceover(text=NARRATION["physics"]) as tracker:
            self.play(FadeIn(heading, shift=0.12 * UP), run_time=tracker.duration * 0.15)
            self.play(GrowFromCenter(centre), run_time=tracker.duration * 0.15)
            self.play(
                LaggedStart(*[Create(link) for link in links], lag_ratio=0.08),
                LaggedStart(*[FadeIn(branch) for branch in branches], lag_ratio=0.08),
                run_time=tracker.duration * 0.39,
            )
            qualifier = stable_text(
                "Derived links · structural proposals · open bridges",
                font=FONT,
                font_size=23,
                color=MUTED,
            ).to_edge(DOWN, buff=0.20)
            self.play(FadeIn(qualifier), run_time=tracker.duration * 0.14)
            self.wait(tracker.duration * 0.08)
        self.play(FadeOut(VGroup(heading, centre, branches, links, qualifier)), run_time=0.55)

    def scene_status(self) -> None:
        """Separate the programme's principal epistemic statuses."""

        heading = make_heading("AN EPISTEMIC MAP", "Different statements carry different scientific status")
        cards = VGroup(
            make_card("PROVED", "in stated\nmathematical settings", GREEN, width=3.45, height=1.75),
            make_card("CONDITIONAL", "given explicit\nbridge hypotheses", AMBER, width=3.45, height=1.75),
            make_card("OPEN", "physical identification\nor completion", CORAL, width=3.45, height=1.75),
        ).arrange(RIGHT, buff=0.48).shift(0.20 * DOWN)
        footer = stable_text(
            "A research programme — not a finished theory",
            font=FONT,
            font_size=29,
            color=FOREGROUND,
            weight="BOLD",
        ).to_edge(DOWN, buff=0.58)

        with self.voiceover(text=NARRATION["status"]) as tracker:
            self.play(FadeIn(heading, shift=0.12 * UP), run_time=tracker.duration * 0.16)
            self.play(
                LaggedStart(*[FadeIn(card, shift=0.15 * UP) for card in cards], lag_ratio=0.15),
                run_time=tracker.duration * 0.45,
            )
            self.play(FadeIn(footer, shift=0.12 * UP), run_time=tracker.duration * 0.17)
            self.wait(tracker.duration * 0.12)
        self.play(FadeOut(VGroup(heading, cards, footer)), run_time=0.55)

    def scene_closing(self) -> None:
        """Close on the precise question that organizes the programme."""

        network = make_network(ORIGIN + 0.65 * UP, scale=0.78)
        ring = Circle(radius=1.52, color=CYAN, stroke_width=2.2, stroke_opacity=0.72).move_to(network)
        question = VGroup(
            stable_text("Which structures of observable physics", font=FONT, font_size=38, color=FOREGROUND, weight="BOLD"),
            stable_text("become unavoidable under non-injective projection?", font=FONT, font_size=34, color=CYAN),
        ).arrange(DOWN, buff=0.16).to_edge(DOWN, buff=0.76)
        question = fit_width(question, 12.2)
        wordmark = stable_text("COSMOCHRONY", font=FONT, font_size=25, color=MUTED, weight="BOLD").to_edge(DOWN, buff=0.22)

        with self.voiceover(text=NARRATION["closing"]) as tracker:
            self.play(
                Create(ring),
                LaggedStart(*[Create(line) for line in network[0]], lag_ratio=0.04),
                LaggedStart(*[GrowFromCenter(node) for node in network[1]], lag_ratio=0.07),
                run_time=tracker.duration * 0.33,
            )
            self.play(Write(question), run_time=tracker.duration * 0.42)
            self.play(FadeIn(wordmark), run_time=tracker.duration * 0.10)
            self.wait(tracker.duration * 0.10)
        self.play(FadeOut(VGroup(network, ring, question, wordmark)), run_time=0.85)
