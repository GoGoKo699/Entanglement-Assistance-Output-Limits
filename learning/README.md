# Learning the output-dimension bound

Preshared entanglement can increase the number of classical bits reliably transmitted through a noisy quantum channel. This project proves that the multiplicative gain stays uniformly finite when the channel-output dimension is fixed, even as the ordinary capacity approaches zero and the input dimension grows.

The educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition (2017)**, [Cambridge University Press, DOI: 10.1017/9781316809976](https://doi.org/10.1017/9781316809976). Its capacity and entropy framework leads into the project's additional BKM and output-image argument.

## Reading routes

| Goal | Start here |
|---|---|
| Connect a familiar communication task to the theorem | [Wilde-to-project bridge](WILDE_BRIDGE.md), including a complete noisy-qubit example |
| Follow the project's conceptual dependencies | [The 30-milestone map](MILESTONES.md) |
| Check definitions and assumptions | [Communication model](../science/model.md#communication-task) and [effective output dimension](../science/model.md#effective-output-dimension) |
| Read the analytical argument | [BKM geometry](../science/bkm_geometry.md) and [the output bound](../science/output_bound.md#the-theorem) |
| Understand sharp examples and remaining limitations | [Channel comparisons](../science/examples.md) and [open scaling](../science/interpretation.md#the-remaining-question) |
| Trace imported theorems and the contribution | [Related work and primary sources](../references/RELATED_WORK.md) |

## How the map fits the science

The map has two phases. [M01–M14](MILESTONES.md#background-preliminaries) build from states and channels through correlations, coding rates, and output geometry to the uniform-comparison problem. [M15–M30](MILESTONES.md#narrative-innovation) assemble the proof's center, radius, and amplification estimates, then connect the theorem to examples, attribution, verification, and physical meaning.

The allocation follows the argument: fourteen targets establish a common framework, and sixteen explain the mechanism and its consequences. Each milestone records a central question, an understanding target, dependencies, a conceptual connection, and source pointers.

The bridge translates notation and units, identifies the relevant sections of the **printed 2017 edition**, and explains the additional research-level steps. Wilde is the single pedagogical anchor; the primary papers remain the sources for imported results and scientific attribution. The canonical statements and full proofs are in [science/](../science/README.md).
