#!/usr/bin/python3
<<<<<<< HEAD
"""13-pascal_triangle.py"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascals triangle of n
    """

=======
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
