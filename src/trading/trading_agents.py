from swarm import Swarm, Agent
import json
import pandas as pd
import numpy as np
from datetime import datetime, UTC
import re

class TradingSwarm:
    def __init__(self, config):
        self.client = Swarm()
        self.config = config
        
        # Initialize specialized agents
        self.technical_agent = Agent(
            name="Technical Analysis Agent",
            instructions="""You are a technical analysis expert. Analyze market data using:
            - Moving averages (SMA, EMA)
            - Momentum indicators (RSI, MACD)
            - Volatility indicators (Bollinger Bands)
            - Volume analysis
            Provide clear trading signals based on technical patterns."""
        )
        
        self.sentiment_agent = Agent(
            name="Sentiment Analysis Agent",
            instructions="""You are a sentiment analysis expert. Analyze market sentiment using:
            - News articles
            - Social media trends
            - Market commentary
            Provide clear sentiment signals based on qualitative data."""
        )
        
        self.risk_agent = Agent(
            name="Risk Management Agent",
            instructions="""You are a risk management expert. Monitor and control:
            - Position sizes
            - Portfolio exposure
            - Stop loss levels
            - Risk/reward ratios
            Ensure all trades comply with risk parameters.
            
            Format your response as a JSON object with the following structure:
            {
                "approved": true/false,
                "risk_parameters": {
                    "position_size_check": "Valid/Invalid",
                    "portfolio_exposure_check": "Valid/Invalid", 
                    "stop_loss_level_check": "Valid/Invalid",
                    "risk_reward_ratio_check": "Valid/Invalid",
                    "compliance": "Approved/Rejected"
                },
                "reason": "explanation if rejected"
            }"""
        )
        
        self.execution_agent = Agent(
            name="Trade Execution Agent",
            instructions="""You are a trade execution expert. Handle:
            - Order placement
            - Position management
            - Trade timing
            Execute trades efficiently while minimizing slippage."""
        )

    def _calculate_rsi(self, df, period=14):
        """Calculate RSI indicator"""
        try:
            # Convert to pandas DataFrame if needed
            if isinstance(df, dict):
                df = pd.DataFrame(df)
            elif not isinstance(df, pd.DataFrame):
                return None

            # Ensure we have close prices
            if 'close' not in df.columns:
                return None

            # Need at least 3 data points to calculate meaningful RSI
            if len(df) < 3:
                return None

            # Calculate price changes
            delta = df['close'].diff()
            delta = delta.fillna(0)

            # Check if all prices are the same
            if (df['close'] == df['close'].iloc[0]).all():
                return 50.0

            # Special case: check for all increasing/decreasing prices
            if (delta[1:] > 0).all():
                return 100.0
            if (delta[1:] < 0).all():
                return 0.0

            # Adjust period if we have less data than the default period
            actual_period = min(len(df)-1, period)

            # Calculate gains and losses
            gain = delta.where(delta > 0, 0.0)
            loss = -delta.where(delta < 0, 0.0)

            # Calculate average gain and loss
            avg_gain = gain.rolling(window=actual_period).mean()
            avg_loss = loss.rolling(window=actual_period).mean()

            # Handle division by zero
            avg_loss = avg_loss.replace(0, np.finfo(float).eps)

            # Calculate RS and RSI
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))

            # Return the latest RSI value
            latest_rsi = float(rsi.iloc[-1])
            return latest_rsi if not np.isnan(latest_rsi) else 50.0

        except Exception as e:
            print(f"Error calculating RSI: {e}")
            return None

    def _fetch_news_sentiment(self, symbol):
        """Fetch and analyze news sentiment"""
        # Implement news sentiment analysis
        return 0.5  # Neutral sentiment

    def _fetch_social_sentiment(self, symbol):
        """Fetch and analyze social media sentiment"""
        # Implement social sentiment analysis
        return 0.5  # Neutral sentiment

    def _aggregate_sentiment(self):
        """Aggregate different sentiment signals"""
        # Implement sentiment aggregation
        return 0.5  # Neutral sentiment

    def _check_daily_loss_limit(self):
        """Check if within daily loss limits"""
        # Implement daily loss checking
        return True  # Placeholder

    def _parse_agent_response(self, response):
        """Parse agent response and convert to dictionary if needed"""
        if not response or not response.messages or not response.messages[0]["content"]:
            return {}
        
        content = response.messages[0]["content"]
        
        # If content is already a dict, return it directly
        if isinstance(content, dict):
            return content
            
        # If content is a string, try to parse it
        if isinstance(content, str):
            # First try parsing as JSON
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                # If JSON parsing fails, check for markdown code block
                if '```' in content:
                    json_match = re.search(r'```(?:json)?\n(.*?)\n```', content, re.DOTALL)
                    if json_match:
                        try:
                            return json.loads(json_match.group(1).strip())
                        except json.JSONDecodeError:
                            pass
                
                # Try to extract approved status and risk parameters from the text
                approved_match = re.search(r'approved:\s*(true|false)', content, re.IGNORECASE)
                if approved_match:
                    approved_value = approved_match.group(1).lower() == 'true'
                    
                    # Extract risk parameter statuses from the text
                    risk_params = {
                        "position_size_check": "Valid",
                        "portfolio_exposure_check": "Valid",
                        "stop_loss_level_check": "Valid",
                        "risk_reward_ratio_check": "Valid",
                        "compliance": "Approved"
                    }
                    
                    # Update risk parameters based on any "Invalid" or "Rejected" mentions
                    if re.search(r'position size.*?invalid|invalid.*?position size', content, re.IGNORECASE):
                        risk_params["position_size_check"] = "Invalid"
                    if re.search(r'portfolio exposure.*?invalid|invalid.*?portfolio exposure', content, re.IGNORECASE):
                        risk_params["portfolio_exposure_check"] = "Invalid"
                    if re.search(r'stop loss.*?invalid|invalid.*?stop loss', content, re.IGNORECASE):
                        risk_params["stop_loss_level_check"] = "Invalid"
                    if re.search(r'risk.?reward.*?invalid|invalid.*?risk.?reward', content, re.IGNORECASE):
                        risk_params["risk_reward_ratio_check"] = "Invalid"
                    if re.search(r'rejected|not approved|cannot be approved', content, re.IGNORECASE):
                        risk_params["compliance"] = "Rejected"
                    
                    return {
                        "approved": approved_value,
                        "risk_parameters": risk_params,
                        "message": content
                    }
                
                return {"status": "processed", "message": str(content)}
                
        return {}

    def _check_risk_approval(self, risk_data):
        """Helper method to check risk approval status from nested response"""
        if not isinstance(risk_data, dict):
            return False

        # Check in nested content structure first
        if "content" in risk_data and isinstance(risk_data["content"], dict):
            return self._check_risk_approval(risk_data["content"])

        # Check risk parameters if they exist
        if "risk_parameters" in risk_data:
            risk_params = risk_data["risk_parameters"]
            if isinstance(risk_params, dict):
                # Check if all parameters are "Valid" and compliance is "Approved"
                all_valid = all(
                    value == "Valid"
                    for key, value in risk_params.items()
                    if isinstance(value, str) and key.endswith("_check")
                )
                compliance_approved = risk_params.get("compliance") == "Approved"
                if not all_valid or not compliance_approved:
                    return False

        # Finally check direct approved field
        if "approved" in risk_data:
            return bool(risk_data["approved"])

        return False

    def analyze_trading_opportunity(self, symbol, market_data):
        """
        Analyze trading opportunity using all agents
        """
        try:
            # Handle both DataFrame and dictionary inputs
            if isinstance(market_data, pd.DataFrame):
                market_data_dict = {
                    "close": market_data["close"].tolist(),
                    "high": market_data["high"].tolist() if "high" in market_data else [],
                    "low": market_data["low"].tolist() if "low" in market_data else [],
                    "volume": market_data["volume"].tolist() if "volume" in market_data else [],
                    "timestamp": [str(ts) for ts in market_data.index.tolist()]
                }
            elif isinstance(market_data, dict):
                market_data_dict = {
                    "close": market_data["close"],
                    "high": market_data.get("high", []),
                    "low": market_data.get("low", []),
                    "volume": market_data.get("volume", []),
                    "timestamp": market_data.get("timestamp", [
                        datetime.now(UTC).isoformat()
                    ])
                }
            else:
                return {"status": "error", "reason": f"Invalid market data type: {type(market_data).__name__}"}

            # Validate market data
            if not market_data_dict["close"]:
                return {"status": "error", "reason": "No price data available"}

            # Get technical analysis
            technical_message = {
                "role": "user",
                "content": f"Analyze technical indicators for {symbol}. Market data: {json.dumps(market_data_dict)}. Return response as JSON."
            }
            technical_response = self.client.run(
                agent=self.technical_agent,
                messages=[technical_message]
            )
            technical_data = self._parse_agent_response(technical_response)

            if "error" in technical_data:
                return {"status": "error", "reason": f"Technical analysis error: {technical_data['error']}"}

            # Get sentiment analysis
            sentiment_message = {
                "role": "user",
                "content": f"Analyze market sentiment for {symbol}. Return response as JSON."
            }
            sentiment_response = self.client.run(
                agent=self.sentiment_agent,
                messages=[sentiment_message]
            )
            sentiment_data = self._parse_agent_response(sentiment_response)

            # Prepare trade parameters
            current_price = float(market_data_dict["close"][-1])
            trade_params = {
                "symbol": symbol,
                "size": 10,  # Example size
                "price": current_price,
                "timestamp": market_data_dict["timestamp"][-1],
                "technical_signal": technical_data.get("signal"),
                "sentiment_signal": sentiment_data.get("signal")
            }

            # Check risk limits with structured request
            risk_message = {
                "role": "user",
                "content": json.dumps({
                    "command": "check_risk",
                    "trade": trade_params,
                    "risk_parameters": {
                        "position_size_check": "required",
                        "portfolio_exposure_check": "required",
                        "stop_loss_level_check": "required",
                        "risk_reward_ratio_check": "required"
                    }
                })
            }
            risk_response = self.client.run(
                agent=self.risk_agent,
                messages=[risk_message]
            )
            risk_data = self._parse_agent_response(risk_response)

            # Debug print
            print(f"Risk data received: {risk_data}")

            # Check for risk approval using the helper method
            is_approved = self._check_risk_approval(risk_data)
            print(f"Risk approval status: {is_approved}")

            # If risk is not approved, return rejection with reason
            if not is_approved:
                reason = (
                    risk_data.get("reason") or
                    (risk_data.get("risk_parameters", {}).get("reason") if isinstance(risk_data.get("risk_parameters"), dict) else None) or
                    "Risk limits exceeded"
                )
                return {
                    "status": "rejected",
                    "reason": reason,
                    "price": current_price,
                    "timestamp": trade_params["timestamp"]
                }

            # Execute trade if risk is approved
            execution_message = {
                "role": "user",
                "content": json.dumps({
                    "command": "execute_trade",
                    "trade": trade_params
                })
            }
            execution_response = self.client.run(
                agent=self.execution_agent,
                messages=[execution_message]
            )
            execution_data = self._parse_agent_response(execution_response)

            # Return successful execution result
            return {
                "status": "executed",
                "price": current_price,
                "size": trade_params["size"],
                "timestamp": trade_params["timestamp"]
            }

        except Exception as e:
            return {"status": "error", "reason": str(e)}
