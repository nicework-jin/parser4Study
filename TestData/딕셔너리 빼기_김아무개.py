"""
https://programmers.co.kr/learn/courses/30/lessons/42579


테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
"""

from collections import defaultdict


def solution(genres, plays):
    # 장르별 총 플레이 횟수 (내림차순)
    genre_total_play_dict = defaultdict(int)
    for genre, play in zip(genres, plays):
        genre_total_play_dict[genre] += play
    genre_rank = sorted(genre_total_play_dict.items(), key=lambda x: -x[1])

    # 장르 내 플레이 횟수 (플레이횟수: 내림차순,  고유번호: 오름차순)
    rank_in_genre_dict = defaultdict(list)
    for idx, genre_play_pair in enumerate(zip(genres, plays)):
        rank_in_genre_dict[genre_play_pair[0]].append((idx, genre_play_pair[1]))

    # 장르별 두 개씩 선출
    ans = []
    for genre, _ in genre_rank:
        top2_in_genre = sorted(rank_in_genre_dict[genre], key=lambda x: (-x[1], x[0]))[:2]
        ans.extend(map(lambda x: x[0], top2_in_genre))
    return ans


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))