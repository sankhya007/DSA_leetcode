# top k frequency elements

class Solution(): 
    def topKFrequent(self, nums, k): 

        count = {}

        for num in nums: 
            count[num] = count.get(num, 0)+1
        # count and store

        sorted_nums = sorted(count, key=count.get, reverse=True)
        # key = is what metric we have to use to count
        # reverse=True (sequence)

        return sorted_nums[:k]
        # till the number we are asked to