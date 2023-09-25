class Solution:
    def isValidIPAddressSegment(self, segment):
        return segment and int(segment) <= 255 and len(segment) == len(str(int(segment)))

    # O(1) time and O(1) space
    def restoreIpAddressesRecursive(self, string, start, currentIp, currentSegment, ipAddresses):
        if currentSegment == 4:
            if start == len(string):
                ipAddresses.append(currentIp)
            return

        for i in range(1, min(4, len(string) - start + 1)):
            segment = string[start:start+i]
            
            if self.isValidIPAddressSegment(segment):
                newIp = currentIp + segment if currentSegment == 3 else currentIp + segment + '.'
                self.restoreIpAddressesRecursive(string, start + i, newIp, currentSegment + 1, ipAddresses)

        return ipAddresses

    # O(1) time and O(1) space
    def restoreIpAddressesIterative(self, s):
        ipAddresses = []
    
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    firstSegment = s[:i]
                    secondSegment = s[i:i+j]
                    thirdSegment = s[i+j:i+j+k]
                    fourthSegment = s[i+j+k:]

                    if (
                        self.isValidIPAddressSegment(firstSegment) and
                        self.isValidIPAddressSegment(secondSegment) and
                        self.isValidIPAddressSegment(thirdSegment) and
                        self.isValidIPAddressSegment(fourthSegment)
                    ):
                        ipAddress = ".".join([
                            firstSegment,
                            secondSegment,
                            thirdSegment,
                            fourthSegment
                        ])
                        ipAddresses.append(ipAddress)                

        return ipAddresses

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restoreIpAddressesRecursive(s, 0, '', 0, [])
