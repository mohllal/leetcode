class Solution:
    # O(n) time and O(n) space - exculding the space for converting string into mutable type
    def reverseVowels(self, s: str) -> str:
        sAsArray = list(s)
        i = 0
        j = len(sAsArray) - 1

        vowels = {
            'a': True,
            'e': True,
            'i': True,
            'o': True,
            'u': True
        }

        while i < j:
            head = sAsArray[i].lower()
            tail = sAsArray[j].lower()
            
            if not head in vowels:
                i += 1
            elif not tail in vowels:
                j -= 1
            elif head in vowels and tail in vowels:
                sAsArray[i], sAsArray[j] = sAsArray[j], sAsArray[i]
                i += 1
                j -= 1
            else:
                i += 1
                j -= 1

        return ''.join(sAsArray)