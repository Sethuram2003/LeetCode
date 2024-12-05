class Solution:
    def validStrings(self, n: int) -> List[str]:
        binary_list=[]
        for i in range(2**n):
            binary_string = format(i, '0{}b'.format(n))
            if '00' not in binary_string and len(binary_string)==n:
                binary_list.append(binary_string)
        return binary_list


        
