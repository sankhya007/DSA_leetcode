class Solution(): 
    def nextGreaterElement(self, nums1, nums2): 

        stack = []
        next_greater = {}

        for num in nums2: 
            # step 2: compare value
            while stack and num > stack[-1]: 
                # step 3: if bigger pop and add in next_greater set
                prev = stack.pop()
                next_greater[prev] = num
            # step: append value in stack
            stack.append(num)

        # step 4: every value becomes -1 and gets added in next greater
        while stack:
            next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]