class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        c = len(mat)
        i = 0
        dsum = 0
        for row in mat:
            #checking for common point of both diagonals
            #adding it only once
            if i == c-i-1:
                dsum = dsum+row[i]
            #for other points of each diagonal adding them to dsum
            else:
                dsum = dsum+row[i]+row[c-i-1]
            i += 1
        return dsum
        