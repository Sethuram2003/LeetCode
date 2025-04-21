class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]

        def lowerbound(nums,target):

            n=len(nums)
            low=0
            high=n-1
            mid=(low+high)//2

            while(low<=high):
                if nums[mid]==target:
                    high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                mid=(low+high)//2


            return mid     

        def upperbound(nums,target):

            n=len(nums)
            low=0
            high=n-1
            mid=(low+high)//2

            while(low<=high):
                if nums[mid]==target:
                    low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                elif nums[mid]>target:
                    high=mid-1
                mid=(low+high)//2


            return mid   

           

        return [lowerbound(nums,target)+1,upperbound(nums,target)]