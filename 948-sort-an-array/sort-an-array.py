# sort an array - merge sort 

class Solution(): 
    def sortArray(self, nums): 
        if len(nums) <= 1: 
            return nums

        mid = len(nums) // 2 
        left = self.sortArray(nums[:mid])
        # sort the left and right part if the array  
        right = self.sortArray(nums[mid:])

        merged = []
        i = j = 0 

        while i < len(left) and j < len(right):
            # will keep going till both of the sides have unused elements
            # compare the two front elements
            # 1st case: the left is smaller
            # 2nd case: the right is smaller
            if left[i] <= right[j]: 
                merged.append(left[i])
                i += 1
            else: 
                merged.append(right[j])
                j += 1

        # i and j will be at the end of the smaller loop 
        # what we have to do is take the bigger portion of the parts and then keep adding the elements that are left over because the loop was ended before, because we have smaller list in one side 
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged
