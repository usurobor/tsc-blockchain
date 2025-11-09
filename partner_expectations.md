# TSC Blockchain - Partner Work Agreement

**Effective Date:** November 2025  
**Partners:** Peter Lisovin (TSC Core) + Renfei Zou (TSC Blockchain)  
**Project Duration:** 12-18 months (Phase 0-1c)  
**Review Frequency:** Monthly

---

## Purpose of This Document

This agreement clarifies:
- **What each party owns and delivers**
- **How we communicate and make decisions**
- **When to check progress (critical gates)**
- **What happens if things don't go as planned**

This is a collaboration agreement, not a legal contract. The goal is clarity and alignment, not legal enforcement.

---

## I. Roles & Ownership

### TSC Core Owner (Peter) Provides:

**Technical Foundation:**
- ✅ TSC framework (v2.3.0 → v2.4.0 by Q1 2025)
- ✅ Reference Python implementation
- ✅ Mathematical specifications (C≡, witnesses, gates)
- ✅ Vision paper (arXiv preprint, joint authorship)

**Consultation:**
- ✅ 2 hours/week async availability (Slack/Discord responses)
- ✅ 1 hour/month sync call (video, scheduled in advance)
- ✅ Emergency support when needed (rare, <2 hrs/month average)

**Not Responsible For:**
- ❌ Blockchain-specific implementation
- ❌ Data acquisition budgets
- ❌ Partnership development
- ❌ Day-to-day coding decisions
- ❌ Funding (partner secures budget)

---

### TSC Blockchain Partner Owns:

**Implementation:**
- ✅ All blockchain-specific code (parsers, oracle, smart contracts)
- ✅ Phase 0-1c execution (12-18 months)
- ✅ Technical decisions (which RPC provider, analytics platform, etc.)
- ✅ Resource allocation (hiring, contractors, tools)

**Data & Infrastructure:**
- ✅ Data acquisition (~$18K for Phase 0-1a)
- ✅ Cloud infrastructure (~$12K for Phase 1b-1c)
- ✅ Analytics platform subscriptions (Nansen/Flipside/Dune)

**Partnerships:**
- ✅ Outreach to bridges, lenders, exchanges
- ✅ Partnership agreements and integrations
- ✅ Oracle business development (if monetizing)

**Documentation:**
- ✅ Implementation decisions logged
- ✅ Validation notebooks (public GitHub)
- ✅ API documentation (OpenAPI/Swagger)

**Funding:**
- ✅ Securing $245K-365K budget (grants, self-funding, investors)
- ✅ Budget management and reporting

---

## II. Communication & Decision Making

### Weekly Check-In (Async)

**Format:** Slack/Discord post every Monday

**Template:**
```
Week of [Date]:

✅ Completed:
- [Specific achievements]

🔄 In Progress:
- [Current work]

⏳ Blockers:
- [Issues preventing progress, if any]

📅 Next Week:
- [ ] Planned task 1
- [ ] Planned task 2

💰 Budget:
- Spent this week: $X
- Total spent: $Y / $Z

❓ Questions:
- [Specific questions for owner, if any]
```

**Response SLA:** Owner responds within 48 hours (business days)

---

### Monthly Sync (Video Call)

**Scheduling:** First Monday of each month, 10am PT (or mutually agreed time)

**Duration:** 1 hour

**Agenda:**
1. **Progress review** (20 min)
   - What shipped this month
   - Compare to roadmap
   - Celebrate wins

2. **Technical deep dive** (20 min)
   - Demo current work
   - Discuss implementation decisions
   - Code review if needed

3. **Planning & risks** (15 min)
   - Next month priorities
   - Budget review
   - Risk assessment (timeline, technical, funding)

4. **Q&A** (5 min)
   - Open discussion
   - Action items

**Minutes:** Partner documents key decisions and shares within 24 hours

---

### Emergency Escalation

**When to escalate:**
- ⚠️ **Critical blocker:** Can't proceed (e.g., can't acquire Terra data)
- ⚠️ **Methodology issue:** Validation produces unexpected results (C_Σ = 0.65 not 0.27)
- ⚠️ **Budget overrun:** Risk of exceeding budget by >20%
- ⚠️ **Timeline risk:** Likely to miss critical gate by >1 month

**How to escalate:**
- Post in #tsc-urgent with @owner mention
- Email: [owner email] with subject "[URGENT] TSC Blockchain - [issue]"
- Include: What's blocking, what you've tried, what you need

**Response SLA:** Within 24 hours (including weekends for true emergencies)

**Philosophy:** Escalate early. Silence is worse than raising concerns.

---

## III. Critical Gates (Do NOT Skip)

### Gate 1: Month 3 - Parser Demo

**Deliverable:**
- Alpha/beta/gamma parsers working on 5 chains (BTC, ETH, Solana, Arbitrum, Optimism)
- Unit tests passing (80%+ coverage)
- Features extracted in <30 minutes total

**Review Format:**
- 1-hour demo call
- Show live execution on 2 chains
- Walk through test results
- Q&A

**Success Criteria:**
- ✓ Parsers extract features (20+ alpha, 30+ beta, 90%+ gamma)
- ✓ Performance <30 min for 5 chains
- ✓ Reproducibility 99%+
- ✓ Code quality: readable, tested, documented

**If PASS:** Proceed to Phase 1a (validation notebooks)

**If FAIL:**
- Extend Phase 0 by 4 weeks
- Address specific issues (performance, reproducibility, test coverage)
- Re-demo

---

### Gate 2: Month 6 - Terra Validation (CRITICAL)

**Deliverable:**
- `notebooks/terra_202204.ipynb` running successfully
- C_Σ = 0.27 ± 0.10 (within tolerance)
- Reproducible (99%+ across 10 runs)
- All witnesses pass (S₃, variance, budget)
- Computational cost <$10 per run

**Review Format:**
- 2-hour deep dive
- Walk through notebook cell-by-cell
- Show reproducibility test results
- Discuss methodology and any tuning

**Success Criteria:**
- ✓ Score within tolerance (0.27 ± 0.10)
- ✓ Reproducible (std dev ≤ 0.01)
- ✓ All global gates pass
- ✓ Cost within budget

**If PASS:** Proceed to Phase 1b (oracle infrastructure)

**If FAIL:** **STOP. DO NOT PROCEED.**
- **This is the most critical decision point.**
- Iterate on methodology 4-8 weeks
- Debug which axis is wrong (α/β/γ)
- Tune witness functions
- Document what changed and why
- Re-submit for Gate 2 review

**After 3 failed iterations:** Pause project, reassess TSC blockchain applicability

**Rationale:** If TSC can't detect Terra's failure retroactively, the methodology doesn't work for blockchains. Building infrastructure without validation is waste.

---

### Gate 3: Month 12 - Oracle Testnet Stability

**Deliverable:**
- Oracle contract deployed on testnet
- REST API functional
- 30 consecutive days of Ethereum monitoring without failures
- 2-3 internal users providing feedback
- Logs showing consistent performance

**Review Format:**
- 1-hour dashboard review
- Show uptime statistics (target: 99.9%)
- User feedback summary
- Infrastructure cost review

**Success Criteria:**
- ✓ 30 days uptime ≥99.9%
- ✓ SLO: <5 min latency per measurement
- ✓ No crashes or data corruption
- ✓ Positive feedback from internal users

**If PASS:** Proceed to Phase 1c (production launch)

**If FAIL:**
- Extend Phase 1b by 8 weeks
- Address stability issues (monitoring, error handling, failover)
- Re-demonstrate 30-day stability

---

## IV. Budget & Resources

### Phase 0-1a: Parser Development + Validation (Months 1-6)

| Category | Monthly Cost | Duration | Total |
|----------|--------------|----------|-------|
| **Engineering** | Varies by rate | 6 months | $60K-100K |
| **Data access** | $1,500 | 6 months | $9,000 |
| **Analytics platforms** | $2,000 | 3 months | $6,000 |
| **Historical datasets** | One-time | -- | $3,000 |
| **Cloud compute** | $500 | 6 months | $3,000 |
| **Dev machines** | One-time | -- | $1,000 |
| **Phase 0-1a Subtotal** | | | **$82K-122K** |

### Phase 1b-1c: Infrastructure + Production (Months 7-18)

| Category | Monthly Cost | Duration | Total |
|----------|--------------|----------|-------|
| **Engineering** | Varies by rate | 12 months | $120K-200K |
| **Infrastructure** (testnet) | $500 | 6 months | $3,000 |
| **Infrastructure** (production) | $2,000 | 6 months | $12,000 |
| **Data access** (ongoing) | $1,500 | 12 months | $18,000 |
| **Partnership development** | -- | -- | $10,000 |
| **Phase 1b-1c Subtotal** | | | **$163K-243K** |

### Total Project Budget: $245K-365K (12-18 months)

**Budget Responsibility:** Partner secures funding through:
- Grant programs (Ethereum Foundation, Protocol Guild, ecosystem grants)
- Self-funding
- Investor backing
- Consulting/contracting revenue

**Owner NOT providing funding** - only technical guidance.

---

### Budget Tracking & Reporting

**Monthly:**
- Partner reports actual spend vs. budget
- Flag if >10% over in any category
- Discuss adjustments if needed

**Quarterly:**
- Review total burn rate
- Project remaining runway
- Adjust scope if budget constrained

**Red Flags:**
- Spending >20% over budget in any category
- Runway <3 months remaining
- Unplanned major expenses

**Contingency:** Budget includes ~20% buffer for unknowns

---

## V. IP & Commercialization

### TSC Core Framework

**Ownership:** TSC Core team (Peter Lisovin et al.)

**License:** MIT (open source)

**Partner Usage:**
- ✅ Can use freely in blockchain application
- ✅ Can modify for blockchain-specific needs
- ✅ Must attribute TSC Core in documentation
- ❌ Cannot claim ownership of core framework
- ❌ Cannot relicense under restrictive terms

**Future Changes:** If TSC Core relicenses (unlikely), existing versions remain MIT

---

### Blockchain Parsers & Oracle

**Ownership:** Partner

**License:** Apache 2.0 or MIT (must be open source)

**Rationale:**
- Community benefit (others can reproduce/verify)
- Reproducibility requirement (closed source breaks trust)
- Ecosystem contribution

**Partner Rights:**
- ✅ Can commercialize oracle service (subscriptions, consulting)
- ✅ Can build proprietary tools ON TOP of parsers
- ✅ Can provide paid support/hosting
- ❌ Cannot make parsers closed-source

---

### Vision Paper

**Authors:** Peter Lisovin (first author), [Partner Name] (second author)

**License:** ArXiv preprint (open access, CC BY 4.0)

**Usage:**
- ✅ Both can reference in presentations
- ✅ Both can cite in future papers
- ✅ Both can share publicly

**Future Publications:**
- Implementation results: Partner first author, Owner second
- Methodology refinements: Joint authorship (discuss case-by-case)

---

### Oracle Business

**Ownership:** Partner

**Revenue:** 100% to partner

**Attribution:** Acknowledge TSC Core framework in product docs

**Example:**
> "TSC Blockchain Oracle powered by Triadic Self-Coherence framework"

---

## VI. Success Metrics & Review

### 3-Month Review (End of Phase 0)

**Technical:**
- [ ] Parsers work on 5 chains
- [ ] Features extracted as specified
- [ ] Performance <30 min
- [ ] Tests passing (80%+ coverage)

**Process:**
- [ ] Weekly updates posted consistently
- [ ] Monthly syncs attended
- [ ] Communication effective

**Budget:**
- [ ] On track (<10% variance)

**Decision:** Proceed to Phase 1a / Adjust / Pause

---

### 6-Month Review (End of Phase 1a)

**Technical:**
- [ ] Terra validation PASS (C_Σ = 0.27 ± 0.10)
- [ ] DAO validation PASS (C_Σ = 0.56 ± 0.10)
- [ ] Reproducibility ≥99%
- [ ] Notebooks public on GitHub

**Process:**
- [ ] Methodology documented
- [ ] Decisions logged
- [ ] Community can verify

**Budget:**
- [ ] Phase 0-1a complete within $82K-122K estimate

**Decision:** Proceed to Phase 1b / Iterate methodology / Pivot / Exit

**CRITICAL:** This is the biggest decision point. If validation fails repeatedly, seriously consider whether to continue.

---

### 12-Month Review (End of Phase 1b)

**Technical:**
- [ ] Oracle contract deployed
- [ ] REST API functional
- [ ] 30 days stability ≥99.9%
- [ ] 2-3 users providing feedback

**Process:**
- [ ] Documentation complete
- [ ] Infrastructure documented
- [ ] Runbooks for operations

**Budget:**
- [ ] Phase 1b within estimate

**Decision:** Proceed to Phase 1c / Extend testnet period / Pause

---

### 18-Month Review (End of Phase 1c)

**Technical:**
- [ ] Oracle measuring 5-10 chains daily
- [ ] 2-3 pilot partnerships live
- [ ] Public API operational
- [ ] Uptime ≥99.5%

**Business:**
- [ ] User adoption (100+ API requests/day target)
- [ ] Revenue potential identified
- [ ] Sustainability plan

**Decision:** Continue to Phase 2 / Commercialize / Transfer to community / Exit gracefully

---

## VII. Exit Conditions

### Partner Can Exit If:

**Valid Reasons:**
- Validation fails repeatedly (>3 iterations without passing Gate 2)
- Budget constraints (can't secure remaining funding)
- Priorities shift (other opportunities more compelling)
- Timeline extends beyond 24 months (fatigue)

**Exit Protocol:**
- 30 days written notice (email)
- Final handoff call (1-2 hours)
- Transfer code to owner (already open source, so mostly documentation)
- Document lessons learned (public blog post encouraged)

**No Penalty:** Research projects sometimes don't work out. Clean exit is OK.

---

### Owner Can Exit If:

**Valid Reasons:**
- Two consecutive missed checkpoints (no monthly sync + no weekly updates for 2 months)
- Communication blackout (no response for 4+ weeks without notice)
- Methodology divergence (partner changes core TSC math without consultation)
- Gate-skipping (partner proceeds to Phase 1b without passing Gate 2)

**Exit Protocol:**
- 30 days written notice
- Final consult call (2 hours)
- Document handoff state
- Partner keeps code (open source)

**Philosophy:** If communication breaks down, collaboration can't work.

---

### Mutual Agreement to Pause/Pivot

**Scenarios:**
- Validation reveals TSC doesn't work for blockchains (pivot to methodology paper)
- Budget runs out mid-project (pause until funding secured)
- External factors (major crypto regulation change, market crash)

**Decision Process:**
- Either party can suggest pause/pivot
- Discuss in monthly sync or emergency call
- Document reasoning
- Agree on next steps (pause duration, pivot direction, or clean exit)

---

## VIII. Amendments & Evolution

**This document can be updated** by mutual agreement as the project evolves.

**Amendment Process:**
1. Either party proposes change (email or Slack)
2. Discuss in next monthly sync
3. Both parties agree (documented in sync minutes)
4. Update this document with version number

**Version History:**
- v1.0 (November 2025): Initial agreement

---

## IX. Expectations Alignment Check

**Before signing, both parties should be able to answer:**

### For Partner:
- [ ] I understand the 12-18 month timeline
- [ ] I have secured or have a plan to secure $245K-365K budget
- [ ] I can dedicate 20-40 hours/week (1 FTE or 2 × 50%)
- [ ] I'm willing to iterate if validation fails (not just rush to production)
- [ ] I understand Gate 2 (Terra validation) is critical and cannot be skipped
- [ ] I know how to reach owner for questions and emergencies
- [ ] I'm excited about measuring blockchain coherence

### For Owner:
- [ ] I can provide 2 hrs/week async + 1 hr/month sync for 12-18 months
- [ ] I will maintain TSC Core framework (v2.4.0 self-coherence)
- [ ] I won't block partner's technical decisions (parsers, infrastructure)
- [ ] I understand partner may need to exit if validation fails
- [ ] I'm committed to joint authorship on vision paper
- [ ] I'm excited to see TSC applied to blockchains

**If all checked → Both parties sign below.**

---

## X. Signatures

**TSC Core Owner:**

Name: Peter Lisovin  
Signature: ___________________  
Date: ___________________

**TSC Blockchain Partner:**

Name: Renfei Zou  
Signature: ___________________  
Date: ___________________

---

**Next Review:** Month 3 (after Parser Demo)

**Document Version:** 1.0  
**Last Updated:** November 2025