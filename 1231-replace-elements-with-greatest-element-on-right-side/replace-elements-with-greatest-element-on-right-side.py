class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        # n = len(arr)
        # ans = [0] * n 

        # for i in range(n):
        #     rightMax = -1
        #     for j in range(i+1, n): 
        #         rightMax = max(rightMax, arr[j])
        #     ans[i] = rightMax

        # return ans
        
        n = len(arr)
        ans = [0] * n 
        rightMax = -1 # this is the most negative value possible because everything else is actually positive in the arr, and also we need to return -1 for the last element

        for i in range(n - 1, -1, -1): 
            # we are going in the opposite direction and we need to place a -1 in the right end of the given array so that is why we input the -1 at the 1st and then we start comparing with the rest of the array
            ans[i] = rightMax 
            rightMax = max(rightMax, arr[i])
        
        return ans