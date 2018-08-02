
# Little Monk and his toy-story
# https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/little-monk-and-his-toy-story/

# 4
# 40 100 20 30


import sys
import math

n= int (sys.stdin.readline ())

w = (list (map (int, sys.stdin.readline ().strip ().split (' '))))

w.sort()

total=0
count=0
i=0
while(i<=len(w) and total<=n):
    i+=(1)
    total+=i
    if(total<=n):
        count+=1
    # print("i={}, sum={}".format(i,total))

max_height=int(count)

print(max_height)