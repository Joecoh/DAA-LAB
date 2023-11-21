def is_subset_sum(arr, n, target_sum, subset=[]):
    if target_sum == 0:
        return True
    if n == 0 and target_sum != 0:
        return False

    # Exclude the last element and recur
    without_last = is_subset_sum(arr, n - 1, target_sum, subset)

    # Include the last element and recur
    with_last = is_subset_sum(arr, n - 1, target_sum - arr[n - 1], subset + [arr[n - 1]])

    return without_last or with_last

# Example usage:
arr = [3, 34, 4, 12, 5, 2]
target_sum = 9
subset_sum_result = is_subset_sum(arr, len(arr), target_sum)
print(f"Subset with sum {target_sum} exists: {subset_sum_result}")
