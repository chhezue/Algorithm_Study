input = "abcba"

def is_palindrome(string):
    # 문자열의 길이가 1인 경우에는 무조건 True
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

print(is_palindrome(input))