nums = [0, 1, 0, 3, 12]

lastNonZeroIdx = 0

for idx in range(len(nums)):
    if nums[idx] != 0:
        nums[lastNonZeroIdx] = nums[idx]
        lastNonZeroIdx += 1

for idx in range(lastNonZeroIdx, len(nums)):
    nums[idx] = 0

print(nums)