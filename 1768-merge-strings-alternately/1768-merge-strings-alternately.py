class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result =""
        #getting the minimum length of the two words
        m = min(len(word1),len(word2))
        #adding alternately until the min length
        for i in range(m):
            result = result + word1[i]+word2[i]
        #simply adding the remaining length of word as it is
        return result+word1[m:]+word2[m:]