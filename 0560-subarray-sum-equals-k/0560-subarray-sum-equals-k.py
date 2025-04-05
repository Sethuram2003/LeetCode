class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_map={}
        hash_map[0]=1
        n=len(nums)
        sum_nums=0
        count=0
        for i in range(n):
            sum_nums+=nums[i]

            if sum_nums-k in hash_map:
                count+=hash_map[sum_nums-k]

            if sum_nums not in hash_map:
                hash_map[sum_nums]=1
            else:
                hash_map[sum_nums]+=1

        return(count)
