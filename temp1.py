from sys import maxsize


def maxSubArraySum(a, size,x):
    max_so_far = -maxsize - 1
    max_ending_here = 0

    for i in range (0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here > x:
            max_ending_here = 0
    return max_so_far


# Driver function to check the above function
a = [1,2,3,4]
x=8
print("Maximum contiguous sum is", maxSubArraySum (a, len (a),k))