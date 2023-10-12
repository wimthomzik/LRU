# LRU
LRU cache implementation using Queue and Hashing.

This implementation of a LRU cache implicates a cache in form of a dictionary and a queue in form as a list. The queue holds the key values of the dictionary and keeps it in "usage order" (everytime a key/value pair gets changed or added it moves to the front of the queue). If a key/value pair gets added and the cache is full, the last recently used pair, the one at the end of the queue, gets deleted.

The dictionary is a commonly used data structure for a cache, because it pairs a key with a value, as a cache pairs a 
tag with a value. To keep track of "usage-order" this project uses a list to implement a queue. This keeps the logic simple and easy to understand.



