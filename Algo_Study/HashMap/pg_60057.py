def solution(s):
    answer = float('inf')

    # i 단위로 압축한다. 범위는 n/2까지 (반 이상으로는 2 덩어리로도 압축할 수 없음.)
    for i in range(1, len(s) // 2 + 1):
        zip_arr = []
        zip_str = ""

        for j in range(0, len(s), i):
            item = s[j:j+i]
            zip_arr.append(item)

        prev = ""
        count = 1

        for k in range(len(zip_arr)):
            if prev != zip_arr[k]:
                if count > 1:
                    zip_str += str(count) + prev
                else:
                    zip_str += prev
                count = 1
            else:
                count += 1
            prev = zip_arr[k]

        # for문 끝난 뒤
        if count > 1:
            zip_str += str(count) + prev
        else:
            zip_str += prev

        answer = min(answer, len(zip_str))

    return answer