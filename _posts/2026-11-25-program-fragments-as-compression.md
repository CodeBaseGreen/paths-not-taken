---
title: "Program Fragments as Compression"
date: 2026-11-25 22:36:00 +1300
tags: [abstraction, curiosity, panel]
description: Code, graphs whose nodes are graphs, and the search for reusable parts. A short map of good leads.
image:
  path: /assets/img/posts/cover-program-fragments.jpg
  alt: "Three creature graphs share a recurring fragment, which is promoted to a single library node, shortening every graph"
---

A short introduction (4 pages), with a panel discussion. It's deliberately narrow: a starting list of solid leads,
not a survey.

A program that reproduces some data is a compressed description of it. A fragment that recurs across many
programs can be named once and reused, which shortens all of them. When the programs are graphs of functions, as
in this blog's designs, a reusable fragment is a sub-graph that becomes a single node. That's compression progress
at the level of the *language* things are written in. The yardstick is **minimum description length**: the cost
of the library plus everything written with it.

Three areas give the leads:

- **Library learning:** DreamCoder, then **Stitch** (fast compression of program corpora), **babble** (finding
  shared fragments even when programs differ on the surface) and **LILO** (language-model naming and description
  of each fragment, which is very close to the creatures' named, described genes).
- **Graphs whose nodes are graphs:** **SUBDUE** replaces recurring sub-graphs with single nodes and builds
  hierarchies automatically. It extends to learned graph grammars, which are gene grammars that grow from data.
- **Search over programs:** simplest-first search and the Optimal Ordered Problem Solver; grammatical evolution;
  and language-model-guided evolution (FunSearch, AlphaEvolve). The last is as much a warning about evaluators as
  a model.

It ends with a concrete loop for the creature world. Compress the winners' gene graphs and name the fragments.
Then check that each one does causal work by knock-out and replay, and track the catalogue's description length
as population-level compression progress.

[Read the introduction (PDF, 4 pages)]({{ '/assets/pdf/Program-Fragments-as-Compression.pdf' | relative_url }})

It completes a trio with [Post Pearl]({{ '/posts/post-pearl/' | relative_url }}) and
[The Ruliad and the Spine]({{ '/posts/the-ruliad-and-the-spine/' | relative_url }}).

## Panel discussion

The four synthetic voices on each lead, a worked loop for the creatures, and the pitfalls. 14 minutes.

<audio controls preload="none" style="width:100%" src="{{ '/assets/audio/Program-Fragments-as-Compression-Panel.mp3' | relative_url }}"></audio>

| Time | Chapter |
|---:|:---|
| 0:00 | Welcome, and the idea in one picture |
| 1:53 | How to measure it |
| 3:25 | Lead one: library learning |
| 5:57 | Lead two: graphs whose nodes are graphs |
| 7:27 | Lead three: searching for programs |
| 9:33 | How it fits the creature world |
| 11:14 | What to watch, and objections |
| 12:43 | Where to start reading, and closing |
