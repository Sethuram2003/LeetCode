class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        ans=[]
        flag=0
        for i in nums1:
            for j in nums2:
                if i==j:
                    ans.append(i)
                    flag=1
        if flag==1:
            return min(ans)
        else:
            ans1=[]
            a = int(str(min(nums1))+str(min(nums2)))
            ans1.append(a)
            b = int(str(min(nums2))+str(min(nums1)))
            ans1.append(b)
            return min(ans1)
        