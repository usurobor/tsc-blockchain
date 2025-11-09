# Measuring Blockchain Coherence: From Oracle to Consensus

**A phased approach to making blockchains measurable and self-correcting**

Peter Lisovin  
TSC Blockchain Project  
November 2025

**Document Version:** 1.1.0 (arXiv Ready + Partner Handoff)  
**Status:** Complete Specification with Validation Plan  
**Next Milestone:** Parser Development (Phase 0, Months 1-3)  
**Phase 1 Timeline:** 12-18 months to production oracle (contingent on validation)

**Keywords:** blockchain measurement, coherence, DeFi risk, reproducibility, zero-knowledge

---

## Abstract

Major blockchain blow-ups share one symptom: α (protocol claims), β (economic/implementation reality), and γ (emergent usage) diverge well before loss. No standard tool measures that divergence. We propose a two-phase program built on Triadic Self-Coherence (TSC):

1. **Coherence Oracle (Phase-1):** Specification for off-chain measurement and on-chain attestation of per-chain coherence C_Σ. Parser development (Phase 0) required before validation.

2. **Proof-of-Coherence (Phase-2):** A checkpoint validity rule layered on PoS/PBFT requiring C_Σ ≥ Θ or friction improvement Δλ_Σ ≥ δ.

**Relationship to TSC Core Framework:** This paper describes TSC-blockchain, a specific application of the general-purpose Triadic Self-Coherence framework (github.com/usurobor/tsc, v2.3.0) to blockchain risk measurement. TSC Core provides mathematical foundations and witness functions; this application provides blockchain-specific parsers and use cases.

Phase-1 specification provides the framework; the validation notebooks prove whether the framework works as designed.

---

## I. The Observable Pattern

### 1.1 Operational Definitions

Given a time window W on a chain:

- **α (Protocol/Pattern):** Promised properties—security claims, tokenomics, governance process, performance targets.
- **β (Economics/Relation):** Deployed code and state—stake distribution, fee/MEV dynamics, realized performance.
- **γ (Usage/Process):** Trajectory—transaction mix, retention/turnover, upgrade adoption, incident timelines.

We compute α_c, β_c, γ_c ∈ [0,1] and aggregate:

**C_Σ = (α_c · β_c · γ_c)^(1/3),    λ_Σ = -ln(max(C_Σ, ε))**

with numerical floor **ε = 10^(-12)**.

**Degeneracy guard:** If any axis is 0, C_Σ = 0 (no compensation from other axes).

**Default thresholds:**
- Production ≥ 0.80
- Watch 0.60-0.80
- Hazard 0.40-0.60
- Critical < 0.40

### 1.2 Case Studies (Projected Scores Based on TSC Framework)

#### Terra/Luna (pre-collapse, April 2022):
- **Projected score:** C_Σ ≈ 0.27 ± 0.10 (Critical)
- **Basis:** Estimated using TSC framework on known facts:
  - α_c ≈ 0.65 (protocol claims documented)
  - β_c ≈ 0.08 (Anchor sustainability ratio, reserve coverage)
  - γ_c ≈ 0.38 (usage patterns showed stress)
- **Status:** TO BE VALIDATED in notebook (Phase 1a, Months 4-6)
- Validation will either confirm score or refine methodology

#### The DAO (June 2016):
- **Projected score:** C_Σ ≈ 0.56 ± 0.10 (Hazard)
- **Basis:** β (implementation vs claim) dominated risk
- **Status:** TO BE VALIDATED in notebook (Phase 1a, Months 4-6)

#### Bitcoin Identity Drift (cash→gold):
- **Projected score:** C_Σ ≈ 0.66 (Watch)
- **Basis:** Functional chain, measurable narrative drift
- **Status:** TO BE VALIDATED in notebook (Phase 1a, Months 4-6)

**All values are projections.** Phase 1a notebooks will compute scores from frozen snapshots; **if they differ by >±0.10, we tune witnesses before any infrastructure spend**. Tolerance widened from ±0.05 to ±0.10 for initial validation phase.

---

## II. Minimal TSC We Actually Implement

### II.1 Articulation → Features (Per Chain)

| Axis | Minimal Feature Set (Measurable Today) |
|------|----------------------------------------|
| **α (claims)** | Supply schedule; finality targets; fee model; governance powers & thresholds; security assumptions; declared economic invariants |
| **β (reality)** | Verified bytecode & admin rights; validator set & stake concentration; realized latency/finality/throughput; MEV/fee stats; token distribution (Gini); treasury flows; peg/collateral ratios |
| **γ (usage)** | Tx taxonomy; holding vs spending; call-graph motifs; retention/turnover; L2 routing; upgrade adoption cadence; incident markers |

### II.2 Witness Functions (Simplified for Validation)

We compute distances and convert them to scores s ∈ [0,1].

**W_αβ (claims ↔ implementation):**
- Coverage: What fraction of α properties have checks?
- Pass rate: What fraction of checks pass?
- Severity: Penalize critical failures
- Score: α_c = w₁·(coverage) + w₂·(pass_rate) - w₃·(severity_penalty), clipped to [0,1]

**W_βγ (incentives ↔ behavior):**
- Expected use-mix p from β (fees, yields, latency)
- Observed mix q from γ (actual transaction types)
- Distance: Earth Mover's Distance d = EMD(p, q), normalized to [0,1]
- Score: β_c = 1 - d

**W_γα (behavior ↔ intent):**
- Reference signature u(t) from α (intended usage pattern)
- Observed trajectory v(t) from γ (actual behavior over time)
- Distance: Normalized edit distance between sequences
- Score: γ_c = 1 - norm_dist(u, v)

**Future work:** More sophisticated witnesses (optimal transport, graph matching) may be explored in Phase 2 after base framework is validated.

### II.3 Global Witness Gates

- **S₃ symmetry:** C_Σ invariant under axis permutation (within tolerance τ_sym)
- **Stability:** VRF-seeded repeats; variance ≤ τ_var
- **Budget (Phase-1: report-only; Phase-2: enforced):** Report B and η = Δλ_Σ / B each run. In Phase-2, require B ≤ B_max and η ≥ η_min.

**Missing-data policy:** Primitives that cannot be computed in a window are marked NA; their declared weights are added to an axis penalty bucket (no imputation). The NA mask is written to provenance.

---

## III. Phase-0 — Parser Development (NEW)

**Before validation notebooks can be built, we must create blockchain-specific parsers to extract α/β/γ articulations from chain data.**

### III.0.1 Why Parsers Come First

The TSC framework is domain-agnostic—it doesn't "know" about blockchains. To apply TSC to blockchain measurement, we need:

1. **Alpha parser:** Extract protocol claims from whitepapers, governance docs, specs
2. **Beta parser:** Extract on-chain implementation metrics from RPC endpoints
3. **Gamma parser:** Extract usage patterns from transaction history

**These parsers represent 60-80% of Phase 1 engineering effort.** The TSC framework provides the coherence computation; parsers provide the blockchain domain expertise.

### III.0.2 Parser Requirements

**Alpha Parser (`blockchain_parsers/alpha.py`)**

**Inputs:**
- Chain ID (e.g., "ethereum", "bitcoin", "sol

ana")
- Time window (start_date, end_date)

**Outputs:**
- Dictionary of {claim_id: claim_text}
- Feature vector for α-axis stability computation

**Data sources:**
- Governance proposals (on-chain + forum)
- Technical specification documents
- Whitepaper claims (parsed from PDF/markdown)
- Declared economic invariants

**Success criteria:**
- Extract 20+ measurable claims per chain
- 99%+ reproducibility across runs
- Complete in <5 minutes per chain
- Works on 5 test chains (BTC, ETH, Solana, Arbitrum, Optimism)

**Beta Parser (`blockchain_parsers/beta.py`)**

**Inputs:**
- Chain ID
- Time window
- RPC endpoint (or analytics platform API key)

**Outputs:**
- On-chain metrics dictionary
- Feature vector for β-axis coherence computation

**Data sources:**
- RPC queries (eth_getBlock, beacon chain API)
- Token holder analytics (Etherscan, Nansen)
- Gas/fee market data
- MEV extraction metrics

**Metrics to compute:**
- Validator/miner concentration (Gini, Nakamoto coefficient)
- Stake distribution
- Token holder concentration
- Realized performance (latency, throughput, finality)
- MEV extracted (if measurable)
- Treasury flows

**Success criteria:**
- Collect 30+ metrics per chain
- Handle RPC rate limits gracefully
- Cache results (don't re-query same blocks)
- Complete in <10 minutes per chain

**Gamma Parser (`blockchain_parsers/gamma.py`)**

**Inputs:**
- Chain ID
- Time window
- Analytics platform API key

**Outputs:**
- Transaction type distribution
- Usage pattern time series
- Feature vector for γ-axis stability computation

**Data sources:**
- Dune Analytics (pre-computed dashboards)
- Flipside Crypto (SQL queries)
- The Graph (subgraphs)
- Direct transaction parsing

**Metrics to compute:**
- Transaction taxonomy (DEX, lending, NFT, bridge, transfers)
- Active user counts (daily/weekly/monthly)
- Transaction value distribution
- Gas usage patterns
- Retention/churn rates
- L2 routing patterns

**Success criteria:**
- Classify 90%+ of transactions by type
- Compute time series (7-day, 30-day windows)
- Handle missing data gracefully
- Complete in <15 minutes per chain

### III.0.3 Data Sources & Availability

**Critical dependency:** Historical blockchain data for parser development and validation.

**Primary (Archive Nodes):**
- Alchemy, Infura, QuickNode (RPC access)
- Cost: ~$1,500/month for historical queries
- Limitation: Rate limits, some chains pruned

**Secondary (Analytics Platforms):**
- Nansen (institutional access, ~$1,000/month)
- Flipside Crypto (free tier available, limited)
- Dune Analytics (public dashboards, aggregated)

**Tertiary (Blockchain Explorers):**
- Etherscan, BscScan, etc. (APIs, rate limited)
- Free tier: 5 calls/sec
- Pro tier: ~$200/month

**Known Challenges:**

**Terra/Luna (2022 data):**
- Most nodes pruned post-collapse
- Options:
  1. Flipside Crypto (has frozen snapshot)
  2. Nansen (institutional access required)
  3. Public datasets (Kaggle, academic archives)
- **Estimated cost:** $2,000-5,000 for data access
- **Trust assumption:** Rely on third-party snapshots (not first-party nodes)

**The DAO (2016 data):**
- Ethereum archive nodes available
- Alchemy historical queries sufficient
- **Estimated cost:** $500/month during validation

**Mt. Gox (2014 data):**
- Bitcoin full nodes have complete history
- Public block explorers sufficient
- **Estimated cost:** $0 (free access)

**Budget Estimate (Phase 0-1a):**
- Archive node access: $1,500/month × 6 months = $9,000
- Analytics platform subscriptions: $2,000/month × 3 months = $6,000
- One-time data purchases: $3,000
- **Total data costs:** ~$18,000

This should be budgeted in Phase 0-1a planning.

### III.0.4 Timeline & Deliverables

**Months 1-3: Parser Development**

**Month 1-2: Alpha Parser**
- Design protocol claim catalog (20-30 standard properties)
- Implement whitepaper/governance doc parser
- Test on 5 chains
- Deliverable: `blockchain_parsers/alpha.py` + tests

**Month 2-3: Beta & Gamma Parsers**
- Implement RPC query layer with rate limiting
- Implement analytics platform integrations
- Test on 5 chains
- Deliverables: `blockchain_parsers/beta.py`, `blockchain_parsers/gamma.py` + tests

**Month 3: Integration & Testing**
- End-to-end test: Parse 5 chains × 3 parsers = 15 runs
- Verify reproducibility (99%+ across runs)
- Performance test (<30 min total for 5 chains)
- Deliverable: Working parser suite

**Success gate:** All parsers working on 5 chains before proceeding to Phase 1a validation.

---

## IV. Phase-1 — Coherence Oracle (Specification)

### IV.1 Architecture (Data Flow)

```
┌─────────────────────────────────────────────────────────────┐
│                     BLOCKCHAIN ECOSYSTEMS                    │
│  Ethereum │ Bitcoin │ Arbitrum │ Optimism │ [New Chain]     │
└──────┬───────┬───────────┬──────────┬────────────┬───────────┘
       │       │           │          │            │
       └───────┴───────────┴──────────┴────────────┘
                          │
            ┌─────────────▼──────────────┐
            │   ADAPTER LAYER            │  (RPC, Graph, APIs)
            │   [Phase 0 Parsers]        │
            └─────────────┬──────────────┘
                          │
            ┌─────────────▼──────────────┐
            │  ARTICULATION BUILDERS     │  α/β/γ → features
            └─────────────┬──────────────┘
                          │
            ┌─────────────▼──────────────┐
            │   WITNESS COMPUTATION      │  W_αβ, W_βγ, W_γα
            │   (coverage/EMD/edit-dist) │
            └─────────────┬──────────────┘
                          │
            ┌─────────────▼──────────────┐
            │   COHERENCE CORE           │  α_c, β_c, γ_c → C_Σ, λ_Σ
            │   gates: S₃, VAR, Budget   │
            └─────────────┬──────────────┘
                          │
                ┌─────────▼─────────┐
                │  ATTESTATION      │  (provenance JSON)
                └─────────┬─────────┘
                          │
                ┌─────────▼─────────┐
                │  ORACLE SMART CT  │  publishes (C_Σ, λ_Σ, provHash)
                └───────────────────┘
```

### IV.2 Interfaces

**On-chain ABI:**

```solidity
interface ICoherenceOracle {
  struct Report {
    uint64  chainId;
    uint64  blockNumber;
    uint32  methodId;
    uint32  semver;
    uint64  Csigma_milli;    // C_Σ × 1000
    uint64  lambda_milli;    // λ_Σ × 1000
    bytes32 provHash;        // provenance bundle hash
  }
  
  function latest(uint64 chainId) external view returns (Report memory);
  function verify(Report calldata r) external view returns (bool);
}
```

**REST API:**

```
GET /v1/coherence/{chain}
→ { C_Σ, λ_Σ, α_c, β_c, γ_c, trend_7d, methodId, provenance_url }
```

### IV.3 Cadence & SLOs (Tiered)

| Tier | Wall Time SLO | Cost SLO | Notes |
|------|---------------|----------|-------|
| **Standard** (hot cache) | ≤ 60s | ≤ $1 | Primary consumption tier |
| **Deep analysis** (optional) | ≤ 5 min | ≤ $5 | Adds heavier γ features, MEV |
| **Cold start** (first run) | ≤ 10 min | ≤ $10 | First run initialization |
| **Reproducibility** | N/A | N/A | ≥99.99% identical C_Σ for frozen inputs |

### IV.4 Budget-Efficiency Gate: Example

**Phase-1 defaults:**
- B_max = 10^6 gas-equivalent units
- η_min = 10^(-6) (realistic threshold; will tune on testnet)

**Example (Standard tier):**

Estimated costs:
- RPC queries (~100 calls): ~$0.10
- Computation (coverage checks, EMD, edit distance): ~$0.02
- On-chain attestation (50k gas @ 20 gwei): ~$2-4
- Storage (IPFS): ~$0.01
- **Total budget B: ~$2.50-4.50**

Estimated improvement:
- Before: C_Σ = 0.82 → λ_Σ = 0.198
- After: C_Σ = 0.84 → λ_Σ = 0.174
- **Improvement: Δλ_Σ ≈ 0.024**

Budget-efficiency:
```
η = Δλ_Σ / B ≈ 0.024 / 4.00 ≈ 6×10^(-3)
```

Gate check: η ≥ η_min = 10^(-6)?  
✓ **YES** (3 orders of magnitude headroom)

**Units:** In Phase-1 the gate uses reported USD cost per checkpoint (operator-auditable via invoices); Phase-2 migrates to a gas-equivalent or fixed budget unit (with published weights) for cross-chain comparability.

We will log (Δλ_Σ, B, η) alongside each attestation.

**Note:** These are engineering estimates. Actual costs will be measured during implementation.

### IV.5 Validation Strategy: Why Notebooks First

The validation notebooks are **THE critical first deliverable** (after parsers) because they establish whether the TSC framework works as specified for blockchain measurement. This is a deliberate fork in the development path.

#### Why Notebooks After Parsers?

1. **Proves concept:** Can TSC detect incoherence retroactively on blockchains?
2. **Calibrates methodology:** Do scores match expected ranges?
3. **Validates degeneracy:** Does low β_c collapse C_Σ as theory predicts?
4. **Establishes reproducibility:** Can independent teams get same scores?

#### The Fork: Two Possible Outcomes

**Outcome A: Validation Succeeds**
- Terra produces C_Σ ≈ 0.27 ± 0.10 (critical threshold)
- DAO produces C_Σ ≈ 0.56 ± 0.10 (hazard threshold)
- Scores are reproducible (99%+ match across runs)
- All global gates pass (S₃, variance, budget)

**→ PROCEED:** Build oracle infrastructure (Phase 1b, Months 7-12)  
**→ Framework proven, specification validated**  
**→ Risk: LOW** (methodology works)

**Outcome B: Validation Reveals Issues**
- Terra produces C_Σ = 0.65 (not critical as expected)
- OR scores not reproducible (variance >5%)
- OR witness functions need tuning

**→ ITERATE:** Refine methodology (additional 4-8 weeks)  
**→ Framework needs adjustment, specification revised**  
**→ Risk: MEDIUM** (learn what needs fixing)

#### What We Learn from Outcome B:
- Which witnesses need recalibration
- Whether tolerances are too tight/loose
- If additional α/β/γ features are needed
- How to improve reproducibility

**Either outcome is valuable.** Success proves the framework; failure teaches us how to improve it. This is why validation comes BEFORE infrastructure investment.

**If validation criteria are not met:** tune witnesses/tolerances and re-measure before any infrastructure spend.

#### Validation Acceptance Criteria

**For each validation notebook to PASS:**

1. **Score within tolerance:**
   - Terra: C_Σ = 0.27 ± 0.10 (widened from ±0.05 for Phase 1a)
   - The DAO: C_Σ = 0.56 ± 0.10
   - Mt. Gox: C_Σ = 0.31 ± 0.10

2. **Reproducibility:**
   - ≥99% identical C_Σ across 10 runs with frozen inputs
   - Standard deviation ≤ 0.01

3. **Computational feasibility:**
   - Complete computation in <30 minutes (standard tier)
   - Total cost <$10 per run (including RPC queries)

4. **Witness gates:**
   - S₃ permutation: All 6 permutations within tolerance
   - Variance floor: Alignment methods agree within 10%

**If ANY criterion fails:**
→ STOP: Do not proceed to oracle infrastructure (Phase 1b)
→ Iterate on methodology 4-8 weeks
→ Re-run validation
→ Document what changed and why

**Rationale for ±0.10 tolerance:**
Phase 1a is methodology validation, not precision measurement. Tighter tolerances (±0.05) will be enforced in Phase 2 after methodology is proven.

**Success = all three notebooks PASS all four criteria**

#### Deliverables (Phase 1a, Months 4-6):

Three public notebooks demonstrating reproducible retroactive measurement:

1. **Terra/Luna notebook**
   - **Snapshot anchor:** as_of: 2022-04-15T00:00:00Z
   - Expected: C_Σ ≈ 0.27 ± 0.10
   - If validated: Strong proof of concept
   - If not: Iterate on witness functions

2. **The DAO notebook**
   - **Snapshot anchor:** as_of: 2016-06-10T00:00:00Z
   - Expected: C_Σ ≈ 0.56 ± 0.10
   - Secondary validation of methodology

3. **Mt. Gox notebook**
   - **Snapshot anchor:** as_of: 2014-02-10T00:00:00Z
   - Expected: C_Σ ≈ 0.31 ± 0.10
   - Bitcoin-specific validation

All notebooks will be public (GitHub) with frozen data snapshots, allowing independent verification. Block heights are resolved inside each notebook from the UTC timestamp anchor.

**Success criteria:**
- ✓ Scores within ±0.10 of projections
- ✓ Reproducibility ≥99% across 10 runs with frozen inputs
- ✓ Witness functions pass S₃, stability, budget gates
- ✓ Community can independently verify

**Timeline: 8-10 weeks focused work** (includes iteration cycles)
- Weeks 1-2: Terra snapshot acquisition, parser integration
- Weeks 3-4: Implement witness functions, compute C_Σ
- Weeks 5-6: Debug methodology if needed, achieve acceptance criteria
- Weeks 7-8: Add DAO notebook, verify reproducibility
- Weeks 9-10: Add Mt.Gox notebook (optional), finalize documentation

### IV.6 Attestation Strategy (Provenance-First)

Phase-1 relies exclusively on **reproducible provenance** (stored in IPFS/Arweave) for auditability.

**Provenance bundle includes:**
- Input data hash
- Method version (methodId)
- Computation timestamp
- Result (C_Σ, α_c, β_c, γ_c, λ_Σ)
- Container image/Nix flake pin
- Data source licenses

**Anyone can verify:** Same inputs + same method → same result ± tolerance

**Zero-knowledge proofs (zk-MFI) are deferred to Phase-2.** When measurement moves into consensus, cryptographic guarantees become valuable. Phase-1 commitment: Reproducible provenance is sufficient for oracle use case.

### IV.7 Consumption Patterns (Concrete Use Cases)

**Bridges:**
- Accept transfers > $N only if C_Σ ≥ 0.80 AND β_c ≥ 0.75
- Alert when ΔC_Σ < -0.10 week-over-week

**Lenders:**
- Map Loan-to-Value (LTV) from C_Σ with floor at 0.60
- Linear interpolation between 0.60 and 0.80

**Exchanges:**
- Listing gates: Require C_Σ ≥ 0.70
- Watchlist: Flag when C_Σ < 0.60
- Delisting consideration: C_Σ < 0.40 for >30 days

---

## V. Phase-2 — Proof-of-Coherence (Validity Layer)

We integrate the coherence metric as a validity rule at checkpoints. This is a research direction contingent on Phase-1 validation success.

**Checkpoint acceptance:**
- If global gates pass AND (C_Σ ≥ Θ OR Δλ_Σ ≥ δ): **accept**
- Else: **degraded mode** (rate-limit risky surfaces, quarantine incoherent contracts) until coherence recovers

**Default parameters:**
- Threshold: Θ = 0.80 (production)
- Minimum improvement: δ = 0.01

**Economic sanity:** Reward proportional to leverage reduction (Δλ_Σ), applying Budget-Efficiency gate network-wide to prevent "buying" coherence with unbounded compute.

**Research questions for Phase-2:**
1. Checkpoint frequency optimization
2. Challenge window design
3. Validator economic game theory
4. Migration path (L2 first, then L1)
5. ZK-proof integration

**Timeline:** 12-18 months after Phase-1 validation.

---

## VI. Why This Works (Engineer's Criteria)

TSC is effective because it:

- **Measures the failure mode.** α/β/γ aren't opinions; they're feature sets tied to code, state, and usage.
- **Reproducible.** Provenance bundle makes "same inputs → same numbers" enforceable.
- **Cheap to consume.** Downstream logic needs a scalar and a breakdown.
- **Incremental.** Phase-0 parsers + Phase-1a validation + Phase-1b infrastructure build naturally.

### VI.1 How This Relates to Existing Tools

TSC **complements** existing infrastructure:

| Tool | What It Measures | TSC Adds |
|------|------------------|----------|
| **Chainlink** | Price feeds, external data | Chain health metrics (C_Σ as new data primitive) |
| **Gauntlet/Chaos Labs** | Economic simulation | Continuous measurement of actual vs modeled (β/γ alignment) |
| **Formal Verification** | Code correctness | Measures if correct code produces intended economics (α/β/γ coherence) |
| **Audits** | Point-in-time security | Continuous monitoring, drift detection |

**Integration example:** DeFi protocol uses Chainlink for prices, Gauntlet for risk params, and TSC for collateral chain health. If TSC reports C_Σ < 0.60 for a bridged chain, Gauntlet adjusts LTV down. Three complementary layers.

### VI.2 What TSC Does Not Measure

TSC measures coherence (whether claims/economics/usage fit together), **not:**
- Absolute security (use audits)
- Code correctness (use formal verification)
- Market legitimacy (use due diligence)
- Price accuracy (use oracles)

TSC complements these tools by adding dimensional consistency measurement.

### VI.3 What Could Go Wrong (Honest Risk Assessment)

**Parser development risks (Phase 0, Months 1-3):**

1. **Risk: Can't extract measurable claims**
   - Whitepapers are vague marketing, not specifications
   - Mitigation: Use governance proposals (more specific)
   - Learning: Define canonical property catalog

2. **Risk: RPC rate limits too restrictive**
   - Archive queries expensive, slow
   - Mitigation: Cache aggressively, batch queries
   - Learning: Budget $1,500/month minimum

3. **Risk: Transaction classification too hard**
   - No standard taxonomy across chains
   - Mitigation: Start with top 10 tx types by volume
   - Learning: Accept 80-90% coverage (not 100%)

**Validation risks (Phase 1a, Months 4-6):**

1. **Risk: Scores don't match projections**
   - Terra produces C_Σ = 0.65 instead of 0.27
   - Mitigation: Iterate on witness functions, adjust weights
   - Learning: Discover which articulations need refinement

2. **Risk: Poor reproducibility**
   - Same input produces C_Σ = 0.27 ± 0.15 (too wide)
   - Mitigation: Stabilize computation, add determinism checks
   - Learning: Identify non-deterministic components

3. **Risk: Data availability**
   - Can't fetch April 2022 Terra data (nodes pruned)
   - Mitigation: Use Flipside/Nansen archives
   - Fallback: Use publicly available snapshots
   - **Trust assumption acknowledged**

4. **Risk: Computational cost exceeds budget**
   - Measurement takes 10 hours instead of 30 minutes
   - Mitigation: Optimize, reduce feature set, adjust SLO tier
   - Learning: Understand actual performance characteristics

**These are LEARNING opportunities, not failures.** The specification provides the framework; Phase 0-1a teaches us how to implement it correctly for blockchains.

---

## VII. Roadmap (Execution-Grade)

### VII.1 Complete Timeline (12-18 Months)

| Timeline | Focus | Deliverable |
|----------|-------|-------------|
| **Months 1-3** | **Phase 0: Parser Development** | Alpha/beta/gamma parsers working on 5 chains. **GATE: Parser demo before Phase 1a.** |
| **Months 4-6** | **Phase 1a: Validation** | Terra/DAO/Mt.Gox notebooks. **FORK: Success → Phase 1b. Failure → iterate 4-8 weeks.** |
| **Months 7-12** | **Phase 1b: Oracle Infrastructure** | Smart contract, REST API, Ethereum monitoring. **Contingent on Phase 1a success.** |
| **Months 13-18** | **Phase 1c: Production Launch** | Multi-chain support, pilot partnerships, public oracle. **Contingent on Phase 1b stability.** |
| **Months 19+** | **Phase 2: Research** | Proof-of-Coherence mechanism, validator economics. **Long-term research track.** |

### VII.2 Critical Gates (Do NOT Skip)

**Gate 1: Month 3 - Parser Demo**
- **Required:** Parsers extract features from 5 chains in <30 min total
- **Acceptance:** 99%+ reproducibility, 20+ features per axis
- **If FAIL:** Extend Phase 0 by 4 weeks

**Gate 2: Month 6 - Terra Validation**
- **Required:** C_Σ = 0.27 ± 0.10, all witnesses pass
- **Acceptance:** Reproducible across 10 runs
- **If FAIL:** STOP. Iterate methodology 4-8 weeks. DO NOT proceed to Phase 1b.

**Gate 3: Month 12 - Oracle Testnet**
- **Required:** 30 days of Ethereum monitoring without failures
- **Acceptance:** 2-3 internal users, SLO <5 min latency
- **If FAIL:** Extend Phase 1b by 8 weeks

### VII.3 Budget Summary

**Phase 0 (Months 1-3):**
- Engineering: 1 FTE × 3 months
- Data access: $1,500/month × 3 = $4,500
- **Subtotal: ~$25K-35K** (depending on engineer cost)

**Phase 1a (Months 4-6):**
- Engineering: 1 FTE × 3 months (includes iteration)
- Data access: $2,000/month × 3 = $6,000
- Historical datasets: $3,000 one-time
- **Subtotal: ~$30K-40K**

**Phase 1b (Months 7-12):**
- Engineering: 1-2 FTE × 6 months
- Infrastructure: $1,000/month × 6 = $6,000
- Data access: $1,500/month × 6 = $9,000
- **Subtotal: ~$60K-100K**

**Phase 1c (Months 13-18):**
- Engineering: 1-2 FTE × 6 months
- Infrastructure: $2,000/month × 6 = $12,000
- Partnership development: $10,000
- **Subtotal: ~$70K-120K**

**Total Phase 0-1c budget: $185K-295K** (12-18 months)

### VII.4 Dependencies

**Critical path:**
```
Phase 0 (parsers) 
  → Phase 1a (validation) 
    → Phase 1b (oracle infrastructure) 
      → Phase 1c (production)
```

**Each phase is contingent on the previous phase succeeding.**

Months 4-18 are CONTINGENT on Month 1-3 parser success.
Months 7-18 are CONTINGENT on Month 4-6 validation success.

If validation fails repeatedly (>3 iterations), consider pausing project to reassess TSC blockchain applicability.

---

## VIII. TSC Self-Coherence Status

**This section addresses TSC Core framework's self-application results.**

### VIII.1 Current Status (v2.3.0)

**TSC Self-Coherence Measurement:**

*Target (v2.4.0):* C_Σ(TSC) ≥ 0.90 [milestone in progress]

*Current (v2.3.0):* C_Σ(TSC) = 0.238 [FAIL - expected during development]

**Why this is honest measurement:**

The v2.3.0 FAIL verdict indicates the TSC repository is not yet fully self-coherent by its own standards. This demonstrates that TSC holds itself to the same standards it applies to other systems.

**Breakdown by witness:**
- ✅ S₃ symmetry: PASS (all permutations within tolerance)
- ❌ Braided interchange: FAIL (parser needs extension for subscripts)
- ❌ β-axis coherence: 0.061 (specs need cross-references)
- ✅ γ-axis stability: 0.721 (good temporal consistency)

**Aggregate:**
- α_c = 0.487 (pattern articulation quality)
- β_c = 0.061 (relational coherence - low due to missing cross-refs)
- γ_c = 0.721 (process stability)
- **C_Σ = (0.487 × 0.061 × 0.721)^(1/3) = 0.238**

The low β_c dominates due to geometric mean (no compensation from other axes).

### VIII.2 Path to v2.4.0 (Target: Q1 2025)

**Improvement roadmap:**

- **v2.3.1 (2-3 weeks):** Fix braided parser
  - Extend parser for subscripts, implicit parens, α-renaming
  - Target: braid_CI_hi ≤ 0.001
  
- **v2.3.2 (2-3 weeks):** Add cross-references between specs
  - Add explicit "see §X" links
  - Reference glossary terms with markdown links
  - Target: β_c ≥ 0.50

- **v2.4.0 (integration):** Achieve self-coherence
  - CI blocks merges if `tsc self` returns FAIL
  - Public demonstration: C_Σ(TSC) ≥ 0.90
  - **This validates that TSC methodology works**

### VIII.3 What This Means for TSC-Blockchain

**TSC Core is still under development toward full self-coherence.**

However, the **methodology is sound:**
- S₃ symmetry works (no role privilege)
- Geometric mean prevents compensation (detects weak axes)
- Honest measurement (reports FAIL when criteria not met)

**For blockchain application:**
- Phase 0-1a can proceed in parallel with TSC Core v2.4.0 development
- Blockchain parsers use TSC framework as library (don't need self-coherence)
- TSC Core v2.4.0 completion (Q1 2025) aligns with Phase 1a validation (Months 4-6)

**If TSC Core v2.4.0 fails to achieve C_Σ ≥ 0.90:** Reassess blockchain application viability. A framework that can't measure itself coherently may not generalize to blockchains.

---

## IX. Engineering Appendix

### Minimal α Property Vocabulary (Starter)

Supply schedule; finality target; fee model; validator/committee bounds; governance powers & thresholds; security assumptions; economic invariants (collateral/solvency/peg rules).

### W_αβ (Scoring Sketch)

α_c = clip(w₁·(coverage) + w₂·(pass_rate) - w₃·(severity_penalty)) ∈ [0,1]

where:
- coverage = (properties_with_checks) / (total_properties)
- pass_rate = (checks_passed) / (total_checks)
- severity_penalty = weighted sum of critical failures

### W_βγ (Distributional)

Build expected use-mix p from β (fees, latency, yields). Observe q from transaction data. Earth Mover's Distance: d = EMD(p, q), normalize to [0,1] → β_c = 1-d.

### W_γα (Drift)

From α, derive reference signature u(t) (e.g., "cash-like": many micro-payments). Compare to observed v(t) via normalized edit distance → γ_c = 1-norm_dist(u,v).

### Global Witness Gates

- **S₃ symmetry:** Recompute C_Σ under axis permutations; equality within tolerance
- **Stability:** VRF-seeded repeats; variance ≤ τ_var
- **Budget:** B ≤ B_max AND η = Δλ_Σ/B ≥ η_min (Phase-1 start at 10^(-6))

### Oracle Policy Templates

**Bridge large-transfer gate:**
```
C_Σ ≥ 0.80 ∧ β_c ≥ 0.75
```

**Lending LTV curve:**
```
LTV = 0.50 + 0.30·(C_Σ - 0.60)/0.20, clamped to [0.50, 0.80]
```

---

## Appendix A — Scoring Primitives (Deterministic)

Let clip(x) = min(1, max(0, x)).

**Two-sided range [L, U]:**
```
s_range(x; L, U, τ) = clip(1 - max(0, x-U, L-x) / τ)
```

**One-sided (≤ T):**
```
s_≤(x; T, τ) = clip(1 - max(0, x-T) / τ)
```

**One-sided (≥ T):**
```
s_≥(x; T, τ) = clip(1 - max(0, T-x) / τ)
```

**Invariant check:**
```
s_inv = 1 if holds else 0
```

**Distributional (JS divergence d ∈ [0,1]):**
```
s_dist = 1 - d
```

**Process distortion:**
```
s_proc = clip(1 - distortion / τ)
```

Axis scores are geometric means of their per-witness scores; C_Σ is the geometric mean of axis scores.

---

## Appendix B — Visual Diagrams

### Oracle Architecture
(See Section IV.1 for detailed data flow diagram)

### Coherence Trajectory (Terra 2022)

```
C_Σ
1.0 │                                    
0.9 │ ████████████ Production Threshold (0.80)
0.8 │                                    
0.7 │     ●━━━━━● Terra enters warning zone
0.6 │           ●                       ▓▓▓▓▓▓ Warning (0.60-0.80)
0.5 │             ╲                     
0.4 │               ●  ALERT            ░░░░░░ Critical (<0.40)
0.3 │                 ╲      ●          
0.2 │                   ●─────●  Depeg & Collapse
0.0 └── Jan  Feb  Mar  Apr  May  Jun
        ←———————— 2022 ————————→
```

**Key events:**
- **Feb 2022:** C_Σ ≈ 0.72 (functional but β_c showing strain)
- **Mar 2022:** C_Σ ≈ 0.64 (enters warning zone)
- **Apr 2022:** C_Σ ≈ 0.42 (ALERT) ← **TSC would flag here**
- **May 9, 2022:** Depeg and collapse

**Note:** Projected scores; validation notebook will verify.

---

## Appendix C — Reference Schema (Ethereum mainnet)

```yaml
version: "1.0.0"
chain: "ethereum-mainnet"
checkpoint_frequency: "daily"
window_size: 7200  # blocks (~1 day)

alpha_requirements:
  - id: block_time_target
    type: range_two_sided
    claim: "12 s block time"
    target: {L: 11.0, U: 13.0, unit: "seconds"}
    datasource: "rpc://<eth-rpc>"  # placeholder
    query: "avg(diff(block.timestamp)) over window"
    weight: 1.0
    tolerance: 0.15

  - id: finality_gasper
    type: range_le
    claim: "≤2 epochs to finality"
    target: {T: 900, unit: "seconds"}
    datasource: "beacon://<consensus-client>"  # placeholder
    query: "time_to_finality_p95"
    weight: 1.0
    tolerance: 300

  - id: validator_decentralization
    type: range_le
    claim: "No entity >25% stake"
    target: {T: 0.25, unit: "fraction"}
    datasource: "beacon://<consensus-client>"  # placeholder
    query: "max(entity_stake_share)"
    weight: 2.0
    tolerance: 0.05

  - id: erc20_transfer_safety
    type: invariant
    claim: "ERC20 transfers cannot reenter"
    target: {holds: true}
    datasource: "analyzer://mythril"
    query: "check_invariant('no_reentrancy','transfer')"
    weight: 2.0

beta_sources:
  rpc_endpoint: "https://<eth-rpc>"  # placeholder
  beacon_endpoint: "https://<beacon-api>"  # placeholder
  gas_market:
    - source: "etherscan/gastracker"
      metrics: ["base_fee","priority_fee_p50","priority_fee_p95"]
  token_distribution:
    - source: "etherscan/tokenholders"
      metrics: ["top10_concentration","gini_coefficient"]

gamma_features:
  - id: tx_type_distribution
    type: distribution
    baseline: "s3://baselines/eth_txmix.parquet"
    current: "query: tx_type_histogram over window"
    distance_metric: "jensen_shannon"
    datasource: "rpc://<eth-rpc>"  # placeholder

  - id: gas_usage_stability
    type: process
    metric: "coefficient_of_variation(base_fee)"
    threshold: {le: 0.5}
    datasource: "etherscan/gastracker"

  - id: validator_participation
    type: range_ge
    target: {T: 0.95, unit: "fraction"}
    datasource: "beacon://<consensus-client>"  # placeholder
    query: "active_validators / total_validators"

scoring_config:
  primitives:
    range_two_sided: "1 - max(0, max(x-U, L-x))/τ"
    range_le:        "1 - max(0, x-T)/τ"
    range_ge:        "1 - max(0, T-x)/τ"
    invariant:       "1 if holds else 0"
    distribution:    "1 - JS_divergence(current, baseline)"
    process:         "1 - distortion/τ"
  aggregation:
    axis_scores:     "geometric_mean"
    global:          "geometric_mean(alpha_c, beta_c, gamma_c)"
  thresholds:
    production: 0.80
    warning: 0.60
    critical: 0.40

provenance:
  method_version: "tsc-oracle-v1.0.0"
  schema_version: "1.0.0"
  implementation: "github.com/tsc-blockchain/oracle@<commit>"  # placeholder
  frozen_inputs_hash: "sha256:<blob>"  # placeholder
  container_image: "ghcr.io/tsc/oracle@sha256:<digest>"  # placeholder
  licenses:
    - id: "etherscan_terms_v2025-01"
    - id: "beacon_api_terms_v2025-02"
```

---

## Appendix D — Implementation Roadmap (Partner Guide)

**This appendix provides detailed month-by-month implementation guidance for the blockchain team working independently.**

### D.1 Phase 0: Parser Development (Months 1-3)

#### Month 1-2: Alpha Parser

**Goal:** Extract protocol claims from whitepapers, governance docs, technical specs.

**Deliverable:** `blockchain_parsers/alpha.py`

**Tasks:**
1. **Week 1-2: Design claim catalog**
   - Survey 5 chains (BTC, ETH, Solana, Arbitrum, Optimism)
   - Identify 20-30 common property types
   - Create template: {claim_id, claim_type, measurable (bool)}
   
2. **Week 3-4: Whitepaper parser**
   - Implement PDF→text extraction
   - Parse declarative statements ("MUST", "SHALL", "targets")
   - Filter for measurability
   
3. **Week 5-6: Governance proposal parser**
   - Fetch on-chain proposals (Governor contracts)
   - Parse forum posts (Discourse, Commonwealth APIs)
   - Extract claimed properties from proposals
   
4. **Week 7-8: Integration & testing**
   - Test on 5 chains
   - Verify reproducibility (99%+ across runs)
   - Document edge cases

**Success criteria:**
- ✓ Extract 20+ measurable claims per chain
- ✓ <5 minutes per chain
- ✓ 99%+ reproducible

**Open questions requiring experimentation:**
- How to handle vague language? ("highly scalable" → measurable?)
- Agreement between two annotators? (inter-rater reliability test)
- What fraction of whitepaper claims are measurable? (estimate: 20-40%)

#### Month 2-3: Beta & Gamma Parsers

**Goal:** Extract on-chain metrics (beta) and usage patterns (gamma).

**Deliverable:** `blockchain_parsers/beta.py`, `blockchain_parsers/gamma.py`

**Beta Parser Tasks:**
1. **Week 1-2: RPC query layer**
   - Implement connection pooling
   - Rate limit handling (exponential backoff)
   - Caching (don't re-query same blocks)
   
2. **Week 3-4: Metrics extraction**
   - Validator distribution (query staking contracts)
   - Token holder concentration (Etherscan/Nansen APIs)
   - Performance metrics (block times, finality, throughput)
   
3. **Week 5-6: Cross-chain support**
   - Abstract RPC interface (Ethereum vs. Solana vs. Bitcoin)
   - Handle different consensus mechanisms (PoW vs. PoS)
   - Normalize metrics to [0,1] range

**Gamma Parser Tasks:**
1. **Week 1-2: Transaction taxonomy**
   - Design classification schema (DEX/lending/NFT/bridge/transfer)
   - Implement heuristics (method signatures, recipient addresses)
   - Test on Ethereum (most complex)
   
2. **Week 3-4: Analytics platform integration**
   - Dune Analytics API (if available)
   - Flipside Crypto (SQL queries)
   - The Graph (subgraph queries)
   
3. **Week 5-6: Time series computation**
   - Rolling windows (7-day, 30-day)
   - User retention metrics
   - Gas usage stability

**Success criteria:**
- ✓ Beta: 30+ metrics per chain, <10 min per chain
- ✓ Gamma: 90%+ transaction classification, <15 min per chain
- ✓ Both: Handle missing data gracefully

#### Month 3: Integration & Testing

**Goal:** End-to-end parser suite working on 5 chains.

**Tasks:**
1. **Week 1: Integration**
   - Combine alpha/beta/gamma into unified pipeline
   - Test on all 5 chains
   - Debug edge cases
   
2. **Week 2: Performance optimization**
   - Profile bottlenecks
   - Parallelize where possible
   - Target: <30 min for 5 chains
   
3. **Week 3: Reproducibility validation**
   - Run parsers 10 times on same input
   - Measure variance
   - Fix non-deterministic components
   
4. **Week 4: Documentation**
   - Write parser README
   - Document data source requirements
   - Provide usage examples

**Deliverable:** Working parser suite ready for Phase 1a validation.

**Gate checkpoint:** Demonstrate parsers to stakeholders before proceeding.

### D.2 Phase 1a: Validation Notebooks (Months 4-6)

#### Month 4-5: Terra/Luna Validation

**Goal:** Prove TSC can retroactively detect Terra's coherence collapse.

**File:** `notebooks/terra_202204.ipynb`

**Tasks:**
1. **Week 1-2: Data acquisition**
   - Acquire Terra snapshot (2022-04-15T00:00:00Z)
   - Options: Flipside Crypto, Nansen, public archives
   - Verify data integrity (block hashes match)
   - Freeze dataset (create immutable snapshot)
   
2. **Week 3-4: Feature extraction**
   - Run all three parsers on frozen data
   - Extract α/β/γ features
   - Save intermediate results
   
3. **Week 5-6: Witness computation**
   - Implement W_αβ (coverage/pass-rate/severity)
   - Implement W_βγ (EMD between expected/observed)
   - Implement W_γα (edit distance between trajectories)
   
4. **Week 7-8: Coherence computation**
   - Compute α_c, β_c, γ_c
   - Aggregate to C_Σ
   - Check: C_Σ ≈ 0.27 ± 0.10?
   
5. **Week 9-10: Iteration (if needed)**
   - If C_Σ outside tolerance, debug
   - Which axis is wrong? (α/β/γ)
   - Adjust witness functions
   - Re-run

**Success criteria:**
- ✓ C_Σ = 0.27 ± 0.10 (within tolerance)
- ✓ Reproducible (99%+ across 10 runs)
- ✓ All witnesses pass (S₃, variance, budget)
- ✓ Computational cost <$10 per run

**If FAIL after 10 weeks:** STOP. Escalate to owner for methodology review.

#### Month 6: DAO Validation

**Goal:** Secondary validation on different failure mode.

**File:** `notebooks/dao_201606.ipynb`

**Tasks:**
1. **Week 1-2: Data acquisition + feature extraction**
   - Ethereum archive node (2016-06-10T00:00:00Z)
   - Run parsers (should be faster than Terra)
   
2. **Week 3-4: Witness computation + coherence**
   - Reuse methodology from Terra
   - Target: C_Σ ≈ 0.56 ± 0.10
   - Verify reproducibility

**Success criteria:** Same as Terra validation.

**Mt. Gox notebook (optional):** If time permits, add as third validation case.

**Gate checkpoint:** All validation notebooks PASS before proceeding to Phase 1b.

### D.3 Phase 1b: Oracle Infrastructure (Months 7-12)

**Only proceed if Phase 1a validation succeeds.**

#### Month 7-8: Smart Contract Development

**Goal:** Deploy coherence oracle contract on testnet.

**File:** `oracle/contracts/CoherenceOracle.sol`

**Tasks:**
1. **Week 1-2: Contract development**
   - Implement ICoherenceOracle interface
   - latest() and verify() functions
   - Provenance hash storage
   
2. **Week 3-4: Testing**
   - Unit tests (Foundry/Hardhat)
   - Integration tests (testnet deployment)
   - Gas optimization
   
3. **Week 5-6: Testnet deployment**
   - Deploy to Sepolia/Goerli
   - Publish one report per day for 7 days
   - Monitor for failures
   
4. **Week 7-8: Security review**
   - Internal audit
   - Consider external audit (if budget allows)
   - Fix vulnerabilities

#### Month 9-10: REST API Development

**Goal:** HTTP interface for oracle queries.

**File:** `oracle/api/server.py`

**Tasks:**
1. **Week 1-2: API implementation**
   - GET /v1/coherence/{chain}
   - Response format: {C_Σ, λ_Σ, α_c, β_c, γ_c, trend}
   - Authentication (API keys)
   
2. **Week 3-4: Caching layer**
   - Redis for hot data
   - PostgreSQL for historical reports
   - Cache invalidation strategy
   
3. **Week 5-6: Rate limiting**
   - Per-user quotas
   - DDoS protection
   - Error handling
   
4. **Week 7-8: Documentation**
   - API reference (OpenAPI/Swagger)
   - Usage examples
   - Client libraries (Python, JavaScript)

#### Month 11-12: Single-Chain Monitoring

**Goal:** Daily measurements of Ethereum mainnet.

**Tasks:**
1. **Week 1-2: Automation**
   - Cron job: measure Ethereum daily
   - Store results in database
   - Publish to smart contract
   
2. **Week 3-4: Alerting**
   - Email/Slack alerts when C_Σ < 0.60
   - Weekly digest emails
   - Anomaly detection
   
3. **Week 5-6: Dashboard (read-only)**
   - Visualize C_Σ over time
   - Show α/β/γ breakdown
   - Historical charts
   
4. **Week 7-8: Internal pilot**
   - Invite 2-3 users
   - Collect feedback
   - Fix bugs

**Deliverable:** Working oracle monitoring Ethereum testnet + mainnet.

**Gate checkpoint:** 30 consecutive days without failures before Phase 1c.

### D.4 Phase 1c: Production Launch (Months 13-18)

**Only proceed if Phase 1b testnet is stable.**

#### Month 13-14: Multi-Chain Support

**Goal:** Expand from Ethereum to 5-10 chains.

**Tasks:**
1. **Week 1-2: Chain integration**
   - Add parsers for: Bitcoin, Solana, Arbitrum, Optimism, Polygon
   - Test each chain individually
   
2. **Week 3-4: Infrastructure scaling**
   - Multiple RPC endpoints per chain
   - Load balancing
   - Parallel measurements
   
3. **Week 5-6: Cross-chain dashboard**
   - Multi-chain view
   - Comparative metrics
   - Risk ranking

#### Month 15-16: Pilot Partnerships

**Goal:** Integrate oracle with 2-3 real users.

**Target partners:**
1. **Bridge protocol** (e.g., Across, Connext)
   - Use C_Σ for transfer limits
   - Alert when source/dest chain C_Σ drops
   
2. **Lending protocol** (e.g., Aave, Compound)
   - Adjust LTV based on collateral chain C_Σ
   - Pause markets when C_Σ < 0.40
   
3. **Exchange** (optional)
   - Listing gates (require C_Σ ≥ 0.70)
   - Watchlist warnings

**Tasks:**
1. **Week 1-4: Partnership development**
   - Outreach, NDAs, technical integration
   - Custom policies for each partner
   
2. **Week 5-8: Integration + testing**
   - Test on testnet
   - Monitor in production (shadow mode first)
   - Tune thresholds based on feedback

#### Month 17-18: Public Launch

**Goal:** Production oracle service available to all.

**Tasks:**
1. **Week 1-2: Marketing**
   - Blog post announcing launch
   - Twitter/Discord promotion
   - Conference presentation (if possible)
   
2. **Week 3-4: Documentation finalization**
   - Complete API docs
   - Use case examples
   - FAQ
   
3. **Week 5-6: Monitoring + support**
   - 24/7 uptime monitoring
   - User support channel (Discord/Telegram)
   - Bug bounty program (optional)
   
4. **Week 7-8: Review + planning**
   - Retrospective: What worked? What didn't?
   - Measure success metrics (users, API calls, partnerships)
   - Plan Phase 2 research (if proceeding)

**Deliverable:** Production oracle measuring 5-10 chains daily, 2-3 pilot partnerships live, public API available.

**Success milestone:** This completes Phase 1 (12-18 month goal).

### D.5 Implementation Tips

**Communication:**
- Weekly async updates (15 min write-up)
- Monthly sync call (1 hour)
- Escalate blockers immediately

**Quality gates:**
- Don't skip validation (Phase 1a)
- Don't rush to production (Phase 1c)
- Iterate on methodology if validation fails

**Budget discipline:**
- Track data costs monthly
- Optimize RPC queries (caching!)
- Don't overspend on infrastructure

**Documentation:**
- Write as you build (not afterward)
- Document every decision
- Future you will thank you

---

## Appendix E — Open Research Questions

**These questions do NOT have known answers. Implementation team must experiment to find solutions.**

### E.1 Alpha Articulation: Measurability

**Problem:** Not all protocol claims are measurable. How do we filter?

**Question:** What fraction of whitepaper statements can be turned into testable properties?

**Experiment:**
1. Take 5 whitepapers (BTC, ETH, Solana, Cardano, Polkadot)
2. Extract all declarative statements (e.g., sentences with "must", "shall", "targets")
3. Annotate each statement: measurable (yes/no/maybe)
4. Two independent annotators → measure inter-rater agreement

**Hypothesis:** 20-40% of statements are measurable.

**Success metric:** Cohen's kappa >0.6 (substantial agreement between annotators)

**Time estimate:** 2-3 weeks

### E.2 Beta Calibration: Heterogeneous Metrics

**Problem:** β-axis combines Gini coefficient (concentration), block time (performance), MEV (financial). These have different units.

**Question:** How do we normalize heterogeneous metrics to [0,1]?

**Experiments to try:**
1. **Z-score normalization:** (x - μ) / σ, then clip to [0,1]
2. **Min-max scaling:** (x - min) / (max - min)
3. **Rank-based:** Convert to percentile ranks
4. **Learned embedding:** Train neural network to map metrics → [0,1]

**Test:** Measure 20 chains, compute C_Σ under each normalization. Which produces ranking that matches expert intuition?

**Success metric:** Spearman correlation >0.7 with expert ranking

**Time estimate:** 3-4 weeks

### E.3 Gamma Taxonomy: Transaction Classification

**Problem:** Ethereum has 100+ transaction types. Which matter for "usage coherence"?

**Question:** What's the minimal transaction taxonomy that captures usage patterns?

**Experiments:**
1. **Top-N heuristic:** Use top 10 types by volume
2. **Clustering:** Group transactions by bytecode similarity
3. **Manual taxonomy:** DEX/lending/NFT/bridge/other (5 categories)
4. **Topic modeling:** LDA on transaction data

**Test:** Does chosen taxonomy predict 30-day user retention?

**Success metric:** Predictive AUC >0.65

**Time estimate:** 4-5 weeks

### E.4 Temporal Stability: Window Size

**Problem:** γ-axis uses time windows. Too short = noisy, too long = slow to detect drift.

**Question:** What's the optimal window size for stability measurement?

**Experiment:**
1. Compute γ_c for windows: 1-day, 7-day, 14-day, 30-day
2. Measure across 12 months on 5 chains (5 × 12 = 60 measurements per window size)
3. Compare: variance, lag to detect known incidents, false positive rate

**Success metric:** 30-day window shows best balance (low variance, reasonable lag)

**Time estimate:** 2-3 weeks

### E.5 Threshold Calibration: Optimal Θ

**Problem:** Oracle uses Θ = 0.80 as production threshold. Is this right?

**Question:** What threshold maximizes detection accuracy?

**Experiment:**
1. Label 50 chains as "healthy" or "at-risk" (expert judgment or historical outcome)
2. Compute C_Σ for each chain
3. ROC curve: vary Θ from 0.4 to 0.9
4. Find Θ that maximizes F1 score (balance precision/recall)

**Test:** Validate on 20 held-out chains

**Success metric:** F1 >0.75 on held-out set

**Time estimate:** 3-4 weeks (requires large dataset)

**Note:** This comes AFTER Phase 1a validation. Don't optimize Θ before proving methodology works.

### E.6 Data Availability: Trust Assumptions

**Problem:** Terra nodes are pruned. We rely on Flipside/Nansen archives.

**Question:** How do we verify third-party data integrity?

**Approaches:**
1. **Cross-validation:** Compare multiple sources (Flipside vs. Nansen)
2. **Spot checks:** Sample blocks, verify hashes against multiple providers
3. **Cryptographic proofs:** Request Merkle proofs for critical data points
4. **Accept risk:** Document trust assumption explicitly

**Recommendation:** Use approach #1 (cross-validation) + #4 (document assumption).

**Time estimate:** 1-2 weeks

### E.7 Performance: Computational Cost

**Problem:** Full TSC conformance requires optimal transport (O(n³)) and bootstrap CIs (expensive).

**Question:** Can we get "good enough" results with cheaper approximations?

**Experiments:**
1. **EMD approximation:** Use Sinkhorn algorithm (faster than linear program)
2. **Fewer bootstrap samples:** 1000 → 100 samples
3. **Simpler witnesses:** Skip braided interchange (Phase 1 only)

**Test:** Compare C_Σ from full vs. approximate computation. Acceptable error: ±0.05

**Success metric:** 10x speedup with <0.05 error

**Time estimate:** 2-3 weeks

---

## References & Availability

- Triadic Self-Coherence (TSC) framework (2024). Mathematical foundations and axioms. github.com/usurobor/tsc
- Coherent Blockchain (2025). Protocol direction and leverage-based gating.
- Incident reports: Terra/Luna post-mortems, The DAO reentrancy analyses, archival Bitcoin studies.
- Earth Mover's Distance: Rubner, Y., Tomasi, C., & Guibas, L. J. (2000). The Earth Mover's Distance as a metric for image retrieval. *International Journal of Computer Vision*.
- Edit distance: Wagner, R. A., & Fischer, M. J. (1974). The string-to-string correction problem. *Journal of the ACM*.

A full bibliography with DOIs/URLs will be included in the arXiv submission.

---

## ArXiv Submission Checklist

- **Categories:** `cs.CR` (Cryptography and Security), `cs.DC` (Distributed Computing)
- **Keywords:** blockchain measurement, coherence, DeFi risk, reproducibility, zero-knowledge
- **Source:** LaTeX or PDF from Markdown
- **Include:** `.bib` with 5-8 core references (TSC framework, Terra/DAO post-mortems, EMD/edit-distance citations)
- **Artifacts:** Link to validation notebooks repo when ready
- **Diagrams:** Replace ASCII diagrams with vector PDFs if possible
- **Math rendering:** Uses Unicode symbols for GitHub; convert to LaTeX for arXiv
- **Placeholders:** Clearly marked in schema (e.g., `<eth-rpc>`, `<commit>`, `<blob>`, `<digest>`)

---

## Conclusion

This paper specifies TSC-blockchain, an application of the general-purpose Triadic Self-Coherence framework to blockchain risk measurement. The implementation follows a phased approach:

**Phase 0 (Months 1-3):** Build blockchain-specific parsers (α/β/γ articulation)

**Phase 1a (Months 4-6):** Validate methodology on historical failures (Terra, DAO)

**Phase 1b (Months 7-12):** Build oracle infrastructure (smart contract, API, monitoring)

**Phase 1c (Months 13-18):** Production launch (multi-chain support, pilot partnerships)

**Phase 2 (Months 19+):** Research Proof-of-Coherence consensus mechanism

**Total timeline: 12-18 months to production oracle.**

**Critical gates:**
- Month 3: Parser demo (before validation)
- Month 6: Terra validation (before infrastructure)
- Month 12: Oracle testnet stability (before production)

**Each phase is contingent on the previous phase succeeding.** If validation fails, iterate methodology before infrastructure investment.

**Next artifact to ship:** Three parser implementations (`alpha.py`, `beta.py`, `gamma.py`) working on 5 chains (BTC, ETH, Solana, Arbitrum, Optimism).

---

**End of v1.1.0**