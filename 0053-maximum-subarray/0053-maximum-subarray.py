class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=0
        max_num= -1e10
        if len(nums)==1:
            return nums[0]

        for num in nums:
            total+=num
            if total>max_num:
                max_num=total
            if total<0:
                total=0
        return max_num
        
        