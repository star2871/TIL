import sys

sys.stdin = open("66_암기왕.txt")

t = int(input())
for k in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    isIn = list(map(int, input().split()))

    arr = sorted(arr)
    for i in isIn:
        s = 0
        e = n - 1
        flag = True
        while s <= e:
            mid = (s + e) // 2
            if arr[mid] == i:
                print(1)
                flag = False
                break
            elif arr[mid] < i:
                s = mid + 1
            else:
                e = mid - 1
        if flag:
            print(0)
