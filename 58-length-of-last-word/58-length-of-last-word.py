class Solution:
    # O(n) time and O(1) space
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        last = True
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if last:
                    continue
                else:
                    break
            else:
                last = False
                length += 1

        return length