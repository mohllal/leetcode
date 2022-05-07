class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hashmap = {}
        for element in strs:
            for i in range(0, len(element)):
                substr = element[:i + 1]
                if substr in hashmap:
                    hashmap[substr] += 1
                else:
                    hashmap[substr] = 1

        maximum = -1
        result = ''
        for element in hashmap:
            if hashmap[element] >= maximum and len(element) > len(result):
                result = element
                maximum = hashmap[element]
        
        return result if (maximum == len(strs)) else ''