class DoubleHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def hash1(self, key):
        """Primary hash function."""
        return hash(key) % self.size

    def hash2(self, key):
        """Secondary hash function (must not return 0)."""
        # A common choice is (PRIME - (key % PRIME))
        # where PRIME is a prime smaller than the table size.
        # For simplicity with Python strings/objects, we'll use:
        return 1 + (hash(key) % (self.size - 1))

    def insert(self, key, value):
        if self.count >= self.size:
            raise Exception("Hash table overflow")

        h1 = self.hash1(key)
        h2 = self.hash2(key)
        
        index = h1
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            i += 1
            index = (h1 + i * h2) % self.size
            
            if i >= self.size:
                raise Exception("Could not find a slot for insertion")

        self.table[index] = (key, value)
        self.count += 1

    def get(self, key):
        h1 = self.hash1(key)
        h2 = self.hash2(key)
        
        index = h1
        i = 0
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
            index = (h1 + i * h2) % self.size
            if i >= self.size:
                break
        return None

    def __repr__(self):
        return str(self.table)

if __name__ == "__main__":
    print("--- Double Hashing Interactive Table ---")
    try:
        size = int(input("Enter the size of the hash table: "))
        ht = DoubleHash(size)
        
        while True:
            print("\n1. Insert  2. Get  3. Display Table  4. Exit")
            choice = input("Choose an option: ")
            
            if choice == '1':
                key = input("Enter key: ")
                val = input("Enter value: ")
                try:
                    ht.insert(key, val)
                    print(f"Inserted ('{key}', '{val}')")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == '2':
                key = input("Enter key to retrieve: ")
                result = ht.get(key)
                if result is not None:
                    print(f"Value for '{key}': {result}")
                else:
                    print(f"Key '{key}' not found.")
            elif choice == '3':
                print(f"Current Table: {ht}")
            elif choice == '4':
                break
            else:
                print("Invalid choice.")
    except ValueError:
        print("Please enter a valid integer for size.")
