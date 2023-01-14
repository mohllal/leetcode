class Solution:
    maximum = 1

    # O(n) time and O(n) space
    def dfs(self, node, adjacent, s):
        if node not in adjacent:
            return 1

        firstLongest = 0
        secondLongest = 0
        for child in adjacent[node]:
            currentLongest = self.dfs(child, adjacent, s)

            if s[child] == s[node]:
                continue

            if currentLongest > firstLongest:
                secondLongest = firstLongest
                firstLongest = currentLongest
            elif currentLongest > secondLongest:
                secondLongest = currentLongest

        self.maximum = max(self.maximum, firstLongest + secondLongest + 1)
        return firstLongest + 1

    # O(n) time and O(n) space
    def longestPath(self, parents: List[int], s: str) -> int:
        adjacent: DefaultDict[int, []]= defaultdict(lambda: [])

        for i in range(1, len(parents)):
            adjacent[parents[i]].append(i)

        self.dfs(0, adjacent, s)
        return self.maximum
