# What the quadratic scaling means

[Exact theorem](model.md) · [Upper-bound proof](output_bound.md) · [Matching examples](sharp_examples.md)

## Quantum and commuting outputs

Let $`G_b`$ be the supremum of $`C_E(T)/C(T)`$ over channels with positive ordinary capacity, any finite input dimension, and effective output dimension at most $`b`$. For $`b\ge2`$ the [two bounds](sharp_examples.md) give

```math
b^2-1\le G_b\le
\bigl(2\sqrt{(e-1)(b^2-1)}+\sqrt b\bigr)^2.
```

The same quadratic order holds if the supremum is restricted to entanglement-breaking channels. A measure-and-prepare channel can output noncommuting states. The full traceless output space then contains $`b^2-1`$ independent directions. If the output states commute, that space has at most $`b-1`$ active directions and the worst-case factor has linear order instead. The [trine measurement example](examples.md) illustrates why a channel with classical output can still benefit from assistance.

## Why proximity to a replacer matters

The elementary bound $`C_E(T)\le2\ln b`$ controls the assisted rate itself. The relative gain concerns channels where $`C(T)`$ can be arbitrarily small. In the explicit weak-signal family, assisted and ordinary capacities both tend to zero quadratically in signal strength, with a ratio that tends to a positive dimension-dependent value. At the exact replacer both capacities vanish.

A Holevo information-radius center controls the distance from every output using the same amount of information that is available for ordinary communication. Adding $`\chi(T)I`$ to that center gives a reference that dominates all outputs up to a universal constant. The reference's BKM quadratic form resolves changes into the $`r`$ active output directions, while the trace correction costs a separate term controlled by $`b\chi(T)`$. The converse therefore remains uniform near rank changes.

## Relation to earlier bounds

[Wolff et al.](../references/RELATED_WORK.md#wolff2025) bound the gain in terms of input dimension. [Belzig's thesis](../references/RELATED_WORK.md#belzig2023) gives an output estimate carrying a spectral factor. The [padding example](examples.md) appends a discarded input register without changing any capacity or output dimension. For comparable input and output sizes, an input-dimension bound can be stronger. The two dimensions describe different resource regimes.

## The remaining question

The exact optimal coefficient in $`G_b`$ remains open. The explicit Clifford family uses an input dimension exponential in the number of output directions, and assistance is unlimited under the capacity definition. Determining the sharp ratio with a joint input-size cap or a finite entanglement budget requires a separate analysis.
