"""
blockchain_parsers/gamma.py — Usage Patterns Parser

Extracts transaction patterns and user behavior for TSC γ-axis articulation:
transaction taxonomy, usage trends, retention metrics.

Part of TSC-blockchain Phase 0 (Partner implementation).

"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
import numpy as np


class TransactionType(Enum):
    """Standard transaction taxonomy across chains."""
    TRANSFER = "transfer"                # Simple token transfers
    DEX_SWAP = "dex_swap"               # Decentralized exchange swaps
    LENDING_SUPPLY = "lending_supply"    # Deposit to lending protocol
    LENDING_BORROW = "lending_borrow"    # Borrow from lending protocol
    NFT_MINT = "nft_mint"               # NFT minting
    NFT_TRADE = "nft_trade"             # NFT marketplace trades
    BRIDGE_DEPOSIT = "bridge_deposit"    # Cross-chain bridge deposit
    BRIDGE_WITHDRAW = "bridge_withdraw"  # Cross-chain bridge withdrawal
    STAKING = "staking"                  # Validator staking operations
    GOVERNANCE = "governance"            # Governance voting/proposals
    OTHER = "other"                      # Unclassified


@dataclass
class UsageSnapshot:
    """
    Snapshot of blockchain usage patterns for a time window.
    """
    # Transaction Taxonomy
    tx_type_distribution: Dict[TransactionType, int]  # Count per type
    total_transactions: int
    
    # User Metrics
    active_addresses_daily: List[int]  # Daily active addresses in window
    new_addresses: int  # Addresses appearing for first time
    retention_rate: float  # % of addresses active in both windows
    
    # Value Metrics
    avg_transaction_value_usd: float
    median_transaction_value_usd: float
    total_volume_usd: float
    
    # Gas/Fee Metrics
    avg_gas_price: float
    gas_price_volatility: float  # Coefficient of variation
    
    # Temporal Patterns
    hourly_activity: List[int]  # Transactions per hour (24 buckets)
    weekend_vs_weekday_ratio: float  # Weekend activity / weekday activity
    
    # Metadata
    chain_id: str
    window_start: datetime
    window_end: datetime


class GammaParser:
    """
    Extracts usage patterns for TSC γ-axis articulation.
    
    Usage:
        parser = GammaParser("ethereum", analytics_api_key="...")
        snapshot = parser.extract_usage_snapshot("2024-01-01", "2024-01-31")
        features = parser.compute_gamma_features(snapshot)
    
    TODO (Partner): Implement all methods marked with 'raise NotImplementedError'
    """
    
    def __init__(
        self, 
        chain_id: str,
        analytics_api_key: Optional[str] = None,
        rpc_url: Optional[str] = None
    ):
        """
        Initialize parser with analytics platform access.
        
        Args:
            chain_id: Blockchain identifier
            analytics_api_key: API key for Dune/Flipside/The Graph
            rpc_url: RPC endpoint (for direct transaction parsing if needed)
        
        TODO: Initialize connections
        - Analytics platform (Dune Analytics, Flipside, The Graph)
        - RPC provider (fallback for direct parsing)
        - Transaction classifier (heuristics or ML model)
        """
        self.chain_id = chain_id
        self.analytics_api_key = analytics_api_key
        self.rpc_url = rpc_url
        
    def classify_transaction(self, tx: Dict[str, Any]) -> TransactionType:
        """
        Classify a single transaction by type.
        
        Args:
            tx: Transaction dict with fields:
                - to: Recipient address
                - value: Transaction value
                - input: Call data (bytecode)
                - from: Sender address
        
        Returns:
            TransactionType enum value
        
        TODO: Implement classification heuristics
        
        **Approach 1: Method signature matching (fast, simple)**
        
        Parse first 4 bytes of tx.input (function selector):
        - 0xa9059cbb: transfer(address,uint256) → TRANSFER
        - 0x38ed1739: swapExactTokensForTokens → DEX_SWAP
        - 0x095ea7b3: approve → likely precedes DEX_SWAP or LENDING
        - 0x42842e0e: safeTransferFrom → likely NFT_TRADE
        
        Build lookup table of common function selectors → types.
        
        **Approach 2: Recipient address matching (chain-specific)**
        
        Known protocol addresses:
        - Uniswap router: 0x... → DEX_SWAP
        - Aave pool: 0x... → LENDING_SUPPLY/LENDING_BORROW
        - OpenSea: 0x... → NFT_TRADE
        - Lido: 0x... → STAKING
        
        Build registry of protocol addresses per chain.
        
        **Approach 3: Analytics platform labels (easiest)**
        
        Dune/Flipside already label transactions:
        - Query pre-classified data
        - Map their labels to TransactionType enum
        - Pro: No classification logic needed
        - Con: Depends on third party
        
        **Recommendation for Phase 0:**
        Use analytics platform labels (Approach 3)
        Fallback to method signature matching (Approach 1) if no label
        
        **Challenges:**
        - Not all transactions fit neat categories
        - Complex transactions (multi-call, batch operations)
        - New protocol types emerge constantly
        - Accept 80-90% classification coverage (not 100%)
        """
        raise NotImplementedError("Partner to implement transaction classification")
    
    def query_transaction_taxonomy(
        self,
        start_date: str,
        end_date: str
    ) -> Dict[TransactionType, int]:
        """
        Count transactions by type in time window.
        
        Args:
            start_date: ISO date string (e.g., "2024-01-01")
            end_date: ISO date string
        
        Returns:
            Dict mapping transaction type to count
        
        TODO: Implement
        
        **Option 1: Query analytics platform (RECOMMENDED)**
        
        Dune Analytics example query:
        ```sql
        SELECT 
            tx_type,
            COUNT(*) as count
        FROM ethereum.transactions
        WHERE block_time >= '2024-01-01'
          AND block_time < '2024-02-01'
        GROUP BY tx_type
        ```
        
        Flipside Crypto similar API.
        
        **Option 2: Direct RPC parsing (SLOW)**
        - Query all transactions in date range
        - Classify each transaction
        - Aggregate counts
        - This can take hours for busy chains
        
        **Performance considerations:**
        - Ethereum: ~1M transactions/day
        - Classifying 30M transactions = slow
        - Use analytics platform for Phase 0
        - Consider sampling (every 10th transaction) if needed
        
        **Output format:**
        {
            TransactionType.TRANSFER: 15000000,
            TransactionType.DEX_SWAP: 3000000,
            TransactionType.LENDING_SUPPLY: 500000,
            ...
        }
        """
        raise NotImplementedError("Partner to implement transaction taxonomy query")
    
    def query_user_retention(
        self,
        window1_start: str,
        window1_end: str,
        window2_start: str,
        window2_end: str
    ) -> float:
        """
        Compute user retention between two time windows.
        
        Args:
            window1_start: First window start date
            window1_end: First window end date
            window2_start: Second window start date
            window2_end: Second window end date
        
        Returns:
            Retention rate (float in [0, 1])
            = (addresses active in both windows) / (addresses active in window 1)
        
        TODO: Implement
        
        **Query logic:**
        ```sql
        WITH window1_users AS (
            SELECT DISTINCT from_address
            FROM transactions
            WHERE block_time >= '{window1_start}'
              AND block_time < '{window1_end}'
        ),
        window2_users AS (
            SELECT DISTINCT from_address
            FROM transactions
            WHERE block_time >= '{window2_start}'
              AND block_time < '{window2_end}'
        ),
        retained AS (
            SELECT COUNT(*) as count
            FROM window1_users
            INNER JOIN window2_users
            ON window1_users.from_address = window2_users.from_address
        )
        SELECT 
            retained.count::float / COUNT(window1_users.from_address)::float
        FROM window1_users, retained
        ```
        
        **Interpretation:**
        - High retention (>0.7): Sticky users, healthy ecosystem
        - Low retention (<0.3): High churn, speculative activity
        - Compare to α claims: If whitepaper says "daily use", retention should be high
        
        **Performance:**
        - Requires SET operations on millions of addresses
        - Use analytics platform's pre-indexed data
        - Or sample (e.g., track cohort of 10k random addresses)
        """
        raise NotImplementedError("Partner to implement retention query")
    
    def query_temporal_patterns(
        self,
        start_date: str,
        end_date: str
    ) -> Tuple[List[int], float]:
        """
        Analyze temporal activity patterns.
        
        Args:
            start_date: ISO date string
            end_date: ISO date string
        
        Returns:
            Tuple of (hourly_activity, weekend_ratio)
            - hourly_activity: List of 24 ints (tx count per hour of day, averaged)
            - weekend_ratio: Weekend activity / weekday activity
        
        TODO: Implement
        
        **Hourly activity:**
        ```sql
        SELECT 
            EXTRACT(HOUR FROM block_time) as hour,
            COUNT(*) / COUNT(DISTINCT DATE(block_time)) as avg_tx_per_hour
        FROM transactions
        WHERE block_time >= '{start_date}'
          AND block_time < '{end_date}'
        GROUP BY EXTRACT(HOUR FROM block_time)
        ORDER BY hour
        ```
        
        Result: [tx_count_0am, tx_count_1am, ..., tx_count_11pm]
        
        **Weekend ratio:**
        ```sql
        WITH weekend_activity AS (
            SELECT COUNT(*) as count
            FROM transactions
            WHERE block_time >= '{start_date}'
              AND block_time < '{end_date}'
              AND EXTRACT(DOW FROM block_time) IN (0, 6)  -- Sunday=0, Saturday=6
        ),
        weekday_activity AS (
            SELECT COUNT(*) as count
            FROM transactions
            WHERE block_time >= '{start_date}'
              AND block_time < '{end_date}'
              AND EXTRACT(DOW FROM block_time) BETWEEN 1 AND 5
        )
        SELECT 
            weekend_activity.count::float / weekday_activity.count::float
        FROM weekend_activity, weekday_activity
        ```
        
        **Interpretation:**
        - Weekend ratio ~1.0: Activity constant (likely bots/protocols)
        - Weekend ratio <0.5: Retail users dominate (lower weekend activity)
        - Weekend ratio >1.5: Speculation or gaming (higher weekend activity)
        
        - Hourly peaks at specific times: Geographic concentration or bot activity
        - Flat hourly distribution: Global, 24/7 activity
        """
        raise NotImplementedError("Partner to implement temporal pattern query")
    
    def extract_usage_snapshot(
        self,
        window_start: str,
        window_end: str
    ) -> UsageSnapshot:
        """
        Main entry point: Extract all γ-axis metrics for time window.
        
        Args:
            window_start: ISO date string
            window_end: ISO date string
        
        Returns:
            UsageSnapshot object with all measurements
        
        TODO: Implement
        1. Query transaction taxonomy
        2. Query user retention (compare to previous window)
        3. Query temporal patterns
        4. Query value metrics (avg/median transaction value)
        5. Query gas metrics (avg price, volatility)
        6. Aggregate into UsageSnapshot
        
        **Window selection:**
        - 7-day window: Good for detecting short-term changes
        - 30-day window: Smoother, better for trends
        - Phase 0: Use 30-day windows
        
        **Previous window for retention:**
        If window is Jan 1-31, previous window is Dec 1-31
        Compute retention = (users in both) / (users in Dec)
        
        Performance target: <15 minutes per chain
        """
        # TODO: Implement
        # Stub implementation:
        return UsageSnapshot(
            tx_type_distribution={TransactionType.OTHER: 0},
            total_transactions=0,
            active_addresses_daily=[],
            new_addresses=0,
            retention_rate=0.0,
            avg_transaction_value_usd=0.0,
            median_transaction_value_usd=0.0,
            total_volume_usd=0.0,
            avg_gas_price=0.0,
            gas_price_volatility=0.0,
            hourly_activity=[0] * 24,
            weekend_vs_weekday_ratio=1.0,
            chain_id=self.chain_id,
            window_start=datetime.fromisoformat(window_start),
            window_end=datetime.fromisoformat(window_end)
        )
    
    def compute_gamma_features(
        self,
        snapshot: UsageSnapshot
    ) -> Dict[str, Any]:
        """
        Convert usage snapshot into feature vector for TSC γ-axis.
        
        Args:
            snapshot: UsageSnapshot object
        
        Returns:
            Feature dict matching TSC expectations
        
        TODO: Implement
        1. **Transaction type entropy:**
           - Measure diversity of transaction types
           - High entropy = diverse usage (healthy)
           - Low entropy = dominated by one type (risky)
           - Formula: H = -sum(p_i * log(p_i)) where p_i = fraction of type i
        
        2. **User engagement score:**
           - Combine retention rate + daily active addresses trend
           - Growing DAA + high retention = engaged users
           - Declining DAA + low retention = exodus
        
        3. **Temporal stability:**
           - Measure consistency of activity patterns
           - Stable hourly distribution = predictable usage
           - Erratic patterns = speculation or manipulation
           - Use coefficient of variation on hourly_activity
        
        4. **Value distribution:**
           - Compare avg vs median transaction value
           - Large gap = whale-dominated (few large txs)
           - Small gap = retail-dominated (many small txs)
        
        Output format:
        {
            "tx_entropy": float,  # Shannon entropy of tx type distribution
            "retention_rate": float in [0,1],
            "user_growth_rate": float,  # % change in daily active addresses
            "temporal_stability": float in [0,1],  # 1 = very stable
            "value_concentration": float in [0,1],  # 0 = evenly distributed
            "weekend_ratio": float,
            "dominant_tx_type": str,  # Which type has highest count
            # Raw counts for reference
            "total_tx": int,
            "active_addresses": int,
        }
        
        These features feed into TSC W_γα witness function (edit distance).
        """
        # TODO: Implement feature extraction
        # Stub implementation:
        total_tx = snapshot.total_transactions
        
        return {
            "tx_entropy": 0.0,
            "retention_rate": snapshot.retention_rate,
            "user_growth_rate": 0.0,
            "temporal_stability": 0.0,
            "value_concentration": 0.0,
            "weekend_ratio": snapshot.weekend_vs_weekday_ratio,
            "dominant_tx_type": "unknown",
            "total_tx": total_tx,
            "active_addresses": 0,
        }


# ============================================================================
# Test Cases
# ============================================================================

def test_transaction_classification():
    """
    Test classifying individual transactions.
    
    Success criteria:
    - Common function selectors classified correctly
    - Unknown selectors → TransactionType.OTHER
    - Classification completes quickly (<1ms per tx)
    """
    parser = GammaParser("ethereum")
    
    # Mock transaction: Uniswap swap
    mock_tx_swap = {
        "to": "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D",  # Uniswap V2 Router
        "value": "0",
        "input": "0x38ed1739...",  # swapExactTokensForTokens signature
        "from": "0xuser123..."
    }
    
    # Mock transaction: Simple transfer
    mock_tx_transfer = {
        "to": "0xrecipient...",
        "value": "1000000000000000000",  # 1 ETH
        "input": "0x",  # Empty input = simple transfer
        "from": "0xuser456..."
    }
    
    # Classification
    type_swap = parser.classify_transaction(mock_tx_swap)
    type_transfer = parser.classify_transaction(mock_tx_transfer)
    
    print(f"✓ Transaction classification:")
    print(f"  Swap: {type_swap}")
    print(f"  Transfer: {type_transfer}")
    
    # Assertions
    # assert type_swap == TransactionType.DEX_SWAP
    # assert type_transfer == TransactionType.TRANSFER


def test_taxonomy_query():
    """
    Test querying transaction taxonomy over date range.
    
    Success criteria:
    - Returns counts for multiple transaction types
    - Total transactions matches expected order of magnitude
    - Completes in reasonable time (<5 min)
    """
    parser = GammaParser("ethereum", analytics_api_key="...")
    
    # Query January 2024
    taxonomy = parser.query_transaction_taxonomy("2024-01-01", "2024-01-31")
    
    total = sum(taxonomy.values())
    
    print(f"✓ Transaction taxonomy (Jan 2024):")
    for tx_type, count in sorted(taxonomy.items(), key=lambda x: -x[1]):
        pct = 100 * count / max(total, 1)
        print(f"  {tx_type.value:20s}: {count:10,d} ({pct:5.1f}%)")
    
    # Sanity check: Ethereum does ~30M tx/month
    # assert 20_000_000 < total < 40_000_000


def test_user_retention():
    """
    Test computing retention between two months.
    
    Success criteria:
    - Returns retention rate in [0, 1]
    - Reasonable value (e.g., 0.3-0.7 for most chains)
    - Completes in reasonable time (<5 min)
    """
    parser = GammaParser("ethereum", analytics_api_key="...")
    
    # Retention from Dec 2023 → Jan 2024
    retention = parser.query_user_retention(
        window1_start="2023-12-01",
        window1_end="2023-12-31",
        window2_start="2024-01-01",
        window2_end="2024-01-31"
    )
    
    print(f"✓ User retention (Dec→Jan): {retention:.1%}")
    
    assert 0 <= retention <= 1, "Retention must be in [0,1]"


def test_temporal_patterns():
    """
    Test analyzing temporal activity patterns.
    
    Success criteria:
    - Returns 24-element hourly activity list
    - Weekend ratio is reasonable (e.g., 0.5-1.5)
    - Patterns make sense (not all zeros)
    """
    parser = GammaParser("ethereum", analytics_api_key="...")
    
    hourly, weekend_ratio = parser.query_temporal_patterns("2024-01-01", "2024-01-31")
    
    print(f"✓ Temporal patterns (Jan 2024):")
    print(f"  Weekend ratio: {weekend_ratio:.2f}")
    print(f"  Peak hour: {np.argmax(hourly):02d}:00 UTC")
    print(f"  Lowest hour: {np.argmin(hourly):02d}:00 UTC")
    
    # Plot hourly distribution (simple ASCII)
    max_count = max(hourly)
    print(f"  Hourly distribution:")
    for hour, count in enumerate(hourly):
        bar = "█" * int(20 * count / max(max_count, 1))
        print(f"    {hour:02d}:00 {bar} {count:,}")


def test_feature_extraction():
    """
    Test converting snapshot to feature vector.
    
    Success criteria:
    - All required features present
    - Values in valid ranges
    - Entropy calculation correct
    """
    parser = GammaParser("ethereum")
    
    # Mock snapshot
    mock_snapshot = UsageSnapshot(
        tx_type_distribution={
            TransactionType.TRANSFER: 10000,
            TransactionType.DEX_SWAP: 3000,
            TransactionType.LENDING_SUPPLY: 500,
            TransactionType.OTHER: 1500,
        },
        total_transactions=15000,
        active_addresses_daily=[100000] * 30,
        new_addresses=5000,
        retention_rate=0.65,
        avg_transaction_value_usd=1000.0,
        median_transaction_value_usd=50.0,
        total_volume_usd=15_000_000.0,
        avg_gas_price=30.0,
        gas_price_volatility=0.3,
        hourly_activity=[625] * 24,  # Uniform distribution
        weekend_vs_weekday_ratio=0.9,
        chain_id="ethereum",
        window_start=datetime(2024, 1, 1),
        window_end=datetime(2024, 1, 31)
    )
    
    features = parser.compute_gamma_features(mock_snapshot)
    
    print(f"✓ Feature extraction:")
    for key, value in features.items():
        print(f"  {key}: {value}")
    
    # Validate
    assert "tx_entropy" in features
    assert "retention_rate" in features
    assert features["retention_rate"] == 0.65


# ============================================================================
# Main: Run Tests
# ============================================================================

if __name__ == "__main__":
    print("TSC Blockchain - Gamma Parser Test Suite")
    print("=" * 60)
    print()
    
    print("⚠️  Most tests require analytics platform API access.")
    print("Configure API key before running tests.")
    print()
    
    # Partner: Uncomment and run tests as you implement
    
    # test_transaction_classification()
    # print()
    
    # test_taxonomy_query()
    # print()
    
    # test_user_retention()
    # print()
    
    # test_temporal_patterns()
    # print()
    
    test_feature_extraction()  # Works with mock data
    print()
    
    print("=" * 60)
    print("Next steps:")
    print("1. Get analytics platform API access (Dune/Flipside)")
    print("2. Implement classify_transaction()")
    print("3. Implement query_transaction_taxonomy()")
    print("4. Implement query_user_retention()")
    print("5. Implement query_temporal_patterns()")
    print("6. Uncomment and run all tests")
    print()
    print("Target: All tests passing by end of Month 3")
