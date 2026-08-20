class LRUCache:

    # O(n) -> can make it faster

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.lru = deque()
        

    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.remove(key)
            self.lru.append(key)
            return self.store[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.lru) >= self.capacity:
            if key in self.lru:
                self.lru.remove(key)
            else:
                self.lru.popleft()
        self.lru.append(key)
        self.store[key] = value

