class MyHashSet(object):

    def __init__(self):
        self.data = [False] * ((10**6) + 1) 

    # used add rather than put
    def add(self, key):
        self.data[key] = True

    def remove(self, key):
        self.data[key] = False

    def contains(self, key):
        return self.data[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)