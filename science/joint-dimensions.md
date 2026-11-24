# Joint input and output limits on the capacity gain

[Scientific account](README.md) · [Output-only proof](output_bound.md) · [Source comparison](../references/RELATED_WORK.md)

Let $`a`$ be the input dimension, $`b`$ the effective output dimension, and $`r`$ the affine dimension of the output-state image. The gain is the ratio $`C_E/C`$ of the entanglement-assisted and ordinary asymptotic classical capacities of the same memoryless channel. An input purification in the assisted-capacity formula can have any Schmidt rank up to $`a`$.

For $`2\le b\le a`$, the largest gain over channels at those dimensions is $`\Theta(\min\{a,b^2-1\})`$. The upper bound holds for arbitrary channels. Small nonzero signals about a full-rank state give matching examples. In the weak-signal limit the same order holds for every input-to-output dimension ratio.

## A joint bound for arbitrary channels

Every finite-dimensional channel satisfies

```math
\begin{aligned}
B_{a,b,r}&=\left(\sqrt{2(e-1)\min\{2r,\,4a-3\}}+\sqrt b\right)^2,\\
C_E&\le B_{a,b,r}\chi\le B_{a,b,r}C .
\end{aligned}
```

where $`\chi`$ is the one-use Holevo quantity. A constant-output channel has $`C_E=C=\chi=0`$.

Take the [Holevo center and regularized reference](output_bound.md) $`\sigma`$ and $`\tau=\sigma+\chi I`$ on the effective output support. The output-only proof gives

```math
M=\sup_{\rho_A}K_\tau(T(\rho_A)-\sigma)\le 2(e-1)\chi .
```

Write $`\Delta=T-R_\sigma`$, where $`R_\sigma(X)=\mathrm{Tr}(X)\sigma`$. For orthonormal input vectors $`i,j`$, let $`X_{ij}=\Delta(|i\rangle\langle j|)`$. Apply $`\Delta`$ to the pure state with vector $`(|i\rangle+e^{\mathrm{i}\theta}|j\rangle)/\sqrt 2`$ and average its squared BKM norm over $`\theta`$. Since $`X_{ji}=X_{ij}^{\dagger}`$ has the same norm, this gives

```math
\frac14 K_\tau(X_{ii}+X_{jj})+\frac12 K_\tau(X_{ij})\le M
\qquad(i\ne j).
```

For a pure input-reference state $`\psi`$ with positive Schmidt weights $`p_i`$ and rank $`k`$, set $`Y=(\mathrm{id}\otimes\Delta)(\psi)`$. The [Schmidt-weight inequality](bkm_geometry.md#the-schmidt-weight-inequality) gives

```math
K_{\rho_R\otimes\tau}(Y)
\le \sum_{i,j}\max(p_i,p_j)K_\tau(X_{ij})
\le (4k-3)M .
```

The diagonal weights sum to one. The off-diagonal weights sum to at most $`2(k-1)`$, since each is at most $`p_i+p_j`$, and their blocks contribute at most $`2M`$ each. The [output-coordinate estimate](output_bound.md#complete-amplification-through-output-coordinates) bounds the same form by $`2rM`$. The two estimates use the same reference $`\rho_R\otimes\tau`$. The [extended relative-entropy argument](output_bound.md#from-the-quadratic-bound-to-capacities) adds a floor correction of BKM norm at most $`\sqrt{b\chi}`$. Taking $`k\le a`$ gives the bound. The phase-superposition step follows [Wolff et al.](../references/RELATED_WORK.md#wolff2025). The regularized output reference lets it be used together with the output-rank estimate.

For $`b\le a`$, this gives $`C_E/C=O(\min\{a,b^2-1\})`$ when $`C>0`$. The same order holds for $`b\le Ka`$ for any fixed numerical $`K`$, with a constant that can depend on $`K`$. With unrestricted aspect ratio and arbitrary signal strength, the general linear-in-$`a`$ bound remains open.

## The weak-signal capacity ratio

Fix a positive definite state $`\sigma`$ on $`b`$ dimensions and a fixed Hermiticity-preserving linear map $`L`$ with traceless values and nonconstant restriction to states. Consider

```math
T_t(X)=\mathrm{Tr}(X)\sigma+tL(X).
```

The limit is $`t\to0`$ with dimensions, $`\sigma`$ and $`L`$ fixed. In the output BKM metric $`K_\sigma`$, let $`c`$ and $`R>0`$ be the center and radius of the minimum ball enclosing $`L(\rho_A)`$. Choose a real orthonormal basis $`F_1,\ldots,F_r`$ of its affine directions in this metric. Then

```math
L(X)=\mathrm{Tr}(X)c+
\sum_{j=1}^r\mathrm{Tr}(A_jX)F_j ,
\qquad A_j=A_j^\dagger .
```

The enclosing ball implies $`\Vert\sum_j x_j A_j\Vert_\infty\le R\Vert x\Vert_2`$ for real $`x`$. For $`B\ge\max_j\Vert A_j\Vert_\infty`$ and $`B>0`$, measure the effects $`(I\pm A_j/B)/(2r)`$ and prepare $`\sigma+tc\pm t\,rB F_j`$. This realizes $`T_t`$, with positive prepared states for sufficiently small $`|t|`$. Thus $`T_t`$ is entanglement breaking in a neighborhood of zero and [Shor's theorem](../references/RELATED_WORK.md#shor2002) gives $`C=\chi`$ there.

For a purification $`\psi_{RA}`$ of $`\rho_A`$ with reference marginal $`\rho_R`$, define

```math
D_\psi=(\mathrm{id}\otimes L)(\psi)-\rho_R\otimes L(\rho_A).
```

The exact limit is

```math
G_\sigma(L)=\lim_{t\to0}\frac{C_E(T_t)}{C(T_t)}
=\frac{\max_{\rho_A}K_{\rho_R\otimes\sigma}(D_\psi)}{R^2} .
```

All joint forms use the Schmidt support. Conjugating the joint perturbation by $`\rho_R^{-1/2}\otimes\sigma^{-1/2}`$ on that support gives a compression of the fixed Choi matrix of $`L`$ conjugated by $`I\otimes\sigma^{-1/2}`$. Its norm is bounded independently of the Schmidt weights. Hence both states in the mutual-information relative entropy, and the segment joining them, lie between $`(1-\alpha)\rho_R\otimes\sigma`$ and $`(1+\alpha)\rho_R\otimes\sigma`$ with $`\alpha=O(|t|)`$. Partial trace gives the same sandwich at $`\sigma`$ for each output and its ensemble mean. Hessian integration bounds each relative entropy between $`t^2/[2(1+\alpha)]`$ and $`t^2/[2(1-\alpha)]`$ times the squared BKM norm of its perturbation difference at the common baseline.

For ordinary capacity, the quadratic optimization is the maximum ensemble variance of $`L(\rho_A)`$. This is at most $`R^2`$ by expanding about $`c`$, and is attained by a mixture of contact points with mean $`c`$. Such a mixture exists since a separating direction from the convex hull of contact points would allow the center to move and decrease the radius. For assisted capacity the quadratic optimization gives the displayed joint form. Its maximum exists even across rank changes. With fixed positive output eigenvalues $`u,v`$, the weights $`pq\,h(pu,qv)`$ extend continuously by zero when either Schmidt weight is zero. At one zero weight this follows from logarithmic growth of the BKM kernel $`h`$. At two zeros it follows from the Schmidt-weight inequality. Compactness of eigenbases gives continuity of the quadratic form.

At nonzero signal the capacity ratio is between $`G_\sigma(L)(1-\alpha)/(1+\alpha)`$ and $`G_\sigma(L)(1+\alpha)/(1-\alpha)`$. Both rates are of order $`t^2`$ for a fixed nonconstant direction.

### Bound at a full-rank baseline

The squared norm of $`D_\psi`$ is the squared joint perturbation centered at $`c`$ less $`K_\sigma(L(\rho_A)-c)`$. The cross term of a joint matrix with $`\rho_R\otimes Z`$ is the BKM inner product of its marginal with $`Z`$, because $`p\,h(pu,pv)=h(u,v)`$. The phase-superposition and output-coordinate estimates therefore apply with $`\tau=\sigma`$ and $`M=R^2`$, giving

```math
G_\sigma(L)\le\min\{2r,\,4a-3\}.
```

This coefficient is independent of the spectrum of $`\sigma`$. The signal range for the comparison can depend on $`\sigma`$ and $`L`$.

## Order-optimal examples with smaller inputs

For $`a,b\ge2`$ put $`m=\min\{a,b^2-1\}`$ and take $`m`$ orthonormal output directions in $`K_\sigma`$. Independently draw $`m`$ traceless Hermitian input observables with real $`N(0,1/a)`$ coefficients in a traceless Hilbert–Schmidt orthonormal basis. For fixed unit $`x\in\mathbb R^m`$ and $`u\in\mathbb C^a`$, the real variable $`u^\dagger A(x)u`$ for $`A(x)=\sum_j x_j A_j`$ has variance at most $`1/a`$. Quarter-radius nets have sizes at most $`9^m`$ and $`9^{2a}`$. The Gaussian tail at threshold $`4.5`$ gives failure probability at most $`2\exp[(3\ln 9-81/8)a]\lt0.002`$ on the two nets. Extension in $`u`$ uses a factor $`2`$ by the Hermitian Rayleigh quotient. Extension in $`x`$ uses a factor $`4/3`$ by linearity. Thus with the complementary probability,

```math
\sup_{\Vert x\Vert_2=1}\Vert A(x)\Vert_\infty\le12 .
```

Also $`a^{-1}\sum_j\mathrm{Tr}(A_j^2)`$ is a chi-square variable with $`m(a^2-1)`$ degrees of freedom divided by $`a^2`$. Its mean is at least $`3m/4`$. The second-moment inequality at half the mean gives

```math
\frac1a\sum_j\mathrm{Tr}(A_j^2)\ge\frac38 m
```

with probability at least $`0.15`$. Both bounds therefore hold simultaneously for some draw, and the draws are linearly independent with probability one.

Take $`L(X)=\sum_j\mathrm{Tr}(A_jX)F_j`$ for such a draw. Its enclosing radius is at most $`12`$. A maximally entangled input gives zero marginal perturbation by tracelessness and joint BKM square $`a^{-1}\sum_j\mathrm{Tr}(A_j^2)`$. This proves $`G_\sigma(L)\ge m/384`$. The measure-and-prepare realization gives channels at sufficiently small nonzero signal with positive ordinary capacity. The probability argument gives existence of the channel observables.

The optimum weak-signal gain is thus $`\Theta(\min\{a,b^2-1\})`$ at every fixed full-rank baseline. The examples also give the arbitrary-channel lower bound when $`b\le a`$. In the large-$`b`$ regime, achieving quadratic order requires $`a=\Omega(b^2)`$ by the arbitrary-channel bound, and it is possible with $`a=O(b^2)`$.

## Exact coefficients at the maximally mixed baseline

For $`\sigma=I/b`$, use Hilbert–Schmidt orthonormal output directions and their enclosing radius $`R`$. The common BKM factor $`b`$ cancels. For a rank-$`k`$ input the numerator is

```math
\sum_{j,i,l}p_i p_l\,h(p_i,p_l)|(A_j)_{il}|^2
-\sum_j\bigl(\mathrm{Tr}(\rho_A A_j)\bigr)^2 .
```

Since $`pq\,h(p,q)\le(p+q)/2`$, the first sum is at most $`\sum_j\mathrm{Tr}[\rho_A(PA_jP)^2]`$ for Schmidt support $`P`$. Each term is at most $`R^2`$. A distinct bound uses $`pq\,h(p,q)\le\sqrt{pq}`$, since the logarithmic mean is at least the geometric mean. Let $`g`$ be a circular complex Gaussian on that support with covariance $`\sqrt{\rho_A}`$. Its fourth moments give

```math
\begin{aligned}
\sum_{j,i,l}\sqrt{p_i p_l}|(A_j)_{il}|^2
&\le \mathbb E\sum_j|g^\dagger A_j g|^2\\
&\le R^2\mathbb E\Vert g\Vert^4\\
&=R^2\bigl((\mathrm{Tr}\sqrt{\rho_A})^2+1\bigr)
\le R^2(k+1).
\end{aligned}
```

The first inequality drops the squared Gaussian means. The second uses the enclosing radius on every pure vector. Thus a rank-$`k`$ input yields at most $`\min\{r,k+1\}`$ in the local ratio.

When $`b\ge a\ge2`$, embed a full traceless Hilbert–Schmidt orthonormal input basis into the same number of orthonormal output directions. The input image has radius squared $`1-1/a`$ by purity and its average over a uniform input ensemble is zero. The maximally entangled calculation gives numerator $`(a^2-1)/a`$. Hence the optimum over directions is $`a+1`$, including the same-dimension depolarizing benchmark.

### Exact saturation of the output-rank coefficient

Suppose $`r\ge2`$ and a rank-$`k`$ input gives local ratio $`r`$. Each compressed moment must attain $`R^2`$. Because the input is faithful on the support, $`\Gamma_j=PA_jP/R`$ are Hermitian unitaries there. The radius bound gives $`\Vert\Gamma_i\pm\Gamma_j\Vert_\infty\le\sqrt2`$ for $`i\ne j`$. Squaring both signs proves anticommutation.

The $`\lfloor r/2\rfloor`$ involutions $`\mathrm{i}\Gamma_{2l-1}\Gamma_{2l}`$ commute. Conjugation by $`\Gamma_{2l-1}`$ flips exactly the $`l`$th sign in their joint eigenspaces. Every sign pattern has equal nonzero multiplicity, so $`k`$ is a positive multiple of $`2^{\lfloor r/2\rfloor}`$. A Clifford representation of that minimum size attains $`r`$ with a maximally entangled input, using tensor Pauli strings and their chirality product for odd $`r`$.

This dimension cost concerns exact saturation at the maximally mixed replacer. The Gaussian examples achieve the same order with a smaller input. Here the Schmidt rank describes a single-use capacity witness under standard unlimited preshared entanglement. A fixed operational supply per channel use requires a separate capacity model.

