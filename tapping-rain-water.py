# Source: GFG
def findWater(arr, n):

    left = [0]*n

    right = [0]*n

    # Initialize result
    water = 0

    # Fill left array
    left[0] = arr[0]
    for i in range( 1, n):
        left[i] = max(left[i-1], arr[i])

    # Fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);

    # Calculate the accumulated water element by element
    # consider the amount of water on i'th bar, the
    # amount of water accumulated on this particular
    # bar will be equal to min(left[i], right[i]) - arr[i] .
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water

arr = [5,2,0,2,3,2]
n = len(arr)
print("Maximum water that can be accumulated is", findWater(arr, n))
