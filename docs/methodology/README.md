# TSC Self-Measurement Methodology

This directory contains the methodology we use to measure our own coherence.

## Files

- `self_measurement_v1.0.md` - Full methodology specification (coming soon)
- `measurements.md` - History of all measurements (coming soon)
- `CHANGELOG.md` - Methodology evolution (coming soon)

## Current Methodology

**Version:** 1.0 (pending finalization)  
**Cadence:** Bi-weekly  
**Public:** All results published here

## Measurement Process

1. Extract α (claims from documentation)
2. Extract β (actual implementation state)
3. Extract γ (development process/activity)
4. Compute witnesses (W_αβ, W_βγ, W_γα)
5. Compute C_Σ = (α_c · β_c · γ_c)^(1/3)
6. Identify bottleneck
7. Plan fix

## Next Measurement

**Scheduled:** Week of [TBD]  
**Expected Baseline:** C_Σ ≈ 0.0 - 0.15  
**Owner:** Gemini (Coherence Audit Lead)
