class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans=0
        for i in range(len(items)):
            if ruleKey=="color":
                if ruleValue==items[i][1]:
                    ans+=1
            elif ruleKey=="type":
                if ruleValue==items[i][0]:
                    ans+=1
            elif ruleKey=="name":
                if ruleValue==items[i][2]:
                    ans+=1
        return ans