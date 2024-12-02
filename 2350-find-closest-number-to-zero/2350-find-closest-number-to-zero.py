class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        n=len(nums)
        negative=[]
        positive=[]
        for i in range(n):
            if nums[i]<0:
                negative.append(nums[i])
            elif nums[i]>=0:
                positive.append(nums[i])
        negative.sort()
        positive.sort()
        ng=len(negative)-1
        if len(negative)!=0 and len(positive)!=0:
            if abs(negative[ng])==positive[0]:
                return positive[0]
            elif negative[ng]*(-1)<positive[0]:
                return negative[ng]
            elif negative[ng]*(-1)>positive[0]:
                return positive[0]
        elif len(negative)==0 and len(positive)==0:
            return nums[0]
        elif len(positive)==0:
            return negative[ng]
        elif len(negative)==0:
            return positive[0]
            