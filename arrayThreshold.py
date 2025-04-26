# T: O(n * log(max(arr) / precision)), S: O(1)
def findThreshold(arr, desiredSum):
    left, right = 0, max(arr)
    precision = 1e-5  # fine enough precision for floating values

    while right - left > precision:
        mid = (left + right) / 2
        current_sum = sum(min(x, mid) for x in arr)

        if current_sum < desiredSum:
            left = mid
        else:
            right = mid

    return round((left + right) / 2, 2)  # Round to 2 decimal places as per examples
