def recursive_iter(lst: list):
    """Recursively iterates over an arbitrarily nested list"""
    for item in lst:
        if isinstance(item, list):
            yield from recursive_iter(item)
        else:
            yield item


if __name__ == "__main__":
    nested = [1, 2, [3, [[4], 5]], 6, [[7, 8], 9]]
    assert list(recursive_iter(nested)) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
