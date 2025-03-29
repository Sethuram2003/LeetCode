class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        for i in range(len(word1)):
            for j in range(i,len(word2)):
                ans=ans+word1[i]+word2[j]
                break
        if len(word1)>len(word2):
            for i in range(len(word2),len(word1)):
                ans=ans+word1[i]
        elif len(word1)<len(word2):
            for i in range(len(word1),len(word2)):
                ans=ans+word2[i]


        return ans
        