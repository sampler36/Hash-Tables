

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity
        # underlying data sructure
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = (( hash << 5) + hash) + ord(x)
    return hash % max

    


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # # hash_table.append((key, value))
    # hash_key = hashing_func(key)
    # hash_table[hash_key] = value 
    # get index via hash function
    index = hash(key, len(hash_table.storage))
    # create a new pair using key and value
    pair = Pair(key, value)

    stored_pair = hash_table.storage[index]

    if stored_pair is not None:
        if stored_pair.key != key:
            print(f"Warning: Overwriteing value {stored_pair.key} / {stored_pair.value} with {pair.key} / {pair.value}")
    
    # write the pair to the hash_table.storage at the index
    hash_table.storage[index] = pair 


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # get the index via hash function
      index = hash(key, len(hash_table.storage))
    #   if storage at index is empty print ERROR
    if (hash_table.storage[index] is None or hash_table.storage[index].key != key):
        print(f"Unable to retrieve key {key}")
    else:
        hash_table.storage[index] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
     # get the index via the hash function
    index = hash(key, len(hash_table.storage))

    # if the storage at index is empty or the key can not be found. print error
    if (hash_table.storage[index] is None or hash_table.storage[index].key != key):
        print(f"Unable to retrieve entry with the key: {key}")
        return None
    # return value at index in storage
    return hash_table.storage[index].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()

