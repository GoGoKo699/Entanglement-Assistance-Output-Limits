# An output-dimension bound for entanglement assistance

[Model and notation](model.md) · [BKM geometry](bkm_geometry.md)

An arbitrarily large input space cannot provide an unbounded relative communication gain from preshared entanglement when the channel-output dimension remains fixed. We prove this by controlling the geometry of the channel's entire output-state image.

The [model page](model.md) defines the memoryless channel $`T`$, its ordinary classical capacity $`C(T)`$, its entanglement-assisted classical capacity $`C_E(T)`$, and its single-use Holevo quantity $`\chi(T)`$. Here $`b=\mathrm{rank}T(I_A)`$ is the effective output dimension, and $`r`$ is the real affine dimension of the output-state image. The receiver's share of the preshared entanglement is unrestricted; $`b`$ counts only the system delivered by one channel use.

## The theorem

**Theorem.** Every finite-dimensional completely positive trace-preserving channel satisfies

```math
\begin{aligned}
C_E(T)
&\le16br\,\chi(T)\\
&\le16b(b^2-1)\chi(T)\\
&\le16b(b^2-1)C(T).
\end{aligned}
```

All information quantities use the same units. The proof below uses natural logarithms; dividing every quantity by $`\ln2`$ gives the identical theorem in bits. The bound is uniform over all finite input dimensions and requires no lower bound on nonzero output eigenvalues.

If $`r=0`$, the channel is a replacer and all three information quantities vanish. The capacity inequality includes this case without taking a ratio. The constant and its dimension dependence are not asserted to be optimal; [examples](examples.md) explain the comparison with sharper results for special channel families.

## An output state that dominates the whole image

Write

```math
S=T(\mathcal S(A)),
\qquad
Q=\mathrm{supp}T(I_A).
```

Every output is supported on $`Q`$: for a density matrix $`\rho`$, positivity gives $`T(\rho)\le T(I_A)`$. We restrict the receiving space to $`Q`$, whose dimension is $`b`$. The state $`T(I_A/\dim A)`$ is positive definite on this space.

**Lemma 1.** There is a positive definite $`\sigma\in S`$ such that

```math
x\le b\sigma\qquad\text{for every }x\in S.
```

**Proof.** The image $`S`$ is compact and convex. Maximize the determinant on $`S`$. Its maximum is positive because $`S`$ contains a positive definite state, so a maximizing state $`\sigma`$ is positive definite. Equivalently, it maximizes $`\ln\det\sigma`$.

For each $`x\in S`$, the segment $`(1-t)\sigma+tx`$ remains in $`S`$. The one-sided derivative at a maximum is nonpositive:

```math
\mathrm{Tr}\bigl[\sigma^{-1}(x-\sigma)\bigr]\le0,
\qquad
\mathrm{Tr}(\sigma^{-1}x)\le b.
```

The positive matrix $`\sigma^{-1/2}x\sigma^{-1/2}`$ has largest eigenvalue at most its trace. It is therefore at most $`bI`$, which proves the claim. $`\square`$

The state $`\sigma`$ is used only to prove the bound. No efficient procedure for finding it or preparing a code is assumed.

## Binary communication controls the output radius

Use the BKM form $`K_\sigma`$ from the [geometry page](bkm_geometry.md#the-quadratic-form), and set

```math
M=\sup_{x\in S}K_\sigma(x-\sigma).
```

**Lemma 2.** The output radius satisfies

```math
M\le8b\,\chi(T).
```

**Proof.** For any $`x\in S`$, both $`x`$ and $`\sigma`$ are at most $`b\sigma`$. The [binary segment bound](bkm_geometry.md#a-segment-bound-for-binary-holevo-information) gives

```math
J(x,\sigma)\ge\frac{1}{8b}K_\sigma(x-\sigma).
```

Both endpoints belong to the channel image. They can therefore be produced by two input states used with equal probability, so $`J(x,\sigma)\le\chi(T)`$. Taking the supremum over $`x`$ proves the claim. $`\square`$

This estimate retains the full state-dependent metric. It remains valid when the smallest eigenvalue of the chosen center is arbitrarily small; no inverse-minimum-eigenvalue factor appears in the bound.

## Complete amplification through output coordinates

Define the replacement channel and its difference from $`T`$ by

```math
R_\sigma(X)=\mathrm{Tr}(X)\sigma,
\qquad
\Delta=T-R_\sigma.
```

Let $`V=\mathrm{span}_{\mathbb R}(S-\sigma)`$. Because $`\sigma\in S`$, this space has dimension $`r`$ and consists of traceless Hermitian matrices. Every Hermitian input is a real linear combination of density matrices, so $`\Delta`$ maps Hermitian inputs into $`V`$ and arbitrary complex inputs into $`V+iV`$.

Choose a real $`K_\sigma`$-orthonormal Hermitian basis $`F_1,\ldots,F_r`$ of $`V`$. Its complexification is an orthonormal basis of $`V+iV`$ for the sesquilinear BKM inner product. Write $`\Delta^*`$ for the Hilbert–Schmidt adjoint, defined by

```math
\mathrm{Tr}\bigl[Y^\dagger\Delta(X)\bigr]
=\mathrm{Tr}\bigl[(\Delta^*(Y))^\dagger X\bigr].
```

Set

```math
H_j=\Delta^*\!\left(D\log_\sigma(F_j)\right).
```

Each $`H_j`$ is Hermitian because both maps in its definition preserve Hermitian operators. Self-adjointness of $`D\log_\sigma`$ and the adjoint identity give

```math
\langle F_j,\Delta(X)\rangle_\sigma
=\mathrm{Tr}(H_jX).
```

The orthonormal expansion and Parseval identity are therefore

```math
\begin{aligned}
\Delta(X)
&=\sum_{j=1}^r\mathrm{Tr}(H_jX)F_j,\\
K_\sigma(\Delta(X))
&=\sum_{j=1}^r|\mathrm{Tr}(H_jX)|^2.
\end{aligned}
```

For every unit input vector $`v`$, the second identity is at most $`M`$ when $`X=|v\rangle\langle v|`$. In particular, choosing an extremal eigenvector of $`H_j`$ proves

```math
\|H_j\|_\infty^2\le M.
```

**Lemma 3.** For every pure reference/input state $`\psi`$, with reference marginal $`\rho_R`$,

```math
K_{\rho_R\otimes\sigma}
\bigl((\mathrm{id}_R\otimes\Delta)(\psi)\bigr)
\le2rM,
```

where the reference system is restricted to the support of $`\rho_R`$.

**Proof.** Write $`\psi=|\psi\rangle\langle\psi|`$ and use a Schmidt decomposition with positive coefficients on its support:

```math
|\psi\rangle
=\sum_k\sqrt{p_k}|k\rangle_R|k\rangle_A,
\qquad p_k>0,
\qquad\sum_kp_k=1.
```

Let $`P`$ project onto the input Schmidt subspace. On the reference support, $`\rho_R=\mathrm{diag}(p_k)`$ is positive definite. Diagonalize $`\sigma`$ with eigenvalues $`\mu_s>0`$. The spectral BKM formula and the [Schmidt-weight inequality](bkm_geometry.md#the-schmidt-weight-inequality) give

```math
\begin{aligned}
&K_{\rho_R\otimes\sigma}
 \bigl((\mathrm{id}_R\otimes\Delta)(\psi)\bigr)\\
&\quad=\sum_{k,l,s,t}
 p_kp_l h(p_k\mu_s,p_l\mu_t)
 \left|\bigl[\Delta(|k\rangle\langle l|)\bigr]_{st}\right|^2\\
&\quad\le\sum_{k,l}\max(p_k,p_l)
 K_\sigma\!\left(\Delta(|k\rangle\langle l|)\right)\\
&\quad=\sum_{j=1}^r\sum_{k,l}
 \max(p_k,p_l)|(H_j)_{lk}|^2.
\end{aligned}
```

The sums over $`k,l`$ run only over the Schmidt subspace. Since $`H_j`$ is Hermitian and $`\rho_A=\sum_kp_k|k\rangle\langle k|`$ is supported there,

```math
\begin{aligned}
\sum_{k,l}\max(p_k,p_l)|(H_j)_{lk}|^2
&\le\sum_{k,l}(p_k+p_l)|(H_j)_{lk}|^2\\
&=2\mathrm{Tr}\!\left[\rho_A(PH_jP)^2\right]\\
&\le2\mathrm{Tr}(\rho_AH_j^2)\\
&\le2\|H_j\|_\infty^2.
\end{aligned}
```

The compression inequality follows from

```math
PH_j^2P-(PH_jP)^2
=PH_j(I-P)H_jP\ge0.
```

Summing over $`j`$ and using $`\|H_j\|_\infty^2\le M`$ proves the lemma. $`\square`$

The estimate contains neither the input dimension nor an inverse power of a Schmidt coefficient. The factor $`r`$ counts Hermitian directions in the output image, even when the input space supporting those directions is much larger.

## From the quadratic bound to capacities

For a pure reference/input state, let

```math
\omega_{RB}=(\mathrm{id}_R\otimes T)(\psi).
```

Its reference marginal is $`\rho_R`$. Restricting to the reference Schmidt support and the common output support makes $`\rho_R\otimes\sigma`$ positive definite. The joint state has no blocks outside these supports, as follows from positivity and its marginals.

The relative-entropy chain rule gives

```math
D(\omega_{RB}\|\rho_R\otimes\sigma)
=I(R:B)_\omega+D(\omega_B\|\sigma).
```

Apply the [quadratic upper bound for relative entropy](bkm_geometry.md#relative-entropy-and-its-quadratic-upper-bound), followed by Lemmas 3 and 2:

```math
\begin{aligned}
I(R:B)_\omega
&\le D(\omega_{RB}\|\rho_R\otimes\sigma)\\
&\le K_{\rho_R\otimes\sigma}
       (\omega_{RB}-\rho_R\otimes\sigma)\\
&=K_{\rho_R\otimes\sigma}
       \bigl((\mathrm{id}_R\otimes\Delta)(\psi)\bigr)\\
&\le2rM\\
&\le16br\,\chi(T).
\end{aligned}
```

The [BSST entanglement-assisted capacity theorem](../references/RELATED_WORK.md#bsst2002) maximizes $`I(R:B)_\omega`$ over purifications of arbitrary input density matrices. Thus the pure joint-state calculation already covers mixed channel inputs and proves the first capacity inequality.

Every translated output is traceless Hermitian on a $`b`$-dimensional space, so $`r\le b^2-1`$. Finally, [Holevo](../references/RELATED_WORK.md#holevo1998) and [Schumacher–Westmoreland](../references/RELATED_WORK.md#schumacher1997) establish achievability of the single-use Holevo quantity, giving $`C(T)\ge\chi(T)`$. No single-letter formula for the ordinary classical capacity is assumed. These facts complete the theorem. $`\square`$

When $`r=0`$, the image consists of one state. Since density matrices span the Hermitian input space, $`T=R_\sigma`$ on all inputs, and the zero-capacity case follows directly. If $`b=1`$, this replacement case is automatic.

## What the bound establishes

For channels with positive ordinary capacity, the theorem uniformly bounds the ratio $`C_E(T)/C(T)`$ at fixed output dimension. A family whose ratios tend to infinity must therefore have effective output dimensions tending to infinity.

[Wolff et al.](../references/RELATED_WORK.md#wolff2025) give a uniform bound in terms of input dimension and explicitly ask whether an output-dimension bound exists. Their BKM and Schmidt-coefficient tools are used here. The additional channel-image argument chooses a dominating state inside the image and controls the complete quadratic form through Hermitian output coordinates. This yields the receiver-side uniformity proved above, including limits in which the output spectrum approaches a lower-rank state. Further comparisons are in [related work](../references/RELATED_WORK.md).

## Continue

- [Model and operational definitions](model.md)
- [The inherited BKM tools](bkm_geometry.md)
- [Examples and comparisons](examples.md)
- [Interpretation and open questions](interpretation.md)
