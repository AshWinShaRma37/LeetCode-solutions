class Solution:
    def romanToInt(self, s: str) -> int:
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        rom=0
        while (i < len(s)):
            s1 = dic[(s[i])]
            if (i + 1 < len(s)):
                s2 = dic[(s[i + 1])]
                if (s1 >= s2):
                    rom = rom + s1
                    i = i + 1
                else:
                    rom = rom + s2 - s1
                    i = i + 2
            else:
                rom = rom + s1
                i = i + 1
        return rom