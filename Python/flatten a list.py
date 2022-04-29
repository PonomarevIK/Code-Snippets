def recursive_iter(lst):
    """Recursively iterates over an arbitrarily nested collection"""
    for item in lst:
        if isinstance(item, (list, tuple)):
            yield from recursive_iter(item)
        else:
            yield item


if __name__ == "__main__":
    nested_list = [1, 2, [3, ([4], 5)], 6, [(7, 8), 9]]
    assert list(recursive_iter(nested_list)) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
