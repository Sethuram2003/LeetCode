class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans={}
        count=0
        for num in nums:
            if num in ans.keys():
                ans[num]=1+ans[num]
            else:
                ans[num]=0
        maax=0
        for num in nums:
            if ans[num]>maax:
                maax=ans[num]
        return(ans.keys()[ans.values().index(maax)])


        