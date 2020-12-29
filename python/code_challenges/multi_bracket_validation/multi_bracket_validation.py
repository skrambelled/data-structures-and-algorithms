from code_challenges.stacks_and_queues.stacks_and_queues import Stack


def validate_string(string):
    stack = Stack()

    # opening symbols
    opening = '{[('
    # closing symbols, must be in the matched order of opening
    closing = '}])'

    # iterate through the string we are testing
    for char in string:
        # if we encounter an opening symbol, push it to the stack
        if char in opening:
            stack.push(char)
        # if we encounter a closing symbol, check if it matches the top of the stack
        elif char in closing:
            i = closing.index(char)
            if stack.is_empty() or stack.pop() != opening[i]:
                return False

    # if we've not matched all the symbols... fail!
    if not stack.is_empty:
        return False

    # we have matched all the symbols, success!
    return True
