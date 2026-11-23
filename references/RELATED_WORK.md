# Related work and source attribution

The communication model is a finite-dimensional memoryless quantum channel with ordinary asymptotic classical capacity $`C`$, single-use Holevo quantity $`\chi`$, and classical capacity $`C_E`$ assisted by unlimited preshared entanglement. There is no additional communication channel. The dimension $`b`$ is the common support dimension of the channel outputs; it does not bound the receiver's local share of the preshared entanglement.

Machine-readable records for every source below are in [references.bib](references.bib).

## Position of the result

For a channel $`T`$ whose output-state image has real affine dimension $`r`$ and effective support dimension $`b`$, the [main proof](../science/output_bound.md) gives

```math
C_E(T)\le \bigl(2\sqrt{(e-1)r}+\sqrt b\bigr)^2\,\chi(T).
```

The [measure-and-prepare family](../science/sharp_examples.md) approaches ratio $`b^2-1`$ at fixed $`b`$. These results give the sharp quadratic order of the largest gain, uniformly over finite input dimensions and output spectra.

| Result | Dependence of the bound | Relation to this project |
|---|---|---|
| [Wolff et al. (2025)](#wolff2025) | Input dimension, asymptotically $`8d_A^2/\ln d_A`$. The proof also bounds $`C_E/\chi`$. | Asks whether an output-only bound exists. |
| [Belzig (2023), Theorem 4.4.2](#belzig2023) | Near the associated replacer, $`4\ln(2)d_B^5/\lambda_{\min}(\sigma_*)`$. | Retains the least eigenvalue of the output divergence center. |
| Present theorem | Effective output support and affine image dimension. | Gives the sharp quadratic order in the output dimension, including rank-changing limits. |

[Chitambar et al.](#chitambar2023) study a one-use guessing score called communication value. Its output-dimension bounds pertain to that score. The capacities here concern reliable transmission over arbitrarily many independent uses.

## Inherited tools and the uniform step

The [Bennett–Shor–Smolin–Thapliyal theorem](#bsst2002) identifies $`C_E(T)`$ with a maximum over reference–output mutual information. The coding theorems of [Schumacher–Westmoreland](#schumacher1997) and [Holevo](#holevo1998) supply $`\chi(T)\le C(T)`$. [Gao–Rouzé](#gaorouze2022) and [Wolff et al.](#wolff2025) provide the relative-entropy and BKM estimates used in the argument.

The proof starts with the mean of an optimal Holevo ensemble and uses its relative-entropy radius. A binary divergence inequality controls the whole output image by a constant multiple of that state plus $`\chi(T)I`$. Comparing relative entropy along the image segment then bounds its BKM radius. The BKM amplification still resolves only the $`r`$ active output directions. An explicit trace correction accounts for the added identity.

The lower example uses anticommuting Hermitian unitaries to keep the output coefficient vector of every unassisted input in a Euclidean unit ball. A maximally entangled input contributes all output directions to the leading squared joint norm. [Shor's theorem](#shor2002) identifies the unassisted capacity of this measure-and-prepare channel with its single-use Holevo quantity. The [spin-unitary background](#farenick2021) supplies the operator geometry.

## Established benchmark channels

[Holevo](#holevo2002) and [King](#king2003) give the depolarizing capacity formulas. At fixed dimension, the gain tends to $`b+1`$ as the signal vanishes. At the negative complete-positivity boundary, the gain grows as $`2b(1+o(1))`$. These families give useful exact benchmarks at comparable input and output dimensions.

The worked trine example uses [Shor's additivity theorem](#shor2002) and [Holevo's measurement-channel formula](#holevo2012). A rank-one trine measurement has $`C_E=1`$ and $`C=\log_2 3-1`$.

## Primary sources

<a id="wolff2025"></a>

### Wolff et al. — Input-dimension bound

Lasse H. Wolff, Paula Belzig, Matthias Christandl, Bergfinnur Durhuus, and Marco Tomamichel, “Fundamental Limit on the Power of Entanglement Assistance in Quantum Communication,” *Physical Review Letters* **134**, 020802 (2025). [DOI: 10.1103/PhysRevLett.134.020802](https://doi.org/10.1103/PhysRevLett.134.020802). [arXiv:2408.17290](https://arxiv.org/abs/2408.17290).

Relevant locations in [version 3](https://arxiv.org/html/2408.17290v3): Section II for the bound; Section III.2 and Appendix equations (21)–(22) for the inherited BKM estimates; the end of Section III.3 for replacing $`C`$ by $`\chi`$; Section IV for the output-only open question.

<a id="belzig2023"></a>

### Belzig — Output dimension with a conditioning factor

Paula Belzig, *Quantum communication and fault-tolerance*, PhD thesis, University of Copenhagen (2023). [University manuscript](https://noter.math.ku.dk/phd23pb.pdf). [arXiv:2412.20736](https://arxiv.org/abs/2412.20736), posted in 2024.

Relevant locations: Chapter 4, especially Theorem 4.4.2, printed pages 129–130, and Section 4.5, printed pages 131–132. The near-replacer theorem assumes $`\Vert T-R_{\sigma_*}\Vert_{1\to1}\le1/(2d_B)`$ and retains $`\lambda_{\min}(\sigma_*)^{-1}`$. The thesis was submitted and defended in 2023; the later arXiv posting does not change that thesis date.

<a id="gaorouze2022"></a>

### Gao–Rouzé — BKM and relative-entropy comparisons

Li Gao and Cambyse Rouzé, “Complete Entropic Inequalities for Quantum Markov Chains,” *Archive for Rational Mechanics and Analysis* **245**, 183–238 (2022). [DOI: 10.1007/s00205-022-01785-1](https://doi.org/10.1007/s00205-022-01785-1).

Relevant locations: Lemma 2.1 for weighted quadratic-form order comparison, and Lemma 2.2 for the two-sided comparison with relative entropy and the Hessian argument. These are also credited explicitly by Wolff et al.

<a id="bsst2002"></a>

### Bennett–Shor–Smolin–Thapliyal — Entanglement-assisted capacity

Charles H. Bennett, Peter W. Shor, John A. Smolin, and Ashish V. Thapliyal, “Entanglement-assisted capacity of a quantum channel and the reverse Shannon theorem,” *IEEE Transactions on Information Theory* **48**(10), 2637–2655 (2002). [DOI: 10.1109/TIT.2002.802612](https://doi.org/10.1109/TIT.2002.802612). [arXiv:quant-ph/0106052](https://arxiv.org/abs/quant-ph/0106052).

Relevant locations: Theorem 1, equation (7), and Section II of [version 2](https://arxiv.org/html/quant-ph/0106052v2). The present proof uses the general entanglement-assisted capacity formula, not the reverse Shannon theorem.

<a id="holevo1998"></a>

### Holevo — Classical coding with general signal states

Alexander S. Holevo, “The capacity of the quantum channel with general signal states,” *IEEE Transactions on Information Theory* **44**(1), 269–273 (1998). [DOI: 10.1109/18.651037](https://doi.org/10.1109/18.651037). [arXiv:quant-ph/9611023](https://arxiv.org/abs/quant-ph/9611023).

The coding theorem for classical–quantum channels with possibly mixed signal states supplies the achievability used in $`\chi(T)\le C(T)`$.

<a id="schumacher1997"></a>

### Schumacher–Westmoreland — Classical coding through noisy quantum channels

Benjamin Schumacher and Michael D. Westmoreland, “Sending classical information via noisy quantum channels,” *Physical Review A* **56**, 131–138 (1997). [DOI: 10.1103/PhysRevA.56.131](https://doi.org/10.1103/PhysRevA.56.131).

Together with Holevo's independent theorem, this is the primary coding reference for the ordinary-capacity lower bound.

<a id="king2003"></a>

### King — Depolarizing-channel classical capacity

Christopher King, “The Capacity of the Quantum Depolarizing Channel,” *IEEE Transactions on Information Theory* **49**(1), 221–229 (2003). [DOI: 10.1109/TIT.2002.806153](https://doi.org/10.1109/TIT.2002.806153). [arXiv:quant-ph/0204172](https://arxiv.org/abs/quant-ph/0204172).

Relevant locations: equation (2) for the full complete-positivity range; equations (9)–(11) for the output entropy and Holevo formula; Theorems 1–2 for additivity and equality with the regularized classical capacity.

<a id="holevo2002"></a>

### Holevo — Depolarizing-channel entanglement assistance

Alexander S. Holevo, “On Entanglement-Assisted Classical Capacity,” *Journal of Mathematical Physics* **43**(9), 4326–4333 (2002). [DOI: 10.1063/1.1495877](https://doi.org/10.1063/1.1495877). [arXiv:quant-ph/0106075](https://arxiv.org/abs/quant-ph/0106075).

Relevant locations: equations (23)–(26) and the subsequent discussion of the two depolarizing limits. The exact endpoint formulas yield the more precise expansion $`2b+4/3-4/(9b)+O(b^{-2})`$. The paper's $`2(b+1)`$ describes the leading multiplicative growth, rather than an additive asymptote.

<a id="shor2002"></a>

### Shor — Entanglement-breaking channel additivity

Peter W. Shor, “Additivity of the Classical Capacity of Entanglement-Breaking Quantum Channels,” *Journal of Mathematical Physics* **43**(9), 4334–4340 (2002). [DOI: 10.1063/1.1498000](https://doi.org/10.1063/1.1498000). [arXiv:quant-ph/0201149](https://arxiv.org/abs/quant-ph/0201149).

This supplies $`C=\chi`$ for the trine measurement and the Clifford measure-and-prepare examples.

<a id="holevo2012"></a>

### Holevo — Measurement-channel information capacity

Alexander S. Holevo, “Information Capacity of a Quantum Observable,” *Problems of Information Transmission* **48**(1), 1–10 (2012). [DOI: 10.1134/S0032946012010012](https://doi.org/10.1134/S0032946012010012). [arXiv:1103.2615](https://arxiv.org/abs/1103.2615).

Relevant locations: Section 2 for measurement-channel capacities and Section 3, equation (9), for the entanglement-assisted capacity of rank-one measurements.

<a id="chitambar2023"></a>

### Chitambar et al. — Communication value

Eric Chitambar, Ian George, Brian Doolittle, and Marius Junge, “The Communication Value of a Quantum Channel,” *IEEE Transactions on Information Theory* **69**, 1660–1679 (2023). Section VI studies assistance for the one-use guessing score. [arXiv:2109.11144](https://arxiv.org/abs/2109.11144).

<a id="farenick2021"></a>

### Farenick et al. — Spin unitaries

Douglas Farenick, Farrah Huntinghawk, Adili Masanika, and Sarah Plosker, “Complete Order Equivalence of Spin Unitaries,” *Linear Algebra and its Applications* **610**, 1–28 (2021). The spin-unitary relations are background for the Clifford geometry. [arXiv:2006.06810](https://arxiv.org/abs/2006.06810).
