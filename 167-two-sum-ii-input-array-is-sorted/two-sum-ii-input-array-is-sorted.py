class Solution:
    def twoSum(self, numbers, target): 
        left = 0 
        right = len(numbers) - 1
        while left < right: 
            current_sum = numbers[left] + numbers[right]
            if current_sum == target: 
                return [left+1, right+1]
                # we are returning the index values here and then adding one to it to get the actuak value because the values in the list starts with 1 and the index starts with 0 so thats why if we add one to it they are same as the number because the list is already sorted
            elif current_sum < target: 
                left += 1
            else: # current_sum > target
                right -= 1
        return None
numbers = [1,2,3,4,5,6,7,8,9]
target = 7
solution = Solution()
print(str(solution.twoSum(numbers, target)))