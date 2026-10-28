class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # fuck leet code this passed 93/94 test cases
        # vowels = ['a', 'e', 'i', 'o', 'u']
        # storage = []
        # length = []
                
        # for i, word in enumerate(words): 
        #     if word[0] in vowels and word[-1] in vowels: 
        #         storage.append(i)

        # for querie in queries: 
        #     count = 0 
        #     for i in range(querie[0], querie[-1] + 1): 
        #         if i not in storage: 
        #             continue
        #         count += 1
        #     length.append(count)

        # return length



        # same principal, better execution but time limit will exceed if we use n^2 as time complexity
        # vowels = set("aeiou")
        # res = []

        # for start, end in queries: 
        #     count = 0 
        #     for i in range(start, end + 1): 
        #         if words[i][0] in vowels and words[i][-1] in vowels: 
        #             count += 1

        #     res.append(count)

        # return res




        vowel_set = set("aeiou")
        prefix_count = [0] * (len(words) + 1)
        prev = 0 

        # in the past positions how ever many times we have seen the vowels
        for i, w in enumerate(words): 
            if w[0] in vowel_set and w[-1] in vowel_set: 
                prev += 1
            prefix_count[i + 1] = prev

        res = [0] * len(queries)
        for i, q in enumerate(queries): 
            l, r = q
            # ending+1 - starting
            res[i] = prefix_count[r+1] - prefix_count[l]

        return res