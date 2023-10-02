class Solution:
    def letterCombinations(self, digits):
        return self.letterCombinationsIterative(digits)

    # O(4^n) time and O(4^n) space
    def letterCombinationsRecursive(self, digits):
        def letterCombinationsHelper(digits, associations, start, prefix, combinations):
            if start == len(digits):
                if len(prefix) != 0:
                    combinations.append("".join(prefix[:]))
                return
            
            digit = digits[start]
            buttons = associations[digit]
            
            for button in buttons:
                prefix.append(button)
                letterCombinationsHelper(digits, associations, start + 1, prefix, combinations)
                prefix.pop()
        
        associations = {
            "0": ["0"],
            "1": ["1"],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        start = 0
        prefix = []
        combinations = []
        letterCombinationsHelper(digits, associations, start, prefix, combinations)
        return combinations
    
    # O(4^n) time and O(4^n) space
    def letterCombinationsIterative(self, digits):
        combinations = [""] if len(digits) > 0 else []
        associations = {
            "0": ["0"],
            "1": ["1"],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
    
        for digit in digits:
            current = []
            for button in associations[digit]:
                for combination in combinations:
                    current.append(combination + button)
            combinations = current

        return combinations        