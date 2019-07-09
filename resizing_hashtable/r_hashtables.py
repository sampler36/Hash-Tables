

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
     def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity
        # underlying data sructure
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = (( hash << 5) + hash) + ord(x)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    pass
    # index = hash(key, len(hash_table.storage))
    #     # create a new pair using key and value
    #     pair = Pair(key, value)

    #     stored_pair = hash_table.storage[index]

    #     if stored_pair is not None:
    #         if stored_pair.key != key:
    #             print(f"Warning: Overwriteing value {stored_pair.key} / {stored_pair.value} with {pair.key} / {pair.value}")
        
    #     # write the pair to the hash_table.storage at the index
    #     hash_table.storage[index] = pair 


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass
    #     # get the index via hash function
    # index = hash(key, len(hash_table.storage))
    # #   if storage at index is empty print ERROR
    # if (hash_table.storage[index] is None or hash_table.storage[index].key != key):
    #     print(f"Unable to retrieve key {key}")
    # else:
    #     hash_table.storage[index] = None



# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass
    #   # get the index via the hash function
    # index = hash(key, len(hash_table.storage))

    # # if the storage at index is empty or the key can not be found. print error
    # if (hash_table.storage[index] is None or hash_table.storage[index].key != key):
    #     print(f"Unable to retrieve entry with the key: {key}")
    #     return None
    # # return value at index in storage
    # return hash_table.storage[index].value


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
