import sys

sys.stdin = open("106_꼬리를 무는 숫자 나열.txt")

n, m = map(int,input().split())

n -= 1
m -= 1
print( abs ( n // 4 - m // 4 ) + abs ( n % 4 - m % 4 ) )

# def list_chunk(lst, n):
#     return [lst[i:i+n] for i in range(0, len(lst), n)]
# list_c = list(range(1, 37))
# list_chunked = list_chunk(list_c, 4)


# for i in range(len(list_chunked)):            
#     for j in range(len(list_chunked[i])):
#         if list_chunked[i][j] == n:
#             print(i, j+1)
#         elif list_chunked[i][j] == m:
#             print(i, j+1)




