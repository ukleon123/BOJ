from sys import stdin

if __name__ == "__main__":
    data = []
    N = int(stdin.readline())
    M = int(stdin.readline())

    for _ in range(M):
        data.append(tuple(map(int, stdin.readline().split())))
    
    
# 1개가 참여하고 0개의 관계가 정해진 경우 => 1
# 2개가 참여하고 0개의 관계가 정해진 경우 => 2
# 2개가 참여하고 1개의 관계가 정해진 경우 => 1
# 3개가 참여하고 0개의 관계가 정해진 경우 => 6
# 3개가 참여하고 1개의 관계가 정해진 경우 => 3
# 3개가 참여하고 2개의 관계가 정해진 경우 => 2
# 3개가 참여하고 3개의 관계가 정해진 경우 => 1
# 4개가 참여하고 0개의 관계가 정해진 경우 => 24
# 4개가 참여하고 1개의 관계가 정해진 경우 => 12 
# 4개가 참여하고 2개의 관계가 정해진 경우 => 16 4 + 6 + 8
# 4개가 참여하고 3개의 관계가 정해진 경우 => 10 1 + 2 + 3 + 4 
# 4개가 참여하고 4개의 관계가 정해진 경우 => 3
# 4개가 참여하고 5개의 관계가 정해진 경우 => 2
# 4개가 참여하고 6개의 관계가 정해진 걍우 => 1
# 관계가 0인 경우 n! 1인 경우는 n! / 2 2인 경우 1개에 동시에 연결된 경우 => n! / 3 따로 연결된 경우 => n! / 4
