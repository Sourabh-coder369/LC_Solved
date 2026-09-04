class MyHashMap:
    def __init__(self):
        self.arr=[-1 for i in range(10**6+2)]

    def put(self, key: int, value: int) -> None:
        idx=key%len(self.arr)
        self.arr[idx]=value

        return self.arr[idx]

    def get(self, key: int) -> int:
        idx=key%len(self.arr)
        if(self.arr[idx]==-1):
            return -1
        
        return self.arr[idx]

    def remove(self, key: int) -> None:
        idx=key%len(self.arr)
        self.arr[idx]=-1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)