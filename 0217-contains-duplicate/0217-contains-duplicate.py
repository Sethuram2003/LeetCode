class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr=nums
        pair={}
        for i in range(len(arr)):
            if f"""{arr[i]}""" not in pair.keys():
                pair[f"""{arr[i]}"""]=1
            else:
                pair[f"""{arr[i]}"""]=pair[f"""{arr[i]}"""]+1
        if max(list(pair.values()))==1:
            return False
        else:
            return True
        