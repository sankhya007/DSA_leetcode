class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix = [0]
        # so here we are calculating the prefix sum, of the given list
        for x in nums: 
            self.prefix.append(self.prefix[-1] + x)

    def sumRange(self, left: int, right: int) -> int:
        # negate left element form next right element 
        return self.prefix[right + 1] - self.prefix[left]        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)