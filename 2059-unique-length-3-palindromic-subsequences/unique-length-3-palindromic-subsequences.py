class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # res = set()

        # for i in range(len(s) - 2): # -2 because i + 2
        #     for j in range(i + 1, len(s) - 1): # because i + j + 1
        #         for k in range(j + 1, len(s)): # because i + j + k
        #         # the middle one can be anything, no one cares
        #         # if the 1st and last element are not same, skip to next
        #             if s[i] != s[k]: 
        #                 continue
        #             # if the 1st and last match, add
        #             res.add(s[i] + s[j] + s[k])

        # return len(res)

        # res = set()

        # def rec(i, cur):
        #     if len(cur) == 3: 
        #         if cur[0] == cur[2]: 
        #             res.add(cur)
        #         return # this is why we stop at 3
        #     # when we reach the same length stop
        #     if i == len(s): 
        #         return # stop at length because there is nothing more for us to add
        #     rec(i + 1, cur)
        #     rec(i + 1, cur + s[i])

        # rec(0, "")
        # return len(res)

        '''
        lets trace that with, aba
        rec(0, "")
        ├─ skip a: rec(1, "")
        │   ├─ skip b: rec(2, "")
        │   │   ├─ skip a: rec(3, "")    -> i == 3, stop
        │   │   └─ take a: rec(3, "a")   -> i == 3, stop
        │   └─ take b: rec(2, "b")
        │       ├─ skip a: rec(3, "b")   -> stop
        │       └─ take a: rec(3, "ba")  -> stop
        └─ take a: rec(1, "a")
            ├─ skip b: rec(2, "a")
            │   ├─ skip a: rec(3, "a")   -> stop
            │   └─ take a: rec(3, "aa")  -> stop
            └─ take b: rec(2, "ab")
                ├─ skip a: rec(3, "ab")  -> stop
                └─ take a: rec(3, "aba") -> len is 3, first == last, add "aba"

        now lwts trace with 
        s = "aabca"
        rec(0, "")
        ├─ skip: rec(1, "")
        │  ├─ skip: rec(2, "")
        │  │  ├─ skip: rec(3, "")
        │  │  │  ├─ skip: rec(4, "")
        │  │  │  │  ├─ skip: rec(5, "")      -> i == 5, stop
        │  │  │  │  └─ take: rec(5, "a")     -> i == 5, stop
        │  │  │  └─ take c: rec(4, "c")
        │  │  │     ├─ skip: rec(5, "c")     -> i == 5, stop
        │  │  │     └─ take: rec(5, "ca")    -> i == 5, stop
        │  │  └─ take b: rec(3, "b")
        │  │     ├─ skip: rec(4, "b")
        │  │     │  ├─ skip: rec(5, "b")     -> i == 5, stop
        │  │     │  └─ take: rec(5, "ba")    -> i == 5, stop
        │  │     └─ take c: rec(4, "bc")
        │  │        ├─ skip: rec(5, "bc")    -> i == 5, stop
        │  │        └─ take: rec(5, "bca")   -> len 3, b != a, not added
        │  └─ take a(1): rec(2, "a")
        │     ├─ skip b: rec(3, "a")
        │     │  ├─ skip c: rec(4, "a")
        │     │  │  ├─ skip: rec(5, "a")     -> i == 5, stop
        │     │  │  └─ take: rec(5, "aa")    -> i == 5, stop
        │     │  └─ take c: rec(4, "ac")
        │     │     ├─ skip: rec(5, "ac")    -> i == 5, stop
        │     │     └─ take: rec(5, "aca")   -> len 3, a == a, ADD "aca"
        │     └─ take b: rec(3, "ab")
        │        ├─ skip c: rec(4, "ab")
        │        │  ├─ skip: rec(5, "ab")    -> i == 5, stop
        │        │  └─ take: rec(5, "aba")   -> len 3, a == a, ADD "aba"
        │        └─ take c: rec(4, "abc")    -> len 3, a != c, not added
        └─ take a(0): rec(1, "a")
        ├─ skip a(1): rec(2, "a")
        │  ├─ skip b: rec(3, "a")
        │  │  ├─ skip c: rec(4, "a")
        │  │  │  ├─ skip: rec(5, "a")     -> i == 5, stop
        │  │  │  └─ take: rec(5, "aa")    -> i == 5, stop
        │  │  └─ take c: rec(4, "ac")
        │  │     ├─ skip: rec(5, "ac")    -> i == 5, stop
        │  │     └─ take: rec(5, "aca")   -> len 3, a == a, already in set
        │  └─ take b: rec(3, "ab")
        │     ├─ skip c: rec(4, "ab")
        │     │  ├─ skip: rec(5, "ab")    -> i == 5, stop
        │     │  └─ take: rec(5, "aba")   -> len 3, a == a, already in set
        │     └─ take c: rec(4, "abc")    -> len 3, a != c, not added
        └─ take a(1): rec(2, "aa")
            ├─ skip b: rec(3, "aa")
            │  ├─ skip c: rec(4, "aa")
            │  │  ├─ skip: rec(5, "aa")    -> i == 5, stop
            │  │  └─ take: rec(5, "aaa")   -> len 3, a == a, ADD "aaa"
            │  └─ take c: rec(4, "aac")    -> len 3, a != c, not added
            └─ take b: rec(3, "aab")       -> len 3, a != b, not added
        '''


        res = 0 

        for ch in set(s): 
            first = s.find(ch)
            # find from left to right
            last = s.rfind(ch)
            # find from right to left

            if last - first > 1: # greater than 1 means there is atleast one character between them
            # we are trying to count how many distinct characters are there
                res += len(set(s[first + 1:last]))
                '''
                Example: ch='a', middle {a,b,c} → aaa, aba, aca = 3.
                '''

        return res