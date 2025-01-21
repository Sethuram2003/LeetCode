class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False

        highest=max(arr)
        if len(arr)-1 == arr.index(highest):
            return False
        flag=0
        for i in range(1,len(arr)):
            if arr[i-1]>=arr[i]:
                flag=1
                break
            if arr[i]==highest:
                break
        for i in range(arr.index(highest),len(arr)-1):
            if arr[i]<=arr[i+1]:
                flag=1
                break
        if flag==1:
            return False
        else:
            return True
        