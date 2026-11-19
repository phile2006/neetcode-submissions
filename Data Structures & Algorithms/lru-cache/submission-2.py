class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {} 
        self.order = []

    def get(self, key: int) -> int:
        if key in self.order:
            self.order.remove(key)
            self.order.append(key) # so its to the right
            return self.dic[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if len(self.order) >= self.cap:
            if key in self.order:
                self.order.remove(key)
                self.order.append(key)
                self.dic[key] = value
            else:
                self.order.pop(0)
                self.order.append(key)
                self.dic[key] = value
        else:
            if key in self.order:
                self.dic[key] = value
            else:
                self.order.append(key)
                self.dic[key] = value

