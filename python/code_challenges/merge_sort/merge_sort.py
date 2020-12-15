def merge_sort(the_list):
    """
    In-place merge sort method
    """
    length = len(the_list)
    if length > 1:
        mid = length // 2
        left = the_list[0:mid]
        right = the_list[mid:]

        merge_sort(left)

        merge_sort(right)

        merge(left, right, the_list)


def merge(left, right, the_list):
    # left iterator
    l = 0

    # right iterator
    r = 0

    # main iterator
    i = 0

    # we have more entries in both the left and also the right half
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            the_list[i] = left[l]
            l += 1
        else:
            the_list[i] = right[r]
            r += 1

        i += 1

    # we've reached the end of (at least) one half, so lets bring in the
    # remaining values from the other half (if any)
    if l == len(left):
        while r < len(right):
            the_list[i] = right[r]
            r += 1
            i += 1
    else:
        while l < len(left):
            the_list[i] = left[l]
            l += 1
            i += 1
