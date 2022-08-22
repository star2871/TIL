import sys

sys.stdin = open("1983.txt")

T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T+1):
    n, m = map(int,input().split())
    total_list = []
    for i in range(n):
        mid, final, hws = map(int, input().split())
        total = 0.35*mid + 0.45*final + 0.2*hws
        total_list.append(total)

    k_score  = total_list[m-1]

    total_list.sort(reverse=True)

    div = n//10
    final_k_score = total_list.index(k_score) // div

    print(f'#{tc} {grades[final_k_score]}')