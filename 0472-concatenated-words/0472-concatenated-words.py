class Solution:
    def dfs(self, word, length, visited, words):
        if length == len(word):
            return True

#         if visited[length]:
#             return False

#         visited[length] = True
        for i in range(len(word) - (1 if length == 0 else 0), length, -1):
            if (
                word[length:i] in words and
                self.dfs(word, i, visited, words)
               ):
                return True
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordsSet = set(words)
        answer = []

        for word in words:
            length = len(word)
            visited = [False] * length
            if self.dfs(word, 0, visited, wordsSet):
                answer.append(word)

        return answer