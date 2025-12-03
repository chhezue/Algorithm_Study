def get_melon_best_album(genre_array, play_array):
    result = [] # 결괏값 4개
    count_dict = {}
    song_dict = {}

    for i in range(len(genre_array)):
        if genre_array[i] not in count_dict:
            count_dict[genre_array[i]] = play_array[i]
        else:
            count_dict[genre_array[i]] += play_array[i]

        if genre_array[i] not in song_dict:
            song_dict[genre_array[i]] = [(i, play_array[i])]
        else:
            song_dict[genre_array[i]] += [(i, play_array[i])]

    # sort: 원본 배열 변경, 리스트만 가능
    # sorted: 새로운 배열 반환, 모든 iterable 가능
    sorted_count_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True) # 총 재생 수 내림차순으로 정렬

    # 장르별 곡 목록 정렬
    # song_dict.items()는 (genre, [(index, plays), ...]) 형태의 2 튜플이므로 for문 내에서 다시 정렬해야 함.
    for genre, _ in sorted_count_dict:
        sorted_song_dict = sorted(song_dict[genre], key=lambda x: (-x[1], x[0])) # 재생 횟수 내림차순, 인덱스 오름차순으로 정렬
        for idx, _ in sorted_song_dict[:2]: # 정렬된 곡 목록에서 최대 2개의 곡을 가져옴.
            result.append(idx)

    return result

print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))