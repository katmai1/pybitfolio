from tabulate import tabulate


# ─── BASE CLASS FOR TRADES ──────────────────────────────────────────────────────

class TradeBase:
    """ClassBase for all trade classes."""
    
    position_types = ['long', 'short']
    exchange = None
    market = None
    position = None
    open_price = None
    close_price = None
    amount = None

    def setExchange(self, exchange):
        """Define exchange name.

        Args:
        
            exhange (str): exchange name
        """
        self.exchange = str(exchange).strip().lower()
    
    def setMarket(self, market):
        """Define market name.

        Args:
        
            market (str): market name
        """
        self.market = str(market).strip().lower()
    
    def setPosition(self, position):
        """Define position type.

        Args:
        
            position (str): This value should be 'long' or 'short'
        """
        if str(position).strip().lower() in self.position_types:
            self.position = str(position).strip().lower()
        else:
            raise ValueError("Only accepts 'long' or 'short' as parameter.")
    
    def setOpenPrice(self, price):
        """Define price value

        Args:
        
            price (float): price value
        """
        try:
            self.open_price = float(price)
        except Exception:
            raise
    
    def setClosePrice(self, price):
        """Define close price value

        Args:
        
            price (float): close price value
        """
        try:
            self.close_price = float(price)
        except Exception:
            raise
    
    def setAmount(self, amount):
        """Define amount value

        Args:
        
            amount (float): amount value
        """
        try:
            self.amount = float(amount)
        except Exception:
            raise

    def exportData(self):
        """Returns 2 lists. First is header names and second are the values"""
        header = ['Exchange', 'Market', 'Pos.Type', 'OpenPrice', 'Amount', 'Profit/Loss %', 'Profit/Loss']
        values = [
            self.exchange.title(), self.market.upper(), self.position.title(),
            self.open_price_str, self.amount_str,
            self.profit_loss_100, self.profit_loss
        ]
        return header, values
        
    def printTable(self, table_format="grid"):
        """Print table with trade data."""
        header, values = self.exportData()
        print(tabulate([values], headers=header, tablefmt=table_format))

    
    # ─── PROPIEDADES ────────────────────────────────────────────────────────────────

    @property
    def open_price_str(self):
        """Return price in string format"""
        return "%.8f" % self.open_price
    
    @property
    def close_price_str(self):
        """Return price in string format"""
        return "%.8f" % self.close_price
    
    @property
    def amount_str(self):
        """Return amount in string format"""
        return "%.8f" % self.amount
    
    @property
    def profit_loss(self):
        if self.close_price is not None:
            close_total = self.close_price * self.amount
            open_total = self.open_price * self.amount
            if self.position == "long":
                return close_total - open_total
            if self.position == "short":
                return open_total - close_total
        return None
    
    @property
    def profit_loss_100(self):
        if self.close_price is not None:
            if self.position == "long":
                return ((self.close_price - self.open_price) / self.open_price) * 100
            if self.position == "short":
                return ((self.open_price - self.close_price) / self.close_price) * 100
        return None

# ────────────────────────────────────────────────────────────────────────────────