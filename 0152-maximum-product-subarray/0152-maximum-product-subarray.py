class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        suffix=1
        n=len(nums)
        maximum=-inf
        for i in range(n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix=prefix*nums[i]
            suffix=suffix*nums[n-1-i]
            maximum=max(maximum,max(prefix,suffix))
        return maximum
        