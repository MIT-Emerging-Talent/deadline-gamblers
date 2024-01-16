
def deletions_to_make_valid_parentheses(s: str) -> int:
    """
    :param s: string of parentheses
    :return: the number of required deletion to make a valid parentheses
    """
    # Basic case
    if len(s) <=1:
        return len(s)

    # create counter to count the number of parentheses ( == increment by 1, )== decrease by 1
    inValidParentheses =0
    for char in s:
        # ( == char - increment by 1
        if char == '(': inValidParentheses+=1
        # ) == char - decrease by 1
        if char == ')': inValidParentheses -= 1

    return abs(inValidParentheses)