class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output=[]
        def test(openb, closeb, out):
            if openb==closeb and openb+closeb==n*2:
                output.append(out)
            if openb < n:
                test(openb+1,closeb,out+"(")
            if closeb < openb:
                test(openb,closeb+1,out+")")
            



        test(0,0,"")
        return output
        