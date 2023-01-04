class Solution:
    # O(n) time and O(n) space
    def minimumRounds(self, tasks: List[int]) -> int:
        occurrences = {}
        for task in tasks:
            if task in occurrences:
                occurrences[task] += 1
            else:
                occurrences[task] = 1
        
        minimumNumberOfRounds = 0
        for _, count in occurrences.items():
            if count == 1:
                return -1
            elif count % 3 == 0:
                minimumNumberOfRounds += count // 3
            else:
                remainOfThree = count % 3
                divideByThree = count // 3
                
                if remainOfThree % 2 == 0:
                    minimumNumberOfRounds += (divideByThree + (remainOfThree // 2))
                else:
                    divideByThree -= 1
                    remainOfThree += 3

                    if remainOfThree % 2 == 0:
                        minimumNumberOfRounds += (divideByThree + (remainOfThree // 2))
                    else:
                        return -1

        return minimumNumberOfRounds
