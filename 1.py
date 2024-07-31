def round_robin_merge(lists):
    result = []
    max_len = max(len(lst) for lst in lists)
    
    for i in range(max_len):
        for lst in lists:
            if i < len(lst):
                result.append(lst[i])
    
    return result

# Example usage
lists = [[1, 2, 3], [4, 5], [6], [], [7, 8, 9]]
merged_list = round_robin_merge(lists)
print(merged_list)  # Output: [1, 4, 6, 7, 2, 5, 8, 3, 9]
