# An output-dimension bound for entanglement assistance

[Model and notation](model.md) · [BKM geometry](bkm_geometry.md)

An arbitrarily large input space cannot provide an unbounded relative communication gain from preshared entanglement when the channel-output dimension remains fixed. The gain is at most quadratic in the effective output dimension. The proof uses the Holevo information to set a positive floor on the output reference operator and to bound the resulting quadratic form.

The [model page](model.md) defines the memoryless channel $`T`$, its ordinary classical capacity $`C(T)`$, its entanglement-assisted classical capacity $`C_E(T)`$, and its single-use Holevo quantity $`\chi(T)`$. Here $`b=\mathrm{rank}T(I_A)`$ is the effective output dimension, and $`r`$ is the real affine dimension of the output-state image. The receiver's share of the preshared entanglement is unrestricted. Here $`b`$ counts only the system delivered by one channel use.

## The theorem

**Theorem.** With $`e=\exp(1)`$, every finite-dimensional completely positive trace-preserving channel satisfies

```math
\begin{aligned}
C_E(T)&\le \left(2\sqrt{(e-1)r}+\sqrt b\right)^2\chi(T)\\
&\le\left(2\sqrt{(e-1)r}+\sqrt b\right)^2 C(T).
\end{aligned}
```

The proof uses natural logarithms. Dividing both sides by $`\ln 2`$ gives the same inequalities in bits. The dimension bound $`r\le b^2-1`$ gives the quadratic estimate, uniformly over the input dimension and the nonzero output spectrum. For commuting outputs, $`r\le b-1`$ and the estimate is linear in $`b`$.

If $`r=0`$, the channel is a replacer and all three information quantities vanish. The [weak-signal family](sharp_examples.md) matches both dimension orders. It approaches the ratio $`b^2-1`$ in the general case and $`b-1`$ for commuting outputs. [Worked comparisons](examples.md) show how particular channel classes can yield different constants.

## The regularized Holevo center

Write

```math
S=T(\mathcal S(A)),
\qquad
Q=\mathrm{supp}T(I_A).
```

Every output is supported on $`Q`$ because positivity gives $`T(\rho)\le T(I_A)`$ for every input density matrix $`\rho`$. We restrict the receiving space to $`Q`$, whose dimension is $`b`$. The state $`T(I_A/\dim A)`$ is positive definite there.

Write $`\eta=\chi(T)`$ in nats. If $`\eta=0`$, every pair of output states has zero equal-weight Holevo information. Strict concavity of entropy implies that the two states coincide. Hence $`T`$ is a replacer, and we assume $`\eta>0`$ for the rest of the proof.

**Lemma 1.** There is a state $`\sigma\in S`$ with $`D(x\|\sigma)\le\eta`$ for all $`x\in S`$. The positive operator $`\tau=\sigma+\eta I_Q`$ satisfies

```math
x\le(e-1)\tau\qquad\text{for all }x\in S.
```

**Proof.** The set of pairs $`(x,H(x))`$, with $`H(x)=-\mathrm{Tr}(x\ln x)`$, is compact. Its convex hull is compact by Carathéodory's theorem and contains all pairs of ensemble means and average entropies. Maximizing the continuous difference between mean-state entropy and average entropy in this convex hull gives a finite optimal Holevo ensemble $`(p_j,x_j)_j`$. Let $`\sigma=\sum_j p_jx_j`$ be its mean. Include any $`x\in S`$ with weight $`u\in(0,1)`$ and scale the old weights by $`1-u`$. The new mean is $`\sigma_u=(1-u)\sigma+ux`$. Expanding the new ensemble's Holevo information gives

```math
(1-u)\eta+(1-u)D(\sigma\|\sigma_u)+uD(x\|\sigma_u)\le\eta.
```

Nonnegativity of relative entropy gives $`D(x\|\sigma_u)\le\eta`$. Lower semicontinuity as $`u\downarrow0`$ then yields $`D(x\|\sigma)\le\eta`$. All outputs are supported on $`\sigma`$, which is therefore positive definite on $`Q`$.

For a unit vector $`v\in Q`$, measure the two-outcome projector onto $`v`$. Write $`p=\langle v|x|v\rangle`$ and $`q=\langle v|\sigma|v\rangle`$. By data processing the relative entropy of the resulting Bernoulli distributions is at most $`\eta`$. Its variational lower bound with test function equal to one on the first outcome and zero on the other gives

```math
\eta\ge D_{\mathrm{Ber}}(p\|q)
\ge p-\ln\bigl(1+(e-1)q\bigr)
\ge p-(e-1)q.
```

The variational inequality follows by tilting the probabilities $`(q,1-q)`$ by the factors $`(e,1)`$, normalizing, and applying nonnegativity of relative entropy to the tilted distribution. The bound for every $`v`$ gives $`x\le(e-1)\sigma+\eta I_Q\le(e-1)\tau`$. $`\square`$

## Relative entropy controls the output radius

Use the BKM form $`K_\tau`$ from the [geometry page](bkm_geometry.md#the-quadratic-form), and set

```math
M=\sup_{x\in S}K_\tau(x-\sigma).
```

**Lemma 2.** The output radius satisfies

```math
M\le 2(e-1)\eta.
```

**Proof.** For any $`x\in S`$, fix $`Z=x-\sigma`$ and let $`z_s=\sigma+sZ`$. Lemma 1 bounds the whole segment by $`(e-1)\tau`$. The [relative-entropy integral and metric order](bkm_geometry.md#relative-entropy-and-its-quadratic-upper-bound) give

```math
\eta\ge D(x\|\sigma)=\int_0^1(1-s)K_{z_s}(Z)\,ds
\ge\frac{K_\tau(Z)}{2(e-1)}.
```

The integral uses the positive segment points $`s<1`$ and is valid for a singular endpoint by continuity. Taking the supremum proves the claim. $`\square`$

The floor $`\eta I_Q`$ controls the metric as an output eigenvalue approaches zero. The final step accounts for its contribution to the joint quadratic form.

## Complete amplification through output coordinates

For any center $`\sigma\in S`$ and positive definite metric reference $`\tau`$ on $`Q`$, define the replacement channel and its difference from $`T`$.

```math
R_\sigma(X)=\mathrm{Tr}(X)\sigma,
\qquad
\Delta=T-R_\sigma.
```

Let $`V=\mathrm{span}_{\mathbb R}(S-\sigma)`$. Because $`\sigma\in S`$, this space has dimension $`r`$ and consists of traceless Hermitian matrices. Every Hermitian input is a real linear combination of density matrices, so $`\Delta`$ maps Hermitian inputs into $`V`$ and arbitrary complex inputs into $`V+iV`$.

Choose a real $`K_\tau`$-orthonormal Hermitian basis $`F_1,\ldots,F_r`$ of $`V`$. Its complexification is an orthonormal basis of $`V+iV`$ for the sesquilinear BKM inner product. Write $`\Delta^*`$ for the Hilbert–Schmidt adjoint, defined by

```math
\mathrm{Tr}\bigl[Y^\dagger\Delta(X)\bigr]
=\mathrm{Tr}\bigl[(\Delta^*(Y))^\dagger X\bigr].
```

Set

```math
H_j=\Delta^*\!\left(D\log_\tau(F_j)\right).
```

Each $`H_j`$ is Hermitian because both maps in its definition preserve Hermitian operators. Self-adjointness of $`D\log_\tau`$ and the adjoint identity give

```math
\langle F_j,\Delta(X)\rangle_\tau
=\mathrm{Tr}(H_jX).
```

The orthonormal expansion and Parseval identity are therefore

```math
\begin{aligned}
\Delta(X)
&=\sum_{j=1}^r\mathrm{Tr}(H_jX)F_j,\\
K_\tau(\Delta(X))
&=\sum_{j=1}^r|\mathrm{Tr}(H_jX)|^2.
\end{aligned}
```

For every unit input vector $`v`$, the second identity is at most $`M=\sup_{x\in S}K_\tau(x-\sigma)`$ when $`X=|v\rangle\langle v|`$. In particular, choosing an extremal eigenvector of $`H_j`$ proves

```math
\|H_j\|_\infty^2\le M.
```

**Lemma 3.** For every pure reference/input state $`\psi`$, with reference marginal $`\rho_R`$,

```math
K_{\rho_R\otimes\tau}
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

Let $`P`$ project onto the input Schmidt subspace. On the reference support, $`\rho_R=\mathrm{diag}(p_k)`$ is positive definite. Diagonalize $`\tau`$ with eigenvalues $`\mu_s>0`$. The spectral BKM formula and the [Schmidt-weight inequality](bkm_geometry.md#the-schmidt-weight-inequality) give

```math
\begin{aligned}
&K_{\rho_R\otimes\tau}
 \bigl((\mathrm{id}_R\otimes\Delta)(\psi)\bigr)\\
&\quad=\sum_{k,l,s,t}
 p_kp_l h(p_k\mu_s,p_l\mu_t)
 \left|\bigl[\Delta(|k\rangle\langle l|)\bigr]_{st}\right|^2\\
&\quad\le\sum_{k,l}\max(p_k,p_l)
 K_\tau\!\left(\Delta(|k\rangle\langle l|)\right)\\
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

For a pure reference/input state $`\psi`$, set $`\omega=(\mathrm{id}_R\otimes T)(\psi)`$. Its reference marginal is $`\rho_R`$. Restricting to the reference Schmidt support and the common output support makes $`\rho_R\otimes\tau`$ positive definite. The joint state has no blocks outside these supports by positivity and its marginals.

The [extended relative entropy](bkm_geometry.md#relative-entropy-and-its-quadratic-upper-bound) permits the generally unnormalized reference operator $`\tau`$. Its chain rule follows by expanding the tensor-product logarithm and the trace correction.

```math
D_{\mathrm{ext}}(\omega\|\rho_R\otimes\tau)
=I(R:B)_\omega+D_{\mathrm{ext}}(\omega_B\|\tau)
\ge I(R:B)_\omega.
```

Write $`Y=(\mathrm{id}_R\otimes\Delta)(\psi)`$. The difference from the joint reference is

```math
\omega-\rho_R\otimes\tau=Y-\eta\rho_R\otimes I_Q.
```

The last term is diagonal in the product eigenbasis of $`\rho_R`$ and $`\tau`$. With reference eigenvalues $`p_k`$ and output eigenvalues $`\mu_s`$, its BKM square is

```math
K_{\rho_R\otimes\tau}(\eta\rho_R\otimes I_Q)
=\eta^2\sum_{k,s}\frac{p_k^2}{p_k\mu_s}
=\eta^2\mathrm{Tr}(\tau^{-1})\le b\eta,
```

since $`\mu_s\ge\eta`$. Lemma 3 bounds the square of the other term by $`2rM`$. Apply the quadratic upper bound for extended relative entropy and the triangle inequality for the BKM norm. Lemma 2 then gives

```math
\begin{aligned}
I(R:B)_\omega
&\le K_{\rho_R\otimes\tau}(Y-\eta\rho_R\otimes I_Q)\\
&\le \bigl(\sqrt{2rM}+\sqrt{b\eta}\bigr)^2\\
&\le\left(2\sqrt{(e-1)r}+\sqrt b\right)^2\eta.
\end{aligned}
```

The [BSST entanglement-assisted capacity theorem](../references/RELATED_WORK.md#bsst2002) maximizes $`I(R:B)_\omega`$ over purifications of arbitrary input density matrices. This proves the assisted-capacity inequality. The coding results of [Holevo](../references/RELATED_WORK.md#holevo1998) and [Schumacher–Westmoreland](../references/RELATED_WORK.md#schumacher1997) give $`\chi(T)\le C(T)`$ for the regularized ordinary capacity.

If $`r=0`$, the image consists of a single state $`\sigma`$. Density matrices span the Hermitian input space, so $`T=R_\sigma`$ on all inputs and both capacities are zero. This case includes $`b=1`$. Every translated output is traceless Hermitian on $`Q`$, giving $`r\le b^2-1`$. For commuting outputs it is traceless diagonal in one common basis, giving $`r\le b-1`$. $`\square`$

## The maximum-determinant bound

The original estimate $`C_E(T)\le16br\,\chi(T)`$ can give a smaller coefficient at low output dimension. Use as center a state $`\sigma_{\det}\in S`$ maximizing $`\ln\det`$ on $`Q`$. A determinant maximizer exists by compactness and is positive definite because the image contains $`T(I_A/\dim A)`$. For any $`x\in S`$, the one-sided derivative along the segment toward $`x`$ gives

```math
\mathrm{Tr}[\sigma_{\det}^{-1}(x-\sigma_{\det})]\le0,
\qquad
\mathrm{Tr}(\sigma_{\det}^{-1}x)\le b.
```

The largest eigenvalue of the positive matrix $`\sigma_{\det}^{-1/2}x\sigma_{\det}^{-1/2}`$ is at most its trace, so $`x\le b\sigma_{\det}`$. The [binary segment bound](bkm_geometry.md#a-segment-bound-for-binary-holevo-information) gives a radius of at most $`8b\chi(T)`$ in $`K_{\sigma_{\det}}`$. In Lemma 3 use $`\sigma_{\det}`$ as the replacer state and the metric reference. The joint quadratic form at $`\rho_R\otimes\sigma_{\det}`$ is at most $`16br\,\chi(T)`$. The relative-entropy chain rule and capacity maximization then give the estimate.

## What the bound establishes

The upper argument counts the affine directions available to the channel output, even though the input space and the receiver's preshared entanglement may grow much faster. The [matching families](sharp_examples.md) establish the worst-case quadratic dimension order and its linear counterpart for commuting outputs.

[Wolff et al.](../references/RELATED_WORK.md#wolff2025) give a uniform input-dimension bound and explicitly ask whether an output-dimension bound exists. Their BKM and Schmidt-weight tools enter the amplification estimate here. The regularized Holevo center keeps the curvature constant independent of the output dimension. Charging its floor in the joint reference gives the stated receiver-side bound even as the output approaches a lower-rank state. [Further comparisons](../references/RELATED_WORK.md)

## Continue

- [Model and operational definitions](model.md)
- [The inherited BKM tools](bkm_geometry.md)
- [Examples and comparisons](examples.md)
- [Interpretation and open questions](interpretation.md)
