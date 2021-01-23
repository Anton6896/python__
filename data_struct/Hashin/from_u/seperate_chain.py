"""
hashtable with separate chaining approach 
"""


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.hash = hash(key)  # <- gey key hash

    # objects with different keys will have diferent hashes
    # in case of collision check the keys
    def equals(self, other) -> bool:
        if self.hash != other.hash:
            return False

        return (self.key == other.key)

    def __str__(self):
        return "entry : " + str(self.value)


class HashTable_my:
    def __init__(self, capasity_=3, load_factor_=0.75):
        self.capasity = capasity_
        self.load_factor = load_factor_
        # fill all with None value
        self.table_list = [None for x in range(capasity_)]
        self.threshold = (capasity_ * load_factor_)
        self.size = 0

    def size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def normalize_index(self, key_hash) -> int:
        # get index that in range of max capasity
        return abs(key_hash) % self.capasity

    def clear(self):
        self.table_list = [None for x in range(self.capasity)]
        self.size = 0

    def has_key(self, key):
        bucket_index = self.normalize_index(hash(key))
        return self.table_list[bucket_index] is not None

    def insert(self, key, value):
        e = Entry(key, value)
        bucket_index = self.normalize_index(e.hash)
        return bucket_insert_entry(bucket_index, e)

    def bucket_insert_entry(index, entry):
        bucket = self.table_list[index]


<<<<<<< HEAD
# if "__main__" == __name__:
#     pass
=======
if "__main__" == __name__:
    pass
>>>>>>> baf7f44370184c85209ad94358036bc8977f2258
