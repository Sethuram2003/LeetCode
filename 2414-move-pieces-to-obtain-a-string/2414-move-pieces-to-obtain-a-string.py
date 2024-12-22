class Solution:
    def canChange(self, start: str, target: str) -> bool:
        left = 0
        right = 0

        for i in range(len(start)):
            if start[i] == 'R':
                right += 1
                if left != 0:
                    return False
            elif start[i] == 'L':
                left -= 1
            if target[i] == 'R':
                right -= 1
            elif target[i] == 'L':
                left += 1
                if right != 0:
                    return False
            if left < 0 or right < 0:
                return False

        return left == 0 and right == 0