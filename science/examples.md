# Worked channel comparisons

These examples explain what an output-only bound on entanglement assistance controls. We use memoryless, finite-dimensional channels, ordinary unassisted classical capacity $`C`$, the single-use Holevo quantity $`\chi`$, and unlimited-entanglement-assisted classical capacity $`C_E`$. All capacities here are in bits per channel use. The main proof uses natural logarithms; converting every capacity from nats to bits leaves all ratios and multiplicative bounds unchanged. Write $`b`$ for the dimension of the common output support and $`r`$ for the real affine dimension of the state image. The output-dimension theorem gives

```math
C_E(T)\le 16br\,\chi(T)\le 16b(b^2-1)C(T).
```

The factor is uniform over input dimension and over nonzero output eigenvalues. It is not an optimal enhancement factor. The capacity formulas used below are established benchmarks; the calculations make their implications for this bound explicit.

## 1. Identity: the familiar factor of two

For the identity channel on a $`b`$-dimensional register, with $`b\ge2`$,

```math
\chi(\mathrm{id}_b)=C(\mathrm{id}_b)=\log_2 b,
\qquad
C_E(\mathrm{id}_b)=2\log_2 b.
```

An orthogonal alphabet attains the unassisted rate, and the output dimension bounds it from above. For entanglement assistance, a purification of input $`\rho`$ remains pure, so its input-reference mutual information is $`2S(\rho)`$. The maximum occurs at $`\rho=I_b/b`$, yielding the usual dense-coding factor of two. This follows directly from the entanglement-assisted capacity theorem [BSST](../references/RELATED_WORK.md#bsst2002).

The image has $`r=b^2-1`$. Thus the universal bound is far from saturated even for a channel with a full-dimensional state image. Image dimension controls a uniform upper estimate; it does not determine the actual gain.

## 2. A classical channel: no entanglement-assisted gain

Let $`W(y\mid x)`$ be a stochastic matrix, and embed its input and output alphabets in fixed orthonormal bases:

```math
T_W(\rho)
=\sum_{x,y}W(y\mid x)\langle x|\rho|x\rangle\,|y\rangle\langle y|.
```

Then

```math
C_E(T_W)=C(T_W)=\chi(T_W)
=\max_{p(x)}I(X:Y).
```

To see the upper bound, take any reference-input state $`\rho_{RA}`$ and retain the classical input-basis label $`X`$ in an extension of the output. Writing $`\rho_R^x=\langle x|\rho_{RA}|x\rangle`$, which is subnormalized, this extension is

```math
\Omega_{RXY}
=\sum_{x,y}W(y\mid x)\rho_R^x\otimes|x\rangle\langle x|
\otimes|y\rangle\langle y|.
```

Conditioned on $`X`$, the systems $`R`$ and $`Y`$ are independent. Data processing and the mutual-information chain rule therefore give

```math
I(R:Y)\le I(RX:Y)=I(X:Y)\le C(W).
```

The capacity theorem [BSST](../references/RELATED_WORK.md#bsst2002) yields $`C_E(T_W)\le C(W)`$. Sending the basis states attains the ordinary Shannon rate, so the reverse inequalities follow. The affine dimension satisfies $`r\le b-1`$, after unused output symbols are removed. If $`C(W)=0`$, both capacities vanish and their ratio is undefined; the capacity inequality still applies.

### Classical output alone does not imply this equality

The assumption that the channel first reads a fixed input basis matters. A quantum measurement with noncommuting effects can have $`C_E>C`$, even though its output is a classical register. This is a known feature of measurement channels [Shor](../references/RELATED_WORK.md#shor2002) and [Holevo](../references/RELATED_WORK.md#holevo2012). A qubit trine measurement gives a short exact example.

Let $`\mathbf n_0,\mathbf n_1,\mathbf n_2`$ be coplanar unit vectors separated by $`120`$ degrees, and take

```math
E_y=\frac{I+\mathbf n_y\cdot\boldsymbol\sigma}{3},
\qquad
M(\rho)=\sum_{y=0}^2\mathrm{Tr}(E_y\rho)|y\rangle\langle y|.
```

For an input with Bloch vector $`\mathbf v`$, the probabilities obey

```math
p_y=\frac{1+\mathbf n_y\cdot\mathbf v}{3},
\qquad
\sum_y p_y^2=\frac13+\frac{\|\mathbf v_\parallel\|^2}{6}\le\frac12.
```

Hence $`H(p)\ge-\log_2\sum_y p_y^2\ge1`$. An input antipodal to one trine vector gives $`(0,1/2,1/2)`$, attaining this minimum. The uniform ensemble of the three antipodal inputs has uniform average output, and consequently

```math
\chi(M)=\log_2 3-1.
```

The channel is entanglement-breaking, so its Holevo quantity is additive [Shor](../references/RELATED_WORK.md#shor2002) and $`C(M)=\log_2 3-1`$. Each measurement effect is rank one; applying the measurement to one half of a purification leaves the reference conditionally pure. Therefore $`I(R:Y)=S(\rho)`$ and $`C_E(M)=1`$ [Holevo](../references/RELATED_WORK.md#holevo2012). Here $`b=3`$, $`r=2`$, and

```math
\frac{C_E(M)}{C(M)}=\frac{1}{\log_2 3-1}>1.
```

Thus neither a classical output register nor entanglement-breaking dynamics removes the possibility of an assisted classical-capacity gain.

## 3. Depolarizing channels: two distinct limits

Use the parameter convention

```math
D_{b,q}(\rho)=q\rho+(1-q)\frac{I_b}{b},
\qquad
-\frac{1}{b^2-1}\le q\le1,
\qquad b\ge2.
```

The stated interval is the full complete-positivity range. Negative $`q`$ is allowed in this parametrization; it is not a negative probability in a mixture of physical channels. At $`q=0`$ the map is a replacer. At $`q=1`$ it is the identity.

Define, with $`0\log_2 0=0`$,

```math
F_m(q)=\frac{1}{m}\left[
\bigl(1+(m-1)q\bigr)\log_2\bigl(1+(m-1)q\bigr)
+(m-1)(1-q)\log_2(1-q)
\right].
```

The exact capacities are

```math
C(D_{b,q})=\chi(D_{b,q})=F_b(q),
\qquad
C_E(D_{b,q})=F_{b^2}(q).
```

For the unassisted formula, every pure input has output eigenvalues

```math
\frac{1+(b-1)q}{b},\quad
\underbrace{\frac{1-q}{b},\ldots,\frac{1-q}{b}}_{b-1}.
```

Concavity of entropy makes these the minimum-entropy outputs. A uniform orthogonal input ensemble has average output $`I_b/b`$, giving $`\chi=\log_2 b-S_{\min}=F_b(q)`$. King's additivity theorem identifies this with the full regularized classical capacity throughout the stated complete-positivity interval [King](../references/RELATED_WORK.md#king2003).

For the assisted formula, unitary covariance and concavity of channel mutual information put its maximum at $`I_b/b`$ [BSST](../references/RELATED_WORK.md#bsst2002) and [Holevo](../references/RELATED_WORK.md#holevo2002). The normalized Choi state has eigenvalues

```math
\frac{1+(b^2-1)q}{b^2},\quad
\underbrace{\frac{1-q}{b^2},\ldots,\frac{1-q}{b^2}}_{b^2-1}.
```

Its two marginals are maximally mixed, so $`C_E=2\log_2 b-S(\text{Choi})=F_{b^2}(q)`$. For every $`q\ne0`$, the image has $`r=b^2-1`$; at $`q=0`$, $`r=0`$.

### Fixed output dimension and vanishing capacity

At fixed $`m`$, Taylor expansion gives

```math
F_m(q)
=\frac{m-1}{2\ln2}q^2
-\frac{(m-1)(m-2)}{6\ln2}q^3
+O_m(q^4).
```

It follows that, for fixed $`b`$,

```math
\lim_{q\to0,\ q\ne0}
\frac{C_E(D_{b,q})}{C(D_{b,q})}=b+1.
```

Both capacities vanish quadratically. Their ratio remains finite and can exceed the noiseless value two. At the exact replacer $`q=0`$, the ratio is $`0/0`$ and is not defined. This distinction is why the universal result is stated as a capacity inequality. The weak-signal enhancement is a standard benchmark [Holevo](../references/RELATED_WORK.md#holevo2002).

### The negative complete-positivity boundary as dimension grows

Now choose $`q_b=-1/(b^2-1)`$ and let $`b`$ grow. The channel becomes

```math
D_b^-(\rho)=\frac{bI_b-\rho}{b^2-1}.
```

The normalized Choi state is uniform on the subspace orthogonal to a maximally entangled vector. Put

```math
a_b=-\ln(1-b^{-2}),\qquad u_b=\ln(1+b^{-1}).
```

The preceding spectra yield the exact expressions

```math
C_E(D_b^-)=\frac{a_b}{\ln2},
\qquad
C(D_b^-)=\frac{ba_b-u_b}{(b+1)\ln2},
```

and therefore

```math
R_b:=\frac{C_E(D_b^-)}{C(D_b^-)}
=\frac{(b+1)a_b}{ba_b-u_b}.
```

These endpoint formulas were already given by Holevo [Holevo](../references/RELATED_WORK.md#holevo2002); King's theorem [King](../references/RELATED_WORK.md#king2003) supplies the equality with regularized $`C`$. Expanding the two logarithms gives

```math
C_E(D_b^-)=\frac{1}{b^2\ln2}\bigl(1+O(b^{-2})\bigr),
```

```math
C(D_b^-)=\frac{1}{2b^3\ln2}\bigl(1+O(b^{-1})\bigr),
```

```math
R_b=2b+\frac43-\frac{4}{9b}+O(b^{-2}).
```

In particular, $`R_b/[2(b+1)]\to1`$. The expression $`2(b+1)`$ correctly describes the leading multiplicative growth, but it is not an additive asymptote: $`R_b-2(b+1)\to-2/3`$. The fixed-$`b`$, $`q\to0`$ result $`b+1`$ and the present $`b\to\infty`$, $`q=q_b`$ result concern different orders of limits. The Taylor remainder in the former is not uniform in growing dimension.

This family requires any universal output-dimension enhancement factor to grow at least linearly with $`b`$. It does not establish that the optimal factor is linear. The bound $`16b(b^2-1)`$ remains cubic in the output dimension, leaving its dimension dependence unoptimized. For square channels, existing input-dimension bounds can be stronger; the distinct feature here is uniformity when the input dimension is unrestricted.

The boundary channel is itself entanglement-breaking. One explicit measure-and-prepare representation is

```math
D_b^-(\rho)
=\int b\langle\psi|\rho|\psi\rangle
\frac{I_b-|\psi\rangle\langle\psi|}{b-1}\,d\psi,
```

with normalized Haar measure on pure states. The Haar second-moment identity evaluates the integral to $`(bI_b-\rho)/(b^2-1)`$. This gives another example where destruction of transmitted entanglement coexists with a substantial assisted classical-capacity gain.

## 4. Input padding leaves the communication problem unchanged

For any channel $`T:A\to B`$, add an arbitrary finite input register $`K`$ and define

```math
\widetilde T_{AK\to B}=T\circ\mathrm{Tr}_K.
```

Let $`J(\rho)=\rho\otimes|0\rangle\langle0|_K`$. Then

```math
\widetilde T=T\circ\mathrm{Tr}_K,
\qquad
T=\widetilde T\circ J.
```

Each channel simulates the other by an allowed local preprocessing operation. These simulations hold at every block length, including encodings using preshared entanglement. Consequently

```math
C(\widetilde T)=C(T),\qquad
C_E(\widetilde T)=C_E(T).
```

The state images are exactly equal, so $`\chi`$, $`b`$ and $`r`$ are also unchanged. The input dimension can nevertheless be multiplied by any integer. An output-based estimate therefore remains fixed under this operationally irrelevant enlargement of the transmitter's register.

This padding example does not itself produce a larger enhancement. It explains why a bound that remains uniform in input dimension is a separate statement from an input-dimension estimate.

## Reproduction of the limiting calculation

[check_depolarizing_limits.py](../verification/check_depolarizing_limits.py) performs one focused, 100-decimal-digit check of the two depolarizing limits, the exact identity/replacer endpoints, and the cancellation-sensitive negative boundary. The saved values are in [depolarizing_limit_checks.json](../verification/expected/depolarizing_limit_checks.json). The dependency tested is `mpmath==1.3.0`. The calculation evaluates established capacity formulas and does not numerically optimize capacities.

From the repository root, reproduce the saved values with:

```bash
python verification/check_depolarizing_limits.py --compare verification/expected/depolarizing_limit_checks.json
```

Use `--output PATH` to write a fresh report instead of comparing the saved one.

At $`b=2`$, the negative-boundary ratio is $`5.0797593302113559\ldots`$. At $`b=10^6`$, the same calculation gives $`R_b-2b=1.3333328888888370\ldots`$, consistent with the derived $`4/3`$ constant. The checked formulas and asymptotic statements are proved above; the numerical calculation supplies a reproducible endpoint check.
