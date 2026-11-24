# What the dimension scaling means

[Exact theorem](model.md) · [Joint-dimension law](joint-dimensions.md) · [Matching examples](sharp_examples.md)

## Quantum and commuting outputs

Let $`G_b`$ be the supremum of $`C_E(T)/C(T)`$ over channels with positive ordinary capacity, any finite input dimension, and effective output dimension at most $`b`$. For $`b\ge2`$ the [two bounds](sharp_examples.md) give

```math
b^2-1\le G_b\le
\bigl(2\sqrt{(e-1)(b^2-1)}+\sqrt b\bigr)^2.
```

The same quadratic order holds if the supremum is restricted to entanglement-breaking channels. A measure-and-prepare channel can output noncommuting states. The full traceless output space then contains $`b^2-1`$ independent directions. If the output states commute, that space has at most $`b-1`$ active directions and the worst-case factor has linear order instead. The [trine measurement example](examples.md) illustrates why a channel with classical output can still benefit from assistance.

## How large must the sender be?

For dimensions $`a`$ and $`b`$ with $`2\le b\le a`$, the [joint converse and a measure-and-prepare family](joint-dimensions.md) give the worst-case order $`\Theta(\min\{a,b^2-1\})`$. A receiver with $`b`$ dimensions needs a sender of order $`b^2`$ dimensions to realize the quadratic gain in order.

Exact local saturation requires a distinct resource. Around the maximally mixed replacer, a witness with Schmidt rank $`k`$ contributes at most $`\min\{r,k+1\}`$ to the limiting ratio. Reaching the exact value $`r\ge2`$ forces a Clifford representation on the Schmidt support, which needs dimension at least $`2^{\lfloor r/2\rfloor}`$. The Gaussian family uses order $`b^2`$ input dimensions to obtain a quadratic ratio.

## Why proximity to a replacer matters

The elementary bound $`C_E(T)\le2\ln b`$ controls the assisted rate itself. The relative gain concerns channels where $`C(T)`$ can be arbitrarily small. In the explicit weak-signal family, assisted and ordinary capacities both tend to zero quadratically in signal strength, with a ratio that tends to a positive dimension-dependent value. At the exact replacer both capacities vanish.

For the global bound, a Holevo information-radius center controls the distance from every output. Adding $`\chi(T)I`$ to that center gives a reference that dominates all outputs up to a universal constant. Two estimates in the resulting BKM geometry use the $`r`$ active output directions or the input Schmidt directions. The trace correction is controlled by $`b\chi(T)`$, so the argument stays uniform near rank changes.

For the weak-signal law, the full-rank replacer itself supplies the quadratic reference. The matching estimate covers every aspect ratio in this local regime, with the dimensions, replacer, and perturbation fixed before taking the limit.

## Relation to earlier bounds

[Wolff et al.](../references/RELATED_WORK.md#wolff2025) give a global bound in terms of input dimension and the phase-superposition estimate used in the joint proof. [Belzig's thesis](../references/RELATED_WORK.md#belzig2023) gives an output estimate carrying a spectral factor. The joint theorem combines an input-sensitive estimate with a regularized output reference to give a bound linear in $`a+b`$.

## Open regimes

The global sharp order for outputs much larger than inputs and the exact optimal coefficient in $`G_b`$ remain open here. The capacity model assumes unlimited prior entanglement. The Schmidt-rank bound characterizes a witness within that model, while a finite entanglement budget defines a separate operational problem.
