# Light Quark Mass Ratios

Empirical validation of mathematical relationships among light quark masses using FLAG 2024 lattice QCD data.

## Overview

This repository contains validation code for empirical relationships discovered in light quark mass ratios at μ = 2 GeV:

1. **m_s/m_d = 20.0** (exact agreement with FLAG 2024)
2. **m_d/m_u = ∛10** (0.16σ deviation)
3. **Scale-invariant form**: 2(m_d/m_u)³ = m_s/m_d

These dimensionless relationships reduce the three light quark masses (u, d, s) to a single fundamental parameter.

## Key Results

- All relationships agree with FLAG 2024 data within <0.3σ
- Scale-invariant formulation verified across energy scales (0.5 GeV - 1 TeV)
- Statistical analysis: p < 0.005 against random mass distributions

## Usage

```bash
python3 light_quark_prover.py
```

### Requirements

- Python 3.6+
- NumPy

### Output

The script validates:
- Scale-invariant relation: 2(m_d/m_u)³ = m_s/m_d
- Individual ratio constraints
- Statistical significance of deviations

## Data Sources

- **FLAG 2024**: Flavor Lattice Averaging Group world averages
- **Reference scale**: μ = 2 GeV (MS-bar scheme)

## Citation

If you use this work, please cite:

```
A. Brilliant (2024)
"Empirical Scale-Invariant Relationships in Light Quark Mass Ratios"
Submitted to Chinese Physics C
ORCID: 0009-0004-8024-5442
```

## Related Work

Full computational validation including QCD RG evolution available at:
https://github.com/AndBrilliant/scale-dependent-fermion-provers

## License

MIT License - See LICENSE file for details

## Author

**A. Brilliant**
AD Research (international research consortium)
Computational Physics Division
Senior Member, IEEE
ab@ad-research.org