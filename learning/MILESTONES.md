# Thirty milestones for the output-dimension bound

[Learning route](README.md) · [Wilde bridge](WILDE_BRIDGE.md) · [Scientific account](../science/README.md) · [Exact theorem](../science/model.md#uniform-output-bound)

The scientific question is whether unlimited preshared entanglement can produce an unbounded relative advantage for classical communication when each channel use delivers a system of fixed dimension. This map follows the objects, operational quantities and geometric mechanism needed to understand the uniform bound and its limits.

The map has **14 background/preliminaries milestones, M01–M14, and 16 narrative/innovation milestones, M15–M30**. The background joins two foundations: channel capacities describe the communication task, while spectrum-dependent matrix geometry supplies the comparison tool. Its final milestone combines them into the precise comparison addressed by the proof. The narrative begins with a state inside the output image, builds the amplification argument, and then places the theorem among examples, earlier bounds and the remaining scaling question. The allocation follows these two connected parts of this project.

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

**Conceptual connection:** A binary ensemble involving the proof's center will turn a geometric output displacement into an achievable information quantity.

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

### M10 — Two different dimensions of the output

**ID and phase:** M10 · background/preliminaries.

**Central question:** What do the effective output dimension $`b`$ and the affine image dimension $`r`$ each count?

**Understanding target:** Explain why all outputs are supported on $`\mathrm{supp}T(I_A)`$ and why the image contains a state positive on that support. Distinguish this support dimension from the number of real independent output variations, with $`r\le b^2-1`$. Keep both distinct from the input dimension and the receiver's entanglement register.

**Dependencies and story role:** M02, M03. The operational setting is connected to the two geometric parameters appearing in the theorem.

**Conceptual connection:** Removing inactive output dimensions makes the statement intrinsic to the channel; counting affine directions will remove input dimension from amplification.

**Source pointers:** [Effective output dimension and affine span](../science/model.md#effective-output-dimension); [Receiver-side constraint](../science/interpretation.md#the-receiver-side-constraint).

<a id="m11"></a>

### M11 — Expectations and matrix inequalities

**ID and phase:** M11 · background/preliminaries.

**Central question:** How can scalar expectation values control an operator statement?

**Understanding target:** Interpret $`X\le Y`$ as positivity of $`Y-X`$, rather than entrywise comparison. Relate a Hermitian operator's spectral norm to its largest absolute expectation over unit vectors. Distinguish control over all unit vectors from bounds on a few entries in one chosen basis.

**Dependencies and story role:** M02, M10. This supplies the matrix reasoning used for both the dominating center and the Hermitian coefficient operators.

**Conceptual connection:** Operator domination controls all output directions, while Hermiticity later turns pure-input expectation bounds into norm bounds independent of input dimension.

**Source pointers:** [Domination proof](../science/output_bound.md#an-output-state-that-dominates-the-whole-image); [Hermitian coefficient bounds](../science/output_bound.md#complete-amplification-through-output-coordinates).

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

**Central question:** Why do familiar capacity and dimension bounds leave the fixed-output enhancement question open?

**Understanding target:** Assemble the two capacity formulas and the output geometry into the goal $`C_E(T)\le f(b)\chi(T)`$. Explain why an absolute bound on $`C_E`$ does not control its ratio to a capacity approaching zero, and why an inverse-eigenvalue factor fails to give uniform control near rank loss.

**Dependencies and story role:** M07, M08, M09, M10, M13. This synthesizes the background into the exact comparison that the new argument must supply.

**Conceptual connection:** A successful proof must use output dimension alone while allowing arbitrarily large finite input spaces, arbitrarily small positive capacities and arbitrarily small nonzero output eigenvalues.

**Source pointers:** [Why proximity to a replacer matters](../science/interpretation.md#why-proximity-to-a-replacer-matters); [Prior bounds and their distinction](../references/RELATED_WORK.md#position-of-the-result); [Wolff et al.](../references/RELATED_WORK.md#wolff2025), Section IV; [Belzig](../references/RELATED_WORK.md#belzig2023), Theorem 4.4.2 and Section 4.5.

<a id="narrative-innovation"></a>

## Phase 2: Narrative/innovation

The argument begins inside one channel's output image. It constructs a common geometric center, converts its radius to ordinary communication, and controls entangled-input amplification through output directions. The remaining milestones connect that proof to its operational scope, examples and scientific significance.

<a id="m15"></a>

### M15 — A dominating state inside the image

**ID and phase:** M15 · narrative/innovation.

**Central question:** Can one achievable output control every other output without a spectral cutoff?

**Understanding target:** Explain why maximizing determinant on the compact output image produces a positive state on the common support. Connect the one-sided derivative of log determinant to $`\mathrm{Tr}(\sigma^{-1}x)\le b`$, and then to the operator domination $`x\le b\sigma`$ for every achievable output.

**Dependencies and story role:** M10, M11, M14. This is the first local construction in the new argument.

**Conceptual connection:** The center is both geometrically useful and physically achievable. Its feasibility will make the next information bound available even when its least eigenvalue is small.

**Source pointers:** [Dominating output state, Lemma 1](../science/output_bound.md#an-output-state-that-dominates-the-whole-image); [Attribution of the standard optimization ingredients](../references/RELATED_WORK.md#inherited-tools-and-the-uniform-step).

<a id="m16"></a>

### M16 — A binary ensemble pays for the output radius

**ID and phase:** M16 · narrative/innovation.

**Central question:** How does domination by an achievable center turn output geometry into ordinary information?

**Understanding target:** Use the entropy curvature along the segment between $`x`$ and $`\sigma`$ to compare their binary Holevo information with BKM displacement. Explain why both endpoints being in the image gives

```math
M:=\sup_{x\in\mathcal S_T}K_\sigma(x-\sigma)
\le 8b\,\chi(T).
```

**Dependencies and story role:** M07, M12, M13, M15. The center construction is converted into a bound on the whole image using a feasible communication ensemble.

**Conceptual connection:** The proof retains the spectrum-sensitive metric while bounding its radius by achievable information; it does not replace that metric with an inverse-eigenvalue norm estimate.

**Source pointers:** [Binary segment inequality](../science/bkm_geometry.md#a-segment-bound-for-binary-holevo-information); [Output-radius bound, Lemma 2](../science/output_bound.md#binary-communication-controls-the-output-radius).

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

**Understanding target:** Explain the use of a BKM-orthonormal Hermitian output basis and its dual Hermitian input operators $`H_j`$. Relate Parseval's identity to the sum of squared coefficient expectations. Use the full set of pure input states and Hermiticity to obtain $`\|H_j\|_\infty^2\le M`$.

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

### M21 — Complete amplification is controlled by output directions

**ID and phase:** M21 · narrative/innovation.

**Central question:** What remains after the Schmidt sums and Hermitian moments are bounded?

**Understanding target:** Combine the spectral-weight inequality, support compression and individual coefficient bounds to obtain

```math
K_{\rho_R\otimes\sigma}
\bigl((\mathrm{id}_R\otimes\Delta)(\psi)\bigr)
\le 2rM.
```

Explain why the factor counts real affine output directions and contains neither input dimension nor a spectral cutoff.

**Dependencies and story role:** M16, M18, M19, M20. This assembles the local coordinate estimates into the joint-system bound required by the theorem.

**Conceptual connection:** The input register can grow while the number of output directions stays fixed; this is the mechanism behind uniformity in input dimension.

**Source pointers:** [Complete amplification, Lemma 3](../science/output_bound.md#complete-amplification-through-output-coordinates); [Role of affine dimension](../science/interpretation.md#what-the-affine-dimension-contributes).

<a id="m22"></a>

### M22 — Close the argument at the level of capacities

**ID and phase:** M22 · narrative/innovation.

**Central question:** How does the geometric estimate become an operational communication theorem?

**Understanding target:** Use the relative-entropy decomposition into mutual information and a marginal divergence, followed by the BKM upper bound. Combine M16 and M21, maximize over purified inputs using BSST, and then invoke HSW achievability to obtain

```math
C_E(T)\le16br\,\chi(T)
\le16b(b^2-1)C(T).
```

**Dependencies and story role:** M06, M08, M09, M13, M21. This integrates the geometry with both operational capacity statements.

**Conceptual connection:** The proof bounds every purified input and every channel in the model without assuming a single-letter formula for ordinary capacity.

**Source pointers:** [Passage from the quadratic bound to capacities](../science/output_bound.md#from-the-quadratic-bound-to-capacities); Wilde2017 §§20.3 and 21.3; [BSST](../references/RELATED_WORK.md#bsst2002), [Holevo](../references/RELATED_WORK.md#holevo1998) and [Schumacher–Westmoreland](../references/RELATED_WORK.md#schumacher1997).

<a id="m23"></a>

### M23 — Uniformity at small capacity and near rank loss

**ID and phase:** M23 · narrative/innovation.

**Central question:** Which limiting channels are included in the theorem's quantifiers?

**Understanding target:** Explain the zero-capacity and replacer cases without assigning a ratio to $`0/0`$. Distinguish a positive center for each channel from a uniform lower bound on its eigenvalues. Understand why the same dimension factor applies to sequences with tiny capacities or output eigenvalues, and why divergent enhancement requires growing effective output dimension.

**Dependencies and story role:** M10, M14, M15, M22. The completed theorem is checked against the boundaries that motivated it.

**Conceptual connection:** Uniformity concerns the final capacity comparison, even when the individual metrics and channel-dependent centers change substantially along a family.

**Source pointers:** [The theorem and zero-capacity conventions](../science/model.md#uniform-output-bound); [Receiver-side consequence](../science/interpretation.md#the-receiver-side-constraint); [Rank-loss discussion](../science/interpretation.md#why-proximity-to-a-replacer-matters).

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

**Central question:** Why is an output-only bound a different statement from an input-dimension bound?

**Understanding target:** Explain how appending an input register that the channel discards enlarges the input dimension while preserving its state image and both capacities. Use simulations by local preprocessing in each direction to justify this equality for arbitrary block codes, including entanglement-assisted codes.

**Dependencies and story role:** M03, M08, M09, M22. A concrete invariance connects the theorem's mathematical uniformity to the physical communication task.

**Conceptual connection:** A device's description can acquire extra input dimensions without acquiring a new communication resource; the output-image estimate is unchanged by that enlargement.

**Source pointers:** [Input-padding construction](../science/examples.md#4-input-padding-leaves-the-communication-problem-unchanged); [Comparison with earlier bounds](../science/interpretation.md#relation-to-earlier-bounds).

<a id="m26"></a>

### M26 — Weak depolarizing signals at fixed dimension

**ID and phase:** M26 · narrative/innovation.

**Central question:** What happens to enhancement when a fixed-dimensional channel approaches a replacer?

**Understanding target:** Interpret the depolarizing parameter and the exact ordinary and assisted capacity formulas. At fixed $`b`$, explain why both capacities vanish quadratically as the parameter tends to zero while their ratio approaches $`b+1`$. Keep this limit distinct from the undefined ratio at the exact replacer.

**Dependencies and story role:** M05, M07, M09, M23. A solvable family shows why comparing small capacities is physically informative.

**Conceptual connection:** An enhancement greater than two is compatible with both rates being small and with a finite uniform bound at fixed output dimension.

**Source pointers:** [Depolarizing model and capacities](../science/examples.md#3-depolarizing-channels-two-distinct-limits); [Fixed-dimension weak-signal limit](../science/examples.md#fixed-output-dimension-and-vanishing-capacity); [Holevo](../references/RELATED_WORK.md#holevo2002) and [King](../references/RELATED_WORK.md#king2003).

<a id="m27"></a>

### M27 — Growing output dimension and the necessary lower scaling

**ID and phase:** M27 · narrative/innovation.

**Central question:** Why does approaching depolarization while increasing dimension produce a different asymptotic gain?

**Understanding target:** Follow the depolarizing family at the negative complete-positivity boundary as $`b`$ grows. Explain the resulting leading gain $`2b`$, the more precise expansion in the examples, and why this forces at least linear growth of any universal output-dimension factor. Recognize that the fixed-dimension Taylor remainder from M26 is not uniform in growing dimension.

**Dependencies and story role:** M10, M22, M26. The examples now establish a global lower scaling that can be compared with the theorem's cubic upper estimate.

**Conceptual connection:** The family changes the bounded physical resource itself. It therefore complements the fixed-output theorem and exposes the unresolved scaling gap.

**Source pointers:** [Negative-boundary family and expansion](../science/examples.md#the-negative-complete-positivity-boundary-as-dimension-grows); [Remaining scaling question](../science/interpretation.md#the-remaining-question); [Holevo](../references/RELATED_WORK.md#holevo2002) and [King](../references/RELATED_WORK.md#king2003).

<a id="m28"></a>

### M28 — What is inherited and what the uniform argument adds

**ID and phase:** M28 · narrative/innovation.

**Central question:** Which gap does the theorem close relative to the closest earlier results?

**Understanding target:** Distinguish the earlier uniform input-dimension bound from the earlier output estimate with a channel-dependent spectral factor. Attribute the capacity formulas, BKM comparisons and Schmidt-weight inequality to their sources. Identify the contribution as the combination of an achievable dominating center, binary curvature and output-coordinate amplification.

**Dependencies and story role:** M14, M15, M16, M21, M22, M25, M27. The completed result is positioned within the established mathematical and communication framework.

**Conceptual connection:** Removing input and conditioning dependence is consequential even when older bounds are numerically stronger for square channels or special families.

**Source pointers:** [Position of the result](../references/RELATED_WORK.md#position-of-the-result); [Inherited tools and the uniform step](../references/RELATED_WORK.md#inherited-tools-and-the-uniform-step); [Wolff et al.](../references/RELATED_WORK.md#wolff2025), [Belzig](../references/RELATED_WORK.md#belzig2023) and [Gao–Rouzé](../references/RELATED_WORK.md#gaorouze2022).

<a id="m29"></a>

### M29 — What finite verification establishes

**ID and phase:** M29 · narrative/innovation.

**Central question:** How do reproducible calculations support an analytical theorem without replacing its proof?

**Understanding target:** Explain the roles of the finite amplification checks, the exact support-compression regression and the high-precision depolarizing calculations. Distinguish the broader Hermiticity-preserving maps used in the amplification checks from physical channels. Identify which universal claims come from the proof and which algebraic or numerical conventions the checks can expose.

**Dependencies and story role:** M20, M21, M27. The theorem and its examples are connected to their reproducible evidence.

**Conceptual connection:** Checking successive inequalities and cancellation-sensitive formulas is useful evidence about implementation; finite sampling does not establish a universal bound, optimality or priority.

**Source pointers:** [Verification route](../verification/README.md); [Complete-amplification audit](../verification/README.md#complete-amplification-audit); [Depolarizing endpoint and limit checks](../verification/README.md#depolarizing-endpoint-and-limit-checks).

<a id="m30"></a>

### M30 — The complete result and the open scaling problem

**ID and phase:** M30 · narrative/innovation.

**Central question:** What has output geometry established about the power of entanglement assistance?

**Understanding target:** Connect the dominating center, binary information radius, Hermitian output coordinates and capacity theorems into one explanation of uniform finiteness. State the model and quantifiers accurately: finite-dimensional memoryless channels, arbitrary finite input dimension, unrestricted preshared entanglement and no uniform spectral cutoff. Compare the established linear lower scaling with the cubic upper estimate, and distinguish the result from an optimal factor or an efficient coding construction.

**Dependencies and story role:** M23, M24, M28, M29. This final synthesis integrates the mechanism, operational meaning, benchmarks, evidence and limitations of the entire project.

**Conceptual connection:** The theorem locates a necessary physical resource for unbounded relative advantage—growing channel-output dimension—while leaving the best dependence on that resource open.

**Source pointers:** [Exact claims](../science/model.md#uniform-output-bound); [Complete proof](../science/output_bound.md); [Interpretation and open scaling](../science/interpretation.md); [Research attribution](../references/RELATED_WORK.md).
