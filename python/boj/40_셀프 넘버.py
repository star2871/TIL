# # 1. 문자열을 이용한 함수 정의 방법
# def d(n):
#     x = 0
#     num = list(str(n))
    
#     for i in num:
#         x += int(i)

#     return n + x

# total_set = set()

# # 생성자가 있는 숫자 모두 추가
# for j in range(1, 10000):
#     total_set.add(d(j))

# # 전체 set에서 생성자가 있는 숫자를 빼는 차집합 이용
# ans_set = set(range(1, 10000)) - total_set

# # 셀프 넘버 오름차순 정렬 후 한줄에 하나씩 출력
# for k in sorted(ans_set, reverse=False):
#     print(k)

# 2. 한자리수, 두자리수, 세자리수, 네자리수 별로 조건문사용

array = [False] * 10036 #9999 일때의 경우의 수를 고려해 10036까지 배열 설정

for i in range(1, 10001):
    if i < 10: #한자리수일때
        array[i + i] = True #각자리수의 합+전체수를 True로 변경
    elif i < 100: #두자리 수일때
        array[i + (i // 10) + (i % 10)] = True #각자리수의 합+전체수를 True로 변경
    elif i < 1000: #세자리 수일때
        array[i + (i // 100) + (i % 100 // 10) + (i % 100 % 10)] = True #각자리수의 합+전체수를 True로 변경
    elif i < 10000: #네자리 수일때
        array[i + (i // 1000) + (i % 1000 // 100) + (i % 1000 % 100 // 10) + (i % 1000 % 100 % 10)] = True #각자리수의 합+전체수를 True로 변경

for i in range(1, 10001):
    if array[i] == False: #True가 아닌것들은 생성자가 없는 수들이기 때문에 False만 출력
        print(i)
