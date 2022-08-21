class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # Using additive and multiplicative identity 
        # for initial values of sum and product
        Sum=0
        product=1
        while n>0:
            #using n%10 to get the last digit
            Sum = Sum + (n%10)
            product = product*(n%10)
            #removing the last digit
            n = n//10
        return product-Sum
            
            
        