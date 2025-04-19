class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[]
        
        intervals.sort()
        
        for pair in intervals:
            n=len(ans)
            if n==0:
                ans.append(pair)
                continue
            if ans[n-1][0] <= pair[0] and ans[n-1][1] >= pair[0]:
                if ans[n-1][0]>=pair[0]:
                    ans[n-1][0]=pair[0]
                if ans[n-1][1]<=pair[1]:
                    ans[n-1][1]=pair[1]
            else:
                ans.append(pair)
        return ans

            

            

        