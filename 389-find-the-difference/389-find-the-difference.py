class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        st = s+t
        #concating the strings and checking if any character has a odd count
        for a in st:
            if st.count(a)%2==1:
                return a
        
            
        