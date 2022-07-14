class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        g = ""
        if g==s: return 0
        if s[0]=="-":
            g="-"
            s = s[1:]
        elif s[0]=="+":
            s = s[1:]
        for a in s:
            try:
                int(a)
                g=g+a
                
            except:
                break
        if g.replace("-","")=="": g="0"
        n =int(g)
        if n<=-pow(2,31): return -pow(2,31)
        elif n>=pow(2,31): return pow(2,31) - 1
        else: return n