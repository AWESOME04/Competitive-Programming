from collections import defaultdict
from sortedcontainers import SortedDict

class StockTracker:
    def __init__(self, k):
        self.size = k
        self.volume_map = defaultdict(int)
        self.top_k = SortedDict()
        
    def add_stocks(self, name, qty):
        self.volume_map[name] += qty
        current_volume = self.volume_map[name]
        
        if name in self.top_k:
            del self.top_k[name]
            
        self.top_k[name] = current_volume
        
        if len(self.top_k) > self.size:
            lowest_stock = next(iter(self.top_k))
            del self.top_k[lowest_stock]
        
    def top_k_stocks(self, k):
        return list(self.top_k_stocks.items())[-k:]
        
