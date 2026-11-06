"""Run the finite scientific checks against the committed reference outputs."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
checks = (
    ('audit_amplification.py', 'amplification_audit_results.json'),
    ('check_depolarizing_limits.py', 'depolarizing_limit_checks.json'),
)
for script, reference in checks:
    subprocess.run([sys.executable, str(root / script), '--compare',
                    str(root / 'expected' / reference)], check=True)
print('PASS: all finite scientific checks completed.')
