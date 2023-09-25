class Solution:
    def isValidIPAddressPart(self, part):
        return part and int(part) <= 255 and len(part) == len(str(int(part)))

    # O(1) time and O(1) space
    def restoreIpAddressesIterative(self, s):
        ipAddresses = []
    
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    firstPart = s[:i]
                    secondPart = s[i:i+j]
                    thirdPart = s[i+j:i+j+k]
                    fourthPart = s[i+j+k:]

                    if (
                        self.isValidIPAddressPart(firstPart) and
                        self.isValidIPAddressPart(secondPart) and
                        self.isValidIPAddressPart(thirdPart) and
                        self.isValidIPAddressPart(fourthPart)
                    ):
                        ipAddress = ".".join([firstPart, secondPart, thirdPart, fourthPart])
                        ipAddresses.append(ipAddress)                

        return ipAddresses

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restoreIpAddressesIterative(s)
