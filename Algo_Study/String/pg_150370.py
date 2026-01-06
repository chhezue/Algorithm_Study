def solution(today, terms, privacies):
    answer = []
    term_dic = {}

    today_year, today_month, today_day = map(int, today.split("."))
    today_day_num = (today_year * 12 + today_month) * 28 + today_day # 주어진 연/월/일을 일 기준으로 변경

    for term in terms:
        term_a, term_b = term.split(" ")
        term_dic[term_a] = int(term_b)

    for i, privacy in enumerate(privacies, start=1):
        privacy_date, privacy_term = privacy.split(" ")
        privacy_year, privacy_month, privacy_day = map(int, privacy_date.split("."))
        privacy_day_num = (privacy_year * 12 + privacy_month) * 28 + privacy_day # 주어진 연/월/일을 일 기준으로 변경
        term_day = term_dic[privacy_term] * 28

        # print(today_day_num, privacy_day_num)
        # print("현재 날짜와 만료일의 차이:", today_day_num - privacy_day_num)
        # print("만료일 기준 날짜:", term_day)

        if today_day_num - privacy_day_num >= term_day:
            answer.append(i)

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution(	"2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))