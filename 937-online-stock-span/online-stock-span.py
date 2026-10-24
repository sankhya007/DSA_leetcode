class StockSpanner(): 

    def __init__(self): 
        self.stack = []

    def next(self, price): 
        span = 1 # coz by default it is 1 for everyone

        # stack[-1] will be (100, 0)
        # [0] will extrude the 100 from that
        while self.stack and self.stack[-1][0] <= price: 

            # only if the given price is bigger the span will increase, else not
            # [1] extrudes the 2nd element which is 1 from (100, 1)
            span += self.stack.pop()[1]

        # 1st time append will happen because nothing in the stack
        # then append happens every time
        self.stack.append((price, span))

        return span