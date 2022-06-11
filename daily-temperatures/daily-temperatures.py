class Solution:        
    # O(n ^ 2) time and O(n) space
    def dailyTemperaturesQuadraticTimeAndLinearSpace(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(0, len(temperatures)):
            numberOfDays = 0
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    numberOfDays = j - i
                    break
            result.append(numberOfDays)
        return result

    # O(n) time and O(n) space
    def dailyTemperaturesLinearTimeAndLinearSpace(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i in range(0, len(temperatures)):
            current = temperatures[i]
            
            while stack and stack[-1][0] < current:
                prevVal, prevIndx  = stack.pop()
                result[prevIndx] = i - prevIndx
    
            stack.append((current, i))

        return result            

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return self.dailyTemperaturesLinearTimeAndLinearSpace(temperatures)