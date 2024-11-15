# Portfolio Management

This tutorial will guide you through setting up effective portfolio management strategies in Quantum Trader. You'll learn how to implement diversification rules, manage sector exposure, and configure position sizing for optimal risk management.

## Prerequisites
- Completed Sentiment Analysis Setup tutorial
- Understanding of basic risk management concepts
- Familiarity with YAML configuration

## 1. Setting Up Portfolio Diversification Rules

Portfolio diversification helps minimize risk by spreading investments across different assets. Let's configure diversification rules:

1. Open your configuration file (`config/config.yaml`)
2. Add the following portfolio management configuration:

```yaml
risk_management:
  position_limits:
    max_position_size: 100
    max_portfolio_exposure: 0.25
  diversification:
    min_positions: 5
    max_positions: 20
    correlation_threshold: 0.7
```

Key parameters:
- `min_positions`: Minimum number of positions to maintain
- `max_positions`: Maximum number of positions allowed
- `correlation_threshold`: Maximum allowed correlation between positions

### Implementation Steps
1. Set appropriate position limits based on your account size
2. Define minimum and maximum number of positions
3. Configure correlation thresholds to ensure true diversification

## 2. Configuring Sector Exposure Limits

Managing sector exposure prevents overconcentration in any single market sector:

```yaml
risk_management:
  sector_limits:
    max_sector_exposure: 0.30  # 30% maximum per sector
    preferred_sectors:
      technology: 0.25
      healthcare: 0.20
      finance: 0.20
      consumer: 0.15
      other: 0.20
```

Key concepts:
- Set maximum exposure per sector
- Define preferred sector allocations
- Monitor sector concentrations

### Sector Monitoring Setup
1. Configure sector classifications
2. Set exposure limits
3. Implement monitoring rules:

```python
from src.trading.trading_agents import TradingSwarm

# Initialize trading swarm
config = load_config()
trading_swarm = TradingSwarm(config)

# Check sector exposure
result = trading_swarm.check_risk_limits({
    'symbol': 'AAPL',
    'sector': 'technology',
    'position_size': 100
})
```

## 3. Implementing Position Sizing Strategies

Position sizing is crucial for risk management. Configure your position sizing rules:

```yaml
risk_management:
  position_sizing:
    max_position_size: 100
    size_by_volatility: true
    risk_per_trade: 0.02  # 2% risk per trade
    position_scaling:
      min_confidence: 0.65
      scale_factor: 1.5
```

Key components:
- Base position size calculation
- Volatility-based adjustments
- Confidence-based scaling
- Risk-based limits

### Position Sizing Implementation

1. Set up base position size rules:
```python
def calculate_position_size(price, account_size, risk_per_trade):
    """
    Calculate appropriate position size
    
    Args:
        price (float): Current asset price
        account_size (float): Total account value
        risk_per_trade (float): Maximum risk per trade (decimal)
    
    Returns:
        int: Recommended position size
    """
    max_risk_amount = account_size * risk_per_trade
    position_size = max_risk_amount / price
    return int(position_size)
```

2. Implement volatility adjustments:
- Higher volatility → smaller position size
- Lower volatility → larger position size
- Always respect maximum limits

3. Configure confidence-based scaling:
- Higher confidence signals → larger positions
- Lower confidence signals → smaller positions
- Maintain risk parameters

## Best Practices

1. Regular Portfolio Review
- Monitor diversification metrics
- Check sector exposures
- Review position sizes
- Analyze correlations

2. Risk Management
- Track daily loss limits
- Monitor drawdown levels
- Maintain stop losses
- Review risk metrics

3. Performance Monitoring
- Track position performance
- Monitor sector performance
- Analyze risk-adjusted returns
- Review trading decisions

## Troubleshooting Common Issues

1. Position Size Issues
- Check account size calculations
- Verify risk parameters
- Review position limits
- Check order execution

2. Sector Exposure Problems
- Verify sector classifications
- Check exposure calculations
- Monitor sector limits
- Review portfolio balance

3. Diversification Concerns
- Check correlation calculations
- Review position counts
- Verify asset classifications
- Monitor risk metrics

## Next Steps

After implementing these portfolio management strategies:

1. Monitor your portfolio metrics daily
2. Review and adjust limits as needed
3. Track performance against benchmarks
4. Fine-tune parameters based on results

Remember: Effective portfolio management is an ongoing process. Regularly review and adjust your settings based on market conditions and performance results.
