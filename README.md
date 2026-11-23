# Entanglement Assistance Output Limits

How much can preshared entanglement increase the classical capacity of a noisy quantum channel? If the channel delivers a system with effective dimension $`b`$, the **largest possible capacity ratio grows as $`\Theta(b^2)`$**, even among entanglement-breaking channels.

For a finite-dimensional memoryless channel $`T`$, let $`C_E(T)`$ be its classical capacity with unlimited preshared entanglement and $`C(T)`$ its ordinary classical capacity. Writing $`r`$ for the real affine dimension of its output-state image and $`\chi(T)`$ for its single-use Holevo quantity, the universal bound is

```math
C_E(T)\le \bigl(2\sqrt{(e-1)r}+\sqrt b\bigr)^2\,\chi(T),
\qquad r\le b^2-1,\qquad \chi(T)\le C(T).
```

The [proof](science/output_bound.md) regularizes a center of the output image by an amount proportional to its Holevo information. The bound stays uniform as ordinary capacity approaches zero or output eigenvalues approach zero. It is independent of input dimension.

An explicit [measure-and-prepare family](science/sharp_examples.md) approaches the ratio $`b^2-1`$ with a weak signal. Its input observables encode $`b^2-1`$ distinct output directions. When all output states commute, the worst-case gain instead grows as $`\Theta(b)`$.

## Read the science

| Question | Account |
|---|---|
| Which capacities, dimensions and resources are being compared? | [Model and exact claims](science/model.md) |
| Which relative-entropy tools enter the proof? | [BKM geometry](science/bkm_geometry.md) |
| How does output geometry control entangled inputs? | [Output-dimension bound](science/output_bound.md) |
| What makes the quadratic bound sharp? | [Weak-signal channels and commuting outputs](science/sharp_examples.md) |
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

The checks reconstruct the amplification inequalities on finite matrices, verify the depolarizing limits at high precision, and test the weak-signal construction against explicit spectra.

## Scope

The bounded system is the output of one channel use. The receiver's share of the preshared entanglement is unrestricted. The ordinary capacity allows collective encoding and decoding across many independent uses; no general single-letter formula for it is assumed.

The exact optimal constant remains open. The explicit measure-and-prepare example uses an input dimension exponential in the number of output directions. Both of its absolute capacities vanish in the weak-signal limit.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
