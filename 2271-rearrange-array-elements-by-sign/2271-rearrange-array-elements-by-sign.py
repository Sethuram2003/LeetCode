class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        i=0
        j=1
        num1=[0]*len(nums)
        for num in nums:
            if num>0:
                num1[i]=num
                i+=2
            else:
                num1[j]=num
                j+=2
        return num1
        