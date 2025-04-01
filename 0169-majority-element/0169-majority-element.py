class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count=0
        ele=nums[0]

        for num in nums:
            if count==0:
                ele=num
            if ele==num:
                count+=1
            else:
                count-=1
        return ele



        