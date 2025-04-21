class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        low=0
        high=n-1
        while (low<=high):
            mid=(low+high)/2
            if nums[mid]==target:
                return mid
                break
            elif nums[mid]>target:
                high=mid-1
                continue
            elif nums[mid]<target:
                low=mid+1
                continue
        return -1
            
        