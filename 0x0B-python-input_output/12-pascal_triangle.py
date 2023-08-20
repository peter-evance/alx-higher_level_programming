#!/usr/bin/python3
"""
Defines a function that returns a list of lists
of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Creates an list of list(pascal_list) that holds the rows,
    of the pascal's triangle.

    Iterates over each row and assigns value which is the addition of,
    the value at row above it int its index and the adjacent left index.
                    1
                  1   1
                1  2  2  1

    Args:
        n (int): number of rows.

    Returns:
        empty list if n <= 0
        Otherwise: Returns a list of list:
                    e.g for the triangle above:
                        [[1],[1,1],[1,2,1]]
    """

    pascal_list = []
    if n <= 0:
        return pascal_list

    for i in range(n):
        temp_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(pascal_list[i-1][j-1] + pascal_list[i-1][j])
        pascal_list.append(temp_list)
    return (pascal_list)
