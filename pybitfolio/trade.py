from pybitfolio.base import TradeBase


# ─── RAW CLASS ──────────────────────────────────────────────────────────────────

class TradeRaw(TradeBase):
    """Trade class based in raw input data."""
    
    def __init__(self, exchange:str, market:str, position:str, price:float, amount:float):
        """Declare class with all basic values.

        Args:
        
            exchange (str): exchange name
            market (str): markets name
            position (str): position type, 'long' or 'short'
            price (float): price value
            amount (float): amount value
        """
        self.setExchange(exchange)
        self.setMarket(market)
        self.setPosition(position)
        self.setOpenPrice(price)
        self.setAmount(amount)
        
# ────────────────────────────────────────────────────────────────────────────────
