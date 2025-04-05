class Solution(object):



    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def genrow(nrows):
            row=[]
            ans=1

            row.append(ans)
            for i in range(1,nrows):
                ans=ans*(nrows-i)
                ans=ans/i
                row.append(ans)
            return(row)

        ans=[]
        for j in range(1,numRows+1):
            ans.append(genrow(j))
        return ans







            

        