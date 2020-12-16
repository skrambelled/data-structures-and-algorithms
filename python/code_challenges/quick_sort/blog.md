# Quick Sort

Quick sorting is another useful way to sort a list.

First, we pick a pivot value. You can optimize the quick sort by being selective about which value you pick, but for this particular run-through, we will always use the rightmost values as the pivot value.

We'll use three indices throughout the process:

* left index at position 0
* pivot index at the end of the list
* right, 1 position to the left of the pivot

```python
#            right
#              v
#    [4, 2, 5, 7, 3]
#     ^           ^
#   left        pivot
```

In a loop:

1. increment left index until we reach a value *larger or equal to* the pivot value, in this case the first value of `4` is already larger than the pivot value of `3` OR until we the end of the list.
1. decrement the right value until we reach a value *less than* the pivot value; `2` OR until we cross the left index

```python
#      right
#        v
#    [4, 2, 5, 7, 3]
#     ^           ^
#   left        pivot
```

Now, swap the left and right values.

```python
#  left  right
#     v  v
#    [2, 4, 5, 7, 3]
#      \/         ^
#    swapped      pivot
```

Continue the loop.
So increment the left index until we reach a value higher than the pivot. (or reach the end)
Decrement the right until we reach a lower value (or corss the left)

```python
#    right (has crossed left)
#     v
#    [2, 4, 5, 7, 3]
#        ^        ^
#      left     pivot
```

When the right index crosses the left index, then all elements to the left side of the left index is less than or equal to the pivot value, and all values to the right are larger than the pivot value. So we can swamp the pivot with the left value to put it in its proper location relative to the two sides.

```python
#          swapped
#         /      \
#    [2, 3, 5, 7, 4]
#        ^        ^
#       left    pivot
```

Then we can run the same operation recursively on the each of the two sides in a another stack frame, until we reach a base case where each side is only of length 1.

```python
#   left list, which is only a list of [2]
#     v
#    [2, 3, 5, 7, 4]
#           |     |
#       right list, which is a list of [5, 7, 4]
```

So we'll run it on the right portion:

```python
#      right
#        v
#    [5, 7, 4]
#     ^     ^
#   left   pivot
```

Left, 5, is already larger than pivot, 4, so don't inrement.
Decrement right, till we get a value lower than 4 OR we pass the left index

```python
#   right (about to go out of bound, and cross the left)
#     v
#    [5, 7, 4]
#     ^     ^
#   left  pivot
```

Since the right index crossed the left index, we know that all values to the left of the left index (which there are none) are less than the pivot value. And all the values to the right are higher. So we can now swap left with pivot.

```python
#    [4, 7, 5]
#      \   /
#     swapped
```

And now there is no left list, but there is a right list:

```python
#       right list, which is a list of [7, 5]
#        |  |
#    [4, 7, 5]
```

And we can run it again, in a 3rd stack frame on that right list.

```python
#   right
#     v
#    [7, 5]
#     ^  ^
#  left  pivot
```

Increment left till we reach a higher value than pivot. 7 is larger than 5 so we are already set.

Decrement the right till we reach a lower value tahn pivot or cross left. We immediately cross left.

Swap left and pivot.

```python
#    [5, 7]
#      \/
#    swapped
```

Now this 3rd stack frame is resolved, and because we were modifying this list in place, the whole dang thing is done!

```python
#    sorted, hurray!
#
#    [2, 3, 4, 5, 7]
```

---

