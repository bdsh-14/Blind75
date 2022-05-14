# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMin(nums):
    left, right = 0, len(nums)-1
    result = nums[0]

    while left <= right:
        mid = (left+right)//2
        result = min(result, nums[mid])

        # if the array is sorted then the left element is minimum
        if nums[left] < nums[right]:
            result = min(result, nums[left])
            break
        
        # left sorted portion
        if nums[left] <= nums[mid]:
            left = mid + 1 
            # if the left < mid , this means that mid is the pivot of the rotated array and elements to its right would be smaller than mid. 
        else:
            right = mid - 1

    return result
        
nums = [3,4,5,1,2]
print(findMin(nums))

nums1 = [11,13,15,17]
print(findMin(nums1))

nums2 = [4,5,6,7,0,1,2]
print(findMin(nums2))

nums3 = [4,5,1,2,3]
print(findMin(nums3))