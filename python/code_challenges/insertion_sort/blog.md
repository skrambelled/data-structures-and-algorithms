# Insertion Sorting

When all your elements in a list are in order it's much faster to search through these elements and perform other useful operations. But we don't always get a nice sorted list. In that case we need to iterate through the list and sort those elements! There are many strategies for sorting, today we'll go over one of the simpler and more intuitive ones, which we call *insertion sorting*.

Let's say you get an unsorted list:

```python
[5, 2, 7, 4, 1]
```

The idea here is that we'll divide our list into two sub-lists. The left-hand portion represents the sorted portion of the list, and the right-hand portion represents the sorted portion.

We'll start our divider just after the first element, because we can always assume that a list containing only one element is sorted. I'll illustrate this using a pipe character to divide the two sides.

```python
5 | 2 7 4 1
```

As we traverse the right-hand unsorted side of the list, we'll grab each element and compare it to each element on the sorted side, but move **backwards**. In this case we can grab the 2, and compare it to the sorted 5, see that the 2 is smaller and move on. We then reach the end of the list and know we are in the correct position because there are not more elements to compare to.

```python
2 5 | 7 4 1
```

Next we have the 7, which is greater than the first element we encounter on the sorted side, so we are already in the correct position and can move the divider up by one element.

```python
2 5 7 | 4 1
```

Next we encounter a 4, which is less than 7, move on. Less than 5, move on. Greater than 2, we are in the correct position.

```python
2 4 5 7 | 1
```

Lastly, we encoutner a 1. Less than 7, move on, less than 5, move on. Less than 4, move on. Less than 2, move on. End of the list, we are in the correct position, and we have successfully sorted the whole list!

```python
1 2 4 5 7
```

---

```python
# Python code
def insertion_sort(the_list):
    # we can start at element 1, rather than 0
    # because the first element is already designated
    # as being sorted
    i = 1

    while i < len(the_list):
        # grab the value of the first element on the right-hand unsorted
        # side of our list, this is the element we wish to insert into the
        # left-hand sorted side
        elem = the_list[i]

        # this is the internal iterator to go backwards through the sorted
        # portion of the list. it starts at the end of the sorted portion
        # which is one element to the left of our element we are going to
        # insert
        sorted_iterator = i-1

        # now we have to loop through the sorted portion, but we'll
        # traverse backwards until we reach the correct location, which
        # can be either the end of the list (the leftmost side) OR when
        # our element to be inserted is no longer less than the sorted
        # element we are looking at
        while elem < the_list[sorted_iterator] and sorted_iterator >= 0:
            # as we traverse backwards, move each sorted element to the right
            the_list[sorted_iterator+1] = the_list[sorted_iterator]
            sorted_iterator -= 1

        # we've reached the correct location, time for insertion!
        the_list[sorted_iterator + 1] = elem

        # now that we've inserted, move on to the next unsorted element
        i += 1

```
