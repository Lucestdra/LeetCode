def find_median_sorted_arrays(nums1, nums2):
    """
    Find the median of two sorted arrays.
    
    :param nums1: List of integers, first sorted array
    :param nums2: List of integers, second sorted array
    :return: Median of the two sorted arrays
    """
    nums = sorted(nums1 + nums2)  # Combine and sort the two arrays
    length = len(nums)  # Get the total length of the combined array

    if length % 2 == 0:
        # If the length is even, return the average of the two middle elements
        return (nums[length // 2 - 1] + nums[length // 2]) / 2
    else:
        # If the length is odd, return the middle element
        return nums[length // 2]

# Example usage
nums1 = [1, 3]
nums2 = [2]

print(find_median_sorted_arrays(nums1, nums2))  # Output should be 2.0
