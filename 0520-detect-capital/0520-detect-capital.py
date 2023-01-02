class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_upper_case = True
        all_lower_case = True
        first_upper_case = True
        
        for index in range(len(word)): 
            if word[index] >= 'a' and word[index] <= 'z':
                all_upper_case = False

            if word[index] >= 'A' and word[index] <= 'Z':
                all_lower_case = False
                
                if index >= 1:
                    first_upper_case = False
        
        return (
            all_upper_case or
            all_lower_case or
            first_upper_case
        )