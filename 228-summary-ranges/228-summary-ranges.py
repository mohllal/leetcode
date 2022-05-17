class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        result = [(nums[0], nums[0])]
        current = nums[0] + 1
        i = 1

        while i < len(nums):
            if nums[i] == current:
                result[-1] = (result[-1][0], nums[i])
            else:
                result.append((nums[i], nums[i]))

            current = nums[i] + 1
            i += 1
        
        for j in range(0, len(result)):
            start = result[j][0]
            end = result[j][1]
            result[j] = "%d->%d" % (start, end) if start != end else "%d" % (start)

        return result