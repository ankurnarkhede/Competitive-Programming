# HackerEarth Sample hash problem
# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/


import sys

n=int(sys.stdin.readline().strip())

hash_dict={}

for i in range(0,n,+1):
    roll_no,name= (map (str, sys.stdin.readline ().strip ().split (' ')))
    hash_dict[roll_no]=name
    

q=int(sys.stdin.readline().strip())
for i in range(0,q,+1):
    print(hash_dict[sys.stdin.readline ().strip ()])
    
