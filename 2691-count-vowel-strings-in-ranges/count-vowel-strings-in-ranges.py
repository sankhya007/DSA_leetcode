# class Solution:
#     def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
#         vowels = set("aeiou")
#         array = []

#         for quary in queries: 
#             first, last = quary
#             count = 0 

#             for i in range(first, last+1): 
#                 if words[i][0] in vowels and words[i][-1] in vowels: 
#                     count += 1

#             array.append(count)

#         return array


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_set = set("aeiou")
        prefix_count = [0] * (len(words) + 1)
        # we need to have an extra element at the 1st because else when we go calculate it'll just be out of bounds
        prev = 0 

        for i, w in enumerate(words): 
            if w[0] in vowel_set and w[-1] in vowel_set: 
                prev += 1
            # count however many vowels that we have seen till now and then just paste that number
            prefix_count[i+1] = prev

        res = [0] * len(queries) # answer array
        # simple left and right solution that i figured out as well, append one to the right so then we include that word itself while counting
        for i, q in enumerate(queries): 
            l, r = q
            res[i] = prefix_count[r+1] - prefix_count[l]

        return res