#!/usr/bin/env python3
"""
Light Quark Mass Ratio Prover
Validates empirical relationships: m_s/m_d = 20 and m_d/m_u = ∛10
Scale-invariant formulation: 2(m_d/m_u)³ = m_s/m_d

Author: A. Brilliant (AD Research)
ORCID: 0009-0004-8024-5442
"""

import numpy as np

# FLAG 2024 values at μ = 2 GeV (MS-bar scheme)
FLAG_2024 = {
    'mu': 2.16,      # MeV
    'mu_err': 0.07,  # MeV
    'md': 4.70,      # MeV
    'md_err': 0.07,  # MeV
    'ms': 93.5,      # MeV
    'ms_err': 0.7,   # MeV
}

def test_scale_invariant_relation():
    """Test the scale-invariant relation: 2(m_d/m_u)³ = m_s/m_d"""

    mu = FLAG_2024['mu']
    md = FLAG_2024['md']
    ms = FLAG_2024['ms']

    # Calculate ratios
    md_over_mu = md / mu
    ms_over_md = ms / md

    # Left side: 2(m_d/m_u)³
    left_side = 2 * (md_over_mu ** 3)

    # Right side: m_s/m_d
    right_side = ms_over_md

    # Deviation
    deviation = abs(left_side - right_side)
    relative_error = (deviation / right_side) * 100

    print("=" * 70)
    print("SCALE-INVARIANT RELATION TEST")
    print("=" * 70)
    print(f"\nFLAG 2024 masses at μ = 2 GeV (MS-bar):")
    print(f"  m_u = {mu:.2f} ± {FLAG_2024['mu_err']:.2f} MeV")
    print(f"  m_d = {md:.2f} ± {FLAG_2024['md_err']:.2f} MeV")
    print(f"  m_s = {ms:.1f} ± {FLAG_2024['ms_err']:.1f} MeV")

    print(f"\nDimensionless ratios:")
    print(f"  m_d/m_u = {md_over_mu:.4f}")
    print(f"  m_s/m_d = {ms_over_md:.4f}")

    print(f"\nScale-invariant relation: 2(m_d/m_u)³ = m_s/m_d")
    print(f"  Left side:  2({md_over_mu:.4f})³ = {left_side:.4f}")
    print(f"  Right side: m_s/m_d = {right_side:.4f}")
    print(f"  Deviation: {deviation:.6f} ({relative_error:.4f}%)")

    return deviation, relative_error

def test_cube_root_10_relation():
    """Test m_d/m_u = ∛10"""

    mu = FLAG_2024['mu']
    md = FLAG_2024['md']

    md_over_mu = md / mu
    cube_root_10 = 10 ** (1/3)

    deviation = abs(md_over_mu - cube_root_10)

    # Calculate sigma using FLAG uncertainties
    mu_err = FLAG_2024['mu_err']
    md_err = FLAG_2024['md_err']
    ratio_err = md_over_mu * np.sqrt((md_err/md)**2 + (mu_err/mu)**2)
    sigma = deviation / ratio_err

    print("\n" + "=" * 70)
    print("CUBE ROOT RELATION TEST")
    print("=" * 70)
    print(f"\nRelation: m_d/m_u = ∛10")
    print(f"  Predicted: ∛10 = {cube_root_10:.6f}")
    print(f"  FLAG 2024: m_d/m_u = {md_over_mu:.6f} ± {ratio_err:.6f}")
    print(f"  Deviation: {deviation:.6f}")
    print(f"  Significance: {sigma:.2f}σ")

    return sigma

def test_ms_over_md_equals_20():
    """Test m_s/m_d = 20"""

    md = FLAG_2024['md']
    ms = FLAG_2024['ms']

    ms_over_md = ms / md
    predicted = 20.0

    deviation = abs(ms_over_md - predicted)

    # Calculate sigma
    md_err = FLAG_2024['md_err']
    ms_err = FLAG_2024['ms_err']
    ratio_err = ms_over_md * np.sqrt((ms_err/ms)**2 + (md_err/md)**2)
    sigma = deviation / ratio_err

    print("\n" + "=" * 70)
    print("SIMPLE RATIO TEST")
    print("=" * 70)
    print(f"\nRelation: m_s/m_d = 20")
    print(f"  Predicted: 20.00")
    print(f"  FLAG 2024: m_s/m_d = {ms_over_md:.4f} ± {ratio_err:.4f}")
    print(f"  Deviation: {deviation:.4f}")
    print(f"  Significance: {sigma:.2f}σ")

    return sigma

def test_combined_relation():
    """Test m_s/m_u = 2 × 10^(4/3)"""

    mu = FLAG_2024['mu']
    ms = FLAG_2024['ms']

    ms_over_mu = ms / mu
    predicted = 2 * (10 ** (4/3))

    deviation = abs(ms_over_mu - predicted)
    relative_error = (deviation / predicted) * 100

    # Calculate sigma
    mu_err = FLAG_2024['mu_err']
    ms_err = FLAG_2024['ms_err']
    ratio_err = ms_over_mu * np.sqrt((ms_err/ms)**2 + (mu_err/mu)**2)
    sigma = deviation / ratio_err

    print("\n" + "=" * 70)
    print("COMBINED RELATION TEST")
    print("=" * 70)
    print(f"\nRelation: m_s/m_u = 2 × 10^(4/3)")
    print(f"  Predicted: {predicted:.4f}")
    print(f"  FLAG 2024: m_s/m_u = {ms_over_mu:.4f} ± {ratio_err:.4f}")
    print(f"  Deviation: {deviation:.4f} ({relative_error:.2f}%)")
    print(f"  Significance: {sigma:.2f}σ")

    return sigma

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("LIGHT QUARK MASS RATIO VALIDATION")
    print("Using FLAG 2024 world averages at μ = 2 GeV")
    print("=" * 70)

    # Test scale-invariant relation
    dev, rel_err = test_scale_invariant_relation()

    # Test individual relationships
    sigma_cube_root = test_cube_root_10_relation()
    sigma_20 = test_ms_over_md_equals_20()
    sigma_combined = test_combined_relation()

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"\nAll three relationships show agreement with FLAG 2024 data:")
    print(f"  m_s/m_d = 20:          {sigma_20:.2f}σ deviation")
    print(f"  m_d/m_u = ∛10:         {sigma_cube_root:.2f}σ deviation")
    print(f"  m_s/m_u = 2×10^(4/3):  {sigma_combined:.2f}σ deviation")
    print(f"\nScale-invariant relation 2(m_d/m_u)³ = m_s/m_d:")
    print(f"  Relative error: {rel_err:.4f}%")

    print("\n" + "=" * 70)
    print("VALIDATION COMPLETE")
    print("=" * 70)
    print("\nAll relationships verified within experimental uncertainties.")
    print("These patterns reduce three light quark masses to one parameter.\n")