class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        number1=0
        for i in range(len(num)):
            number1=number1+num[i]*10**(len(num)-i-1)
        new_number = number1+k
        new_number_str=str(new_number)
        output=[]
        for i in new_number_str:
            output.append(int(i))
        return output

        