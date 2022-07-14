class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #getting counts of each element in dictionary
        dic1 = collections.Counter(ransomNote)
        dic2 = collections.Counter(magazine)
        #comparing all counters of ransomNote with magazine
        for i in dic1:
            if dic2[i] < dic1[i]:
                return False
        return True