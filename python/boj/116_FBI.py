import sys

sys.stdin = open("116_FBI.txt")

list_cname = []
for tc in range(1, 6):
    cname = input()

    if "FBI" in cname:    
        list_cname.append(tc)
    
if list_cname:
    # 이부분 생각 못함
    print(*list_cname)
else:
    print("HE GOT AWAY!")

