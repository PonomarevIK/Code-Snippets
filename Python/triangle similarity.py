from fractions import Fraction


def similar_triangles(coords_1: list[tuple[int, int]], coords_2: list[tuple[int, int]]) -> bool:
    """ Check two triangles for similarity using ratio of side lengths.
        Each triangle is represented with a list of integer (x, y) points
    """

    # Squared side length since sqrt() leads to slower speed and loss of precision
    def distance_squared(a: tuple[int, int], b: tuple[int, int]):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    # Triangle 1 and 2 sides sorted shortest to longest
    sides_1 = sorted(distance_squared(coords_1[i], coords_1[(i+1) % 3]) for i in range(3))
    sides_2 = sorted(distance_squared(coords_2[i], coords_2[(i+1) % 3]) for i in range(3))

    # All side ratios are equal
    return Fraction(sides_1[0],  sides_2[0]) == Fraction(sides_1[1], sides_2[1]) == Fraction(sides_1[2], sides_2[2])

    # return len(set(Fraction(sides_1[i], sides_2[i]) for i in range(3))) == 1 - another way, less readable though
