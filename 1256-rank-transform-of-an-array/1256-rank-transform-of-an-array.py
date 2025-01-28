class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = sorted(set(arr))
        ar_sort = {num: rank + 1 for rank, num in enumerate(arr2)}
        return [ar_sort[num] for num in arr]
        