class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
                continue
            elif nums[mid]<target:
                low=mid+1
                continue
            if low==high:
                break
        if nums[mid]>target:
            return mid
        return mid+1

        