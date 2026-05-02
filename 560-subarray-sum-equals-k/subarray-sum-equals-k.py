class Solution:
    def subarraySum(self, nums, k): 
        count = 0 
        current_sum = 0 # giving empty containers to store teh value 
        sub_array = {0:1} # here here we are creating the set with 0 being seen already once 

        for num in nums: 
            current_sum += num # addding the values of numes one by one 
            # current_sum - k = the numerber that is left to get to k
            if current_sum - k in sub_array: # does it exist in the sup array
                count += sub_array[current_sum - k] # gets how ever many times it has appreared or however is it's count already is and adds to that
            sub_array[current_sum] = sub_array.get(current_sum , 0) + 1 # this is to add the var in the set, it it already ecist then just add it directly and increase index by 1 and of not then just create it 
            
        return count

nums = [1,1,1]
k = 2
solution = Solution()
print(solution.subarraySum(nums, k))