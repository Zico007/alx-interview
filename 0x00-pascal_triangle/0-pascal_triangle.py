#!/usr/bin/python3
"""
This module contains functions to generate and print Pascal's triangle.
"""


def pascal_triangle(n):
    """Return Pascal’s triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    """Print the triangle."""
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    n = int(input("Enter rows for Pascal's triangle: "))
    print_triangle(pascal_triangle(n))
