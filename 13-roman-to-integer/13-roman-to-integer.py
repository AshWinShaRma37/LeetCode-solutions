class Solution:
    def romanToInt(self, s: str) -> int:
        #creating a dictionary to store values of each symbol
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0 #index
        rom=0  #by default roman number set to 0
        while (i < len(s)):
            #getting the value of ith character in string
            s1 = dic[(s[i])]
            if (i + 1 < len(s)):
                #getting value of next element
                s2 = dic[(s[i + 1])]
                #checking based on next element if it is to be added or subtracted
                if (s1 >= s2):
                    rom = rom + s1
                    i = i + 1
                else:
                    rom = rom + s2 - s1
                    i = i + 2
            #if no more elements left simply add the value
            else:
                rom = rom + s1
                i = i + 1
        return rom