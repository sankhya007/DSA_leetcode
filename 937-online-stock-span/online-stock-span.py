class StockSpanner(): 

    def __init__(self): 
        self.stack = []

    def next(self, price): 
        span = 1 # coz by default it is 1 for everyone
        while self.stack and self.stack[-1][0] <= price: 
            span += self.stack.pop()[1]

        self.stack.append((price, span))

        return span