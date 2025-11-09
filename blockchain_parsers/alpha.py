"""
blockchain_parsers/alpha.py — Protocol Claims Parser

Extracts measurable protocol claims from governance docs, whitepapers, 
technical specifications for TSC α-axis articulation.

Part of TSC-blockchain Phase 0 (Partner implementation).

"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class ClaimType(Enum):
    """Types of protocol claims that can be measured."""
    PERFORMANCE = "performance"      # Block time, throughput, latency targets
    SECURITY = "security"            # Validator requirements, economic security
    ECONOMIC = "economic"            # Token supply, inflation, fee models
    GOVERNANCE = "governance"        # Voting thresholds, proposal processes


@dataclass
class ProtocolClaim:
    """
    A measurable claim about protocol behavior.
    
    Attributes:
        claim_id: Unique identifier (e.g., "eth_blocktime_target")
        claim_text: Human-readable claim text
        claim_type: Category of claim
        source: URL or document reference
        timestamp: When claim was made/extracted
        measurable: Can this be verified on-chain?
        expected_value: Expected measurement value (if applicable)
        unit: Measurement unit (e.g., "seconds", "percentage", "count")
    """
    claim_id: str
    claim_text: str
    claim_type: ClaimType
    source: str
    timestamp: datetime
    measurable: bool
    expected_value: Optional[float] = None
    unit: Optional[str] = None
    
    def __repr__(self):
        measurable_str = "✓" if self.measurable else "✗"
        return f"<Claim {self.claim_id} [{measurable_str}]: {self.claim_text[:50]}...>"


class AlphaParser:
    """
    Extracts protocol claims for TSC α-axis articulation.
    
    Usage:
        parser = AlphaParser("ethereum")
        claims = parser.extract_all_claims("2024-01-01", "2024-01-31")
        features = parser.compute_alpha_features(claims)
    
    TODO (Partner): Implement all methods marked with 'raise NotImplementedError'
    """
    
    def __init__(self, chain_id: str):
        """
        Initialize parser for a specific blockchain.
        
        Args:
            chain_id: Blockchain identifier (e.g., "ethereum", "bitcoin", "solana")
        
        TODO: Initialize data source connections
        - Governance forum API (e.g., Discourse, Commonwealth)
        - Whitepaper storage (local files or URLs)
        - Spec document repository (GitHub, etc.)
        """
        self.chain_id = chain_id
        self.canonical_properties = self._load_canonical_properties()
        
    def _load_canonical_properties(self) -> List[str]:
        """
        Load canonical property catalog for this chain.
        
        Returns:
            List of standard property IDs (e.g., ["block_time", "finality_target"])
        
        TODO: Implement
        - Create YAML/JSON file with 20-30 standard properties per chain
        - Load and validate
        - Return property list
        
        Example properties:
        - block_time_target
        - finality_epochs
        - max_block_size
        - validator_minimum_stake
        - governance_quorum
        """
        # STUB: Return empty list for now
        return []
    
    def parse_governance_proposals(
        self, 
        start_date: str, 
        end_date: str
    ) -> List[ProtocolClaim]:
        """
        Extract claims from on-chain + off-chain governance proposals.
        
        Args:
            start_date: ISO format date string (e.g., "2024-01-01")
            end_date: ISO format date string
        
        Returns:
            List of ProtocolClaim objects extracted from proposals
        
        TODO: Implement
        1. **Fetch proposals:**
           - On-chain: Query Governor contract events
           - Off-chain: Fetch from governance forum API (Discourse, Commonwealth)
        
        2. **Parse proposal text:**
           - Extract declarative statements (look for "must", "shall", "targets", "requires")
           - Identify proposed changes to protocol parameters
           - Extract numeric targets (e.g., "increase gas limit to 30M")
        
        3. **Filter for measurability:**
           - Can this claim be checked on-chain? → measurable=True
           - Is this aspirational/vague? → measurable=False
           - Example: "Block time SHALL be 12 seconds" → measurable=True
           - Example: "Network should be highly scalable" → measurable=False
        
        4. **Return structured claims**
        
        Challenge: Governance proposals are heterogeneous (tech changes + social decisions)
        Need to filter for protocol-level claims only.
        
        Data sources by chain:
        - Ethereum: Snapshot.org API, eth.limo governance forums
        - Bitcoin: Bitcoin-dev mailing list archives, BIPs (Bitcoin Improvement Proposals)
        - Solana: Solana Forum, Discord governance channels
        """
        raise NotImplementedError("Partner to implement governance proposal parsing")
    
    def parse_whitepaper(self, whitepaper_url: str) -> List[ProtocolClaim]:
        """
        Extract technical claims from whitepaper.
        
        Args:
            whitepaper_url: URL to whitepaper (PDF or markdown)
        
        Returns:
            List of ProtocolClaim objects
        
        TODO: Implement
        1. **Download document:**
           - If PDF: Use PyPDF2 or pdfplumber to extract text
           - If markdown: Fetch and parse
           - If HTML: BeautifulSoup extraction
        
        2. **Extract claims:**
           - Parse sentences with technical assertions
           - Look for declarative statements:
             * "The protocol ensures..."
             * "Block time is..."
             * "Finality is achieved within..."
           - Extract numeric values and units
        
        3. **Classify by type:**
           - Performance: Throughput, latency, block time
           - Security: Validator requirements, attack resistance
           - Economic: Supply schedule, fee models
           - Governance: Decision processes, upgrade mechanisms
        
        4. **Flag measurability:**
           - Specific numeric claims → measurable=True
           - Vague aspirations → measurable=False
        
        Challenge: Whitepapers mix marketing with technical specs.
        Need to distinguish:
        - "will be scalable" (marketing) vs. "targets 100k TPS" (measurable)
        - "highly secure" (vague) vs. "66% BFT threshold" (specific)
        
        Example claims from Bitcoin whitepaper:
        - "Proof-of-work involves scanning for a value..." (architectural, not measurable)
        - "Nodes always consider the longest chain correct" (measurable: check fork resolution)
        - "Double-spending is prevented by timestamp server" (measurable: audit attempts)
        """
        raise NotImplementedError("Partner to implement whitepaper parsing")
    
    def parse_technical_specs(self, spec_repo_url: str) -> List[ProtocolClaim]:
        """
        Extract claims from technical specification documents.
        
        Args:
            spec_repo_url: URL to specification repository (e.g., GitHub)
        
        Returns:
            List of ProtocolClaim objects
        
        TODO: Implement
        1. **Clone/fetch spec repository:**
           - Use GitPython or subprocess to clone
           - Or use GitHub API to fetch markdown files
        
        2. **Parse specification documents:**
           - Look for MUST/SHALL/REQUIRED (RFC 2119 keywords)
           - Extract numbered requirements
           - Parse parameter tables (common in specs)
        
        3. **Extract testable properties:**
           - Performance requirements
           - Protocol invariants
           - Consensus rules
        
        4. **Link to governance:**
           - Which proposals amended these specs?
           - Track versioning of claims
        
        Example specs:
        - Ethereum: EIPs (Ethereum Improvement Proposals) on GitHub
        - Bitcoin: BIPs (Bitcoin Improvement Proposals)
        - Solana: Solana docs repo
        
        Example claim from EIP-1559:
        - "BASEFEE is calculated from parent block gas used"
        - → measurable=True, can verify formula on-chain
        """
        raise NotImplementedError("Partner to implement spec parsing")
    
    def extract_all_claims(
        self, 
        window_start: str, 
        window_end: str
    ) -> Dict[str, ProtocolClaim]:
        """
        Main entry point: Extract all claims for a time window.
        
        Combines governance + whitepaper + specs.
        Deduplicates by semantic similarity.
        
        Args:
            window_start: ISO date string
            window_end: ISO date string
        
        Returns:
            Dictionary mapping claim_id → ProtocolClaim
        
        TODO: Implement
        1. Call all parse_* methods:
           - governance_proposals = self.parse_governance_proposals(...)
           - whitepaper_claims = self.parse_whitepaper(...)
           - spec_claims = self.parse_technical_specs(...)
        
        2. Combine all claims
        
        3. Deduplicate:
           - Use TF-IDF or sentence embeddings to find semantic duplicates
           - Example: "Block time is 12 seconds" vs. "Target block time: 12s" → same claim
           - Keep higher-quality source (spec > governance > whitepaper)
        
        4. Generate unique claim_ids:
           - Format: "{chain}_{property}_{version}"
           - Example: "eth_blocktime_v1559"
        
        5. Return unified dictionary
        
        Performance: Should complete in <5 minutes per chain
        """
        # TODO: Implement combination logic
        # Stub implementation:
        claims = {}
        
        # Example stub claim (DELETE when implementing):
        claims["example_claim"] = ProtocolClaim(
            claim_id="example_claim",
            claim_text="Example: Block time SHALL be 12 seconds",
            claim_type=ClaimType.PERFORMANCE,
            source="stub",
            timestamp=datetime.now(),
            measurable=True,
            expected_value=12.0,
            unit="seconds"
        )
        
        return claims
    
    def compute_alpha_features(
        self, 
        claims: Dict[str, ProtocolClaim]
    ) -> Dict[str, float]:
        """
        Convert claims into feature vector for TSC α-axis.
        
        Args:
            claims: Dictionary of extracted claims
        
        Returns:
            Feature dictionary matching TSC expectations
        
        TODO: Implement
        1. Count claims by type (performance/security/economic/governance)
        2. Compute measurability ratio (measurable claims / total claims)
        3. Extract term frequencies (for stability comparison across windows)
        4. Compute coverage (how many canonical properties have claims?)
        
        Output format:
        {
            "total_claims": int,
            "measurable_ratio": float in [0,1],
            "performance_claims": int,
            "security_claims": int,
            "economic_claims": int,
            "governance_claims": int,
            "canonical_coverage": float in [0,1],  # fraction of canonical properties covered
            "term_freq_top100": {...},  # top 100 terms and frequencies (for γ-axis)
        }
        
        These features feed into TSC W_αβ witness function (coverage checks).
        """
        # TODO: Implement feature extraction
        # Stub implementation:
        total = len(claims)
        measurable_count = sum(1 for c in claims.values() if c.measurable)
        
        return {
            "total_claims": total,
            "measurable_ratio": measurable_count / max(total, 1),
            "performance_claims": 0,
            "security_claims": 0,
            "economic_claims": 0,
            "governance_claims": 0,
            "canonical_coverage": 0.0,
        }


# ============================================================================
# Test Cases (Partner: Implement these FIRST to guide development)
# ============================================================================

def test_ethereum_governance():
    """
    Test parsing Ethereum governance proposals.
    
    Success criteria:
    - Extracts ≥1 proposal from date range
    - At least some claims are measurable
    - All claims have valid sources
    """
    parser = AlphaParser("ethereum")
    
    # Test on known governance window (e.g., EIP-1559 discussion period)
    claims = parser.parse_governance_proposals("2020-01-01", "2020-12-31")
    
    # Assertions to guide implementation:
    assert len(claims) > 0, "Should find at least one governance proposal"
    assert any(c.measurable for c in claims), "Should find some measurable claims"
    assert all(c.source.startswith("http"), "All claims should have source URL"
    
    # Print sample for manual verification
    print(f"✓ Parsed {len(claims)} claims from Ethereum governance")
    if claims:
        sample = list(claims)[:3]
        for claim in sample:
            print(f"  - {claim.claim_id}: {claim.claim_text[:60]}...")


def test_bitcoin_whitepaper():
    """
    Test parsing Bitcoin whitepaper (known document, stable claims).
    
    Success criteria:
    - Extracts ≥5 claims from whitepaper
    - Claims categorized by type
    - Measurability flagged correctly
    """
    parser = AlphaParser("bitcoin")
    
    # Bitcoin whitepaper is public domain, stable URL
    whitepaper_url = "https://bitcoin.org/bitcoin.pdf"
    claims = parser.parse_whitepaper(whitepaper_url)
    
    # Expected claims (examples):
    # - "Proof-of-work involves scanning for a value..."
    # - "Nodes always consider the longest chain to be correct..."
    # - "Double-spending is prevented by timestamp server..."
    
    assert len(claims) >= 5, "Bitcoin whitepaper should yield ≥5 claims"
    
    # Check type distribution
    types = [c.claim_type for c in claims]
    assert ClaimType.SECURITY in types, "Should find security-related claims"
    
    print(f"✓ Parsed {len(claims)} claims from Bitcoin whitepaper")
    print(f"  Type distribution: {dict((t, types.count(t)) for t in set(types))}")


def test_feature_extraction():
    """
    Test feature vector extraction from claims.
    
    Success criteria:
    - Feature dict has expected keys
    - Measurability ratio is correct
    - Values are in valid ranges [0,1] or non-negative integers
    """
    parser = AlphaParser("ethereum")
    
    # Mock claims for testing
    mock_claims = {
        "claim1": ProtocolClaim(
            claim_id="claim1",
            claim_text="Block time is 12 seconds",
            claim_type=ClaimType.PERFORMANCE,
            source="https://ethereum.org/spec",
            timestamp=datetime.now(),
            measurable=True,
            expected_value=12.0,
            unit="seconds"
        ),
        "claim2": ProtocolClaim(
            claim_id="claim2",
            claim_text="System is highly secure",
            claim_type=ClaimType.SECURITY,
            source="https://ethereum.org/whitepaper",
            timestamp=datetime.now(),
            measurable=False
        ),
        "claim3": ProtocolClaim(
            claim_id="claim3",
            claim_text="Finality within 2 epochs",
            claim_type=ClaimType.PERFORMANCE,
            source="https://ethereum.org/spec",
            timestamp=datetime.now(),
            measurable=True,
            expected_value=2.0,
            unit="epochs"
        )
    }
    
    features = parser.compute_alpha_features(mock_claims)
    
    # Validate feature dict structure
    assert "total_claims" in features, "Should include total_claims"
    assert "measurable_ratio" in features, "Should include measurability ratio"
    
    # Validate values
    assert features["total_claims"] == 3, "Should count 3 claims"
    assert features["measurable_ratio"] == 2/3, "2 of 3 claims measurable = 0.667"
    assert 0 <= features["measurable_ratio"] <= 1, "Ratio should be in [0,1]"
    
    print(f"✓ Feature extraction produces valid output")
    print(f"  Features: {features}")


def test_reproducibility():
    """
    Test that parser produces identical results across runs.
    
    Success criteria:
    - Same input → same output (deterministic)
    - 99%+ overlap in claim_ids
    """
    parser = AlphaParser("ethereum")
    
    # Run parser twice on same input
    claims1 = parser.extract_all_claims("2024-01-01", "2024-01-31")
    claims2 = parser.extract_all_claims("2024-01-01", "2024-01-31")
    
    # Check reproducibility
    ids1 = set(claims1.keys())
    ids2 = set(claims2.keys())
    
    overlap = len(ids1 & ids2) / max(len(ids1), len(ids2), 1)
    
    assert overlap >= 0.99, f"Reproducibility {overlap:.2%} < 99%"
    
    print(f"✓ Reproducibility: {overlap:.2%}")


def test_performance():
    """
    Test that parser completes within time budget.
    
    Success criteria:
    - Extract features from 1 chain in <5 minutes
    """
    import time
    
    parser = AlphaParser("ethereum")
    
    start = time.time()
    claims = parser.extract_all_claims("2024-01-01", "2024-01-31")
    features = parser.compute_alpha_features(claims)
    elapsed = time.time() - start
    
    print(f"✓ Parsed {len(claims)} claims in {elapsed:.1f}s")
    
    assert elapsed < 300, f"Parser took {elapsed:.1f}s (should be <300s)"


# ============================================================================
# Main: Run Tests
# ============================================================================

if __name__ == "__main__":
    print("TSC Blockchain - Alpha Parser Test Suite")
    print("=" * 60)
    print()
    
    print("⚠️  All tests are stubs until partner implements methods.")
    print("Uncomment tests as you implement functionality.")
    print()
    
    # Partner: Uncomment and run tests as you implement
    
    # test_ethereum_governance()
    # print()
    
    # test_bitcoin_whitepaper()
    # print()
    
    test_feature_extraction()  # This one works (uses mock data)
    print()
    
    # test_reproducibility()
    # print()
    
    # test_performance()
    # print()
    
    print("=" * 60)
    print("Next steps:")
    print("1. Implement parse_governance_proposals()")
    print("2. Implement parse_whitepaper()")
    print("3. Implement parse_technical_specs()")
    print("4. Implement extract_all_claims()")
    print("5. Uncomment and run all tests")
    print()
    print("Target: All tests passing by end of Month 2")
