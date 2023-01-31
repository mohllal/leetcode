class Solution:       
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        pairs = [[age, score] for age, score in zip(ages, scores)]
        pairs.sort(key=lambda x: (x[0], x[1]), reverse=True)

        maximum = 0
        dp = [0] * n
        for i in range(n):
            score = pairs[i][1]
            dp[i] = score

            for j in range(i):
                if pairs[j][1] >= score:
                    dp[i] = max(dp[i], dp[j] + score)

            maximum = max(maximum, dp[i])

        return maximum