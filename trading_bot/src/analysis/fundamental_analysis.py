import pandas as pd

class FundamentalAnalysis:
    def __init__(self, financial_data):
        self.financial_data = financial_data

    def calculate_pe_ratio(self):
        """
        Calculate the Price-to-Earnings (P/E) ratio.

        :return: P/E ratio
        """
        price = self.financial_data['price']
        earnings_per_share = self.financial_data['earnings_per_share']
        pe_ratio = price / earnings_per_share
        return pe_ratio

    def calculate_pb_ratio(self):
        """
        Calculate the Price-to-Book (P/B) ratio.

        :return: P/B ratio
        """
        price = self.financial_data['price']
        book_value_per_share = self.financial_data['book_value_per_share']
        pb_ratio = price / book_value_per_share
        return pb_ratio

    def calculate_debt_to_equity_ratio(self):
        """
        Calculate the Debt-to-Equity (D/E) ratio.

        :return: D/E ratio
        """
        total_debt = self.financial_data['total_debt']
        total_equity = self.financial_data['total_equity']
        debt_to_equity_ratio = total_debt / total_equity
        return debt_to_equity_ratio

    def calculate_return_on_equity(self):
        """
        Calculate the Return on Equity (ROE).

        :return: ROE
        """
        net_income = self.financial_data['net_income']
        total_equity = self.financial_data['total_equity']
        roe = net_income / total_equity
        return roe

    def calculate_current_ratio(self):
        """
        Calculate the Current Ratio.

        :return: Current Ratio
        """
        current_assets = self.financial_data['current_assets']
        current_liabilities = self.financial_data['current_liabilities']
        current_ratio = current_assets / current_liabilities
        return current_ratio

    def calculate_quick_ratio(self):
        """
        Calculate the Quick Ratio.

        :return: Quick Ratio
        """
        current_assets = self.financial_data['current_assets']
        inventory = self.financial_data['inventory']
        current_liabilities = self.financial_data['current_liabilities']
        quick_ratio = (current_assets - inventory) / current_liabilities
        return quick_ratio

    def calculate_gross_margin(self):
        """
        Calculate the Gross Margin.

        :return: Gross Margin
        """
        revenue = self.financial_data['revenue']
        cost_of_goods_sold = self.financial_data['cost_of_goods_sold']
        gross_margin = (revenue - cost_of_goods_sold) / revenue
        return gross_margin

    def calculate_operating_margin(self):
        """
        Calculate the Operating Margin.

        :return: Operating Margin
        """
        operating_income = self.financial_data['operating_income']
        revenue = self.financial_data['revenue']
        operating_margin = operating_income / revenue
        return operating_margin

    def calculate_net_profit_margin(self):
        """
        Calculate the Net Profit Margin.

        :return: Net Profit Margin
        """
        net_income = self.financial_data['net_income']
        revenue = self.financial_data['revenue']
        net_profit_margin = net_income / revenue
        return net_profit_margin

    def calculate_earnings_per_share(self):
        """
        Calculate the Earnings Per Share (EPS).

        :return: EPS
        """
        net_income = self.financial_data['net_income']
        shares_outstanding = self.financial_data['shares_outstanding']
        eps = net_income / shares_outstanding
        return eps
