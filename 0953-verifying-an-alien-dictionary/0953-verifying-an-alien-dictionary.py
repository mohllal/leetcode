class Solution:
    # O(n * m) time and O(1) space
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orders = {order[i]: i + 1 for i in range(len(order))}

        for i in range(len(words) - 1):
            currentWord = words[i]
            nextWord = words[i + 1]
    
            for j in range(len(currentWord)):
                if j >= len(nextWord):
                    return False
                
                if currentWord[j] != nextWord[j]:
                    if orders[currentWord[j]] > orders[nextWord[j]]:
                        return False
                    break
        return True