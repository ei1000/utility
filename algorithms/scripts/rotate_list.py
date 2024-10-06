def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    len_nums = len(nums)
    pivot = k % len_nums

    temp = nums[-pivot:]
    nums[-pivot:] = []

    nums[:0] = temp

    return nums


