class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        for i in range(len(words)): 
            # check if 1th element's last letter is same as i+1th element's 1st letter
            if words[i][-1] != words[(i + 1) % len(words)][0]: 
                return False

        return True
