---
title: "The Research Path Forward"
date: 2026-11-25 20:07:00 +1300
tags: [roadmap, counterfactuals, curiosity, abstraction, simulation, panel]
description: Which parts matter most, which are critical, what can be swapped for something simpler, and in what order, for one person working at small scale.
image:
  path: /assets/img/posts/forward.jpg
  alt: LED strips with orange and green paths
---

The practical follow-up to the essays (23 pages), with a panel discussion. It asks what should actually be built,
by one person on weekends, to test the ideas in [Paths Not Taken]({{ '/posts/paths-not-taken/' | relative_url }})
and [Opening the Markov Blanket]({{ '/posts/opening-the-markov-blanket/' | relative_url }}), using the
[LED creatures]({{ '/posts/led-creatures-a-research-playground/' | relative_url }}) as the first world.

**The alternative in principle.** Instead of one large associative model that absorbs correlations, use small
learners that are counterfactual by construction. Every run is replayable, structure is held as inspectable
graphs of functions, and those graphs are compiled to fast tensor code only late and only for speed. The
learners predict coarse features rather than raw detail, are driven by curiosity measured as compression
progress, and leave the irreversible decisions to people.

**Twenty-five components, evaluated.** Each is rated for what it contributes, whether it's critical, how much
effort it takes, and how unusual it is. The encouraging finding: every critical component is cheap.

![Contribution versus effort]({{ '/assets/img/posts/fig-priority.png' | relative_url }}){: width="826" }
_Each component's contribution against its effort. The critical ones cluster in the high-value, low-effort corner._

**Also covered:**

- **Cheaper swaps:** what can be replaced with something far simpler at little cost.
- **Grammars:** whether a grammar-based, evolved approach is compatible with the essays. It is, under three
  conditions.
- **Computable stand-ins:** what replaces the free energy principle's uncomputable quantities.
- **Batching what-ifs:** how to run thousands to billions of what-if experiments on ordinary graphics-card
  maths.
- **The human–machine blend:** what people and machines each actually do.

![The roadmap]({{ '/assets/img/posts/fig-roadmap.png' | relative_url }}){: width="891" }
_Things first: a testbed, then a counterfactual laboratory, then internal models, breeding and scale in parallel, then curiosity, concept discovery and live performance._

It ends with a worked research scenario, the outcomes that would show the approach is wrong, open questions,
and a log of the main decisions and what would reopen each.

[Read the document (PDF, 23 pages)]({{ '/assets/pdf/The-Research-Path-Forward.pdf' | relative_url }})

## Panel discussion

The four synthetic voices on the path forward. 52 minutes.

<audio controls preload="none" style="width:100%" src="{{ '/assets/audio/Research-Path-Forward-Panel.mp3' | relative_url }}"></audio>

| Time | Chapter |
|---:|:---|
| 0:00 | Welcome, and what this session is for |
| 1:08 | Where we are |
| 3:14 | What was asked, and the alternative in principle |
| 7:20 | The components: foundations and critical requirements |
| 11:42 | The components: structure, prediction, discovery and scale |
| 17:48 | Swaps that save effort |
| 20:48 | Grammar, compilation and composition |
| 25:29 | Calculability, and the giga what-ifs |
| 30:04 | Internal models and curiosity |
| 33:50 | The human and machine blend, implemented |
| 37:52 | Things first: the roadmap |
| 42:02 | Research outputs as files |
| 43:17 | A worked research scenario |
| 46:22 | How this could be wrong |
| 48:13 | Open questions, the decision log, and closing |
