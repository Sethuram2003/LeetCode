class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        n=len(nums)
        if n==1:
            return nums
        j=0
        i=0
        while(j<n):
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
                j+=1
            else:
                j+=1
        n_zeores=j-i
        for i in range(n-n_zeores,n):
            nums[i]=0
        