class Solution:
    def toLowerCase(self, s: str) -> str:
        # an empty string to store the lower case
        result=""
        for a in s:
            #checking the ascii of the character
            #65-90 is for upper case and 97-122 is for lower case
            #changing the upper case ascii to lower case ascii
            #and then adding that ascii char back 
            if ord(a)<=90 and ord(a)>=65:
                result = result + chr(ord(a)+32)
            else:
                result = result + a
        return result