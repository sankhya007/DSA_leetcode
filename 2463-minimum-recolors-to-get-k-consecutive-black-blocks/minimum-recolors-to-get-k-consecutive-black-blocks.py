class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_w = 0 
        for i in range(k): 
            if blocks[i] == "W": 
                count_w += 1

        res = count_w
        for i in range(k, len(blocks)): 
            # k = is window size
            # i - k is the 1st element
            # i is the current element
            if blocks[i - k] == "W": 
                count_w -= 1
            # we are going to skip part this character to we can forget about this character, and include the action that we would have taken if this character was the part of the window
            if blocks[i] == "W": 
                count_w += 1
            # i is 7, but 7 itself is not the part of the sliding window because the reasoning on that is not done yet, so 0..6 is what that is inside the window
            # last block being white means, we are going to leave that while block in the next step thats why we decrease the count by 1
            # and the 1st block being white means we need to change that shit real quick and make it black, and when the last and 1st are the same, nothing happens
            # this gets to stay in the window so we count the action for the character
            # if the last and the 1st both are white then there is change happenning
            res = min(res, count_w)

        return res