class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        ind = -1
        
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break
        
        if ind == -1:
            nums.reverse()
        else:
            swap = None
            for j in range(n-1, ind, -1):
                if nums[j] > nums[ind]:
                    swap = j
                    break
            
            nums[ind], nums[swap] = nums[swap], nums[ind]
            
            left, right = ind+1, n-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1


        





        