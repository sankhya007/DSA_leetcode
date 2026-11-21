from collections import Counter
# seriously i have to use conter or this?

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freqs, freqt = Counter(s), Counter(t)
        for ch in freqt: 
            if ch not in freqs or freqs[ch] < freqt[ch]: 
                return ch