from calendar import c
import sys

sys.stdin = open("42_세로읽기.txt")


data = [[0]*15 for i in range(5)]

for i in range(5) :
  s = list(input())
  for j in range(len(s)) :
    data[i][j] = s[j]

for i in range(15) :
  for j in range(5) :
    if data[j][i] != 0 :
      print(data[j][i], end='')
    else :
      continue