class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for account in accounts:
            #calculating weaalth of each account
            #and storing it in alist
            wealth.append(sum(account))
        #returning the max of the wealth list
        return(max(wealth))