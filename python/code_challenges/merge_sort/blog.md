# Merge Sorting

We've just finsished up with insertion sorting, so let's dive into merge sorting.

The advantage of merge sorting is that we don't need to iterate through our sorted list every single time we want to deal with a new unsorted element, like with insertion sorting. Instead we can sort smaller chunks of a list recursively, and as those recursively calls are resolved we end up with a sorted list! This is much faster sorting, but it does come at a cost. Because we are sorting recursively we will be making copies of the list in the stack. Anyways, onto the algorithm!

---

Let's take an example list:

```python
[ 4, 1, 3, 2 ]
```

The expected outcome is:

```python
[ 1, 2, 3, 4 ]
```

First we need to split the original array into halves:

```python
[ 4, 1 ]
# and
[ 3, 2 ]
```

 We then further break each half into halves:

```python
[4]
[1]
[3]
[2]
```

At this point, each list only has one element in it, so by definition they are each a sorted list.

Now we start the merging process, but recal this is done recursively, so we'll merge 4 and 1, and separately 3 and 2, then re result of each can be merged for our final result.

There are three main steps.

1. set up a left, right, and main iterator. Each corresponds to a left half, right half, and main list.
1. If we have elements to be sorted on both halves, then compare them, set the main list at our current location to be the lower of these two values. Increment the iterator for the main list and also the corresponding half.
1. If we have run out of elements to be sorted on **either** half, then loop through the remaining elements on the other half, and set the main list at our current location to that value. Increment the iterator for the main list and the corresponding half.

And that's it!

Psuedo stepthrough:

1. we pass in [4, 1] as the main array. 4 < 1 is False, so arr[0] <- 1, increment right, increment main
1. the right half is out of elements, so replace the remaining main elements with the remaining left elements: arr[1] <- 4
1. We resolved the [4,1] left half, now lets resolve the [3, 2] right half
1. We pass in [3, 2] as the main array, 3 < 2 is False, so arr[0] <- 2, increment right, increment main
1. the right half is out of elements, so replace the remaining main elements with the remaining left elements: arr[1] <- 3
1. We resolved the [3,2] right half, now lets resolve the merge of [1,4] with [2,3]
1. 1 <= 2 is True, so arr[0] <- 1, increment left and main
1. 4 <= 2 is False, so arr[1] <- 2, increment right and main
1. 4 <= 3 is Falsse, so arr[2] <- 3, increment right and main
1. right is out of elements, lets set the remaining main elements as the value of the remaning left elements
1. while left iterator < length of left arr....
   1. main arr at main iterator position is set to value at left arr at the left iterator
   1. increment both main and left iterator to keep track of where we are on both

Output:

```python
[ 1, 2, 3, 4 ]
```

---
Python code:

```python
def merge_sort(the_list):
    """
    In-place merge sort method
    """
    length = len(the_list)
    if length > 1:
        # find the midpoint of the list
        mid = length // 2
        # create a list containing the left half of the original list
        left = the_list[0:mid]
        # create a list with the right half
        right = the_list[mid:]

        # recursively divide
        merge_sort(left)

        # recursively divide
        merge_sort(right)

        # this is the osrting action, which is called within those above recursive calls
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

```
