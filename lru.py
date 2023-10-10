#Create Class LRUCache
class LRUCache():

    def __init__(self, size):
        self.queue = [] #queue as list
        self.cache = {} #cache as dic
        self.capacity = size #capacity Cache

    #refer function
    def refer(self, input):
        #input is not in cache
        if input not in self.cache.keys():
            #queue is full
            if len(self.queue) == self.capacity:
                #remove item from cache and queue, that is last in queue
                self.cache.pop(self.queue[-1])
                self.queue.pop()
        #input is in cache
        else:
            #remove input from queue
            self.queue.remove(input)

        #add input to cache and queue in front
        self.queue.insert(0, input)
        self.map[input] = 0

    
    #display function
    def display(self):
        print(self.queue)
        print(self.map)

#initiate cache
lru_cache = LRUCache(4)

#test
lru_cache.refer(3)
lru_cache.refer(2)
lru_cache.refer(4)
lru_cache.refer(5)
lru_cache.refer(6)
lru_cache.refer(6)
lru_cache.refer(6)
lru_cache.display()