class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        left=0
        top=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        ans=[]
        while (left<=right and top <=bottom):
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            for j in range(top,bottom+1):
                ans.append(matrix[j][right])
            right-=1
            if top<=bottom:
                for k in range(right,left-1,-1):
                    ans.append(matrix[bottom][k])
                bottom-=1
            if left<=right:
                for l in range(bottom,top-1,-1):
                    ans.append(matrix[l][left])
                left+=1
        return (ans)



        