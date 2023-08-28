class HashTable:
    def __init__(self):
        self.MAX = 100
        self.data = [None for _ in range(self.MAX)]

    def getHash(self, key) -> int:
        hash = 0
        for ch in key:
            hash += ord(ch)
        hash %= self.MAX
        return hash

    def __setitem__(self, key, val) -> None:
        if not len(key):
            return
        hash = self.getHash(key)
        self.data[hash] = val

    def __getitem__(self, key) -> any:
        if not len(key):
            return
        hash = self.getHash(key)
        return self.data[hash]
    
    def print(self):
        for i in range(self.MAX):
            if self.data[i] is not None:
                print(str(i) + ' -> ' + str(self.data[i]))
    
if __name__ == '__main__':
    ht = HashTable()
    ht['March 12'] = 400
    ht['March 13'] = 700
    # ht.setItem('March 14', 4500)
    ht.print()
    print(ht['March 12'])
    print(ht['March 13'])