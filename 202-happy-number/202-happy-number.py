class Solution:
    def isHappy(self, n: int) -> bool:
        # Having a list to store the next numbers
        # Checking if it is not in seen i.e. no case of it forming a loop
        seen = []
        while n not in seen:
            seen.append(n)
            # from str(n) getting each digit and squaring it
            n = sum([int(x) **2 for x in str(n)])
        return n == 1