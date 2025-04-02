class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        m=len(matrix)
        n=len(matrix[0])
        z_r=[]
        z_c=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    z_r.append(i)
                    z_c.append(j)
        
        for i in range(m):
            for j in range(n):
                if i in z_r or j in z_c:
                    matrix[i][j]=0


    
        