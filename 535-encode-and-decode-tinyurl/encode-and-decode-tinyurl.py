class Codec:

    def __init__(self): 
        self.urls = []

    def encode(self, longUrl: str) -> str:
        self.urls.append(longUrl) # append the url at the end of the list
        return 'http://tinyurl.com/' + str(len(self.urls) - 1) # and the addition number of the index of the url that we just added

    def decode(self, shortUrl: str) -> str:
        return self.urls[int(shortUrl.split('/')[-1])] #split the url at where ever there is a '/' and then make them into indivisual elements, then the [-1] helps us take the last element from that which was the index of the url, and return that from the list
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))