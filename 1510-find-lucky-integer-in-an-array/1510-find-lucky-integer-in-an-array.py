class Solution:
    def findLucky(self, arr: List[int]) -> int:
        pair={}
        for i in range(len(arr)):
            if f"""{arr[i]}""" not in pair.keys():
                pair[f"""{arr[i]}"""]=1
            else:
                pair[f"""{arr[i]}"""]=pair[f"""{arr[i]}"""]+1
        count=-1
        for i in range(len(pair)):
            if int(list(pair.keys())[i])==list(pair.values())[i] and count<list(pair.values())[i]:
                    count=list(pair.values())[i]
        return count




        