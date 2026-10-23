class MyHashMap(object):

    def __init__(self):
        # given in ther question
        self.data = [-1] * ((10**6) + 1)

    # insert 
    def put(self, key, value):
        self.data[key] = value

    # ask 
    def get(self, key):
        return self.data[key]

    # remove, and back to default
    def remove(self, key):
        self.data[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)