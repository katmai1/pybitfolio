import unittest
from pyfolio.trade import TradeRaw


# ─── TRADERAW BASIC TEST ────────────────────────────────────────────────────────

class TestBasicTradeRaw(unittest.TestCase):
    """Basic tests for TradeRaw class"""
    
    def setUp(self):
        self.t = TradeRaw("Binance ", "Btc/USDT ", "Long ", 0.12345678, 5)
    
    def test_all_values_are_ok(self):
        """Check if spaces was stripped and low chars."""
        self.assertEqual(self.t.exchange, 'binance')
        self.assertEqual(self.t.market, "btc/usdt")
        self.assertEqual(self.t.position, "long")
        self.assertAlmostEqual(self.t.open_price, 0.12345678)
        self.assertAlmostEqual(self.t.amount, 5.0)
    
    def test_position_type_valid(self):
        """Check if position type is valid (long or short)."""
        with self.assertRaises(ValueError):
            self.t.setPosition("longg")
    
    def test_unvalid_price(self):
        """Check if price value is convertible to float."""
        with self.assertRaises(ValueError):
            self.t.setOpenPrice("no_convertible")
    
    def test_unvalid_amount(self):
        """Check if amount value is convertible to float."""
        with self.assertRaises(ValueError):
            self.t.setAmount("no_convertible")

# ────────────────────────────────────────────────────────────────────────────────

# ─── LONG TRADE ─────────────────────────────────────────────────────────────────

class TestLongTradeRaw(unittest.TestCase):
    """Test a long trade"""
    
    def setUp(self):
        self.t = TradeRaw("binance", "btc/usdt", "long", 8983.49, 0.002265)
        self.t.setClosePrice(9152.45)
    
    def test_tabulate(self):
        self.t.printTable()
    
    def test_profit_loss(self):
        self.assertAlmostEqual(self.t.profit_loss_100, 1.88078, 4)
        self.assertAlmostEqual(self.t.profit_loss, 0.382694, 6)

# ────────────────────────────────────────────────────────────────────────────────

# ─── SHORT TRADE ────────────────────────────────────────────────────────────────

class TestShortTradeRaw(unittest.TestCase):
    """Test a long trade"""
    
    def setUp(self):
        self.t = TradeRaw("binance", "btc/usdt", "short", 9152.45, 0.002265)
        self.t.setClosePrice(8983.49)
    
    def test_tabulate(self):
        self.t.printTable()
    
    def test_profit_loss(self):
        self.assertAlmostEqual(self.t.profit_loss_100, 1.88078, 4)
        self.assertAlmostEqual(self.t.profit_loss, 0.382694, 6)
# ────────────────────────────────────────────────────────────────────────────────


# ─── MAIN ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    unittest.main()