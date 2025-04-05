class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n=len(nums)
        nums_dict={}

        for i in range(n):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]]=1
            else:
                nums_dict[nums[i]]+=1
        ans=[]
        for key,value in nums_dict.items():
            if value >n/3:
                ans.append(key)
        return (ans)

        