import sys

sys.stdin = open("50_베스트셀러.txt")

T = int(input())
dic = {}

for tc in range(1, T+1):
    n = input()
    if n not in dic:
        dic[n]=1 # 여기서 중요한게 없다면 1부터 시작해야 된다 안그러면 0개부터 세지기때문에
    else:
        dic[n]+=1 # 같은 책의 갯수를 더해 나가는 것이다.

book_list = []
num=max(dic.values())

for tc in dic:
    if num == dic[tc]:
        book_list.append(tc)
    a = sorted(book_list)
print(a[0])