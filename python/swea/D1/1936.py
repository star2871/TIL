import sys
sys.stdin = open("1936.txt", "r")


n = list(map(str,input().split()))




# 가위(1)은 보(3)을 이기고 바위(2)는 가위(1)을 이기고 보(3)는 바위(2)를 이긴다.
if n[0] == '1' and n[1] == '3':
    print('A')
elif n[0] == '2' and n[1] == '1':
    print('A')
elif n[0] == '3' and n[1] == '2':
    print('A')
elif n[0] == n[1]:
    print('')    
else:
    print('B')



