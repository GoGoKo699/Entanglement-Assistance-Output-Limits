# Entanglement Assistance Output Limits

**Can shared entanglement produce an unbounded classical communication advantage when a channel has a fixed output dimension?** This project proves that it cannot, even when the input dimension grows without restriction.

For a finite-dimensional memoryless quantum channel $`T`$, let $`C_E(T)`$ be its classical capacity with unlimited preshared entanglement and $`C(T)`$ its ordinary classical capacity. If $`b`$ is the dimension of the channel's effective output support, then

```math
C_E(T)\le16b(b^2-1)\,C(T).
```

The estimate is uniform over channel images approaching rank deficiency and over channels with arbitrarily small positive ordinary capacity. Replacement channels satisfy the capacity inequality with both sides zero.

A sharper form uses the real affine dimension $`r`$ of the output-state image and the single-use Holevo quantity $`\chi(T)`$:

```math
C_E(T)\le16br\,\chi(T),
\qquad r\le b^2-1,\qquad \chi(T)\le C(T).
```

The proof combines a state inside the channel image that dominates every output with a bound on the amplification of the Bogoliubov–Kubo–Mori quadratic form. Counting Hermitian output directions removes input dimension from the estimate.

## Read the science

| Question | Account |
|---|---|
| Which capacities, dimensions and resources are being compared? | [Model and exact claims](science/model.md) |
| Which relative-entropy tools enter the proof? | [BKM geometry](science/bkm_geometry.md) |
| How does output geometry control entangled inputs? | [Output-dimension bound](science/output_bound.md) |
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

The checks reconstruct the amplification inequalities on finite matrices and verify cancellation-sensitive depolarizing limits at high precision. The written proofs establish the general theorem; the finite checks test its calculations and conventions.

## Scope

The bounded system is the output of one channel use. The receiver's share of the preshared entanglement is unrestricted. The ordinary capacity allows collective encoding and decoding across many independent uses; no general single-letter formula for it is assumed.

The constant and cubic universal dimension dependence are not optimality claims. Known depolarizing examples require at least linear growth in any universal output-dimension factor. The result establishes uniform finiteness and leaves the best scaling open.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
