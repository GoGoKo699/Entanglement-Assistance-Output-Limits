# Thirty milestones for the input and output dimension laws

[Learning route](README.md) · [Wilde bridge](WILDE_BRIDGE.md) · [Scientific account](../science/README.md) · [Output bound](../science/model.md#uniform-output-bound) · [Joint dimension laws](../science/joint-dimensions.md)

The scientific question is how the input and effective output dimensions control the gain in classical communication from unlimited preshared entanglement. This map follows the operational quantities, geometric estimates and channel examples that determine the sharp dimension laws.

The map has **14 background/preliminaries milestones, M01–M14, and 16 narrative/innovation milestones, M15–M30**. The background joins two foundations: channel capacities describe the communication task, while spectrum-dependent matrix geometry supplies the comparison tool. Its final milestone combines them into the precise comparison addressed by the proof. The narrative regularizes an achievable Holevo-radius center, carries the resulting bound through reference–output correlations, and explains why the dimensions needed for matching growth can be much smaller than those needed for exact saturation.

The single educational anchor is **Wilde2017**: Mark M. Wilde, *Quantum Information Theory*, second edition (2017). The [source bridge](WILDE_BRIDGE.md) gives the edition, access links, notation translation and the relevant sections: §11.6, §11.8, §§13.3–13.4, §20.3 and §21.3. Section references below always mean that edition. The book supplies the information-theoretic foundations; the local scientific pages supply the output-image construction and its derivation. Research sources cited below are primary proof dependencies or comparison results, not additional educational anchors.

Each milestone records an understanding target, its earlier dependencies and its place in the scientific argument. The map covers the project's connected story; specialist calculations and full proofs remain in the linked scientific sources.

<a id="background-preliminaries"></a>

## Phase 1: Background/preliminaries

The route moves from a single transmitted state to joint systems, information measures and asymptotic communication. It then assembles the dimensions and matrix geometry needed to state a uniform capacity comparison.

<a id="m01"></a>

### M01 — A classical message carried by a quantum system

**ID and phase:** M01 · background/preliminaries.

**Central question:** What is being transmitted, and which physical system carries it?

**Understanding target:** Distinguish a classical message, the quantum state used to encode it, the channel output and the receiver's measurement outcome. Explain why a classical communication task can still involve noncommuting quantum signals and collective decoding.

**Dependencies and story role:** None. This fixes the operational setting before introducing its mathematical representation.

**Conceptual connection:** A capacity concerns reliable message transmission through a physical channel; it is not simply the number of distinguishable states available in one measurement.

**Source pointers:** [Communication task](../science/model.md#communication-task); [Wilde bridge](WILDE_BRIDGE.md), for the route from physical systems to the capacity notation.

<a id="m02"></a>

### M02 — States, mixtures and occupied support

**ID and phase:** M02 · background/preliminaries.

**Central question:** What information does a density matrix contain about a signal's possible states?

**Understanding target:** Recognize a density matrix as a positive operator of trace one. Distinguish pure states, statistical mixtures and the support spanned by eigenvectors with nonzero eigenvalues. Explain why mixing preparations gives a convex set of states and why a zero eigenvalue identifies an unoccupied direction.

**Dependencies and story role:** M01. This supplies the local state geometry used when the channel's output image is constructed.

**Conceptual connection:** Support controls which output dimensions matter, while convexity later permits both binary signal ensembles and a center chosen inside the image.

**Source pointers:** [Effective output dimension](../science/model.md#effective-output-dimension); [Wilde bridge](WILDE_BRIDGE.md), for state and support conventions used in the project.

<a id="m03"></a>

### M03 — A channel and its entire output image

**ID and phase:** M03 · background/preliminaries.

**Central question:** Which properties make a linear map a physical quantum channel?

**Understanding target:** Explain the roles of complete positivity and trace preservation, including compatibility with an untouched reference system. Recognize that a finite-dimensional channel sends the compact convex input state space to a compact convex output image, and that a replacer produces the same output for every input.

**Dependencies and story role:** M01, M02. The focus expands from an individual signal to all signals available through one device.

**Conceptual connection:** The proof will use the full set of achievable outputs, including outputs of mixed inputs, rather than information about a single transmitted state.

**Source pointers:** [Communication model](../science/model.md#communication-task); [Output image and support](../science/model.md#effective-output-dimension).

<a id="m04"></a>

### M04 — Reference systems and purified inputs

**ID and phase:** M04 · background/preliminaries.

**Central question:** How can a pure joint state represent a mixed channel input?

**Understanding target:** Relate a bipartite state to its reduced states through partial trace. Explain purification and the Schmidt decomposition, including the correspondence between positive Schmidt coefficients and the support of each marginal. Distinguish the input sent through the channel from a reference retained outside it.

**Dependencies and story role:** M02, M03. Joint systems make the entanglement-assisted problem visible and prepare its later matrix expansion.

**Conceptual connection:** Bounding every purified input covers every mixed channel input in the entanglement-assisted capacity formula.

**Source pointers:** Wilde2017 §13.4 for the purified-input role in channel mutual information; [Two standard capacity facts](../science/model.md#two-standard-capacity-facts); [Schmidt expansion in the proof](../science/output_bound.md#complete-amplification-through-output-coordinates).

<a id="m05"></a>

### M05 — Entropy, relative entropy and units

**ID and phase:** M05 · background/preliminaries.

**Central question:** How do entropy and relative entropy measure different aspects of a quantum state?

**Understanding target:** Interpret entropy through a state's spectrum and relative entropy as an ordered comparison between two states. Keep the support condition for finite relative entropy explicit. Explain the convention for zero eigenvalues and why changing from natural logarithms to base two rescales all information quantities equally.

**Dependencies and story role:** M02. This introduces the state functionals from which the communication quantities and the geometric comparison are built.

**Conceptual connection:** The proof uses natural logarithms and the examples use bits; common rescaling preserves every capacity ratio and multiplicative constant.

**Source pointers:** Wilde2017 §11.8; [Entropy and divergence conventions](../science/model.md#communication-task); [Relative entropy in the geometry page](../science/bkm_geometry.md#relative-entropy-and-its-quadratic-upper-bound).

<a id="m06"></a>

### M06 — Correlation as relative entropy

**ID and phase:** M06 · background/preliminaries.

**Central question:** What does mutual information compare in a reference–output state?

**Understanding target:** Explain quantum mutual information both as an entropy combination and as relative entropy from the product of the marginals. Distinguish correlations in the joint state from entropy in either subsystem alone, and understand why local processing cannot increase mutual information.

**Dependencies and story role:** M04, M05. State comparisons now become a measure of correlations that a channel preserves with a reference.

**Conceptual connection:** Entanglement assistance is expressed through reference–output mutual information, which can be bounded using the same relative-entropy geometry as ordinary output states.

**Source pointers:** Wilde2017 §§11.6 and 11.8; [Mutual information convention](../science/model.md#communication-task); [Classical-channel comparison](../science/examples.md#2-a-classical-channel-no-entanglement-assisted-gain).

<a id="m07"></a>

### M07 — Ensembles and Holevo information

**ID and phase:** M07 · background/preliminaries.

**Central question:** How does a collection of possible output states carry information about a classical label?

**Understanding target:** Distinguish an ensemble's Holevo information from the channel quantity $`\chi(T)`$, which optimizes over input ensembles. Explain the difference between the entropy of an average output and the average output entropy. Recognize an equiprobable binary ensemble as a valid candidate in this optimization.

**Dependencies and story role:** M03, M05, M06. The discussion connects individual states to information encoded in a set of signals.

**Conceptual connection:** The optimized ensemble quantity also has a radius formulation. It bounds the relative entropy from each achievable output to a common achievable center.

**Source pointers:** Wilde2017 §13.3; [Definition of the Holevo quantity](../science/model.md#two-standard-capacity-facts); [Binary Holevo information](../science/bkm_geometry.md#a-segment-bound-for-binary-holevo-information).

<a id="m08"></a>

### M08 — Ordinary capacity and the coding theorem

**ID and phase:** M08 · background/preliminaries.

**Central question:** How does single-use Holevo information enter an asymptotic communication rate?

**Understanding target:** Explain memoryless repeated uses, block encoding and collective decoding. Distinguish the general ordinary capacity $`C(T)`$ from the single-use quantity $`\chi(T)`$. Identify HSW achievability as the reason $`\chi(T)\le C(T)`$; the accessible-information Holevo bound alone does not give that direction.

**Dependencies and story role:** M01, M07. This connects the local ensemble quantity to the global operational task.

**Conceptual connection:** The main argument only needs the achievable lower bound on ordinary capacity, so it does not require Holevo additivity for a general channel.

**Source pointers:** Wilde2017 §20.3; [Capacity facts](../science/model.md#two-standard-capacity-facts); primary coding theorems of [Holevo](../references/RELATED_WORK.md#holevo1998) and [Schumacher–Westmoreland](../references/RELATED_WORK.md#schumacher1997).

<a id="m09"></a>

### M09 — What entanglement assistance changes

**ID and phase:** M09 · background/preliminaries.

**Central question:** Which additional resource defines $`C_E(T)`$, and why does mutual information give its capacity?

**Understanding target:** Describe unlimited preshared entanglement without an extra communication channel. Explain the maximization over purified inputs in the entanglement-assisted capacity formula. Recover the factor of two for an identity channel while distinguishing that example from a claim about every noisy channel.

**Dependencies and story role:** M04, M06, M08. The two capacities can now be compared under their exact resource assumptions.

**Conceptual connection:** The proof must relate optimized reference–output correlations to information achievable without preshared entanglement through the same channel.

**Source pointers:** Wilde2017 §§13.4 and 21.3; [BSST theorem](../references/RELATED_WORK.md#bsst2002); [Identity example](../science/examples.md#1-identity-the-familiar-factor-of-two).

<a id="m10"></a>

### M10 — Input size, output support and affine image

**ID and phase:** M10 · background/preliminaries.

**Central question:** What do the input dimension $`a`$, effective output dimension $`b`$, and affine image dimension $`r`$ each count?

**Understanding target:** Explain why all outputs lie on $`\mathrm{supp}T(I_A)`$ and why the image contains a state positive on that support. Distinguish the support dimension from the number of independent real output variations, with $`r\le b^2-1`$. Relate the input dimension to the Schmidt rank of a pure reference–input state.

**Dependencies and story role:** M02, M03, M04. The operational setting is connected to the dimensions appearing in the theorems.

**Conceptual connection:** The output count can remain small even when the occupied input and reference spaces are large.

**Source pointers:** [Effective output dimension and affine span](../science/model.md#effective-output-dimension), [joint dimension laws](../science/joint-dimensions.md).

<a id="m11"></a>

### M11 — Expectations and matrix inequalities

**ID and phase:** M11 · background/preliminaries.

**Central question:** How can scalar expectation values control an operator statement?

**Understanding target:** Interpret $`X\le Y`$ as positivity of $`Y-X`$, rather than entrywise comparison. Relate a Hermitian operator's spectral norm to its largest absolute expectation over unit vectors. Distinguish control over all unit vectors from bounds on a few entries in one chosen basis.

**Dependencies and story role:** M02, M10. This supplies the matrix reasoning used for both the dominating center and the Hermitian coefficient operators.

**Conceptual connection:** Operator domination controls all output directions, while Hermiticity later turns pure-input expectation bounds into norm bounds independent of input dimension.

**Source pointers:** [Domination proof](../science/output_bound.md); [Hermitian coefficient bounds](../science/output_bound.md#complete-amplification-through-output-coordinates).

<a id="m12"></a>

### M12 — The spectrum-dependent BKM quadratic form

**ID and phase:** M12 · background/preliminaries.

**Central question:** Which local geometry is naturally associated with quantum relative entropy?

**Understanding target:** Explain the BKM form $`K_\sigma`$ as the Hessian of negative von Neumann entropy at a positive reference state and as a weighted squared size of matrix displacements. Recognize its positive spectral weights, its definition on complex matrices and its dependence on the entire reference spectrum.

**Dependencies and story role:** M05, M11. The proof's geometric tool is introduced without replacing the reference state by a smallest-eigenvalue estimate.

**Conceptual connection:** The same quadratic form can describe ordinary output variations and joint reference–output variations, allowing a direct comparison between them.

**Source pointers:** [The BKM quadratic form](../science/bkm_geometry.md#the-quadratic-form); primary presentations in [Gao–Rouzé](../references/RELATED_WORK.md#gaorouze2022) and [Wolff et al.](../references/RELATED_WORK.md#wolff2025). Wilde2017 §11.8 supplies the relative-entropy foundation.

<a id="m13"></a>

### M13 — From local curvature to a global divergence bound

**ID and phase:** M13 · background/preliminaries.

**Central question:** Why can a quadratic form bound relative entropy beyond an infinitesimal approximation?

**Understanding target:** Explain BKM order monotonicity and scaling, then connect them to the exact entropy integral along a state segment. Understand that $`D(\rho\Vert\sigma)\le K_\sigma(\rho-\sigma)`$ is a global inequality for density matrices $`\rho,\sigma`$ with a positive definite reference state $`\sigma`$, allowing singular $`\rho`$, rather than a truncated Taylor expansion.

**Dependencies and story role:** M12. The local metric becomes a usable tool for bounding full information quantities.

**Conceptual connection:** This inherited comparison is what permits a bound on the complete quadratic form to control entanglement-assisted communication.

**Source pointers:** [BKM order](../science/bkm_geometry.md#monotonicity-in-the-reference-operator); [Relative-entropy upper bound](../science/bkm_geometry.md#relative-entropy-and-its-quadratic-upper-bound); [Gao–Rouzé](../references/RELATED_WORK.md#gaorouze2022), Lemmas 2.1–2.2.

<a id="m14"></a>

### M14 — The uniform comparison that remains to be proved

**ID and phase:** M14 · background/preliminaries.

**Central question:** Why do separate capacity bounds leave the dimension dependence of their ratio open?

**Understanding target:** Use the two capacity formulas and output geometry to formulate a comparison $`C_E(T)\le f(a,b,r)\chi(T)`$. Explain why the multiplier must stay controlled when the ordinary capacity and the nonzero eigenvalues in the output spectrum become small. Identify the output-only estimate as one requirement and the simultaneous input and output constraint as another.

**Dependencies and story role:** M07, M08, M09, M10, M13. This synthesizes the background into the comparison addressed by the uniform proof.

**Conceptual connection:** A small capacity can be divided out only after bounding the assisted capacity proportionally to it.

**Source pointers:** [Why proximity to a replacer matters](../science/interpretation.md#why-proximity-to-a-replacer-matters), [prior bounds](../references/RELATED_WORK.md#position-of-the-result), [joint dimension laws](../science/joint-dimensions.md).

<a id="m15"></a>

### M15 — A Holevo-radius center with a spectral floor

**ID and phase:** M15 · narrative/innovation.

**Central question:** How can a single reference operator control every achievable output at small ordinary capacity?

**Understanding target:** Set $`\eta=\chi(T)`$ in nats and explain why the Holevo information radius supplies an achievable center $`\sigma`$ with $`D(x\Vert\sigma)\le\eta`$ for every output $`x`$. Apply the binary measurement of a unit-vector projector, then apply the classical variational inequality to get $`p\le(e-1)q+\eta`$, where $`p,q`$ are the measured probabilities for $`x,\sigma`$. Convert the bound over all unit vectors to $`x\le(e-1)\tau`$ for $`\tau=\sigma+\eta I_B`$.

**Dependencies and story role:** M05, M07, M10, M11, M14. This turns attainable communication information into a matrix-order estimate.

**Conceptual connection:** The floor depends on the channel’s own Holevo quantity. The domination constant is independent of output dimension and of the smallest output eigenvalue.

**Source pointers:** [Holevo-radius center and domination](../science/output_bound.md); [Entropy units](WILDE_BRIDGE.md#translating-notation-and-assumptions).

<a id="m16"></a>

### M16 — Relative entropy bounds the regularized radius

**ID and phase:** M16 · narrative/innovation.

**Central question:** How does the entropy radius around $`\sigma`$ control output deviations in the geometry defined by $`\tau`$?

**Understanding target:** Apply the relative-entropy Taylor integral along the segment from $`\sigma`$ to $`x`$. The whole segment lies below $`(e-1)\tau`$, so its BKM curvature is at least $`K_\tau(x-\sigma)/(e-1)`$. Integrate with weight $`1-s`$ and use $`D(x\Vert\sigma)\le\chi(T)`$ to obtain

```math
M:=\sup_{x\in\mathcal S_T}K_\tau(x-\sigma)
\le 2(e-1)\chi(T).
```

**Dependencies and story role:** M07, M12, M13, M15. This gives a bound on all achievable output deviations.

**Conceptual connection:** The reference state $`\sigma`$ determines the displacement and the achievable entropy radius. The larger positive operator $`\tau`$ sets the curvature used to measure that displacement.

**Source pointers:** [BKM order](../science/bkm_geometry.md#monotonicity-in-the-reference-operator); [Bound on the regularized output radius](../science/output_bound.md).

<a id="m17"></a>

### M17 — Remove the replacer and keep the output directions

**ID and phase:** M17 · narrative/innovation.

**Central question:** Which part of the channel carries variations away from the chosen center?

**Understanding target:** Define the replacement map $`R_\sigma(X)=\mathrm{Tr}(X)\sigma`$ and the difference $`\Delta=T-R_\sigma`$. Explain why Hermitian inputs map into the real translated image span $`V`$, while arbitrary complex inputs map into $`V+iV`$, whose Hermitian basis has $`r`$ elements.

**Dependencies and story role:** M03, M10, M15. The output geometry is rewritten as a linear map suited to tensoring with a reference.

**Conceptual connection:** The channel may have many input coordinates, but every output variation is expressible through the same finite collection of Hermitian output directions.

**Source pointers:** [Affine image dimension](../science/model.md#effective-output-dimension); [Replacement map and image span](../science/output_bound.md#complete-amplification-through-output-coordinates).

<a id="m18"></a>

### M18 — Hermitian coordinates transfer the radius to the input

**ID and phase:** M18 · narrative/innovation.

**Central question:** Why can each output coordinate be controlled without counting input basis states?

**Understanding target:** Explain how a Hermitian output basis orthonormal in the BKM form at $`\tau`$ defines the dual Hermitian input operators $`H_j`$. Relate Parseval's identity to the sum of squared coefficient expectations. Use the full set of pure input states and Hermiticity to obtain $`\Vert H_j\Vert_\infty^2\le M`$.

**Dependencies and story role:** M11, M12, M16, M17. The ordinary-output radius becomes a dimension-independent norm certificate for each coordinate.

**Conceptual connection:** The Hilbert–Schmidt adjoint transfers a metric coefficient to an input observable; a Hermitian spectral bound then replaces entry-by-entry input counting.

**Source pointers:** [Output basis, adjoint and coefficient operators](../science/output_bound.md#complete-amplification-through-output-coordinates); [Complex BKM inner product](../science/bkm_geometry.md#the-quadratic-form).

<a id="m19"></a>

### M19 — Schmidt weights in the joint quadratic form

**ID and phase:** M19 · narrative/innovation.

**Central question:** What happens to the metric when an input is entangled with a reference?

**Understanding target:** Expand a pure joint state in its positive Schmidt coefficients and relate the product reference spectrum to the BKM spectral weights. Explain how the scalar weight comparison replaces the potentially singular-looking factors by $`\max(p_k,p_l)`$, without an inverse-smallest-Schmidt-coefficient constant.

**Dependencies and story role:** M04, M12, M18. The coordinate bounds are brought into the full reference–output expression.

**Conceptual connection:** This inherited coefficient inequality handles the reference spectrum; the output-coordinate construction determines how its remaining sums are controlled.

**Source pointers:** [Schmidt-weight inequality](../science/bkm_geometry.md#the-schmidt-weight-inequality); [Joint quadratic-form expansion](../science/output_bound.md#complete-amplification-through-output-coordinates); [Wolff et al.](../references/RELATED_WORK.md#wolff2025), equation (13).

<a id="m20"></a>

### M20 — Compress to the occupied Schmidt subspace

**ID and phase:** M20 · narrative/innovation.

**Central question:** Why must a Schmidt-index sum use the compressed coefficient operator?

**Understanding target:** Let $`P`$ project onto the input Schmidt support. Explain why the sum weighted by $`p_k+p_l`$ equals twice the second moment of $`PH_jP`$, and why this is at most twice the full second moment. Recognize the positive difference

```math
PH_j^2P-(PH_jP)^2
=PH_j(I-P)H_jP\ge0.
```

**Dependencies and story role:** M11, M18, M19. This resolves the support boundary in the amplification argument, including rank-deficient input marginals.

**Conceptual connection:** Couplings from the occupied subspace to its orthogonal complement can contribute to the full second moment. They justify an inequality, not equality with the compressed moment.

**Source pointers:** [Support-compression step](../science/output_bound.md#complete-amplification-through-output-coordinates); [Exact compression regression](../verification/README.md#complete-amplification-audit).

<a id="m21"></a>

### M21 — Two counts control the same joint perturbation

**ID and phase:** M21 · narrative/innovation.

**Central question:** How do output coordinates and input Schmidt blocks give different estimates?

**Understanding target:** Use individual output-coordinate bounds to obtain $`2rM`$. Then average equal superpositions of two Schmidt vectors over their relative phase to bound the squared output BKM norm of each off-diagonal block by $`2M`$. Sum the block weights to obtain $`(4k-3)M`$ on Schmidt rank $`k`$.

**Dependencies and story role:** M16, M18, M19, M20. Both estimates control the same joint quadratic form.

**Conceptual connection:** The smaller count applies with the same reference operator. Output rank can control the bound when the input is large, and occupied input dimension can control it when there are many output directions.

**Source pointers:** [Output-coordinate amplification](../science/output_bound.md#complete-amplification-through-output-coordinates), [Schmidt block estimate](../science/joint-dimensions.md).

<a id="m22"></a>

### M22 — Account for the floor and recover the capacity bounds

**ID and phase:** M22 · narrative/innovation.

**Central question:** What does it cost to compare the joint output with the product operator $`\rho_R\otimes\tau`$?

**Understanding target:** Apply the relative-entropy upper bound for a positive reference operator of arbitrary trace. Explain why the marginal divergence is nonnegative and why the floor shift has squared BKM norm at most $`b\chi(T)`$. Combine the costs with M21 through the BKM triangle inequality, then use BSST and HSW to obtain the uniform multiplier.

```math
\left(\sqrt{2(e-1)\min\{2r,4a-3\}}+\sqrt b\right)^2.
```

**Dependencies and story role:** M06, M08, M09, M13, M16, M21. This integrates the joint quadratic estimates and the regularization cost with both capacity formulas.

**Conceptual connection:** The floor contributes at most $`\chi(T)`$ per output dimension to its squared BKM norm. The remaining count comes from either the affine output coordinates or the occupied input directions.

**Source pointers:** [Passage from the quadratic bound to capacities](../science/output_bound.md#from-the-quadratic-bound-to-capacities), [joint dimension bound](../science/joint-dimensions.md), Wilde2017 §§20.3 and 21.3.

<a id="m23"></a>

### M23 — Uniformity at small capacity and near rank loss

**ID and phase:** M23 · narrative/innovation.

**Central question:** Which limiting channels are included in the theorem's quantifiers?

**Understanding target:** Use the capacity inequality to handle the replacer, where both rates are zero. Explain how the floor of size $`\chi(T)`$ can vanish along a channel family while the final estimate still has the same coefficient for fixed $`b,r`$. Understand why the same dimension factor applies to sequences with tiny capacities or output eigenvalues, and why divergent enhancement requires growing effective output dimension.

**Dependencies and story role:** M10, M14, M15, M22. The completed theorem is checked against the boundaries that motivated it.

**Conceptual connection:** Uniformity concerns the final capacity comparison, even when the individual metrics and channel-dependent centers change substantially along a family.

**Source pointers:** [The theorem and zero-capacity conventions](../science/model.md#uniform-output-bound); [Receiver-side consequence](../science/interpretation.md#quantum-and-commuting-outputs); [Rank-loss discussion](../science/interpretation.md).

<a id="m24"></a>

### M24 — Image dimension does not determine the gain

**ID and phase:** M24 · narrative/innovation.

**Central question:** What can identity, classical and measurement channels teach about the bound's meaning?

**Understanding target:** Contrast the identity channel's factor of two with the absence of an assisted gain for a fixed-basis classical stochastic channel. Explain why a noncommuting trine measurement can benefit despite a classical output and entanglement-breaking dynamics. Relate commuting output images to $`r\le b-1`$ without inferring equality of capacities.

**Dependencies and story role:** M06, M09, M10, M22. Established examples separate a uniform geometric bound from an exact characterization of enhancement.

**Conceptual connection:** Output dimension and affine dimension constrain a universal upper estimate; the encoding and measurement structure still determine the actual capacity ratio.

**Source pointers:** [Identity and classical examples](../science/examples.md); [Classical output and the trine measurement](../science/examples.md#classical-output-alone-does-not-imply-this-equality); [Shor](../references/RELATED_WORK.md#shor2002) and [Holevo](../references/RELATED_WORK.md#holevo2012).

<a id="m25"></a>

### M25 — Enlarging an irrelevant input register

**ID and phase:** M25 · narrative/innovation.

**Central question:** Why do separate input and output counts describe different channel restrictions?

**Understanding target:** Explain how appending an input register that the channel discards enlarges $`a`$ while preserving the state image and both capacities. Use local preprocessing in both directions to justify the equality for arbitrary block codes, including entanglement-assisted codes.

**Dependencies and story role:** M03, M08, M09, M22. A concrete invariance connects the uniform theorem to the communication task.

**Conceptual connection:** The output-image estimate survives input padding. With actual input dimension constrained, the Schmidt-block estimate can supply a smaller upper bound.

**Source pointers:** [Input-padding construction](../science/examples.md#4-input-padding-leaves-the-communication-problem-unchanged), [joint dimension laws](../science/joint-dimensions.md).

<a id="m26"></a>

### M26 — Weak depolarizing signals at fixed dimension

**ID and phase:** M26 · narrative/innovation.

**Central question:** What happens to enhancement when a fixed-dimensional channel approaches a replacer?

**Understanding target:** Interpret the depolarizing parameter and the exact ordinary and assisted capacity formulas. At fixed $`b`$, explain why both capacities vanish quadratically as the parameter tends to zero while their ratio approaches $`b+1`$. Keep this limit distinct from the undefined ratio at the exact replacer.

**Dependencies and story role:** M05, M07, M09, M23. A solvable family shows why comparing small capacities is physically informative.

**Conceptual connection:** An enhancement greater than two is compatible with both rates being small and with a finite uniform bound at fixed output dimension.

**Source pointers:** [Depolarizing model and capacities](../science/examples.md#3-depolarizing-channels-two-distinct-limits); [Fixed-dimension weak-signal limit](../science/examples.md#fixed-output-dimension-and-vanishing-capacity); [Holevo](../references/RELATED_WORK.md#holevo2002) and [King](../references/RELATED_WORK.md#king2003).

<a id="m27"></a>

### M27 — Matching weak-signal constructions and exact saturation

**ID and phase:** M27 · narrative/innovation.

**Central question:** Which input resources give the sharp order, and which give equality in the local affine-dimension bound?

**Understanding target:** Explain how a full-rank replacer makes both capacities quadratic in signal strength and how a maximally entangled input accumulates orthogonal reference correlations. Compare the bounded ordinary image radius of the traceless Gaussian observables with that of the Clifford family. Use Shor’s additivity to identify $`C=\chi`$ for these channels. At the maximally mixed replacer, explain why exact saturation of the local $`r`$ bound for $`r\ge2`$ forces Clifford observables on the occupied support.

**Dependencies and story role:** M07, M09, M10, M24, M26. The constructions and the equality argument give two different dimension requirements.

**Conceptual connection:** A sender of dimension proportional to $`b^2`$ suffices for quadratic growth. Exact local saturation with $`r`$ active directions requires Schmidt rank at least $`2^{\lfloor r/2\rfloor}`$.

**Source pointers:** [Local law and saturation](../science/joint-dimensions.md), [Clifford and commuting families](../science/sharp_examples.md), [Shor’s additivity theorem](../references/RELATED_WORK.md#shor2002).

<a id="m28"></a>

### M28 — Inherited tools and the new dimension law

**ID and phase:** M28 · narrative/innovation.

**Central question:** Which gap closes relative to the earlier input and output estimates?

**Understanding target:** Attribute the capacity formulas, BKM comparisons, and input-block estimates to their sources. Explain how one regularized output reference makes both amplification counts usable without spectral conditioning. Identify the matching lower construction that turns the combined bound into a sharp order for $`b\le a`$.

**Dependencies and story role:** M14, M15, M16, M21, M22, M25, M27. The result is placed within the established communication and mathematical framework.

**Conceptual connection:** The matching law concerns a simultaneous restriction on the channel’s input and output dimensions. The output-only bound still applies when the input can grow arbitrarily.

**Source pointers:** [Position of the result](../references/RELATED_WORK.md#position-of-the-result), [joint dimension laws](../science/joint-dimensions.md), [Wolff et al.](../references/RELATED_WORK.md#wolff2025) and [Belzig](../references/RELATED_WORK.md#belzig2023).

<a id="m29"></a>

### M29 — What finite verification establishes

**ID and phase:** M29 · narrative/innovation.

**Central question:** How do reproducible calculations support the two analytical dimension laws?

**Understanding target:** Explain the roles of finite amplification checks, the support-compression regression, the regularization floor, weak-signal calculations, and the exact depolarizing benchmark. Distinguish the Hermiticity-preserving maps in the amplification checks from physical measure-and-prepare channels. Identify which conclusions require the exact proof.

**Dependencies and story role:** M20, M21, M27. The capacity theorems and matching examples are connected to their reproducible evidence.

**Conceptual connection:** Finite calculation helps detect a faulty compression identity, coefficient, or limit. The proofs establish bounds over all allowed channel dimensions and spectra.

**Source pointers:** [Verification route](../verification/README.md), [complete-amplification audit](../verification/README.md#complete-amplification-audit), [joint dimension laws](../science/joint-dimensions.md).

<a id="m30"></a>

### M30 — Sharp order, local limit and exact equality

**ID and phase:** M30 · narrative/innovation.

**Central question:** Which statements hold for arbitrary channels, and which use a fixed full-rank replacer?

**Understanding target:** Trace the arbitrary-channel bound from the regularized Holevo radius to both amplification counts. Combine it with the weak-signal examples to give the worst-case order $`\min\{a,b^2-1\}`$ when $`b\le a`$. State the matching local law for every aspect ratio with a fixed full-rank replacer. At the maximally mixed replacer, explain the sharper local bound $`\min\{r,k+1\}`$ and what exact saturation at $`r\ge2`$ entails.

**Dependencies and story role:** M22, M23, M24, M27, M28, M29. The final synthesis separates the regimes and connects each claim to its proof.

**Conceptual connection:** The output-only bound holds uniformly and commuting outputs retain linear order in $`b`$. A sharp order for arbitrary signal strengths and arbitrarily large output-to-input dimension ratio remains open.

**Source pointers:** [Exact output claims](../science/model.md#uniform-output-bound), [global and local joint dimension laws](../science/joint-dimensions.md), [matching examples](../science/sharp_examples.md).
