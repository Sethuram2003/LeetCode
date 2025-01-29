class Solution:
    def printVertically(self, s: str) -> List[str]:
        chunck=s.split(" ")
        max_length=0
        for i in range(len(chunck)):
            if len(chunck[i])>max_length:
                max_length=len(chunck[i])
        ans=[]
        for j in range(max_length):
            words=""
            for i in range(len(chunck)):
                try:
                    words=words+chunck[i][j]
                except:
                    words=words+" "

            test=" "
            while test==" ":
                h=len(words)
                if h>0:
                    test=words[h-1]
                    if test==" ":
                        words=words[0:h-1]
                else:
                    break

            ans.append(words)
       
        return ans




        