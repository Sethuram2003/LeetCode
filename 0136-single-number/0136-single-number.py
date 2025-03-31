class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans={}
        n=len(nums)
        for i in nums:
            if i in ans.keys():
                ans[i]=ans[i]+1
            else:
                ans[i]=1
        for key,value in ans.items():
            if value==1:
                return key
        