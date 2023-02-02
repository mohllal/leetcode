class Solution:
    # O(m) time and O(1) space
    def wordOrder(self, word, orders):
        order = 0
        for char in word:
            order += orders[char]
        
        return order

    # O(n * m) time and O(1) space
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orders = {order[i]: i + 1 for i in range(len(order))}

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                
                if words[i][j] != words[i + 1][j]:
                    if orders[words[i][j]] > orders[words[i + 1][j]]:
                        return False
                    break
        return True