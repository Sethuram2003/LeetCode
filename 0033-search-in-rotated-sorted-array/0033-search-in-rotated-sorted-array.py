class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        k=nums.index(min(nums))
        n=len(nums)
        low=0
        high=n-1
        if target not in nums:
            return -1

        while(low<=high):
            mid=(low+high)/2
            if nums[(mid+k)%n]==target:
                return (mid+k)%n
                break
            elif nums[(mid+k)%n]>target:
                high=mid-1
            elif nums[(mid+k)%n]<target:
                low=mid+1
        