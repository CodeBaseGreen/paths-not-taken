---
title: "Interference, Not Parallelism"
date: 2026-11-22 13:50:00 +1300
tags: [quantum, abstraction, causality, counterfactuals]
description: Why "try everything at once" is the wrong way to use superposition, and why abstractions, as hidden symmetries, might be the right target.
image:
  path: /assets/img/posts/interference.jpg
  alt: A maze with one route through it and many dead ends
---

A second working paper (12 pages) that replaces the first. The earlier version used quantum computers as
faster searchers: hold every candidate in superposition and boost the good ones. That mode is provably capped
at a square-root saving for unstructured problems, which is why the results were underwhelming.

**The strong mode is interference.** Every known exponential quantum speed-up comes from making a mechanism
interfere with itself so that a *global* property survives measurement: a period, a symmetry, an invariance,
a set of directions the function ignores. Those are exactly what an abstraction is. A coarse variable that
behaves the same whether you intervene at the fine or the coarse level is a statement about what a mechanism
is invariant to.

So the better question is not "can qubits search the space of abstractions faster?" but "can an abstraction
be posed as a hidden symmetry that interference reads out directly?". For one well-defined family, abstractions
with algebraic structure, the answer is yes, with an exponential gap over classical experiments.

Three further ideas follow:

- **Coherent intervention.** Querying a mechanism on a superposition of interventions makes some
  counterfactual quantities identifiable that no classical data can pin down.
- **Compact memory.** Quantum states can carry predictive structure in less memory than any classical model.
- **A quantum teacher.** A quantum instrument used offline finds and certifies abstractions, and an ordinary
  classical model is trained on the checked results.

The paper's open question is whether the abstractions that matter in language and world models are
algebraic enough for any of this to bite. It ranks research bets that need no quantum hardware to start.

[Read the paper (PDF, 12 pages)]({{ '/assets/pdf/Interference-Not-Parallelism-v2.pdf' | relative_url }})
