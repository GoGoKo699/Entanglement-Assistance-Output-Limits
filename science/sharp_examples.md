# Sharp output-dimension scaling

[Output-dimension bound](output_bound.md) · [BKM geometry](bkm_geometry.md) · [Worked comparisons](examples.md)

The [uniform upper bound](output_bound.md) is quadratic in the effective output dimension $`b`$. Here an explicit entanglement-breaking channel attains the same order. For every $`b\ge 2`$, the supremum of $`C_E/C`$ over channels with that output dimension is at least $`b^2-1`$. For channels with commuting outputs, the supremum lies between $`b-1`$ and $`b`$. All capacities below use natural logarithms.

## A channel whose output fills a Euclidean ball

Choose $`m`$ Hilbert–Schmidt orthonormal traceless Hermitian matrices $`F_1,\ldots,F_m`$ on $`\mathbf C^b`$ and $`m`$ traceless pairwise anticommuting Hermitian unitaries $`\Gamma_1,\ldots,\Gamma_m`$ on $`\mathbf C^a`$. The spin-unitary relations are standard. Explicitly, with $`\ell=\lceil m/2\rceil`$ and $`a=2^\ell`$, take the first $`m`$ matrices in the list

```math
Z^{\otimes(j-1)}\otimes X\otimes I^{\otimes(\ell-j)},
\qquad
Z^{\otimes(j-1)}\otimes Y\otimes I^{\otimes(\ell-j)},
\qquad 1\le j\le\ell.
```

Write $`u=I_b/b`$ and define, for real $`t`$ with $`0<\alpha=bm|t|<1`$,

```math
T_t(A)=\mathrm{Tr}(A)u+
t\sum_{j=1}^m\mathrm{Tr}(\Gamma_j A)F_j.
```

The channel measures the $`2m`$ effects $`(I\pm\Gamma_j)/(2m)`$ and prepares $`u\pm mtF_j`$. The effects are positive and sum to identity. Each prepared operator has trace one and is positive because $`\Vert F_j\Vert_\infty\le\Vert F_j\Vert_2=1`$. Expanding the measure-and-prepare map gives exactly $`T_t`$. This proves complete positivity, trace preservation and entanglement breaking. By [Shor's additivity theorem](../references/RELATED_WORK.md#shor2002), $`C(T_t)=\chi(T_t)`$ for the full, regularized unassisted capacity.

For an input state $`\rho`$, put $`v_j=\mathrm{Tr}(\Gamma_j\rho)`$. Since $`(\sum_j x_j\Gamma_j)^2=\Vert x\Vert_2^2 I`$ for every real $`x`$, the expectation vector $`v`$ has Euclidean norm at most one. Conversely, each $`v`$ in the closed unit ball is realized by the state $`(I+\sum_jv_j\Gamma_j)/a`$. Here the anticommutation and trace properties give $`\mathrm{Tr}(\Gamma_i\Gamma_j)=a\,\delta_{ij}`$. Thus the output-state image is the ball

```math
\biggl\{u+t\sum_{j=1}^m v_jF_j:\Vert v\Vert_2\le1\biggr\}.
```

It has real affine dimension $`m`$ and effective output dimension $`b`$. Take $`m=b^2-1`$ for all traceless Hermitian directions or $`m=b-1`$ for all traceless diagonal directions. The displayed realization of the full Hermitian case uses an input dimension exponential in $`b^2`$.

## The two capacities in the weak-signal limit

For density matrices $`\sigma`$ and $`\sigma+\Delta`$ on their common support, suppose $`-\alpha\sigma\le\Delta\le\alpha\sigma`$ with $`0\le\alpha<1`$. The [integral Taylor formula and BKM monotonicity](bkm_geometry.md) give

```math
\frac{K_\sigma(\Delta)}{2(1+\alpha)}
\le D(\sigma+\Delta\Vert\sigma)
\le \frac{K_\sigma(\Delta)}{2(1-\alpha)}.
```

Indeed, the entire segment lies between $`(1-\alpha)\sigma`$ and $`(1+\alpha)\sigma`$. Integrating its curvature against $`1-s`$ gives the factor one half. For any output above, the bound applies at $`\sigma=u`$ with $`K_u(t\sum_jv_jF_j)=bt^2\Vert v\Vert_2^2`$. The average relative entropy to $`u`$ upper-bounds the Holevo information of any ensemble by the relative-entropy decomposition around the ensemble mean. The equiprobable output pair $`u\pm tF_1`$ has mean $`u`$ and attains the same quadratic form at both endpoints. Therefore

```math
\frac{bt^2}{2(1+\alpha)}
\le C(T_t)=\chi(T_t)\le
\frac{bt^2}{2(1-\alpha)}.
```

For the assisted capacity, use an arbitrary pure reference-input state $`\psi`$ in Schmidt form with coefficients $`\sqrt{p_k}`$. On its reference support let $`\rho_R=\operatorname{diag}(p_k)`$ and let $`P`$ project onto the corresponding input Schmidt subspace. With the matrix of $`P\Gamma_jP`$ expressed in the Schmidt basis, the output is $`\rho_R\otimes u+\Delta_\psi`$ with

```math
\Delta_\psi=t\sum_{j=1}^m
\sqrt{\rho_R}\,(P\Gamma_jP)^{\mathsf T}\sqrt{\rho_R}\otimes F_j.
```

Each compressed operator has norm at most one, so conjugating the sum by $`\sqrt{\rho_R}\otimes I_b`$ shows that $`-\alpha(\rho_R\otimes u)\le\Delta_\psi\le\alpha(\rho_R\otimes u)`$. The sandwich is independent of the nonzero Schmidt coefficients. In these bases, output orthogonality and the [spectral formula for BKM](bkm_geometry.md#the-quadratic-form) give

```math
K_{\rho_R\otimes u}(\Delta_\psi)
= bt^2\sum_{j,k,l}p_kp_l h(p_k,p_l)
   \bigl|\langle l|\Gamma_j|k\rangle\bigr|^2
\le bmt^2.
```

For the inequality, $`pq\,h(p,q)=\int_0^1 pq/((1-s)p+sq)\,ds\le(p+q)/2`$ by the scalar weighted harmonic–arithmetic mean inequality. For each Hermitian unitary, summing the squared matrix elements with weights $`(p_k+p_l)/2`$ gives at most $`\mathrm{Tr}(\rho_A\Gamma_j^2)=1`$, including when the Schmidt subspace is proper. The relative-entropy chain rule bounds $`I(R:B)`$ by $`D(\rho_R\otimes u+\Delta_\psi\Vert\rho_R\otimes u)`$. Maximizing via [BSST](../references/RELATED_WORK.md#bsst2002) then gives the upper bound below.

For a maximally entangled input on $`\mathbf C^a\otimes\mathbf C^a`$, both output marginals are maximally mixed, the chain-rule inequality is an equality, and the BKM form above equals $`bmt^2`$. Combining the Taylor comparisons yields

```math
\frac{bmt^2}{2(1+\alpha)}
\le C_E(T_t)\le
\frac{bmt^2}{2(1-\alpha)}.
```

In particular,

```math
m\frac{1-\alpha}{1+\alpha}
\le \frac{C_E(T_t)}{C(T_t)}\le
m\frac{1+\alpha}{1-\alpha}.
```

For each fixed $`b,m`$, the ratio tends to $`m`$ as $`t\to0`$. Both absolute rates vanish quadratically in this limit. One explicit nonzero choice, $`|t|=1/(2bm)`$, certifies a ratio of at least $`m/3`$. Taking $`m=b^2-1`$ gives the quadratic lower bound without a limit in input dimension for any fixed $`b`$. A linear universal bound would therefore fail even for entanglement-breaking channels with full-rank output states.

## Commuting outputs give a linear law

If the output states of $`T`$ commute, diagonalize them on their effective support. This gives a quantum-to-classical channel with effects $`M_i`$ and output labels $`1\le i\le b`$. For a pure reference-input state $`\psi`$, write $`q_i`$ for the output probability and $`\rho_{R|i}`$ for the conditional reference state. Its mutual information is

```math
I(R:Y)=\sum_{i:q_i>0}q_i D(\rho_{R|i}\Vert\rho_R).
```

To bound a term, diagonalize its effect as $`M_i=\sum_j\lambda_jP_j`$. Write $`p_j=\mathrm{Tr}(\rho_A P_j)`$ and let $`\rho_{R|j}`$ be the reference state after the projective measurement $`\{P_j\}`$. Drop terms with $`p_j=0`$. Then $`\rho_R=\sum_jp_j\rho_{R|j}`$ and $`\rho_{R|i}=\sum_jp_j\lambda_j\rho_{R|j}/q_i`$ with $`q_i=\sum_jp_j\lambda_j`$. Preparing the reference states from the classical label $`j`$ is a channel, so relative-entropy data processing gives

```math
q_iD(\rho_{R|i}\Vert\rho_R)
\le \sum_jp_j\lambda_j\ln(\lambda_j/q_i).
```

The right-hand side is at most the mutual information of the classical channel from $`j`$ to the binary event $`Y=i`$: the missing complement is nonnegative by convexity of $`x\ln x`$. The binary information is in turn at most $`\chi(T)`$. To see this, use the valid input ensemble $`\{p_j,P_j/\mathrm{Tr}P_j\}`$ for $`T`$ and coarse-grain its output into that binary event. The probability of the event for the normalized projector is precisely $`\lambda_j`$. If $`q_i=1`$, the term vanishes and the same bound holds. Summing and maximizing over purifications gives

```math
C_E(T)\le b\,\chi(T)=b\,C(T).
```

The equality $`\chi(T)=C(T)`$ uses entanglement breaking as above. The diagonal Clifford family has $`m=b-1`$ and realizes the matching linear order. The quadratic witness requires noncommuting outputs, even though its implementation measures the input and then prepares the transmitted state.

## Where the example fits

[Wolff et al.](../references/RELATED_WORK.md#wolff2025) establish an input-dimension bound and use depolarizing channels as their growing lower benchmark. The [depolarizing formulas](examples.md#3-depolarizing-channels-two-distinct-limits) give linear growth in the output dimension when the two dimensions coincide. In the Clifford family, the output radius still bounds the single-use unassisted information, while every orthogonal output direction contributes to the reference–output information for the same maximally entangled input. The large input register allows all these contributions within the problem's unrestricted-input model.

The [spin-unitary geometry](https://arxiv.org/abs/2006.06810), BKM calculus and capacity theorems supply established ingredients. The channel construction, the matching quadratic order for the receiver dimension, and the comparison with commuting outputs concern the asymptotic classical communication rates defined in the [model](model.md). The [finite checks](../verification/check_sharp_output.py) evaluate small examples and the curvature estimates. The dimension laws follow from the analytic arguments.
