class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  
        rotated = nums[-k:] + nums[:-k]
        nums[:] = rotated 
        return nums


        