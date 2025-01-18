class Solution:
    def countAsterisks(self, s: str) -> int:
        s=s.split("|")
        count=0
        for i in range(0,len(s),2):
            for j in range(len(s[i])):
                if s[i][j]=="*":
                    count+=1
        return count
        