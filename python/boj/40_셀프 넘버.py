def d(n):
    x = 0
    num = list(str(n))
    
    for i in num:
        x += int(i)

    return n + x

total_set = set()

# 생성자가 있는 숫자 모두 추가
for j in range(1, 10000):
    total_set.add(d(j))

# 전체 set에서 생성자가 있는 숫자를 빼는 차집합 이용
ans_set = set(range(1, 10000)) - total_set

# 셀프 넘버 오름차순 정렬 후 한줄에 하나씩 출력
for k in sorted(ans_set, reverse=False):
    print(k)