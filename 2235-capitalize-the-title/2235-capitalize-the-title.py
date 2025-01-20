class Solution:
    def capitalizeTitle(self, title: str) -> str:
        titles=title.split(" ")
        ans=""
        for i in range(len(titles)):
            if len(titles[i])>=3:
                titles[i]=titles[i].capitalize()
            else:
                titles[i]=titles[i].lower()
            if i==0:
                ans+=titles[i]
            else:
                ans+=" "+titles[i]
        
    
        return str(ans)
        