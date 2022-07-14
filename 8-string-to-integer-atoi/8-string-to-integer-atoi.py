class Solution:
    def myAtoi(self, s: str) -> int:
        #removing whitespaces in front
        #this is to make sure other whitespaces are taken into consideration
        s = s.lstrip() 
        #creating an empty string to append the digits
        g = ""
        #if s is empty no need for checking other things they may not work as well 
        if g==s: return 0  
        
        #checking the sign
        if s[0]=="-":
            g="-"
            s = s[1:]
        elif s[0]=="+":
            s = s[1:]
            
        #checking and appending digits to string
        for a in s:
            try:
                int(a)
                g=g+a
                
            except:
                break
        if g.replace("-","")=="": g="0"
            
        #converting the resultant string to int
        n =int(g)
        
        #making sure the integer is in range[-2**31,2**31-1]
        if n<=-pow(2,31): return -pow(2,31)
        elif n>=pow(2,31): return pow(2,31) - 1
        else: return n