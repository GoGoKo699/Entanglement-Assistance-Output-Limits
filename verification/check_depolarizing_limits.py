#!/usr/bin/env python3
"""Check the endpoint and asymptotic formulas in science/examples.md.

Requires mpmath; tested with mpmath 1.3.0 at 100 decimal digits.

Examples:
    python verification/check_depolarizing_limits.py \
        --compare verification/expected/depolarizing_limit_checks.json
    python verification/check_depolarizing_limits.py --output results.json

This is a focused numerical check of analytically established formulas. It
does not numerically optimize channel capacities or prove their additivity.
"""

import argparse
import json
from pathlib import Path

import mpmath as mp


def run_checks():
    """Return the deterministic report after all numerical assertions pass."""
    mp.mp.dps = 100
    ln2 = mp.log(2)

    def xlogx(x):
        return mp.mpf(0) if x == 0 else x * mp.log(x)

    def f(dim, q):
        dim = mp.mpf(dim)
        return (
            xlogx(1 + (dim - 1) * q)
            + (dim - 1) * xlogx(1 - q)
        ) / (dim * ln2)

    def decimal(x):
        return mp.nstr(x, 45)

    weak_rows = []
    for b in [2, 3, 8]:
        for q_text in ["1e-4", "1e-8", "1e-16", "-1e-16"]:
            q = mp.mpf(q_text)
            c, ce = f(b, q), f(b * b, q)
            ratio = ce / c
            weak_rows.append({
                "b": b,
                "q": q_text,
                "C_bits": decimal(c),
                "CE_bits": decimal(ce),
                "ratio": decimal(ratio),
                "target_b_plus_1": b + 1,
                "relative_error_to_limit": decimal(ratio / (b + 1) - 1),
            })
            if abs(q) == mp.mpf("1e-16"):
                assert abs(ratio / (b + 1) - 1) < mp.mpf("1e-12")

    boundary_rows = []
    for b_int in [2, 4, 16, 256, 4096, 1000000]:
        b = mp.mpf(b_int)
        q = -1 / (b * b - 1)
        ce = -mp.log1p(-1 / (b * b)) / ln2
        c = (
            -b * mp.log1p(-1 / (b * b)) - mp.log1p(1 / b)
        ) / ((b + 1) * ln2)
        ratio = ce / c
        assert c > 0 and ce > c

        # Compare the simplified endpoint formulas with their state spectra.
        output_parallel = 1 / (b + 1)
        output_orthogonal = b / (b * b - 1)
        c_from_spectrum = mp.log(b, 2) + (
            xlogx(output_parallel)
            + (b - 1) * xlogx(output_orthogonal)
        ) / ln2
        choi_nonzero_eigenvalue = 1 / (b * b - 1)
        ce_from_spectrum = 2 * mp.log(b, 2) + (
            (b * b - 1) * xlogx(choi_nonzero_eigenvalue)
        ) / ln2
        assert abs(c_from_spectrum / c - 1) < mp.mpf("1e-70")
        assert abs(ce_from_spectrum / ce - 1) < mp.mpf("1e-70")

        residual = b * (ratio - 2 * b - mp.mpf(4) / 3)
        boundary_rows.append({
            "b": b_int,
            "q_min": decimal(q),
            "C_bits": decimal(c),
            "CE_bits": decimal(ce),
            "ratio": decimal(ratio),
            "ratio_over_2b": decimal(ratio / (2 * b)),
            "ratio_minus_2b": decimal(ratio - 2 * b),
            "b_times_next_residual": decimal(residual),
        })
        if b_int == 1000000:
            assert abs(residual + mp.mpf(4) / 9) < mp.mpf("1e-6")
            assert abs(c * 2 * b**3 * ln2 - 1) < mp.mpf("1e-6")
            assert abs(ce * b**2 * ln2 - 1) < mp.mpf("1e-10")

    endpoint_rows = []
    for b in [2, 3, 8]:
        assert f(b, 0) == 0 and f(b * b, 0) == 0
        assert abs(f(b, 1) - mp.log(b, 2)) < mp.mpf("1e-90")
        assert abs(f(b * b, 1) - 2 * mp.log(b, 2)) < mp.mpf("1e-90")
        endpoint_rows.append({
            "b": b,
            "identity_C_bits": decimal(f(b, 1)),
            "identity_CE_bits": decimal(f(b * b, 1)),
            "replacer_C_bits": decimal(f(b, 0)),
            "replacer_CE_bits": decimal(f(b * b, 0)),
        })

    return {
        "purpose": (
            "Distinguish the fixed-dimension weak-signal limit from the "
            "dimension-growing negative complete-positivity boundary"
        ),
        "mpmath_version": mp.__version__,
        "precision_decimal_digits": mp.mp.dps,
        "status": "passed",
        "weak_signal": weak_rows,
        "negative_cp_boundary": boundary_rows,
        "identity_and_replacer": endpoint_rows,
        "interpretation": (
            "For fixed b and q approaching zero, CE/C approaches b+1. "
            "At q=-1/(b^2-1) and growing b, "
            "CE/C=2b+4/3-4/(9b)+O(b^-2); "
            "2(b+1) is not an additive asymptote."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--output", type=Path, help="Write the report to this path.")
    action.add_argument("--compare", type=Path, help="Compare with this saved report.")
    args = parser.parse_args()
    report = run_checks()

    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        expected = json.loads(args.compare.read_text(encoding="utf-8"))
        if report != expected:
            differing_keys = sorted(
                key for key in set(report) | set(expected)
                if report.get(key) != expected.get(key)
            )
            raise SystemExit(
                "Expected report differs in: " + ", ".join(differing_keys)
            )
        print(f"Matched {args.compare}")

    print(
        "Passed 12 weak-signal rows, 6 negative-boundary rows, and "
        "3 identity/replacer checks; "
        f"mpmath {mp.__version__}, {mp.mp.dps} decimal digits."
    )


if __name__ == "__main__":
    main()
