class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #concating both the string and checking if any character counts is odd
        for a in (s+t):
            if (s+t).count(a)%2==1:
                return a
        
            
        