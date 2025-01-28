class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        if x==2:
            return 1
        for i in range(x):
            if i*i >= x:
                if i*i == x:
                    return i
                    break
                else:
                    return i-1
                    break
            