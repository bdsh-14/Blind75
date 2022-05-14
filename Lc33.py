# https://leetcode.com/problems/search-in-rotated-sorted-array/

def searchInSortedArray(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid
        
        # left sorted portion
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        else:
            # right sorted portion
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
    return -1

nums = [4,5,6,7,0,1,2]
print(searchInSortedArray(nums, 0))