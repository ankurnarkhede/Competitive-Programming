def solution(arr):
    arr = sorted(arr)
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == 0:
            return arr[j]
        elif abs(arr[i]) > arr[j]:
            i += 1
        elif abs(arr[i]) < arr[j]:
            j -= 1
    return 0


print(solution([3, 2, -2, 5, -3]))
