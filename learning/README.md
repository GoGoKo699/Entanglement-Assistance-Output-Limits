# Learning the input and output dimension bounds

Preshared entanglement can increase the reliable classical rate through a noisy quantum channel. A channel with effective output dimension $`b`$ can have a gain of order $`b^2`$, and an input dimension of order $`b^2`$ already suffices to realize that order. For $`2\le b\le a`$, where $`a`$ is the input dimension, the worst gain has order $`\min\{a,b^2-1\}`$.

The educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition (2017)** ([Cambridge University Press](https://doi.org/10.1017/9781316809976)). Its capacity and entropy framework leads into the project's use of BKM geometry and channel-image dimension.

## Reading routes

| Goal | Start here |
|---|---|
| Connect a familiar communication task to the theorems | [Wilde-to-project bridge](WILDE_BRIDGE.md), including a complete noisy-qubit example |
| Follow the project's conceptual dependencies | [The 30-milestone map](MILESTONES.md) |
| Check definitions and assumptions | [Communication model](../science/model.md#communication-task) and [effective output dimension](../science/model.md#effective-output-dimension) |
| Understand the uniform estimates | [BKM geometry](../science/bkm_geometry.md), [the output bound](../science/output_bound.md#the-theorem), and [joint dimension laws](../science/joint-dimensions.md) |
| Compare a small sender with exact saturation | [Joint dimension laws](../science/joint-dimensions.md) and [the Clifford family](../science/sharp_examples.md) |
| Trace imported theorems and the contribution | [Related work and primary sources](../references/RELATED_WORK.md) |

## How the map fits the science

[Milestones M01–M14](MILESTONES.md#background-preliminaries) build from states and channels through correlations, coding rates, and output geometry to the uniform-comparison problem. [Milestones M15–M30](MILESTONES.md#narrative-innovation) derive the regularized Holevo-radius estimate, compare two ways to count the joint perturbation, and follow the constructions from order-sharp gain to exact local saturation.

The bridge identifies the relevant sections of the printed 2017 edition and translates notation and units. Wilde supplies the single pedagogical anchor. The primary papers support attribution for imported results, and the [scientific account](../science/README.md) gives the canonical statements and full proofs.
