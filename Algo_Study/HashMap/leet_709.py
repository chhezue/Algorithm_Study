class MyHashMap:
    def __init__(self):
        self.items = [[] for _ in range(8)] # 버킷 개수가 8인 해시 테이블 생성

    def put(self, key: int, value: int) -> None:
        index = hash(key) % len(self.items)
        bucket = self.items[index]

        # 이미 같은 key의 값이 있다면 덮어쓰기
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                print(f"({key}, {value}) 덮어쓰기: {self.items}")
                return

        bucket.append((key, value))
        print(f"({key}, {value}) 삽입: {self.items}")
        return

    def get(self, key: int) -> int:
        index = hash(key) % len(self.items)
        bucket = self.items[index]
        for k, v in bucket:
            if k == key:
                print(f"{key}에 해당하는 값 반환: {v}")
                return v
        return -1

    def remove(self, key: int) -> None:
        index = hash(key) % len(self.items)
        bucket = self.items[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i] # 인덱스(i)에 해당하는 값 (key, value) 삭제
                print(f"({key}에 해당하는 값 삭제: {self.items}")
                return