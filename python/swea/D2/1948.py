import sys

sys.stdin = open("1948.txt")
cal = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for tc in range(int(input())):
    m1,d1,m2,d2 = map(int, input().split())
    print("#{}".format(tc+1), end=" ")
    if m1 == m2:
        # 어차피 문제 조건에 첫번째 날보다 두번째 날이 항상 크다고 했으니, d1d2가 같을때는 고려하지 않아도 된
        print(d2-d1+1)
    else:
        result = d2
        for i in range(m1+1,m2):
            result += cal[i]
        print(result + cal[m1]-d1+1)
