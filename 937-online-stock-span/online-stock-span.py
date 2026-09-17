class StockSpanner(): 
    
    def __init__(self): 
        self.stack = []

    def next(self, price): 
        span = 1 

        # stack has value and the span together (x, y)
        while self.stack and self.stack[-1][0] <= price: 

            # if the price now is equal of bigger than the 1st value of the stack, the span append with the selected value's span 
            span += self.stack.pop()[1]

        # push today as a tuple so that future days can absorb span the same way
        self.stack.append((price, span))

        return span

