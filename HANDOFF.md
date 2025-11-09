# TSC Blockchain - Partner Handoff Package

**Date:** November 2025  
**Partner:** Renfei Zou  
**TSC Core Owner:** Peter Lisovin  
**Handoff Version:** 1.0

---

## What You're Getting

**Complete Package:**
1. ✅ **Vision paper** (v1.1.0): Complete specification, 12-18 month roadmap
2. ✅ **Code skeletons**: Parser templates with TODOs and test cases
3. ✅ **Implementation guide**: Month-by-month deliverables (Appendix D)
4. ✅ **Work agreement**: Expectations, checkpoints, budget (partner_expectations.md)

**Repository:** github.com/[org]/tsc-blockchain

---

## What You're Building

### Phase 0: Parser Development (Months 1-3)
**Goal:** Extract blockchain data for α/β/γ articulation

**Deliverables:**
- `blockchain_parsers/alpha.py` - Protocol claims parser
- `blockchain_parsers/beta.py` - On-chain metrics parser
- `blockchain_parsers/gamma.py` - Usage patterns parser
- Working on 5 test chains (BTC, ETH, Solana, Arbitrum, Optimism)

**Success criteria:**
- ✓ Extract 20+ claims (alpha), 30+ metrics (beta), 90%+ tx classification (gamma)
- ✓ Complete in <30 minutes for 5 chains
- ✓ 99%+ reproducible across runs

### Phase 1a: Validation Notebooks (Months 4-6)
**Goal:** Prove TSC can detect historical blockchain failures

**Deliverables:**
- `notebooks/terra_202204.ipynb` - Terra/Luna collapse (C_Σ ≈ 0.27 ± 0.10)
- `notebooks/dao_201606.ipynb` - The DAO hack (C_Σ ≈ 0.56 ± 0.10)
- `notebooks/mtgox_201402.ipynb` - Mt. Gox (optional, C_Σ ≈ 0.31 ± 0.10)

**Success criteria:**
- ✓ Scores within ±0.10 tolerance
- ✓ Reproducible (99%+ across 10 runs)
- ✓ All witnesses pass (S₃, variance, budget)
- ✓ Computational cost <$10 per run

### Phase 1b: Oracle Infrastructure (Months 7-12)
**Goal:** Deploy production oracle monitoring Ethereum

**Deliverables:**
- `oracle/contracts/CoherenceOracle.sol` - Smart contract on testnet
- `oracle/api/server.py` - REST API (GET /v1/coherence/{chain})
- Ethereum mainnet monitoring (daily measurements)
- Dashboard (read-only, internal pilot)

**Success criteria:**
- ✓ 30 consecutive days without failures
- ✓ 2-3 internal users providing feedback
- ✓ SLO: <5 min latency per measurement

### Phase 1c: Production Launch (Months 13-18)
**Goal:** Public oracle measuring 5-10 chains with pilot partnerships

**Deliverables:**
- Multi-chain support (BTC, ETH, Solana, Arbitrum, Optimism, Polygon)
- 2-3 pilot partnerships (bridge + lender + exchange)
- Public API with documentation
- Monitoring dashboard

**Success criteria:**
- ✓ Daily measurements for 5-10 chains
- ✓ Pilot partners integrated and using data
- ✓ Public API handling 100+ requests/day

---

## What TSC Core Owner Provides

**Your responsibilities:**
- ✅ TSC framework maintenance (v2.3.0 → v2.4.0 by Q1 2025)
- ✅ Reference Python implementation (github.com/usurobor/tsc)
- ✅ Vision paper (arXiv preprint)
- ✅ Consultation: 2 hours/week async + 1 hour/month sync
- ✅ Emergency support (rare, <2 hours/month average)

**What you're NOT responsible for:**
- ❌ Blockchain-specific parser development
- ❌ Data acquisition ($18K budget for Phase 0-1a)
- ❌ Oracle infrastructure deployment
- ❌ Partnership development with bridges/lenders
- ❌ Day-to-day blockchain implementation decisions

---

## What Partner Owns

**Your responsibilities:**
- ✅ All blockchain-specific code (parsers, oracle, smart contracts)
- ✅ Data acquisition (~$18K for Phase 0-1a, ~$30K total)
- ✅ Validation notebook execution
- ✅ Oracle infrastructure (testnet → production)
- ✅ Partnership development (bridges, lenders, exchanges)
- ✅ Documentation of implementation decisions

**Your autonomy:**
- ✅ Technical implementation decisions (which RPC provider, which analytics platform)
- ✅ Resource allocation (hire contractors, buy data access)
- ✅ Partnership priorities (which bridge/lender to approach first)
- ✅ Timeline flexibility within phases (can extend by 2-4 weeks if needed)

**Your constraints:**
- ⚠️ Cannot skip validation (Phase 1a) - must prove methodology works
- ⚠️ Cannot proceed to Phase 1b without passing Gate 2 (Terra validation)
- ⚠️ Must maintain TSC framework compatibility (don't fork the core math)
- ⚠️ Must document major decisions (for reproducibility)

---

## Critical Gates (Do NOT Skip)

### Gate 1: Month 3 - Parser Demo
**What you demonstrate:**
- Parsers working on 5 chains
- Extract features in <30 minutes total
- 99%+ reproducibility across runs
- Unit tests pass

**Review format:**
- 1-hour demo call
- Show live execution on 2 chains (ETH + Solana)
- Show test results
- Q&A

**If PASS:** Proceed to Phase 1a (validation)  
**If FAIL:** Extend Phase 0 by 4 weeks, address issues, re-demo

---

### Gate 2: Month 6 - Terra Validation (CRITICAL)
**What you demonstrate:**
- `terra_202204.ipynb` running successfully
- C_Σ = 0.27 ± 0.10 (within tolerance)
- Reproducible across 10 runs (99%+ agreement)
- All witnesses pass
- Computational cost <$10

**Review format:**
- 2-hour deep dive
- Walk through notebook cell-by-cell
- Show reproducibility results
- Discuss methodology

**If PASS:** Proceed to Phase 1b (oracle infrastructure)  
**If FAIL:** **STOP.** Do NOT proceed to Phase 1b.
- Iterate methodology 4-8 weeks
- Debug which axis is wrong (α/β/γ)
- Tune witness functions
- Re-run validation
- Re-submit for Gate 2 review

**This is the most critical gate.** If TSC can't detect Terra's failure retroactively, the methodology doesn't work for blockchains.

---

### Gate 3: Month 12 - Oracle Testnet Stability
**What you demonstrate:**
- 30 consecutive days of Ethereum measurements
- No failures or crashes
- 2-3 internal users using dashboard
- Logs showing consistent performance

**Review format:**
- 1-hour review of monitoring dashboard
- Show uptime statistics
- User feedback summary
- Infrastructure costs review

**If PASS:** Proceed to Phase 1c (production launch)  
**If FAIL:** Extend Phase 1b by 8 weeks, address stability issues

---

## Communication & Checkpoints

### Weekly (Async)
**Format:** Slack/Discord post (15 min to write)

**Template:**
```
Week of [Date]:

Progress:
- ✅ Completed: [specific achievements]
- 🔄 In progress: [current work]
- ⏳ Blocked: [issues, if any]

Next week plan:
- [ ] Task 1
- [ ] Task 2

Questions for owner:
- Q1: [specific question]
- Q2: [specific question]

Metrics:
- Lines of code: [if relevant]
- Test coverage: [if relevant]
- Budget spent: $X / $Y
```

**Response SLA:** Owner responds within 48 hours (business days)

---

### Monthly (Sync)
**Format:** 1-hour video call

**Agenda:**
1. **Progress review** (20 min)
   - What shipped this month
   - Compare to roadmap
   - Adjust timeline if needed

2. **Technical deep dive** (20 min)
   - Demo current work
   - Discuss technical decisions
   - Code review (if needed)

3. **Roadmap & risks** (15 min)
   - Next month's priorities
   - Budget review
   - Risk assessment

4. **Q&A** (5 min)

**Scheduling:** First Monday of each month, 10am PT (or agreed alternative)

**Minutes:** Partner documents key decisions and shares within 24 hours

---

### Emergency (As Needed)
**When to escalate:**
- ⚠️ Critical blocker preventing progress (can't acquire Terra data)
- ⚠️ Major methodology concern (Terra validation produces C_Σ = 0.65, not 0.27)
- ⚠️ Budget overrun risk (>20% over estimate)
- ⚠️ Timeline slip risk (>1 month delay on critical path)

**How to escalate:**
- Post in #tsc-urgent channel with `@owner` mention
- Email with subject: "[URGENT] TSC Blockchain - [issue]"
- Expected response: Within 24 hours

**Don't hesitate to escalate.** Better to raise concerns early than struggle silently.

---

## Budget & Resources

### Phase 0-1a Budget (Months 1-6)

**Data Acquisition:**
- Archive node access: $1,500/month × 6 = $9,000
- Analytics platforms (Nansen/Flipside): $2,000/month × 3 = $6,000
- One-time datasets (Terra snapshot): $3,000
- **Subtotal: $18,000**

**Compute:**
- Cloud infrastructure (AWS/GCP): $500/month × 6 = $3,000
- Development machines: $1,000 (one-time)
- **Subtotal: $4,000**

**Engineering:**
- 1 FTE × 6 months = varies by location/rate
- Estimate: $60K-100K (depends on engineer cost)

**Total Phase 0-1a: ~$82K-122K**

### Phase 1b-1c Budget (Months 7-18)

**Infrastructure:**
- Testnet deployment: $500/month × 6 = $3,000
- Production infrastructure: $2,000/month × 6 = $12,000
- Data access (ongoing): $1,500/month × 12 = $18,000
- **Subtotal: $33,000**

**Engineering:**
- 1-2 FTE × 12 months = $120K-200K

**Partnerships:**
- Travel, events, legal: $10,000

**Total Phase 1b-1c: ~$163K-243K**

**Grand Total (12-18 months): $245K-365K**

### Partner Responsibility
You are responsible for securing this budget through:
- Grant funding (Ethereum Foundation, Protocol Guild, etc.)
- Self-funding
- Investor backing
- Consulting revenue

Owner is NOT providing funding, only technical guidance.

---

## Success Metrics

### 3-Month Check (End of Phase 0)
- [ ] Parsers work on 5 chains
- [ ] Features extracted: 20+ (alpha), 30+ (beta), 90%+ tx coverage (gamma)
- [ ] Performance: <30 min for 5 chains
- [ ] Reproducibility: 99%+
- [ ] Unit tests: 80%+ coverage

### 6-Month Check (End of Phase 1a)
- [ ] Terra validation PASS (C_Σ = 0.27 ± 0.10)
- [ ] DAO validation PASS (C_Σ = 0.56 ± 0.10)
- [ ] All witnesses pass (S₃, variance, budget)
- [ ] Reproducibility: 99%+ across 10 runs
- [ ] Notebooks public on GitHub

### 12-Month Check (End of Phase 1b)
- [ ] Oracle contract deployed on testnet
- [ ] REST API functional
- [ ] Ethereum monitoring: 30 days without failures
- [ ] 2-3 internal users providing feedback
- [ ] Documentation complete

### 18-Month Check (End of Phase 1c)
- [ ] Oracle measuring 5-10 chains daily
- [ ] 2-3 pilot partnerships live
- [ ] Public API handling 100+ requests/day
- [ ] Revenue potential identified (oracle subscriptions?)
- [ ] Phase 2 research plan (if proceeding)

---

## IP & Ownership

### TSC Core Framework
- **Owner:** TSC Core team (Peter Lisovin)
- **License:** MIT (open source)
- **Usage:** Partner can use freely in blockchain application
- **Modifications:** Suggest improvements to core, but don't fork independently

### Blockchain Parsers & Oracle
- **Owner:** Partner (you)
- **License:** Apache 2.0 or MIT (must be open source)
- **Rationale:** Community benefit, reproducibility, trust

### Vision Paper
- **Authors:** Peter Lisovin (first author), Partner (second author)
- **License:** ArXiv preprint (open access)
- **Usage:** Both can reference, present, build upon

### Oracle Service (Business)
- **Owner:** Partner (you)
- **Monetization:** You can charge for API access, premium features, consulting
- **Revenue:** Partner keeps 100% of revenue
- **Attribution:** Acknowledge TSC Core framework in documentation

---

## Exit Conditions

### Partner Can Exit If:
- Validation repeatedly fails (>3 iterations without progress)
- Budget constraints (can't secure $250K+ funding)
- Priorities shift (other projects take precedence)
- Timeline extends beyond 24 months

**Exit protocol:**
- 30 days written notice (email to owner)
- Transfer all code to owner (MIT/Apache license already covers this)
- Final handoff call (1 hour)
- Document lessons learned

### Owner Can Exit If:
- Two consecutive missed checkpoints (no monthly sync + no weekly updates)
- Communication drops (no updates for 4+ weeks without notice)
- Methodology diverges from TSC principles without consultation
- Partner skips critical gates (proceeds to Phase 1b without passing Gate 2)

**Exit protocol:**
- 30 days written notice
- Final consult call (2 hours)
- Document handoff state

**Clean exit is OK.** Not every research project succeeds. What matters is learning and documentation.

---

## Repository Structure

```
tsc-blockchain/
├── README.md                       # Project overview
├── vision.md                       # v1.1.0 (this document's source)
├── HANDOFF.md                      # This file
├── partner_expectations.md         # Work agreement
│
├── blockchain_parsers/             # Phase 0 deliverables
│   ├── __init__.py
│   ├── alpha.py                    # Protocol claims parser
│   ├── beta.py                     # On-chain metrics parser
│   ├── gamma.py                    # Usage patterns parser
│   └── tests/
│       ├── test_alpha.py
│       ├── test_beta.py
│       ├── test_gamma.py
│       └── fixtures/
│           ├── ethereum_sample.yaml
│           ├── bitcoin_sample.yaml
│           └── solana_sample.yaml
│
├── notebooks/                      # Phase 1a deliverables
│   ├── terra_202204.ipynb
│   ├── dao_201606.ipynb
│   ├── mtgox_201402.ipynb
│   └── data/
│       ├── terra_snapshot/         # Acquired data
│       ├── dao_snapshot/
│       └── mtgox_snapshot/
│
├── oracle/                         # Phase 1b-1c deliverables
│   ├── contracts/
│   │   ├── CoherenceOracle.sol
│   │   └── tests/
│   ├── api/
│   │   ├── server.py
│   │   ├── routes.py
│   │   └── cache.py
│   └── dashboard/
│       └── index.html
│
├── docs/
│   ├── implementation.md           # Partner documents decisions
│   ├── api_reference.md
│   └── partnership_guide.md
│
└── scripts/
    ├── deploy_testnet.sh
    └── measure_chain.py
```

---

## Questions?

**Owner Contact:**
- Slack: @[owner handle]
- Email: [owner email]
- GitHub: @[owner github]
- Response SLA: 48 hours (business days)

**Before asking:**
1. Check vision.md Appendix D (implementation guide)
2. Check vision.md Appendix E (open research questions)
3. Review past weekly updates
4. Search GitHub issues/discussions

**When asking:**
- Be specific (not "How do I build alpha parser?" but "Should alpha parser extract from on-chain governance or forum posts first?")
- Provide context (what you've tried, why it's blocking)
- Suggest options (not just problems, but potential solutions)

---

## Getting Started (First Week)

### Day 1: Onboarding
- [ ] Read complete vision.md (10,000+ words, budget 3-4 hours)
- [ ] Review HANDOFF.md (this document)
- [ ] Review partner_expectations.md
- [ ] Set up repository access

### Day 2: Environment Setup
- [ ] Clone tsc-blockchain repo
- [ ] Set up Python environment (requirements.txt)
- [ ] Get RPC endpoint access (Alchemy/Infura free tier)
- [ ] Test basic queries (eth_getBlock on Ethereum)

### Day 3: Design Session
- [ ] Sketch alpha parser architecture
- [ ] List 5 chains' whitepaper URLs
- [ ] Identify 20-30 protocol property types
- [ ] Write design doc (share with owner for feedback)

### Day 4: First Code
- [ ] Implement `parse_whitepaper()` stub
- [ ] Extract Bitcoin whitepaper text
- [ ] Write test case: should extract ≥5 claims
- [ ] Push to GitHub branch

### Day 5: First Weekly Update
- [ ] Post Week 1 update (use template above)
- [ ] Schedule Month 1 sync call
- [ ] Ask first batch of questions

**By end of Week 1:** You should have running code (even if minimal) and clear plan for Month 1.

---

## Success Tips (From Similar Projects)

### 1. **Start Small, Iterate**
Don't try to parse all whitepaper claims on Day 1. Start with Bitcoin (simplest), extract 5 claims manually, then automate.

### 2. **Cache Aggressively**
RPC queries are expensive. Save raw responses to disk. Never re-query the same block.

### 3. **Document Decisions**
When you choose "Flipside over Nansen", write down why. Future you (or new team member) will thank you.

### 4. **Communicate Often**
Weekly updates seem like overhead, but they prevent 1-month "I've been stuck" surprises.

### 5. **Don't Skip Validation**
It's tempting to say "Terra validation probably works, let's build the oracle." **Don't.** Gate 2 exists for a reason.

### 6. **Use Real Data Early**
Don't build entire parser with mock data. Get real Terra data Week 1 (even if incomplete). Real data reveals edge cases.

### 7. **Budget Discipline**
Track costs monthly. Data access adds up fast. If you hit $20K at Month 3, you'll blow $40K by Month 6.

### 8. **Celebrate Wins**
When alpha parser works on 5 chains, take a day to document/celebrate. Research projects need momentum.

---

## What Happens After 18 Months?

### Success Scenario (Oracle Production)
**You have:**
- ✅ Oracle measuring 5-10 chains daily
- ✅ 2-3 pilot partnerships
- ✅ Public API with users
- ✅ ArXiv paper published

**Options:**
1. **Continue to Phase 2 (Research):** Proof-of-Coherence consensus mechanism (12-18 month research track)
2. **Commercialize:** Build oracle business (subscriptions, consulting, custom integrations)
3. **Transfer to community:** Open-source project, DAO governance
4. **Exit gracefully:** Document everything, hand off to new maintainer

### Partial Success (Validation Works, Infrastructure Delayed)
**You have:**
- ✅ Validation notebooks proving TSC works
- ✅ Parsers on 10+ chains
- ❌ Oracle infrastructure incomplete

**This is still valuable.** Publish notebooks + parsers as open-source contribution. Consider pivoting to:
- Research tool (not production oracle)
- Data-as-a-service (sell pre-computed coherence scores)
- Consulting (help protocols measure their own coherence)

### Validation Fails (Methodology Doesn't Work)
**You discover:**
- Terra validation produces C_Σ = 0.65, not 0.27
- After 3+ iterations, can't get within tolerance
- Methodology issues are fundamental

**This is also valuable learning.** Document:
- What was tried
- Why it didn't work
- What would need to change

Publish as "Lessons from applying TSC to blockchains" (negative results are publishable).

**Either way, you learned, documented, and contributed.**

---

## Final Checklist (Before Starting)

- [ ] I've read the complete vision.md (10,000+ words)
- [ ] I understand the 12-18 month timeline
- [ ] I've secured budget ($250K-365K) or have plan to secure it
- [ ] I have 20-40 hours/week to dedicate (1 FTE or 2 × 50%)
- [ ] I'm willing to iterate if validation fails
- [ ] I understand Gate 2 (Terra validation) is critical
- [ ] I know how to reach owner for questions
- [ ] I'm excited about this problem!

**If all checked → You're ready to start.**

**Welcome to TSC Blockchain. Let's measure the unmeasurable.** 🚀

---

**Version:** 1.0  
**Last Updated:** November 2025  
**Next Review:** Month 3 (after Parser Demo)