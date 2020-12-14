def insertion_sort(the_list):
    """
    In-place list sorting method
    """
    i = 1

    while i < len(the_list):
        elem = the_list[i]
        sorted_iterator = i-1

        while elem < the_list[sorted_iterator] and sorted_iterator >= 0:
            the_list[sorted_iterator+1] = the_list[sorted_iterator]
            sorted_iterator -= 1

        the_list[sorted_iterator + 1] = elem

        i += 1
