class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ''
        last = True
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if last:
                    continue
                else:
                    break
            else:
                last = False
                word += s[i]

        return len(word)