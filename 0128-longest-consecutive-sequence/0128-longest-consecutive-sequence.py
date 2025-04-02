class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count=1
        max_count=1
        n=len(nums)
        if n==1:
            return 1
        elif n==0:
            return 0
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                continue
            if nums[i]+1==nums[i+1]:
                count+=1
                if count>max_count:
                    max_count=count
            else:
                count=1
        return max_count