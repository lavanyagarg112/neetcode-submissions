class TimeMap:

    def __init__(self):
        self.pair = {}
        self.times = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.pair:
            self.pair[key] = {}
        self.pair[key][timestamp] = value

        if key not in self.times:
            self.times[key] = set()

        self.times[key].add(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.pair:
            return ""

        if timestamp in self.times[key]:
            return self.pair[key][timestamp]

        curr_timestamp = float('-inf')
        for t in self.times[key]:
            if t < timestamp and t > curr_timestamp:
                curr_timestamp = t
        
        if curr_timestamp == float('-inf'):
            return ""

        return self.pair[key][curr_timestamp]

        

        
