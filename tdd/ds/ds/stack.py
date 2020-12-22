class Stack:
    def __init__(self):
        # internal storage of data structure
        # using a _ to mark it as private data
        self._storage = []

    def __len__(self):
        return len(self._storage)

    def push(self, item):
        self._storage.append(item)