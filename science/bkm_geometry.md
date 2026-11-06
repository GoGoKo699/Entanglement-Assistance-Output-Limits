# BKM geometry for the capacity comparison

[Model and notation](model.md) · [Output-dimension theorem](output_bound.md)

The proof uses a quadratic form that adapts to the spectrum of a reference state. It controls relative entropy without replacing the reference state by a scalar lower bound. That distinction allows the final capacity estimate to remain uniform when output eigenvalues approach zero.

The identities below are standard Bogoliubov–Kubo–Mori (BKM) tools. We follow the presentation in [Wolff et al.](../references/RELATED_WORK.md#wolff2025), especially equations (6)–(9), (13), and (21)–(22); related relative-entropy comparisons appear in [Gao and Rouzé](../references/RELATED_WORK.md#gaorouze2022). The [next page](output_bound.md) applies these tools to the geometry of a channel's output image.

All logarithms on this page are natural. Dividing all entropies and information quantities by $`\ln 2`$ converts the resulting capacity inequalities to bits.

## The quadratic form

For a positive definite operator $`\tau`$, which need not have unit trace, define the derivative of the matrix logarithm by

```math
D\log_\tau(Y)
=\int_0^\infty
  (\tau+sI)^{-1}Y(\tau+sI)^{-1}\,ds.
```

It defines a sesquilinear inner product on all complex matrices of the same size:

```math
\langle X,Y\rangle_\tau
=\mathrm{Tr}\!\left[X^\dagger D\log_\tau(Y)\right],
\qquad
K_\tau(X)=\langle X,X\rangle_\tau.
```

The inner product is conjugate-linear in its first argument. The map $`D\log_\tau`$ is self-adjoint for the Hilbert–Schmidt inner product and preserves Hermitian operators. On the real vector space of Hermitian matrices, $`K_\tau`$ is the Hessian of $`\mathrm{Tr}(\tau\ln\tau)`$.

In an eigenbasis of $`\tau`$, with eigenvalues $`\lambda_i>0`$,

```math
\begin{aligned}
h(u,v)
&=\int_0^\infty\frac{ds}{(u+s)(v+s)}\\
&=\begin{cases}
\dfrac{\ln u-\ln v}{u-v},&u\ne v,\\[4pt]
\dfrac1u,&u=v,
\end{cases}\\[4pt]
K_\tau(X)
&=\sum_{i,j}h(\lambda_i,\lambda_j)|X_{ij}|^2.
\end{aligned}
```

Every weight is positive. This proves positive definiteness of the inner product and makes its extension from Hermitian to arbitrary complex matrices explicit. The integral also shows that $`h`$ decreases in either argument and that

```math
h(cu,cv)=\frac1c h(u,v),
\qquad
K_{c\tau}(X)=\frac1c K_\tau(X)
\quad(c>0).
```

## Monotonicity in the reference operator

**Lemma 1.** If $`0<\tau\le\eta`$, then

```math
K_\tau(X)\ge K_\eta(X)
```

for every complex matrix $`X`$.

**Proof.** For each $`s\ge0`$, inverse order gives

```math
R=(\tau+sI)^{-1}\ge S=(\eta+sI)^{-1}>0.
```

Vectorization expresses the integrand as the quadratic form of $`R^T\otimes R`$. This operator is ordered because

```math
R^T\otimes R-S^T\otimes S
=(R^T-S^T)\otimes R+S^T\otimes(R-S)\ge0.
```

Integrating the quadratic-form inequality proves the claim. The transpose is taken in any fixed orthonormal basis. $`\square`$

## Relative entropy and its quadratic upper bound

For density matrices $`\rho`$ and $`\tau`$, with $`\tau>0`$, write

```math
D(\rho\|\tau)
=\mathrm{Tr}\bigl[\rho(\ln\rho-\ln\tau)\bigr],
```

using the usual convention $`0\ln0=0`$. A reference state that is positive only on a common support can be treated by restricting every operator to that support.

**Lemma 2.** Let $`Z=\rho-\tau`$ and $`\rho_t=\tau+tZ`$. Then

```math
D(\rho\|\tau)
=\int_0^1(1-t)K_{\rho_t}(Z)\,dt
\le K_\tau(Z).
```

**Proof.** For positive definite $`\rho`$, the first equality is the integral Taylor formula for $`F(t)=\mathrm{Tr}(\rho_t\ln\rho_t)`$. Its second derivative is $`F''(t)=K_{\rho_t}(Z)`$; the first-order correction gives the relative entropy because $`\mathrm{Tr}Z=0`$.

For $`0\le t<1`$, positivity of $`\rho`$ gives $`\rho_t\ge(1-t)\tau`$. Lemma 1 and scaling imply

```math
K_{\rho_t}(Z)
\le\frac{1}{1-t}K_\tau(Z).
```

Substitution into the integral proves the upper bound. For singular $`\rho`$, replace it by $`(1-\delta)\rho+\delta\tau`$ and take $`\delta\downarrow0`$. Both relative entropy against the fixed positive $`\tau`$ and the quadratic form are continuous in this limit. The weighted integrand is bounded by the fixed $`K_\tau(Z)`$, so the integral identity passes to the limit as well. $`\square`$

## A segment bound for binary Holevo information

The next consequence turns operator domination into an information bound. For density matrices $`x,y`$, define their equiprobable binary Holevo information by

```math
J(x,y)
=S\!\left(\frac{x+y}{2}\right)
-\frac{S(x)+S(y)}2,
\qquad
S(x)=-\mathrm{Tr}(x\ln x).
```

**Lemma 3.** Suppose $`\tau`$ is a positive definite density matrix and $`x,y\le c\tau`$ for $`c\ge1`$. Then

```math
J(x,y)\ge\frac{1}{8c}K_\tau(x-y).
```

**Proof.** Every point $`z_t=(1-t)y+tx`$ of the segment is at most $`c\tau`$. When the endpoints are positive definite, Lemma 1 gives

```math
\frac{d^2}{dt^2}\mathrm{Tr}(z_t\ln z_t)
=K_{z_t}(x-y)
\ge\frac1c K_\tau(x-y).
```

Subtracting the quadratic function with this constant second derivative leaves a convex function. Its midpoint inequality yields the factor $`1/8`$. The entropy midpoint gap is exactly $`J(x,y)`$.

For singular endpoints, mix each with $`\delta\tau`$. These regularized endpoints still satisfy the same domination condition. Entropy and the fixed-center quadratic form are continuous as $`\delta\downarrow0`$. $`\square`$

## The Schmidt-weight inequality

**Lemma 4.** For positive scalars $`p,q,u,v`$,

```math
pq\,h(pu,qv)\le\max(p,q)\,h(u,v).
```

**Proof.** Set $`m=\min(p,q)`$. Monotonicity and homogeneity of $`h`$ give

```math
h(pu,qv)\le h(mu,mv)=\frac1m h(u,v).
```

Multiplying by $`pq`$ proves the assertion. In the channel proof, zero Schmidt coefficients are removed by restricting to the Schmidt support before applying this inequality. $`\square`$

This is the coefficient comparison used in [Wolff et al., equation (13)](../references/RELATED_WORK.md#wolff2025). It removes inverse powers of small Schmidt coefficients from the complete quadratic form. The [output-dimension proof](output_bound.md#complete-amplification-through-output-coordinates) then sums that form using Hermitian output coordinates.

## Continue

- [Model and operational definitions](model.md)
- [The output-dimension bound](output_bound.md)
- [Examples and comparisons](examples.md)
- [Interpretation and open questions](interpretation.md)
