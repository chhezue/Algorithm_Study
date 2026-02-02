INT_MIN = -2 ** 31
INT_MAX = 2 ** 31 - 1

class Solution:
    def myAtoi(self, s: str) -> int:
        new_str = s.strip() # 문자열 앞뒤 공백 모두 제거
        operations = ""

        # 문자열을 처리한 결과, 숫자로 변환할 수 있는 문자가 하나도 없다면 0 반환
        if new_str == "":
            return 0

        # 첫 문자에서 부호가 있으면, 그 후보가 결과 숫자의 부호가 된다.
        if new_str[0] == "-":
            operations += "-"
            new_str = new_str[1:]
        elif new_str[0] == "+":
            operations += "+"
            new_str = new_str[1:]

        # 숫자로 해석할 수 있을 때까지 읽기
        num_only_str = ""
        while new_str:
            if new_str[0].isdigit():
                num_only_str += new_str[0]
                new_str = new_str[1:]
            else:
                break

        if num_only_str == "":
            return 0

        num = int(num_only_str)
        if operations == "-":
            num *= -1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num