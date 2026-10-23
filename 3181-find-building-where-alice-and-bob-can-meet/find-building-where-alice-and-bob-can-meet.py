# find building where alice and bob can meet

class Solution(object):
    def leftmostBuildingQueries(self, heights, queries):
        n = len(heights)
        ans = [-1] * len(queries) # store -1 because that is what we need to return if no answer 
        # empty list
        pending = [[] for _ in range(n)]

        '''
        case 1: they are already together
        case 2: alice can jump straight to bob's building
        case 3: everything else, they can not meet at either starting buildings
            a. not at bob's building(bob can not move left)
            b. not at alice's building (need heights[a] < heights[b], but case is opposite)
            c. not in the middle(no body can move left)

        '''
        for qi, (a,b) in enumerate(queries): 
            # make a left person and b right person
            # left is going to be the smaller height
            if a > b: 
                a, b = b, a
            # for these cases the answer is b
            if a == b or heights[a] < heights[b]: 
                ans[qi] = b 
            else: # a != b and heights[a] >= heights[b]
                pending[b].append((heights[a], qi))
                # heights[a] is the one we have to beat 
                # qi is the index of that height

        stack = []

        # answering the hard queries whose b is this building, we already have a(a was bigger than b)
        for i in range(n-1, -1, -1): 
            for need, qi in pending[i]: 

                # two pointer solution
                lo = 0 
                hi = len(stack) - 1
                res = -1

                while lo <= hi: 
                    mid = (lo + hi) // 2
                    if heights[stack[mid]] > need: 
                        res = stack[mid]
                        lo = mid + 1
                    else: 
                        hi = mid - 1
                    # find the answers and place them in the answer array 
                    ans[qi] = res

                # check is the building is taller or not
                # it will automatically be the further left one because we are going right to left in the loop
                # if tall then replace last and append 
            while stack and heights[stack[-1]] <= heights[i]: 
                stack.pop()
            stack.append(i)

        return ans

