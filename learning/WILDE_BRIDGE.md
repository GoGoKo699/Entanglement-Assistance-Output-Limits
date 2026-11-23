# From Wilde to the output-dimension theorem

[Learning route](README.md) · [30-milestone map](MILESTONES.md) · [Exact theorem](../science/output_bound.md#the-theorem)

Alice sends classical messages through a noisy quantum channel. Bob tries to recover them from the received systems. Sharing entanglement before transmission changes the correlations available to the encoder and decoder, and can increase the reliable rate even when the transmitted system is a single qubit.

This project determines how the largest possible multiplicative gain grows with the dimension of the system delivered per channel use. The answer compares two rates of the same channel: its ordinary classical capacity $`C(T)`$ and its entanglement-assisted capacity $`C_E(T)`$. A bound on either rate separately does not control their ratio when both rates approach zero.

## The selected source

The educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition, Cambridge University Press (2017)**. [Publisher and DOI: 10.1017/9781316809976](https://doi.org/10.1017/9781316809976). The print ISBN is 9781107176164.

Section and page references below refer to this printed edition, as listed in its [publisher contents](https://assets.cambridge.org/97811071/76164/toc/9781107176164_toc.pdf). The [author-hosted notes](https://www.markwilde.com/qit-notes.pdf) and [arXiv manuscript](https://arxiv.org/abs/1106.1445) are accessible versions of the same educational work, updated separately; their page numbers differ. They are not a separate textbook edition used by this project.

Wilde supplies the operational language and standard capacity theorems. The [primary research references](../references/RELATED_WORK.md) retain their roles in attribution and in the additional BKM and channel-image arguments.

## A route through the relevant sections

Use these sections for the specific connections below. The [milestone map](MILESTONES.md) organizes the project around its scientific argument.

| Connection to understand | Wilde, 2nd ed. | Use in this project |
|---|---|---|
| Correlation between a reference and an output | §11.6, p. 315 | [Mutual information in the communication model](../science/model.md#communication-task) |
| Relative entropy as distinguishability from a reference state | §11.8, p. 321 | [The quadratic relative-entropy estimate](../science/bkm_geometry.md#relative-entropy-and-its-quadratic-upper-bound) |
| Information in a prepared ensemble | §13.3, p. 383 | [The Holevo information radius controls output deviations](../science/output_bound.md) |
| Optimized reference–output correlation | §13.4, p. 389 | [The assisted-capacity formula](../science/model.md#two-standard-capacity-facts) |
| Reliable ordinary communication | §20.3, p. 548 | The inequality $`\chi(T)\le C(T)`$ |
| Reliable communication with preshared entanglement | §21.3, p. 577 | [The final passage from a state inequality to assisted capacity](../science/output_bound.md#from-the-quadratic-bound-to-capacities) |

## Translating notation and assumptions

A quantum state $`\rho`$ is a positive matrix with trace one; its eigenvalues are probability weights. Its support is the span of eigenvectors with nonzero eigenvalues. A pure state has the form $`|v\rangle\langle v|`$ for a unit vector $`v`$. A pure joint state $`\psi_{RA}`$ can have a mixed input marginal $`\rho_A=\mathrm{Tr}_R\psi_{RA}`$, obtained by discarding the reference.

Register labels identify roles. In Wilde's channel-mutual-information notation, the channel input is often $`A'`$ and its purifying reference is $`A`$. Here the input is $`A`$ and the reference is $`R`$.

| Wilde's notation | Notation here | Meaning |
|---|---|---|
| $`\mathcal N_{A'\to B}`$ | $`T_{A\to B}`$ | The channel used to send a system |
| $`\phi_{AA'}`$ | $`\psi_{RA}`$ | A pure state whose input marginal can be mixed |
| $`H(A)`$ | $`S(\rho_A)`$ | The entropy of a quantum state |
| $`I(\mathcal N)`$ | $`C_E(T)`$ after the capacity theorem | Maximized reference–output mutual information |
| $`\chi(\mathcal N)`$ and regularized Holevo information | $`\chi(T)`$ and $`C(T)`$ | The single-use quantity and its regularization |

The [model](../science/model.md#communication-task) uses independent repeated applications $`T^{\otimes n}`$, finite input and output spaces, arbitrary block encoders and decoders, and no extra communication channel. Ordinary coding already allows entangled signal states across different channel uses. Entanglement assistance adds a shared resource between Alice and Bob before communication; its preparation cost is not charged in this capacity model.

The worked example below uses bits, as in the textbook. The analytical proof uses natural logarithms and nats. Divide every entropy and capacity in that proof by $`\ln2`$ to obtain bits; the multiplier is unchanged.

Two geometric parameters enter later: $`b=\mathrm{rank}T(I_A)`$ counts the common output support, and $`r`$ counts the real affine directions in the output-state image. In particular, $`r\le b^2-1`$. The receiver's preshared entanglement register is not included in $`b`$; it remains unrestricted. See [effective output dimension](../science/model.md#effective-output-dimension).

## Worked example: a noisy qubit with two communication schemes

Consider the qubit depolarizing channel

```math
D_{2,q}(\rho)=q\rho+(1-q)\frac{I_2}{2},
\qquad 0\le q\le1.
```

With probability $`q`$ it preserves the input; otherwise it replaces it by a completely mixed qubit. This example uses the probabilistic-mixture part of the full depolarizing parameter range. Define the entropy of a probability vector and the binary entropy by

```math
H_2(p)=-\sum_jp_j\log_2p_j,
\qquad h_2(t)=H_2(t,1-t),
```

with $`0\log_2 0=0`$.

### Ordinary communication

Alice uses the two inputs $`|0\rangle`$ and $`|1\rangle`$ with equal probabilities. Bob measures the received qubit in that basis. For either transmitted bit $`x`$,

```math
\Pr(\widehat x=x)=\frac{1+q}{2},
\qquad
\Pr(\widehat x\ne x)=\frac{1-q}{2}.
```

The output labels are uniformly distributed, so their entropy is one bit. The conditional uncertainty is $`h_2((1-q)/2)`$. Classical coding over repeated uses of this induced binary channel therefore attains

```math
C(D_{2,q})=\chi(D_{2,q})
=1-h_2\!\left(\frac{1-q}{2}\right).
```

The equality with the full quantum channel's ordinary capacity uses [King's depolarizing-channel result](../references/RELATED_WORK.md#king2003). For a general quantum channel, calculating the rate of one encoding and measurement only supplies an achievable rate.

### Communication with a shared Bell pair

Before each use, Alice and Bob share

```math
|\Phi^+\rangle_{RA}
=\frac{|00\rangle+|11\rangle}{\sqrt2}.
```

Bob holds $`R`$ and Alice holds $`A`$. Alice applies one of the four Pauli operations $`I,X,Z,XZ`$ to her qubit, producing four orthogonal Bell states $`|\Phi_U\rangle`$. She sends that qubit through $`D_{2,q}`$. Bob measures his retained qubit and the received qubit jointly in the Bell basis.

Conditioned on Alice's label $`U`$, the joint output is

```math
\omega_U
=q|\Phi_U\rangle\langle\Phi_U|
 +(1-q)\frac{I_4}{4}.
```

The Bell measurement returns the intended label with probability $`a=(1+3q)/4`$ and each of the three other labels with probability $`t=(1-q)/4`$. With a uniform four-label alphabet, the output entropy is two bits and the conditional entropy is $`H_2(a,t,t,t)`$. Coding across many uses attains

```math
C_E(D_{2,q})=2-H_2(a,t,t,t).
```

The general assisted-capacity formula, together with the symmetry of this channel, establishes optimality; the [depolarizing comparison](../science/examples.md#3-depolarizing-channels-two-distinct-limits) supplies the argument and its primary sources. The received channel system is still one qubit, so $`b=2`$ in both schemes. Bob's additional qubit was supplied by the preshared resource.

At $`q=1/2`$, the ordinary scheme has error probability $`1/4`$. The assisted scheme has output probabilities $`(5/8,1/8,1/8,1/8)`$ relative to the intended label. Thus, in bits per channel use,

| Quantity | Value at $`q=1/2`$ |
|---|---:|
| $`C=\chi`$ | $`0.1887218755\ldots`$ |
| $`C_E`$ | $`0.4512050593\ldots`$ |
| $`C_E/C`$ | $`2.3908466256\ldots`$ |

The gain already exceeds the noiseless factor of two. Both rates nevertheless describe asymptotically reliable communication, not error-free transmission in one use.

### Why this leads to a ratio problem

For small positive $`q`$, the exact formulas give

```math
C(D_{2,q})=\frac{q^2}{2\ln2}+O(q^4),
\qquad
C_E(D_{2,q})=\frac{3q^2}{2\ln2}+O(q^3).
```

Their ratio tends to three while both capacities vanish. At $`q=0`$ itself, both capacities are zero and the ratio is undefined. The [limiting calculation](../science/examples.md#fixed-output-dimension-and-vanishing-capacity) keeps these statements separate.

An absolute bound such as $`C_E\le2`$ loses control of the multiplier as $`C`$ vanishes. This qubit example has three independent output directions for $`q>0`$. The general theorem counts those directions to bound the gain uniformly, including channels with arbitrarily large finite input registers.

## What must be added to the textbook foundations

The capacity formulas reduce the problem to comparing correlations created by entangled inputs with information carried by ordinary ensembles. The following steps supply that comparison. Their full proofs have authoritative homes in `science/`.

### 1. Resolve relative entropy into a quadratic form

The matrix logarithm has a derivative that defines the Bogoliubov–Kubo–Mori, or BKM, form. For a positive definite operator $`\tau`$ and any matrix $`Z`$,

```math
K_\tau(Z)=\int_0^\infty
\mathrm{Tr}\!\left[
Z^\dagger(\tau+sI)^{-1}Z(\tau+sI)^{-1}
\right]ds.
```

For Hermitian $`Z`$, this measures the curvature of $`\mathrm{Tr}(\tau\ln\tau)`$ in direction $`Z`$. In a commuting diagonal case it becomes the familiar weighted expression $`\sum_i |Z_{ii}|^2/\tau_i`$. Small reference probabilities therefore receive greater weight.

For density matrices $`\rho,\tau`$ with $`\mathrm{supp}\rho\subseteq\mathrm{supp}\tau`$, restrict to $`\mathrm{supp}\tau`$, where $`\tau>0`$. The inherited [BKM identities](../science/bkm_geometry.md#the-quadratic-form) and [relative-entropy bound](../science/bkm_geometry.md#relative-entropy-and-its-quadratic-upper-bound) then give

```math
D(\rho\|\tau)\le K_\tau(\rho-\tau).
```

The same estimate applies to a positive operator of arbitrary trace if the divergence includes the trace correction $`\mathrm{Tr}(\tau-\rho)`$. This correction is the linear term in the expansion of $`\mathrm{Tr}(\rho\ln\rho)`$. The proof keeps the spectrum-dependent metric throughout. Replacing every spectral weight by an inverse-smallest-eigenvalue estimate would lose the required uniformity. The relevant research ingredients are credited to [Gao–Rouzé](../references/RELATED_WORK.md#gaorouze2022) and [Wolff et al.](../references/RELATED_WORK.md#wolff2025).

### 2. Regularize an achievable Holevo-radius center

Set $`\eta=\chi(T)`$ in nats. The Holevo information radius gives a state $`\sigma`$ inside the channel’s output image such that every output $`x`$ satisfies $`D(x\Vert\sigma)\le\eta`$. A projective test onto any unit vector gives probabilities $`p`$ from $`x`$ and $`q_0`$ from $`\sigma`$. Data processing and the classical relative-entropy variational bound give

```math
p-\ln(1+(e-1)q_0)
\le D_{\rm Bern}(p\Vert q_0)
\le \eta.
```

Using $`\ln(1+(e-1)q_0)\le(e-1)q_0`$ simultaneously for all these tests proves $`x\le(e-1)\tau`$, where $`\tau=\sigma+\eta I_B`$. The [proof](../science/output_bound.md) separates the achievable center $`\sigma`$ from the regularized operator $`\tau`$, whose trace is $`1+b\eta`$.

For the noisy-qubit example, symmetry gives $`\sigma=I_2/2`$, with $`K_\tau(Z)=(1/2+\eta)^{-1}\mathrm{Tr}(Z^\dagger Z)`$. A pure input gives $`x-\sigma=q(\rho-I_2/2)`$, with squared BKM norm $`q^2/(1+2\eta)`$. The ordinary and assisted capacities both have the same quadratic scale at small depolarizing parameter.

### 3. Use the entropy radius to bound output deviations

The integral formula for $`D(x\Vert\sigma)`$ measures the BKM curvature in direction $`x-\sigma`$ along the segment from $`\sigma`$ to $`x`$. Every point on that segment lies below $`(e-1)\tau`$. By [BKM order and scaling](../science/bkm_geometry.md#monotonicity-in-the-reference-operator), each curvature value is at least $`K_\tau(x-\sigma)/(e-1)`$. The integral of the weight $`1-s`$ is one half, so

```math
\frac{K_\tau(x-\sigma)}{2(e-1)}\le D(x\Vert\sigma)\le\chi(T).
```

Taking the supremum over the outputs gives

```math
M:=\sup_{x\in S}K_\tau(x-\sigma)\le 2(e-1)\chi(T).
```

The center determines the displacement $`x-\sigma`$. The floor controls the curvature that measures it.

### 4. Control entangled inputs using output directions

Define the replacer $`R_\sigma(X)=\mathrm{Tr}(X)\sigma`$ and the difference $`\Delta=T-R_\sigma`$. The translated image spans an $`r`$-dimensional real space of Hermitian matrices. Choose a Hermitian basis $`F_1,\ldots,F_r`$ orthonormal in the BKM form at $`\tau`$. Pull its coordinates back to input observables:

```math
H_j=\Delta^*\!\left(D\log_\tau(F_j)\right).
```

Here $`\Delta^*`$ is the Hilbert–Schmidt adjoint. Each $`H_j`$ is Hermitian, and its squared expectation on any pure input is at most $`M`$. Its extremal eigenvector therefore gives $`\|H_j\|_\infty^2\le M`$.

For a pure input/reference state $`\psi_{RA}`$, the [complete amplification estimate](../science/output_bound.md#complete-amplification-through-output-coordinates) now gives

```math
K_{\rho_R\otimes\tau}
\bigl((\mathrm{id}_R\otimes\Delta)(\psi_{RA})\bigr)
\le2\sum_{j=1}^r\|H_j\|_\infty^2
\le2rM.
```

This step requires more than the ordinary state-radius bound. The proof expands the joint state in Schmidt coordinates, applies the [Schmidt-weight inequality](../science/bkm_geometry.md#the-schmidt-weight-inequality), and sums the result through the Hermitian output coordinates. Its compressed-operator identity treats a non-full-rank input marginal correctly. Zero Schmidt coefficients are removed by restricting to their support; no positive lower bound on the remaining coefficients is assumed. These are the steps that remove dependence on input and reference dimension.

### 5. Account for the floor and return to communication rates

Write $`\omega_{RB}=(\mathrm{id}_R\otimes T)(\psi_{RA})`$. Comparing it with $`A=\rho_R\otimes\tau`$ requires the corrected relative entropy $`\mathrm{Tr}[\omega(\ln\omega-\ln A)]+\mathrm{Tr}(A-\omega)`$. This is mutual information plus a nonnegative marginal comparison with $`\tau`$.

The difference $`\omega_{RB}-A`$ is the centered joint deviation from step 4 minus $`\eta\rho_R\otimes I_B`$. The shift has squared BKM norm $`\eta^2\mathrm{Tr}\,\tau^{-1}\le b\eta`$, so the BKM norm triangle inequality gives

```math
I(R:B)_\omega
\le \left(\sqrt{2rM}+\sqrt{b\eta}\right)^2
\le \left(2\sqrt{(e-1)r}+\sqrt b\right)^2\chi(T).
```

Wilde’s assisted-capacity theorem identifies the maximum on the left with $`C_E(T)`$. The ordinary-capacity theorem gives $`\chi(T)\le C(T)`$. Since $`r\le b^2-1`$, the multiplier grows at most quadratically in $`b`$. The [final comparison](../science/output_bound.md#from-the-quadratic-bound-to-capacities) includes the support and zero-capacity cases.

### 6. Test the dimension dependence with a channel family

A measure-and-prepare channel can give each of the $`b^2-1`$ traceless Hermitian output directions an independent role. Anticommuting input observables constrain the ordinary output displacements to a Euclidean ball. A maximally entangled input instead puts a distinct reference correlation in each of those directions. In the weak-signal limit the ordinary and assisted quantities are both quadratic in signal size, and their ratio approaches $`b^2-1`$. For commuting outputs there are at most $`b-1`$ independent directions. An argument that resolves one classical event at a time gives $`C_E\le bC`$, and the diagonal version of the family yields a ratio approaching $`b-1`$.

The [sharp-order families](../science/sharp_examples.md) give the construction and entropy calculation. [Shor’s additivity theorem](../references/RELATED_WORK.md#shor2002) ensures that the single-use Holevo quantity equals the full ordinary capacity for these entanglement-breaking channels. The exact universal multiplier remains open.

## Connect this bridge to the project map

The [background milestones M01–M14](MILESTONES.md#background-preliminaries) assemble the channel, entropy, capacity, support, and geometric concepts needed to state the comparison. The [narrative milestones M15–M30](MILESTONES.md#narrative-innovation) connect the regularized Holevo center, complete amplification, communication rates, and matching channel families.

For a direct mathematical route, continue with [BKM geometry](../science/bkm_geometry.md), the [output-dimension proof](../science/output_bound.md), and the [precise comparison with earlier work](../references/RELATED_WORK.md#position-of-the-result).
