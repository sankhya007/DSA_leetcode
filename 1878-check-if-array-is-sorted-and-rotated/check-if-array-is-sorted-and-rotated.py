class Solution:
    def check(self, nums: list[int]) -> bool:
        sortedNums = sorted(nums)
        arr = []

        for i in range(len(nums)): 
            # pop last element form sortedNum 
            # append that to start or sorted num
            # check if match with given nums
            arr.insert(0, sortedNums.pop())
            if nums == arr + sortedNums: 
                return True

        return False   