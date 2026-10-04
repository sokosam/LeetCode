class TimeMap:

    def __init__(self):
        self.max_ts = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.max_ts[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        if self.max_ts.get(key, None) is None:
            return ""
        

        vals = self.max_ts[key]
        index = bisect_right(vals, timestamp, key = lambda x : x[0])

        if index == 0:
            return ""
        else:
            return vals[index - 1][1]

        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)