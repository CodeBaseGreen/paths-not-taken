---
title: "Post Pearl"
date: 2026-11-25 22:08:00 +1300
tags: [counterfactuals, causality, abstraction, panel]
description: What Pearl's successors added to the ladder of causation, and what it means for learners that can replay themselves.
image:
  path: /assets/img/posts/cover-post-pearl.jpg
  alt: "The ladder of causation climbed from below in the real world, versus all three rungs computed directly in a replayable world"
---

A short introduction (5 pages), with a panel discussion. It covers only the parts of the post-Pearl literature
that bear on this blog's argument.

Judea Pearl gave us the ladder of causation: seeing, doing, imagining. Over the last decade Elias Bareinboim,
Juan Correa, Duligur Ibeling, Thomas Icard and colleagues turned the ladder into theorems and tools. Four of
their results matter here:

- **The ladder can't be climbed from below.** The Causal Hierarchy Theorem shows that, for almost every causal
  system, complete knowledge of one rung still leaves the rung above it undecided. Rung 3 needs assumptions or
  a rewind. A seeded, replayable world provides the rewind, and the barrier returns only at the live,
  irreversible boundary.
- **Expressive isn't learnable.** A network big enough to represent a causal system still can't learn it from
  data alone. Neural causal models put the structure back as the inductive bias, which supports holding
  *structure as data*.
- **Abstractions you can test.** Causal abstraction, with *interchange interventions*, gives a graded test of
  whether a coarse concept such as "panic contagion" is faithful to what happens underneath.
- **Carrying results between worlds.** Transportability and data fusion say when a lesson learned in rehearsal
  holds in the live world.

There's also a smaller thread on agents using their own *intentions* as evidence, a rung-3 move made by an
agent about itself.

[Read the introduction (PDF, 5 pages)]({{ '/assets/pdf/Post-Pearl.pdf' | relative_url }})

It builds on [Paths Not Taken]({{ '/posts/paths-not-taken/' | relative_url }}),
[Opening the Markov Blanket]({{ '/posts/opening-the-markov-blanket/' | relative_url }}) and
[The Research Path Forward]({{ '/posts/the-research-path-forward/' | relative_url }}).

## Panel discussion

The four synthetic voices take each result through a worked example in the creature world, then raise objections. 28 minutes.

<audio controls preload="none" style="width:100%" src="{{ '/assets/audio/Post-Pearl-Panel.mp3' | relative_url }}"></audio>

| Time | Chapter |
|---:|:---|
| 0:00 | Welcome, and why post Pearl |
| 2:53 | The ladder can't be climbed from below |
| 5:59 | Expressive is not learnable |
| 8:07 | Counterfactuals are computations over programs |
| 10:04 | Abstractions you can test |
| 13:08 | Carrying results between worlds |
| 14:51 | Your own intention as evidence |
| 16:05 | A worked example, start to finish |
| 19:32 | Objections from the panel |
| 22:07 | What to do on a weekend |
| 23:19 | How this threads through the earlier posts |
| 25:54 | What changes for the spine, and closing |
