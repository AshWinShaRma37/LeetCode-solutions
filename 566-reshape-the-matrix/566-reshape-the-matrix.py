class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [] #flattened matrix
        matrix = []
        #creating a flat version of input matrix
        for nlist in mat:
            for n in nlist:
                res.append(n)
                
        #checking if the new r,c fits the input matrix
        if len(res) != r * c:
            return mat
        
        #if they do then just make a new matrix with r,c
        else:
            for i in range(0,len(res),c):
                matrix.append(res[i:i+c])
        return matrix
        