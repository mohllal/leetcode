from collections import Counter

class Solution:
    # O(n) time and O(1) space
    def totalFruit(self, fruits: List[int]) -> int:
        maximum_fruits = float("-inf")
        
        window_start = 0
        window_counter = Counter()
        for window_end in range(len(fruits)):
            window_counter[fruits[window_end]] += 1
            
            while len(window_counter) > 2:
                window_counter[fruits[window_start]] -= 1
                
                if window_counter[fruits[window_start]] == 0:
                    window_counter.pop(fruits[window_start])
                
                window_start += 1
            
            maximum_fruits = max(maximum_fruits, (window_end - window_start) + 1)
        
        return maximum_fruits