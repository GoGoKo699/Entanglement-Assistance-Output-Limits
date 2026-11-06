# Verification

[Scientific account](../science/README.md) · [Main proof](../science/output_bound.md) · [Worked examples](../science/examples.md)

## Run the finite checks

The checked environment uses Python 3 with NumPy 2.3.5 and mpmath 1.3.0. Install the pinned packages if necessary, then run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The runner recomputes both reports and compares them with the committed files in [expected/](expected/). It exits unsuccessfully if an inequality, endpoint assertion, or reference comparison fails. It does not overwrite the expected results.

| Check | Purpose | Scope |
|---|---|---|
| [Amplification audit](audit_amplification.py) | Reconstruct the BKM quadratic form and its successive coefficient, Hermitian-moment and image-coordinate bounds | 120 deterministic random finite maps, plus an exact support-compression regression |
| [Depolarizing limits](check_depolarizing_limits.py) | Verify capacity formulas against spectra, zero/identity endpoints, and two distinct limiting regimes | 100 decimal digits; 12 weak-signal rows, 6 negative-boundary rows and 3 endpoint dimensions |

## Complete-amplification audit

The seed is 20261106. The sampled input/output dimension pairs are (2,2), (8,2), (32,2), (3,3), (16,3), and (8,4), with 20 cases each. Positive reference and output spectra are sampled between exp(-25) and 1 before normalization, with a maximally mixed case in each dimension pair. The real image dimension varies.

The map is constructed from a BKM-orthonormal traceless Hermitian output basis and arbitrary Hermitian input coefficient operators. It is Hermiticity preserving and trace annihilating; complete positivity is not imposed. The amplification lemma applies to this larger class, while the communication theorem separately uses positivity, trace preservation and the geometry of a channel's state image.

For each case the script evaluates the joint quadratic form directly and checks the chain through the separated Schmidt weights, the Hermitian second moments, and the operator-norm bound. A finite set of coefficient-operator eigenvectors supplies a radius certificate: its value is no larger than the full pure-state supremum, and no smaller than the largest individual squared coefficient-operator norm.

The committed run passes all 120 cases. Its largest ratio of the direct joint form to the final finite radius certificate is approximately 0.256259308. This number is a property of the sampled cases, not an estimated sharp universal constant.

A separate two-dimensional regression uses a rank-one Schmidt support and a Pauli X coefficient operator. Twice the compressed second moment is zero while twice the full second moment is two. It checks the distinction required in the [support-compression step](../science/output_bound.md): equality with the uncompressed operator would be incorrect.

The inequality checks use a relative tolerance of 1e-7 and an absolute tolerance of 1e-8. Comparisons with the committed floating-point report use relative tolerance 1e-6 and absolute tolerance 1e-8. Dimension labels, seed, booleans and dependency version must agree exactly.

## Depolarizing endpoint and limit checks

The capacities are evaluated from the formulas derived in [Worked channel comparisons](../science/examples.md), then checked against their output and normalized Choi spectra. The script separates:

- fixed output dimension with the depolarizing parameter approaching zero;
- increasing output dimension at the negative complete-positivity boundary;
- the exact replacement and identity endpoints.

The negative-boundary ordinary capacity involves cancellation between logarithms. High precision keeps that cancellation under control and resolves the constant term in the capacity-ratio expansion. The reported calculations do not optimize either capacity numerically; the exact capacity identifications use the cited coding and additivity theorems.

## Regenerate a report deliberately

```bash
python3 verification/audit_amplification.py \
  --output verification/expected/amplification_audit_results.json
python3 verification/check_depolarizing_limits.py \
  --output verification/expected/depolarizing_limit_checks.json
```

Regeneration is appropriate after a reviewed change to the calculation, not a substitute for resolving a failed comparison.

## Analytical scope

The [written proof](../science/output_bound.md), together with the [inherited metric lemmas](../science/bkm_geometry.md) and [capacity theorems](../references/RELATED_WORK.md), establishes the bound for every channel in the model. The finite calculations test algebraic contractions, numerical conventions and representative limiting formulas. They do not certify global novelty, optimal scaling, infinite-dimensional extensions or the general theorem by sampling.
