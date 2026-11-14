class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        stack = []
        next_greater = {} # hash map for values

        # because nums2 will have the values nums1 already has noting more, in simpler words nums1 is a sub set
        for num in nums2: 

            while stack and num > stack[-1]: 
                prev = stack.pop()
                next_greater[prev] = num

            stack.append(num)

        while stack: 
            next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]