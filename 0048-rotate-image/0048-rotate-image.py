class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        m=len(matrix)
        n=len(matrix[0])

        for i in range(m-1):
            for j in range(i+1,n):
                if i!=j:
                    t=matrix[i][j]
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=t
        for k in range(m):
            matrix[k].reverse()

