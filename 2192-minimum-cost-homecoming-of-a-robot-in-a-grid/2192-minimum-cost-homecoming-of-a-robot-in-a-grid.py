class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        i,j=startPos
        a,b=homePos
        cost=0
        if i<a:
            for k in range(i,a):
                cost+=rowCosts[k+1]
        else:
            for m in range(a,i):
                cost+=rowCosts[m]
        if j<b:
            for l in range(j,b):
                cost+=colCosts[l+1]
        else:
            for n in range(b,j):
                cost+=colCosts[n]
            
        return cost