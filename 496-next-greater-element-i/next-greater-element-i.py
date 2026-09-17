class Solution(): 
    def nextGreaterElement(self, nums1, nums2): 

        # storage
        stack = []
        # will store enumerate values
        next_greater = {}

        # loo through the main list, nums1 is the subset of nums2 
        for num in nums2:  

            # stack has value, current value bigger than stack
            while stack and num > stack[-1]: 

                # not stack[-1], because that value stays in the stack
                prev = stack.pop() 

                # next_greater element in the index position of the previous element
                next_greater[prev] = num

            # if the number is not 
            stack.append(num)

        # make all the left over values in stack, not in next_greater store as -1
        while stack: 
            next_greater[stack.pop()] = -1
            
        # loop through all of the elements in next greater and give out values stored in the next_greater
        return [next_greater[num] for num in nums1]