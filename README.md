# TSC Blockchain - Triadic Self-Coherence

Measuring blockchain health through protocol claims (α), economic reality (β), and usage patterns (γ).

[![Status](https://img.shields.io/badge/Status-Validation-yellow.svg)](notebooks/validation/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📄 Vision Paper

**[Measuring Blockchain Coherence: From Oracle to Consensus](docs/whitepapers/vision.md)** (v1.0.0)

Two-phase coherence measurement system:
- **Phase 1:** Coherence Oracle (off-chain measurement + on-chain attestation)
- **Phase 2:** Proof-of-Coherence (checkpoint validity rule)

**Status:** Complete specification with validation plan  
**Next Milestone:** Validation notebooks (Month 1-2)

## 🔬 Validation

Three frozen-input notebooks proving framework works:
- **Terra/Luna** (April 2022): Expected C_Σ ≈ 0.27 ± 0.05
- **The DAO** (June 2016): Expected C_Σ ≈ 0.56 ± 0.05
- **Mt. Gox** (2014): Expected C_Σ ≈ 0.31 ± 0.06

See [`notebooks/validation/`](notebooks/validation/) for details.

## 🏗️ Project Structure
```
docs/whitepapers/     # Vision paper
notebooks/validation/  # Validation notebooks (Month 1-2)
specs/witnesses/      # Measurement schemas
```

## 📚 Documentation

- [Vision Paper](docs/whitepapers/vision.md) - Complete specification
- [Ethereum Schema](specs/witnesses/ethereum_mainnet.yaml) - Reference implementation
- [Validation Plan](notebooks/validation/README.md) - Month 1-2 deliverables

## 🚀 Roadmap

| Phase | Timeline | Status |
|-------|----------|--------|
| Validation Notebooks | Months 1-2 | 🔴 Not Started |
| Oracle Infrastructure | Months 3-4 | ⚪ Pending validation |
| Pilot Integrations | Month 5 | ⚪ Pending validation |
| Public Launch | Month 6 | ⚪ Pending validation |

See [vision paper Section VI](docs/whitepapers/vision.md#vi-roadmap-execution-grade) for detailed roadmap.

## 📖 Core Concept

**Problem:** Major blockchain failures (Terra, DAO, Mt.Gox) show α/β/γ divergence before collapse

**Solution:** Measure coherence C_Σ = (α_c · β_c · γ_c)^(1/3) to detect risk early

**Approach:** Validate on historical data, then deploy as oracle service

## 📄 License

MIT License - See [LICENSE](LICENSE)

## 🤝 Author

Peter Lisovin - TSC Blockchain Project
