class LinkedTuple:
    def __init__(self):
        self.item = []

    def add(self, key, value):
        self.item.append((key, value)) # [("채연", 1)] -> [("지양", 2)] 튜플 형태로 삽입

    def get(self, key):
        for k, v in self.item:
            if k == key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple()) # [LinkedTuple(), ..., LinkedTuple()]

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value) # index번째의 LinkedTuple [(key, value)]
        # 똑같은 자리에 add 된다면 [(key, value), (key2, value2)]

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

my_dict = LinkedDict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!