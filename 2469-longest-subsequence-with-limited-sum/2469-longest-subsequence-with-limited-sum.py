class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        # return(nums)
        n=len(nums)
        m=len(queries)
        answer=[]
        for i in range(m):
            total=0
            count=0
            for j in range(n):
                total=total+nums[j]

                if total>queries[i]:
                    break
                else:
                    count=count+1
            answer.append(count)
        return answer

        