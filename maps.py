class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def _get_hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))

# Example Usage
h = HashMap()
h.add('Bob', '567-8888')
h.add('Alice', '293-6753')
h.add('Mikey', '293-1456')
h.print()  # Example output: [['Bob', '567-8888'], ['Alice', '293-6753'], ['Mikey', '293-1456']]
print(h.get('Alice'))  # Output: 293-6753
h.delete('Bob')
h.print()  # Example output: [['Alice', '293-6753'], ['Mikey', '293-1456']]