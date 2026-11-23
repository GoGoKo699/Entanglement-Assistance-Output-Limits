# Model and exact claims

[Repository overview](../README.md) · [Proof](output_bound.md) · [Examples](examples.md)

## Communication task

A channel $`T:\mathcal L(A)\to\mathcal L(B)`$ is a completely positive trace-preserving linear map between finite-dimensional matrix algebras. Repeated uses are independent, described by $`T^{\otimes n}`$. The task is reliable transmission of classical messages at an asymptotic rate per channel use.

The ordinary classical capacity $`C(T)`$ permits arbitrary block encodings, including entangled signal states across channel uses, and collective decoding. It supplies no prior shared entanglement and no additional communication channel.

The entanglement-assisted classical capacity $`C_E(T)`$ additionally permits unlimited entanglement shared before transmission. Its preparation cost is not charged in this standard capacity model. Local operations are unrestricted; no extra classical or quantum side channel is supplied during communication.

We use natural logarithms and rates in nats in the proofs. Dividing every information quantity by $`\ln2`$ gives rates in bits and leaves all multiplicative factors unchanged. The worked examples use bits explicitly.

For states, write

```math
S(\rho)=-\mathrm{Tr}\rho\ln\rho,
\qquad
D(\rho\Vert\sigma)=
\mathrm{Tr}\rho(\ln\rho-\ln\sigma),
```

with $`D=+\infty`$ when the support of $`\rho`$ is not contained in that of $`\sigma`$. Quantum mutual information is

```math
I(R:B)_\omega
=S(\omega_R)+S(\omega_B)-S(\omega_{RB})
=D(\omega_{RB}\Vert\omega_R\otimes\omega_B).
```

## Two standard capacity facts

The single-use Holevo quantity is

```math
\chi(T)=
\sup_{\{p_x,\rho_x\}}
\left[
S\!\left(\sum_xp_xT(\rho_x)\right)
-\sum_xp_xS(T(\rho_x))
\right],
```

where the supremum is over finite ensembles of input states. The [Holevo–Schumacher–Westmoreland coding theorem](../references/RELATED_WORK.md#holevo1998) makes these ensemble rates achievable. In particular,

```math
\chi(T)\le C(T).
```

The ordinary capacity can require regularization. The proof uses the displayed lower bound and never assumes $`C(T)=\chi(T)`$.

The [Bennett–Shor–Smolin–Thapliyal theorem](../references/RELATED_WORK.md#bsst2002) gives

```math
C_E(T)=
\max_{\rho_A}
I(R:B)_{(\mathrm{id}_R\otimes T)(\psi_{RA})},
```

where $`\psi_{RA}`$ is any purification of $`\rho_A`$. Thus a bound valid for every pure joint input already covers arbitrary mixed channel inputs and the operational entanglement-assisted capacity. A reference of dimension $`\dim A`$ suffices in this formula.

## Effective output dimension

Let $`\mathcal S(A)`$ denote the input state space, and define

```math
\mathcal S_T=T(\mathcal S(A)),
\qquad
Q=\mathrm{supp}T(I_A),
\qquad
b=\mathrm{rank}T(I_A).
```

For every state $`\rho`$, positivity and $`\rho\le I_A`$ give $`T(\rho)\le T(I_A)`$. Every output therefore lies on $`Q`$. Conversely, $`T(I_A/\dim A)`$ is positive definite on $`Q`$. We restrict $`B`$ to this common support from now on.

The number $`b`$ counts the system delivered by one channel use. It does not count the receiver's local entanglement register, which remains unrestricted. Inactive output dimensions can be removed; retaining them only weakens the bound.

For any fixed $`\sigma\in\mathcal S_T`$, let

```math
V=\mathrm{span}_{\mathbb R}
\{x-\sigma:x\in\mathcal S_T\},
\qquad
r=\dim_{\mathbb R}V.
```

This is the affine dimension of the output image and is independent of the choice of $`\sigma`$. The elements of $`V`$ are traceless Hermitian operators, so $`r\le b^2-1`$. A channel with $`r=0`$ is a replacer: it outputs one fixed state for every input.

## Uniform output bound

**Theorem.** Every channel in the stated model satisfies

```math
C_E(T)\le\bigl(2\sqrt{(e-1)r}+\sqrt b\bigr)^2\,\chi(T)
\le\bigl(2\sqrt{(e-1)r}+\sqrt b\bigr)^2\,C(T).
```

The input dimension can be arbitrarily large and the nonzero output eigenvalues can be arbitrarily small. When $`C(T)=0`$ the inequality implies $`C_E(T)=0`$. If $`b=1`$ or $`r=0`$, the channel is a replacer and $`C_E=C=\chi=0`$.

For positive $`C(T)`$, the theorem bounds the ratio by $`O(b^2)`$. The [measure-and-prepare witness](sharp_examples.md) makes the ratio approach $`b^2-1`$ at each fixed $`b\ge2`$, so the quadratic order is sharp. When the output image consists of mutually commuting states, simultaneous diagonalization gives $`r\le b-1`$. The diagonal witness approaches $`b-1`$, and the [commuting-output proof](sharp_examples.md#commuting-outputs-give-a-linear-law) gives $`C_E\le b\chi`$.

## Proof route and interpretation

The [BKM geometry page](bkm_geometry.md) develops the metric comparisons. The [main proof](output_bound.md) starts with the mean state of an optimal Holevo ensemble:

1. Bound all image states above by a constant multiple of the regularized center $`\sigma+\chi(T)I`$.
2. Use the relative-entropy radius to bound the image's BKM squared radius by $`2(e-1)\chi(T)`$.
3. Resolve the joint channel perturbation into $`r`$ Hermitian output directions and account for the regularization in the reference state.

The [sharp examples](sharp_examples.md) employ the same classical-capacity definitions as the converse. The exact worst-case constant, the requirements on input size, and the gain with finite entanglement supply are separate questions. See [interpretation](interpretation.md).
