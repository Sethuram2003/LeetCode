class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def hours_for_each_pile(pile,k):
            if pile<k:
                return 1
            elif pile%k==0:
                return int(pile/k)
            else:
                return int((pile/k)+1)




        low=1
        high=max(piles)
        lowest=high
        while(low<=high):
            mid=int((low+high)/2)
            total=0
            for pile in piles:
                total+=hours_for_each_pile(pile,mid)


            if total<=h:
                high=mid-1
                if mid <lowest:
                    lowest=mid
            elif total>h:
                low=mid+1
        return lowest



        