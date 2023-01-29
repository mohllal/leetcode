class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minimumFrequency = None
        self.keyFrequencies = {}
        self.frequencyKeys= defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.keyFrequencies:
            return -1
        
        frequency = self.keyFrequencies[key]
        value = self.frequencyKeys[frequency][key]
        
        del self.frequencyKeys[frequency][key]
        if not self.frequencyKeys[frequency]:
            if frequency == self.minimumFrequency:
                self.minimumFrequency += 1
            del self.frequencyKeys[frequency]
        
        self.keyFrequencies[key] = frequency + 1
        self.frequencyKeys[frequency + 1][key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
    
        if key in self.keyFrequencies:
            frequency = self.keyFrequencies[key]
            self.frequencyKeys[frequency][key] = value
            self.get(key)
            return

        if self.capacity == len(self.keyFrequencies):
            delkey, delval = self.frequencyKeys[self.minimumFrequency].popitem(last=False)
            del self.keyFrequencies[delkey]

        self.keyFrequencies[key] = 1
        self.frequencyKeys[1][key] = value
        self.minimumFrequency = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)