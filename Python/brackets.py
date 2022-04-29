def check_brackets(expression: str):
    """Checks an expression for incorrectly placed brackets"""
    bracket_pairs = dict(zip("([{", ")]}"))
    bracket_stack = []

    for ch in expression:
        if ch in bracket_pairs.keys():  # opening bracket
            bracket_stack.append(ch)
        elif ch in bracket_pairs.values():  # closing bracket
            if (len(bracket_stack) == 0) or (bracket_pairs[bracket_stack.pop()] != ch):
                return False

    return len(bracket_stack) == 0


if __name__ == "__main__":
    assert check_brackets("[1+1]+(2*2)-{3/3}") is True
    assert check_brackets("(5+[8*2)]") is False
