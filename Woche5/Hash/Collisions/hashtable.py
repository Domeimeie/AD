class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
    def append(self, key, value):
        node = HashItem(key, value)
        if self.tail:
            self.tail.next = node
            self.tail = node 
        else:
            self.head = node
            self.tail = node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None



class HashTable:
    def __init__(self):
        self.length = 0
        self.size = 8
        self.slots = [None for i in range(self.size)]
        for x in range(self.size) :
            self.slots[x] = SinglyLinkedList()

    def _hash(self, key):
        factor = 1
        hash_value = 0
        for character in key:
            hash_value += factor * ord(character)
            factor += 1
        return hash_value % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        hash_value = self._hash(key)
        self.slots[hash_value].append(key, value)
        self.length += 1

    def get(self, key):
        hash_value = self._hash(key)
        return self.slots[hash_value].search(key)

    def __len__(self):
        return self.length


if __name__ == '__main__':
    table = HashTable()
    table.put("dog", ("Fifi", 3, "brown"))
    assert len(table) == 1
    table.put("cat", ("Garfield", 12, "yellow"))
    table.put("bird", ("Polly", 50, "red"))
    table.put("snake", ("Python", 20, "green"))
    table.put("dog", ("DumDum", 7, "black"))
    table.put("ad", ("recursion", 3, "purple"))
    table.put("ga", ("iteration", 4, "pink"))

    for kind in ("dog", "cat", "bird", "snake", "ad", "ga", "dragon"):
        animal = table.get(kind)
        print(f"at key '{kind}' is animal {animal}")
