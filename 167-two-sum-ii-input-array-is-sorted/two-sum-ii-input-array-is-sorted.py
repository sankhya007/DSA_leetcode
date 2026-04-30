class Solution:
    def twoSum(self, numbers, target): 
        left = 0 
        right = len(numbers) - 1
        while left < right: 
            current_sum = numbers[left] + numbers[right]
            if current_sum == target: 
                return [left+1, right+1]
            elif current_sum < target: 
                left += 1
            else: # current_sum > target
                right -= 1
        return None
numbers = [1,2,3,4,5,6,7,8,9]
target = 7
solution = Solution()
print(str(solution.twoSum(numbers, target)))