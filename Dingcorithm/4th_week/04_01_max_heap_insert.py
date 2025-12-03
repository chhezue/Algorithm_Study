class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 1. 원소를 맨 끝에 추가
        self.items.append(value)
        cur_index = len(self.items) - 1 # 추가한 노드의 인덱스

        # 2. 원소 정렬
        while cur_index != 1: # 인덱스가 1이면 루트 노드라는 뜻이므로 비교 불가
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index # 현재 인덱스를 교체된 부모의 인덱스로 교체
            else:
                break

max_heap = MaxHeap()
max_heap.insert(3) # [None, 3]
max_heap.insert(4) # [None, 3, 4] -> [None, 4, 3]
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!