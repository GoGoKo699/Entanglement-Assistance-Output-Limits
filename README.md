# Entanglement Assistance Output Limits

How much can preshared entanglement increase the classical capacity of a noisy quantum channel? For input dimension $`a`$ and effective output dimension $`b`$ with $`2\le b\le a`$, the **largest possible capacity ratio is $`\Theta(\min\{a,b^2-1\})`$**. Measure-and-prepare channels attain this order.

For a finite-dimensional memoryless channel $`T`$, let $`C_E(T)`$ be its classical capacity with unlimited preshared entanglement and $`C(T)`$ its ordinary classical capacity. Write $`r`$ for the real affine dimension of its output-state image and $`\chi(T)`$ for its single-use Holevo quantity. The [joint-dimension bound](science/joint-dimensions.md) is

```math
\begin{aligned}
C_E(T)&\le
\left(\sqrt{2(e-1)\min\{2r,4a-3\}}+\sqrt b\right)^2\,\chi(T),\\
r&\le b^2-1,\qquad \chi(T)\le C(T).
\end{aligned}
```

The bound is uniform through arbitrarily small ordinary capacities and output eigenvalues. The same sharp order holds for every aspect ratio in the weak-signal limit about a fixed full-rank replacer. A Gaussian-observable construction reaches the quadratic order with $`a=\Theta(b^2)`$. The [Clifford family](science/sharp_examples.md) reaches the exact limiting ratio $`b^2-1`$. At a maximally mixed replacer, exact saturation of the affine-dimension bound requires Schmidt support exponential in the number of directions. When all output states commute, the worst-case gain with unrestricted input dimension grows linearly in $`b`$.

## Read the science

| Question | Account |
|---|---|
| Which capacities, dimensions and resources are being compared? | [Model and exact claims](science/model.md) |
| Which relative-entropy tools enter the proof? | [BKM geometry](science/bkm_geometry.md) |
| How do the input and output jointly constrain the ratio? | [Joint-dimension law](science/joint-dimensions.md) |
| How does output geometry control entangled inputs? | [Output-dimension bound](science/output_bound.md) |
| Which families give exact limits and separate commuting outputs? | [Weak-signal channels and commuting outputs](science/sharp_examples.md) |
| What happens for identity, classical, measurement and depolarizing channels? | [Worked channel comparisons](science/examples.md) |
| What is the physical conclusion, and what remains open? | [Interpretation](science/interpretation.md) |
| What is inherited and what changes relative to earlier work? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Which calculations can be reproduced? | [Verification](verification/README.md) |

The immediate predecessor bounds the advantage using input dimension and explicitly asks whether an output-only bound exists. An earlier output bound retains a channel-dependent spectral factor. The [source comparison](references/RELATED_WORK.md) explains both distinctions and credits the inherited information-theoretic and metric tools.

## Learn the argument

The educational anchor is Mark M. Wilde's *Quantum Information Theory*, second edition (2017). The [source bridge](learning/WILDE_BRIDGE.md) connects its entropy and capacity theorems to the output geometry used here, with notation translations and a worked example. It identifies the additional metric arguments supplied by this project and the primary literature.

The [30-milestone map](learning/MILESTONES.md) develops the prerequisites and then assembles the proof, examples, and physical conclusion. Start with the [learning guide](learning/README.md); specialists can proceed directly to the [scientific account](science/README.md). The [LLM reading guide](llms.txt) maps specific questions to their authoritative sources.

## Reproduce the checks

With the dependencies in [verification/requirements.txt](verification/requirements.txt), run from the repository root:

```bash
python3 verification/run_all.py
```

The checks cover both amplification estimates, depolarizing limits at high precision, and selected weak-signal coefficients and attaining examples.

## Scope

The bounded system is the output of one channel use. The receiver's share of the preshared entanglement is unrestricted. The ordinary capacity allows collective encoding and decoding across many independent uses; no general single-letter formula for it is assumed.

The weak-signal statements take the signal strength to zero at fixed dimensions, replacer, and perturbation. Both rates vanish quadratically in that limit. The global sharp order for outputs much larger than inputs, the general exact optimal constant, and capacity with a finite entanglement budget remain open here.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
