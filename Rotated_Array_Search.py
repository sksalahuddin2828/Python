def search_in_rotated_array(nums, target):
    n = len(nums)

    # Logic
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        # Two cases
        if nums[start] <= nums[mid]:
            # Left
            if target >= nums[start] and target <= nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            # Right
            if target >= nums[mid] and target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


nums = [4, 5, 6, 7, 0, 1, 2, 3]
target = int(input("Enter the target number: "))
print(search_in_rotated_array(nums, target))
