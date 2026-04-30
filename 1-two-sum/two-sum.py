class Solution:
    def twoSum(self, nums, target): 
        num_set = {} 
        # because we are storing the value and the index thats why used a set
        for i, num in enumerate(nums): #enumerate because it turns it into _:_
            complement = target - num
            if complement in num_set: 
                return [num_set[complement], i] #getting both of the index values
            num_set[num] = i #this guy is just adding the values in the numset
            #num_set[2] = 0 so we add {2:0} adn goes on tll the list ends

nums = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(nums,target))