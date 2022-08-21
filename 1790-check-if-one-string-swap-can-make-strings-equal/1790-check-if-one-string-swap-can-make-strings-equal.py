class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        #seeing the difference between the two strings
        diff = [[x, y] for x, y in zip(s1, s2) if x != y]
        #depending on the differece returing true or fasle as required
        return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]