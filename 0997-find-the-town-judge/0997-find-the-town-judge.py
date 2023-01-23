class Solution:
    # O(n) time and O(n) space
    def findJudge(self, n: int, trusts: List[List[int]]) -> int:
        if len(trusts) == 0:
            if n > 1:
                return -1
            else:
                return 1
    
        trusters: DefaultDict[int, set] = defaultdict(lambda: set())
        trustees: DefaultDict[int, set] = defaultdict(lambda: set())
        
        candidate = 0
        candidateOccurrences = 0
        maximumTrusts = 0
        for trust in trusts:
            trusters[trust[0]].add(trust[1])
            trustees[trust[1]].add(trust[0])
            
            if len(trustees[trust[1]]) == maximumTrusts:
                candidateOccurrences += 1

            elif len(trustees[trust[1]]) > maximumTrusts:
                maximumTrusts = len(trustees[trust[1]])
                candidateOccurrences = 1
                candidate = trust[1]
        
        if (maximumTrusts == n - 1
            and len(trusters[candidate]) == 0
            and candidateOccurrences == 1):
            return candidate
        else:
            return -1
