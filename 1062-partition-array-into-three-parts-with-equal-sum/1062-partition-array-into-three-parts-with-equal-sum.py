class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        total=sum(arr)
        if total%3==0:
            small_sum=total/3
            sum_arr=0
            empty=[]

            # part=[]
            for i in arr:
                # part.append(i)
                sum_arr=sum_arr+i
                if sum_arr==small_sum:
                    sum_arr=0
                    empty.append(True)
                    # part=[]
            if len(empty)>=3:
                return True
            else:
                return False
        else:
            return False
        