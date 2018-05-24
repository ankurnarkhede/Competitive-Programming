from sys import stdin
line_index = -1
lines = stdin.readlines ()

def get_line():
    global lines, line_index
    line_index += 1
    return lines[line_index]

def binary_search(arr, val):
    low = 0
    high = len (arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > val:
            high = mid
    else:
        low = mid + 1
    if arr[low] > val:
        return arr[low]
    return -1

def generate_smallest(arr):
    stack = [arr[0]]
    for i in range (1, len (arr)):
        val = arr[i]
        if val < stack[-1]:
            stack.append (val)
        else:
            stack.append (stack[-1])
    return stack

def get_ans(army, stack):
    if not stack:
        return "NO"
    elem = stack[-1]
    for i in range (1, len (army)):
    elem = binary_search (army[i], elem)
    if elem == -1:
    return "NO"
    return "YES"

def main():
    n = int (get_line ())
    army = []
    for _ in range (n):
    row = [int (x) for x in get_line ().split ()[1:]]
    army.append (row)
    q = int (get_line ())
    stack = generate_smallest (army[0])
    for _ in range (q):
    query = [int (x) for x in get_line ().split ()]
    if query[0] == 1:
    row, val = query[1:]
    row -= 1
    army[row].append (val)
    if row == 0:
    if val < stack[-1]:
    stack.append (val)
    else:
    stack.append (stack[-1])
    elif query[0] == 0:
    row = query[1]
    row -= 1
    army[row].pop ()
    if row == 0:
    stack.pop ()
    else:
    print (get_ans (army, stack))


main ()