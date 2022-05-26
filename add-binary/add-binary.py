class Solution:
    # O(1) time and O(1) space
    def add(self, x: int, y: int, z: int):
        arr = [x, y, z]
        ones = arr.count(1)
        
        if ones == 0:
            return 0, 0
        elif ones == 1:
            return 1, 0
        elif ones == 2:
            return 0, 1
        else:
            return 1, 1

    # O(n) time and O(n) space
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        
        result = ''
        carry = 0

        while i >= 0 or j >= 0:
            aBit = int(a[i]) if i >= 0 else 0
            bBit = int(b[j]) if j >= 0 else 0

            bit, carry = self.add(aBit, bBit, carry)

            result = str(bit) + result
            i -= 1
            j -= 1

        return result if carry == 0 else str(carry) + result