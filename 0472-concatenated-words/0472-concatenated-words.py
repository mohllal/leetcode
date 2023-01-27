class Solution:
    def dfs(self, word, length, words):
        if length == len(word):
            return True

        for i in range(len(word) - (1 if length == 0 else 0), length, -1):
            if word[length:i] in words and self.dfs(word, i, words):
                return True
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordsSet = set(words)
        answer = []

        for word in words:
            length = len(word)
            if self.dfs(word, 0, wordsSet):
                answer.append(word)

        return answer