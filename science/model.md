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
C_E(T)\le16br\,\chi(T)
\le16b(b^2-1)\chi(T)
\le16b(b^2-1)C(T).
```

There is no common upper bound on input dimension in this statement. There is also no lower bound on the nonzero eigenvalues of the output states, a distinguished output center, or an optimizing input.

When $`C(T)>0`$, division gives an enhancement bound. When $`C(T)=0`$, the capacity inequality applies directly and implies $`C_E(T)=0`$. In particular, $`b=1`$ or $`r=0`$ gives zero for all three information quantities.

For an output image consisting of mutually commuting states, simultaneous diagonalization gives $`r\le b-1`$ and hence the immediate refinement

```math
C_E(T)\le16b(b-1)\,C(T).
```

This does not assert that entanglement is useless for every channel with classical output. The [measurement example](examples.md) explains the distinction.

## Proof route and interpretation

The [BKM geometry page](bkm_geometry.md) states and proves the inherited metric identities. The [main proof](output_bound.md) has three steps:

1. Choose an output state $`\sigma`$ satisfying $`x\le b\sigma`$ for every output $`x`$.
2. Use a feasible binary ensemble to bound the BKM squared radius of the entire image by $`8b\chi(T)`$.
3. Resolve the channel into $`r`$ Hermitian output directions and control entangled-input amplification by $`2r`$.

The capacity theorems above then give the result. The [examples](examples.md) distinguish zero capacity from its limit and show why dependence on output dimension is necessary.

The theorem establishes a uniform obstruction, not the optimal enhancement factor. It does not make a coding-efficiency claim, constrain blocklength, or cover infinite-dimensional input spaces. The [interpretation](interpretation.md) gives the consequences and the remaining scaling question.
