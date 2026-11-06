"""Finite audit of the BKM complete-amplification estimate.

The analytical proof is in science/output_bound.md. These deterministic
finite cases test coefficient ordering, Hermitian coordinate contractions,
and a rank-deficient Schmidt-support convention; they are not a proof.
"""
import argparse
from pathlib import Path
import math
import sys

parser = argparse.ArgumentParser(description=__doc__)
group = parser.add_mutually_exclusive_group()
group.add_argument('--output', type=Path)
group.add_argument('--compare', type=Path)
args = parser.parse_args()

import numpy as np, json
from numpy.linalg import eigh
rng=np.random.default_rng(20261106)

def slope(x,y):
 x,y=np.broadcast_arrays(np.asarray(x),np.asarray(y))
 out=np.empty(x.shape)
 z=(x-y)/y
 same=np.abs(z)<1e-7
 out[same]=(1-z[same]/2+z[same]**2/3)/y[same]
 out[~same]=(np.log(x[~same])-np.log(y[~same]))/(x[~same]-y[~same])
 return out

def herm_basis(b):
 a=[]
 for i in range(b-1):
  z=np.zeros((b,b),complex);z[i,i]=1;z[-1,-1]=-1;a.append(z)
 for i in range(b):
  for j in range(i+1,b):
   z=np.zeros((b,b),complex);z[i,j]=z[j,i]=1/np.sqrt(2);a.append(z)
   z=np.zeros((b,b),complex);z[i,j]=-1j/np.sqrt(2);z[j,i]=1j/np.sqrt(2);a.append(z)
 return np.array(a)

rows=[]
for a,b in [(2,2),(8,2),(32,2),(3,3),(16,3),(8,4)]:
 for case in range(20):
  p=np.exp(rng.uniform(-25,0,a));p/=p.sum()
  mu=np.exp(rng.uniform(-25,0,b));mu/=mu.sum()
  if case==0:p[:]=1/a;mu[:]=1/b
  L=slope(mu[:,None],mu[None,:])
  B=herm_basis(b)
  G=np.einsum('jrs,rs,krs->jk',B.conj(),L,B).real
  es,U=eigh(G)
  F=np.einsum('jk,krs->jrs',(U/np.sqrt(es))@U.T,B)
  r=int(rng.integers(1,len(F)+1));F=F[:r]
  H=rng.normal(size=(r,a,a))+1j*rng.normal(size=(r,a,a))
  H=(H+H.swapaxes(1,2).conj())/2
  H/=np.sqrt(a)
  D=np.einsum('jlk,jrs->klrs',H,F)
  kap=slope((p[:,None]*mu[None,:])[:,None,:,None],(p[:,None]*mu[None,:])[None,:,None,:])
  kj=float(np.sum((p[:,None,None,None]*p[None,:,None,None])*kap*np.abs(D)**2))
  # coefficient upper bound and Hermitian operator second moment
  ksep=np.einsum('kl,rs,klrs->',np.maximum(p[:,None],p[None,:]),L,np.abs(D)**2).real
  quad=2*np.einsum('k,jkl->',p,np.abs(H)**2).real
  norms=np.array([np.max(np.abs(eigh(h)[0])) for h in H])
  normcap=2*np.sum(norms**2)
  mlb=0.
  for h in H:
   _,vs=eigh(h)
   for v in vs.T:
    vals=np.einsum('k,jkl,l->j',v.conj(),H,v).real
    mlb=max(mlb,float(np.sum(vals**2)))
  final=2*r*mlb
  vals=[kj,ksep,quad,normcap,final]
  ok=all(vals[i] <= vals[i+1]*(1+1e-7)+1e-8 for i in range(len(vals)-1))
  rows.append(dict(a=a,b=b,r=r,case=case,kjoint=kj,ksep=float(ksep),quad=float(quad),normcap=float(normcap),final=float(final),ok=ok,ratio=kj/final))
report=dict(seed=20261106,tests=len(rows),all_pass=all(r['ok'] for r in rows),max_ratio=max(r['ratio'] for r in rows),rows=rows)

# Regression for the support correction: P H^2 P need not equal (P H P)^2.
P = np.diag([1.0, 0.0])
H = np.array([[0.0, 1.0], [1.0, 0.0]])
restricted = float(2 * np.trace(P @ (P @ H @ P) @ (P @ H @ P)))
uncompressed = float(2 * np.trace(P @ H @ H))
gap_min = float(np.min(np.linalg.eigvalsh(P @ H @ H @ P - (P @ H @ P) @ (P @ H @ P))))
report['support_compression'] = {'twice_compressed_second_moment': restricted,
    'twice_full_second_moment': uncompressed, 'gap_min_eigenvalue': gap_min}
report['all_pass'] = bool(report['all_pass'] and restricted == 0.0
    and uncompressed == 2.0 and gap_min >= 0.0)
report['numpy_version'] = np.__version__

def compare(actual, expected, path='report'):
    if isinstance(actual, dict):
        if not isinstance(expected, dict) or actual.keys() != expected.keys():
            raise ValueError(f'{path}: keys differ')
        for key in actual:
            compare(actual[key], expected[key], f'{path}.{key}')
    elif isinstance(actual, list):
        if not isinstance(expected, list) or len(actual) != len(expected):
            raise ValueError(f'{path}: list length differs')
        for i, (a, e) in enumerate(zip(actual, expected)):
            compare(a, e, f'{path}[{i}]')
    elif isinstance(actual, float):
        if not math.isfinite(actual) or not math.isclose(actual, expected, rel_tol=1e-6, abs_tol=1e-8):
            raise ValueError(f'{path}: numerical mismatch {actual} versus {expected}')
    elif actual != expected:
        raise ValueError(f'{path}: value differs')

if not report['all_pass']:
    raise SystemExit('FAIL: an amplification or support-compression inequality failed')
if args.compare:
    compare(report, json.loads(args.compare.read_text()))
if args.output:
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k:v for k,v in report.items() if k != 'rows'}, indent=2))
if args.compare:
    print('PASS: amplification report matches the committed values within the stated tolerance.')
