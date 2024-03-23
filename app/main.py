class Dictionary:
    def __init__(self) -> None:
        self.length = 0
        self.hash_table: list = [None] * 8
        self.load_factor = 2 / 3

    def __len__(self) -> int:
        return self.length

    def __setitem__(self, key: any, value: any) -> None:
        _hash = hash(key)
        cell = _hash % len(self.hash_table)
        while 1:
            if not self.hash_table[cell]:
                if self.check_if_resize_is_required():
                    cell = _hash % len(self.hash_table)
                    continue
                self.length += 1
                self.hash_table[cell] = (key, _hash, value)
                break
            elif self.hash_table[cell][0] == key:
                self.hash_table[cell] = (key, _hash, value)
                break
            cell = (cell + 1) % len(self.hash_table)

    def __getitem__(self, item: any) -> any:
        cell = hash(item) % len(self.hash_table)
        checked = 0
        while checked < len(self):
            if self.hash_table[cell] and self.hash_table[cell][0] == item:
                return self.hash_table[cell][2]
            cell = (cell + 1) % len(self.hash_table)
            checked += 1
        raise KeyError

    def resize(self) -> None:
        old_table = self.hash_table
        self.hash_table = [None] * len(self.hash_table) * 2
        self.length = 0
        [self.__setitem__(cell[0], cell[2]) for cell in old_table if cell]

    def check_if_resize_is_required(self) -> bool:
        if self.length + 1 > self.load_factor * len(self.hash_table):
            self.resize()
            return True
        return False
