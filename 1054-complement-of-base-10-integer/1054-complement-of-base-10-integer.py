class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bit=[]
        if n==0:
            return 1
        while n>1:
            m=int(n%2)
            bit.append(m)
            n=n/2
        bit.reverse()
        for i in range(len(bit)):
            if bit[i]==1:
                bit[i]=0
            elif bit[i]==0:
                bit[i]=1
        num=0
        for i in range(len(bit)):
            num+=bit[len(bit)-i-1]*2**(i)
        return num

        