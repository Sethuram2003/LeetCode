class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ans=[]
        for i in range(len(grid)):
            if i%2==0:
                for j in range(len(grid[i])):
                    if j%2==0:
                        ans.append(grid[i][j])
            else:
                for j in range(len(grid[i])):
                    j=len(grid[i])-j-1
                    if j%2!=0:
                        ans.append(grid[i][j])      
        return ans    
        