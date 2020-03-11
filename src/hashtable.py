# '''
# Linked List hash table key/value pair
# '''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Part 1: Hash collisions should be handled with an error warning.

        Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''

        # Get the Index by using the key
        index = self._hash_mod(key)

        # If the index doesn't exist, add it.
        if not self.storage[index]:
            self.storage[index] = Node(key, value)
        else:
            node = self.storage[index]

            while True:
                # If the node's key equals to the key passed in, change the node's new value
                if node.key == key:
                    node.value = value
                    break
                # If there's no next node, create a new node with the passed in key and value
                elif not node.next:
                    node.next = Node(key, value)
                    break
                # Loop through
                else:
                    node = node.next

        # if self.storage[index]is not None:
        #     print("ERROR: Key in Use")
        # else:
        #     self.storage[index] = value




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        # Get the index using the key
        index = self._hash_mod(key)

        # Get the node using the index
        node = self.storage[index]

        # If the node doesn't exist, print error message
        if not node:
            print("key not found")

        # Loop through to see if key exists, print error message if it doesn't
        while node.key != key:
            if not node.next:
                print("key not found")
                return
            node = node.next

        # Removes the value stored with the given key.
        node.value = None

        # index = self._hash_mod(key)
        #
        # if self.storage[index] is not None:
        #     self.storage[index] = None
        # else:
        #     print("Key Not Found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        # Get the index using the key
        index = self._hash_mod(key)

        # Get the node using the index
        node = self.storage[index]

        if not node:
            return None

        # Loop through to see if key exists
        while node.key != key:
            if not node.next:
                return None
            node = node.next

        # Returns the value if the key is found
        return node.value
        # index = self.storage[self._hash_mod(key)]
        #
        # return self.storage[index]
        #
        # index = self._hash_mod(key)
        #
        # return self.storage[index]


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        temp = self.storage[0:]
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        # Loop through the temporary storage
        for item in temp:
            node = item
            # Add each node into the storage
            while node:
                self.insert(node.key, node.value)
                node = node.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
