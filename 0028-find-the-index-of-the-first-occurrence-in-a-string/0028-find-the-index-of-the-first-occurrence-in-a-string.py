class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=[]
        for i in range(len(haystack)-len(needle)+1):
            flag=0
            for j in range(len(needle)):
                if needle[j]!=haystack[j+i]:
                    flag=1
            if flag==0:
                a.append(i)
        if len(a)==0:
            return -1
        else:
            return min(a)
        