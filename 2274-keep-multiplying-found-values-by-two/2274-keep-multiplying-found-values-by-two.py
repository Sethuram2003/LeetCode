class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        ans=0
        flag=0
        while flag==0:
            if original in nums:
                original*=2
            else:
                flag=1
                ans=original
        return ans
        