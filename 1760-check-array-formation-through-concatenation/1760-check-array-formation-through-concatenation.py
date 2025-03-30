class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        dummy={}
        for piece in pieces:
            dummy[piece[0]]=piece
        ans=[]

        for a in arr:
            ans=ans+dummy.get(a,[])
        if arr==ans:
            return True
        else:
            return False




        