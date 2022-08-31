class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        st = s+t
        for a in st:
            if st.count(a)%2==1:
                return a
        
            
        