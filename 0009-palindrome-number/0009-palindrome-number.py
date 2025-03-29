class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        for i in range(int(len(str(x))/2)):
            if str(x)[i]!=str(x)[int(len(str(x)))-i-1]:
                return False
        return True
        