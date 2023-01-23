class Solution:
    # O(n) time and O(n) space
    def findJudge(self, n: int, trusts: List[List[int]]) -> int:
        if len(trusts) == 0 and n == 1:
            return 1

        if len(trusts) == 0 and n > 1:
                return -1

        trusters: DefaultDict[int, set] = defaultdict(lambda: set())
        trustees: DefaultDict[int, set] = defaultdict(lambda: set())
        
        candidate = 0
        maximum = 0
        occurrence = 0
        for trust in trusts:
            trusters[trust[0]].add(trust[1])
            trustees[trust[1]].add(trust[0])
            
            if len(trustees[trust[1]]) == maximum:
                occurrence += 1
            elif len(trustees[trust[1]]) > maximum:
                maximum = len(trustees[trust[1]])
                occurrence = 1
                candidate = trust[1]
        
        if maximum == n - 1 and len(trusters[candidate]) == 0 and occurrence == 1:
            return candidate
        else:
            return -1
        
#         result = -1
#         for a in trustees:
#             if len(trustees[a]) == n - 1 and len(trusters[a]) == 0:
#                 if result == -1:
#                     result = a
#                 else:
#                     result = -1
#                     break
        
#         return result
            