def equilibriumPoint(arr):
    lsum = 0
    rsum = 0
    for i in range(0, len(nums) - 1):
        rsum += nums[i]
    for j in range(0, len(nums) - 1):
        rsum = rsum - nums[j]
        if (rsum == lsum):
            return (j + 1)
        lsum += nums[j]
    return(-1)


# Sample Input
arr = [-7, 1, 5, 2, -4, 3, 0]

# Function call
print(equilibriumPoint(arr))