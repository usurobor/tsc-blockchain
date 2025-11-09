# TSC Blockchain

**Measuring blockchain coherence using Triadic Self-Coherence (TSC) framework**

Measuring blockchain health through protocol claims (α), economic reality (β), and usage patterns (γ).

[Measuring Blockchain Coherence: From Oracle to Consensus](docs/whitepapers/vision.md) (v1.1.0)

## Overview

Two-phase coherence measurement system:
- **Phase 1:** Coherence Oracle (off-chain measurement + on-chain attestation)
- **Phase 2:** Proof-of-Coherence (checkpoint validity rule)

**Status:** Complete specification with implementation plan  
**Next Milestone:** Parser Development (Phase 0, Months 1-3)  
**Timeline:** 12-18 months to production oracle

## Project Phases

### Phase 0: Parser Development (Months 1-3)
Build blockchain-specific data extractors:
- `blockchain_parsers/alpha.py` - Protocol claims parser
- `blockchain_parsers/beta.py` - On-chain metrics parser
- `blockchain_parsers/gamma.py` - Usage patterns parser

**Success criteria:** Extract features from 5 chains in <30 minutes

### Phase 1a: Validation Notebooks (Months 4-6)
Prove TSC detects historical failures:
- Terra/Luna (April 2022): Expected C_Σ ≈ 0.27 ± 0.10
- The DAO (June 2016): Expected C_Σ ≈ 0.56 ± 0.10
- Mt. Gox (2014): Expected C_Σ ≈ 0.31 ± 0.10

**Critical gate:** Must pass validation before building infrastructure

### Phase 1b: Oracle Infrastructure (Months 7-12)
- Smart contract deployment
- REST API
- Ethereum monitoring

### Phase 1c: Production Launch (Months 13-18)
- Multi-chain support (5-10 chains)
- Pilot partnerships (bridges, lenders)
- Public oracle service

See [vision paper Section VII](docs/whitepapers/vision.md#vii-roadmap-execution-grade) for detailed roadmap.

## Repository Structure
```
tsc-blockchain/
├── docs/
│   └── whitepapers/
│       └── vision.md              # Complete specification (v1.1.0)
├── blockchain_parsers/            # Phase 0 deliverables
│   ├── alpha.py                   # Protocol claims parser
│   ├── beta.py                    # On-chain metrics parser
│   └── gamma.py                   # Usage patterns parser
├── notebooks/
│   └── validation/                # Phase 1a deliverables
│       └── README.md              # Validation plan
├── specs/
│   └── witnesses/
│       └── ethereum_mainnet.yaml  # Reference schema
├── HANDOFF.md                     # Partner onboarding guide
└── partner_expectations.md        # Work agreement
```

## Getting Started

See [HANDOFF.md](HANDOFF.md) for complete implementation guide.

## Current Status

| Phase | Timeline | Status |
|-------|----------|--------|
| **Phase 0:** Parsers | Months 1-3 | 🔴 Not Started |
| **Phase 1a:** Validation | Months 4-6 | ⚪ Pending Phase 0 |
| **Phase 1b:** Infrastructure | Months 7-12 | ⚪ Pending Phase 1a |
| **Phase 1c:** Production | Months 13-18 | ⚪ Pending Phase 1b |

**Critical dependency:** Each phase contingent on previous phase success.

## Key Documents

- [Vision Paper](docs/whitepapers/vision.md) - Complete specification (v1.1.0)
- [HANDOFF.md](HANDOFF.md) - Partner onboarding & implementation roadmap
- [partner_expectations.md](partner_expectations.md) - Work agreement & checkpoints
- [Ethereum Schema](specs/witnesses/ethereum_mainnet.yaml) - Reference implementation
- [Validation Plan](notebooks/validation/README.md) - Historical test cases

## Philosophy

**Problem:** Major blockchain failures (Terra, DAO, Mt.Gox) show α/β/γ divergence before collapse

**Solution:** Measure coherence C_Σ = (α_c · β_c · γ_c)^(1/3) to detect risk early

**Approach:** 
1. Validate on historical data (Phase 0-1a)
2. Deploy oracle if validation succeeds (Phase 1b-1c)
3. DON'T build infrastructure without proving methodology works

## License

MIT License - See [LICENSE](LICENSE)

## Acknowledgments

Built on [TSC Core framework](https://github.com/usurobor/tsc) by Peter Lisovin.
```

---

## 📁 **Final Repository Structure**
```
tsc-blockchain/
├── README.md                          # ✅ Updated (12-18 month timeline)
├── LICENSE                            # ✅ Existing (MIT)
├── HANDOFF.md                         # ✨ NEW (partner guide)
├── partner_expectations.md            # ✨ NEW (work agreement)
│
├── docs/
│   └── whitepapers/
│       └── vision.md                  # ✅ Updated to v1.1.0
│
├── blockchain_parsers/                # ✨ NEW DIRECTORY
│   ├── __init__.py
│   ├── alpha.py                       # ✨ NEW (code skeleton)
│   ├── beta.py                        # ✨ NEW (code skeleton)
│   ├── gamma.py                       # ✨ NEW (code skeleton)
│   └── tests/
│       ├── __init__.py
│       ├── test_alpha.py              # Partner creates
│       ├── test_beta.py               # Partner creates
│       └── test_gamma.py              # Partner creates
│
├── notebooks/
│   └── validation/
│       ├── README.md                  # ✅ Existing
│       ├── terra_202204.ipynb         # Partner creates (Phase 1a)
│       ├── dao_201606.ipynb           # Partner creates (Phase 1a)
│       └── data/                      # Partner adds data
│
└── specs/
    └── witnesses/
        └── ethereum_mainnet.yaml      # ✅ Existing