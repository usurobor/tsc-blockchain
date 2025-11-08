# Validation Notebooks

Validates TSC framework on historical blockchain incidents.

## Status

| Event | Date | Expected C_Σ | Status |
|-------|------|--------------|--------|
| Terra/Luna | April 15, 2022 | 0.27 ± 0.05 | 🔴 Not started |
| The DAO | June 10, 2016 | 0.56 ± 0.05 | 🔴 Not started |
| Mt. Gox | February 2014 | 0.31 ± 0.06 | 🔴 Not started |

## Timeline

**Target:** 2 weeks focused work (Month 1-2)

- **Days 1-3:** Terra snapshot ingestion, freeze with hashes
- **Days 4-6:** Implement feature extractors (coverage/EMD/edit-distance)
- **Days 7-8:** Assemble terra.ipynb, export attestation
- **Days 9-10:** Add DAO and Mt.Gox, verify reproducibility

## Success Criteria

- ✓ Scores within ±0.05 of projections
- ✓ Reproducibility ≥99% across 10 runs
- ✓ All global gates pass (S₃, variance, budget)
- ✓ Community can independently verify

See [vision paper](../../docs/whitepapers/vision.md) Section III.5 for detailed specification.
