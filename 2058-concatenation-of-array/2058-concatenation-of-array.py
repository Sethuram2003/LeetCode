class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for j in range(len(nums)*2):
            ans.append(0)
        for i in range(len(nums)):
            ans[i]=nums[i]
            ans[i+len(nums)]=nums[i]
        return ans
