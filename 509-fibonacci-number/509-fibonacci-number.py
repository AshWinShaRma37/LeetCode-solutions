class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            #for f(0)=0 and f(1)=1 casess
            return n
        else:
            #for f(n)=f(n-1)+f(n-2)
            return self.fib(n-1)+self.fib(n-2)
        