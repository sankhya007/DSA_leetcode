class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count_gap = {0: 0}

        for r in wall: 
            total = 0 
            for i in range(len(r) - 1): 
                total += r[i]
                count_gap[total] = 1 + count_gap.get(total, 0)
                # count_gap.get(total, 0) will give us the number of gap that we have in the total'th postion in current_gap
        
        # length - intersection
        return len(wall) - max(count_gap.values())