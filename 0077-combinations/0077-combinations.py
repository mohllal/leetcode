class Solution:
    # O(C(n,k)) time and O(C(n,k)) space or O(k) space if we exclude the result set space
    # C(n,k) = n! / k!(n-k)!
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combineHelper(n, k, prefix, start, combinations):
            if len(prefix) == k:
                combinations.append(prefix[:])
                return
            
            for i in range(start, n + 1):
                prefix.append(i)
                combineHelper(n, k, prefix, i + 1, combinations)
                prefix.pop()
        
        prefix = []
        combinations = []
        start = 1
        combineHelper(n, k, prefix, start, combinations)
        return combinations