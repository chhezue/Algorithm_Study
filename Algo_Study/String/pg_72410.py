def solution(new_id):
    answer = new_id

    # 1단계
    answer = answer.lower()

    # 2단계
    valid_char = ['-', '_', '.']
    filtered = ""
    for char in answer:
        if char.isalpha() or char.isdigit() or char in valid_char:
            filtered += char
    answer = filtered

    # 3단계
    while ".." in answer:
        answer = answer.replace("..", ".")

    # 4단계
    answer = answer.strip(".")

    # 5단계
    if len(answer) == 0:
        answer = "a"

    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
    answer = answer.strip(".")

    # 7단계
    while len(answer) < 3:
        answer += answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))