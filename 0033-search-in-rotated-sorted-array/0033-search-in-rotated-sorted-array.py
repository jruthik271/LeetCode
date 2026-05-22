class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[low] <= nums[mid]:

                # Target lies inside left sorted half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Right half is sorted
            else:

                # Target lies inside right sorted half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1