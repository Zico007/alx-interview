#!/usr/bin/python3
"""
This module contains a function to generate Pascal's Triangle.

The function `pascal_triangle(n)` returns a list of lists of integers
representing Pascal’s Triangle up to `n` rows.
"""

def pascal_triangle(n):
        """
        Determines if all boxes can be unlocked.

        Args:
            boxes (list of lists): A list where each index represents a box 
            and contains a list of keys to other boxes.

        Returns:
            bool: True if all boxes can be opened, False otherwise.
        """
  
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)
        triangle.append(row)
    return triangle
