class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans={}
        count=0
        for num in nums:
            ans[num]=0
        for num in nums:
            ans[num]=1+ans[num]
        maax=0
        for num in nums:
            if ans[num]>maax:
                maax=ans[num]
        return(ans.keys()[ans.values().index(maax)])


        