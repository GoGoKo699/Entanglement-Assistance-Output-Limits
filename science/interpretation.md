# Interpretation and open scaling

[Exact theorem](model.md) · [Proof mechanism](output_bound.md) · [Worked comparisons](examples.md)

## The receiver-side constraint

Entanglement assistance can increase a channel's classical capacity by more than the factor of two associated with noiseless dense coding. The relevant comparison concerns two capacities of the same noisy channel. Both can be small, and a bound on either capacity separately does not bound their ratio.

The output theorem supplies that uniform comparison. For fixed effective channel-output dimension $`b`$, every positive-capacity finite-dimensional channel satisfies

```math
\frac{C_E(T)}{C(T)}\le16b(b^2-1).
```

The sender's input dimension can vary arbitrarily. The receiver may hold an arbitrarily large share of the preshared entanglement. What remains fixed is the output system supplied by each channel use.

Consequently, any sequence of finite-dimensional channels with enhancement tending to infinity must have effective output dimensions tending to infinity. Growing output dimension is a necessary condition; the theorem does not say that every family with growing output dimension has a growing advantage.

## Why proximity to a replacer matters

For fixed output dimension, the elementary estimate $`C_E(T)\le2\ln b`$ is an absolute bound. It becomes uninformative about a multiplier when $`C(T)`$ approaches zero. Likewise, an estimate with an inverse-smallest-eigenvalue constant does not remain uniform as a distinguished output state loses rank.

The proof addresses both problems together. Its center is chosen inside the image by maximizing determinant. Its least eigenvalue may be arbitrarily small, but the entire image still obeys $`x\le b\sigma`$. The BKM geometry measures fluctuations in the same local coordinates that enter relative entropy. The binary Holevo argument then charges those fluctuations to achievable ordinary communication.

No uniform eigenvalue cutoff or limiting exchange over channel families is used. Each channel has its own center; the same numerical dimension factor applies to every one of them.

At an exact replacer, both capacities vanish. Along the weak depolarizing family they vanish quadratically while their ratio tends to $`b+1`$. The [example derivation](examples.md) keeps this finite limit distinct from a ratio at the zero-capacity endpoint.

## What the affine dimension contributes

The refined bound is $`16br`$, with $`r`$ the number of real affine output directions. The complete quadratic expression initially contains reference indices whose number depends on input dimension. Expanding instead in a Hermitian basis of the output-image span associates one Hermitian input operator with each output direction.

Hermiticity gives direct spectral-norm control from pure-state expectation values. The weighted Schmidt sums then collapse to second moments, rather than leaving a factor proportional to input dimension.

This identifies the role of image geometry without claiming that $`r`$ alone determines the actual gain. The identity channel has the largest possible $`r=b^2-1`$ and an exact enhancement of two. A fixed-basis classical stochastic channel has no assisted gain, while a noncommuting measurement can benefit despite its classical output. These comparisons are worked out in the [examples](examples.md).

## Relation to earlier bounds

[Wolff and collaborators](../references/RELATED_WORK.md#wolff2025) establish an input-dimension multiplicative bound. [Belzig's thesis](../references/RELATED_WORK.md#belzig2023) gives a related output estimate with a channel-dependent spectral factor. The uniform output theorem answers the separate question left by these results: whether a finite bound can depend only on the receiving output dimension.

The proof retains the earlier BKM/relative-entropy framework and standard capacity formulas. Its additional ingredients are an in-image domination argument and a complete amplification estimate indexed by output directions. For square channels, an existing input-dimension bound or a sharp special-family result can be numerically stronger.

Appending an input register that the channel discards leaves every relevant capacity and the output image unchanged. The [padding construction](examples.md) illustrates why a uniform output estimate carries information that is absent from an input-dimension estimate.

## The remaining question

For integers $`b\ge2`$, define the maximal gain over all finite input dimensions and effective output supports of dimension at most $`b`$:

```math
G_b=
\sup_{\substack{T:\ C(T)>0\\
\operatorname{rank}T(I_A)\le b}}
\frac{C_E(T)}{C(T)}.
```

The theorem gives $`G_b\le16b(b^2-1)`$. The known depolarizing channel at the negative complete-positivity boundary gives

```math
G_b\ge2b+\frac43-\frac{4}{9b}+O(b^{-2})
\quad (b\to\infty).
```

The lower expression comes from a specific established channel family and the [explicit expansion](examples.md), not a maximization over all channels. In particular, the current comparison leaves a linear-to-cubic scaling gap. Determining the best growth and constants is a separate open problem.

The established conclusion is uniform finiteness in output dimension, including arbitrarily small ordinary capacities and arbitrarily ill-conditioned output images.
