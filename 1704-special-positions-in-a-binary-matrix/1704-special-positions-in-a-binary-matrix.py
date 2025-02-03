class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        count=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    continue
                isspecial=True
                for k in range(n):
                    if k!=i and mat[k][j]==1:
                        isspecial=False
                for l in range(m):
                    if l!=j and mat[i][l]==1:
                        isspecial=False
                if isspecial:
                    count+=1
        return count

        