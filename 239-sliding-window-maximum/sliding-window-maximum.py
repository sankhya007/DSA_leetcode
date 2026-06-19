# time limit exceeded 

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         result = []
#         for i in range(0, n-k+1): 
#             max_num = nums[i]
#             for j in range(1, k):
#                 if nums[i+j] > max_num:
#                     max_num = nums[i+j]
#             result.append(max_num)
#         return result


from collections import deque
class Solution: 
    def maxSlidingWindow(self, nums, k): 
        if not nums or k == 0: 
            return []
        result = []
        left = right = 0 
        q = deque() # initialize queue
        while right < len(nums): 
            while q and nums[q[-1]] < nums[right]: # if the value we are trying to enter is smaller then the vaue in the right, pop
                q.pop()
            q.append(right)
            if q[0] < left: # if the left in the queue is smaller then the actual value of the left, pop
                q.popleft()
            if (right + 1) >= k: # i do not undertsnd this part clearly
                result.append(nums[q[0]])
                left += 1
            right += 1
        return result