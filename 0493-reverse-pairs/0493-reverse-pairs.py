class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0  
        
        def merge_sort(nums):
            n = len(nums)
            if n <= 1:
                return nums
            mid = n // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)
        
        def merge(left, right):
            i = 0
            for j in range(len(right)):
                while i < len(left) and left[i] <= 2 * right[j]:
                    i += 1
                self.count += len(left) - i  
            
            ans = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    ans.append(left[i])
                    i += 1
                else:
                    ans.append(right[j])
                    j += 1
            ans.extend(left[i:])
            ans.extend(right[j:])
            return ans
        
        merge_sort(nums)
        return self.count