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

    def delete(self):
        # 1. 루트 노드와 맨 끝 노드의 위치를 바꾼다.
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop() # 반환할 최댓값 노드

        # 2. 바뀐 루트 노드를 자식들과 비교하여 정렬
        cur_index = 1

        while cur_index <= len(self.items) - 1: # 트리의 끝까지 순회
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index # 초기화

            # 왼쪽 자식 노드, 오른쪽 자식 노드 중에 큰 것을 현재 노드와 swap
            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index
            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index
            if max_index == cur_index: # 이미 정렬되어 있는 경우
                break

            self.items[max_index], self.items[cur_index] = self.items[cur_index], self.items[max_index]
            cur_index = max_index # 현재 인덱스 업데이트해서 while문 계속 시행

        return prev_max

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]