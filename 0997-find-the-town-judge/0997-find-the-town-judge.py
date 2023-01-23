class Solution:
    # O(n) time and O(n) space
    def findJudge(self, n: int, trusts: List[List[int]]) -> int:
        if len(trusts) == 0 and n == 1:
            return 1

        if len(trusts) == 0 and n > 1:
                return -1

        trusters: DefaultDict[int, set] = defaultdict(lambda: set())
        trustees: DefaultDict[int, set] = defaultdict(lambda: set())
        
        for trust in trusts:
            trusters[trust[0]].add(trust[1])
            trustees[trust[1]].add(trust[0])
        
        result = -1
        for a in trustees:
            if len(trustees[a]) == n - 1 and len(trusters[a]) == 0:
                if result == -1:
                    result = a
                else:
                    result = -1
                    break
        
        return result
            