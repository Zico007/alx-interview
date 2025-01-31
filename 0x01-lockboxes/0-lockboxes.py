#!/usr/bin/python3
"""
This module provides a function to determine if all lockboxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each index represents a box
        and contains a list of keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    unlocked = [0]
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key not in unlocked and 0 <= key < len(boxes):
            unlocked.append(key)
            keys.update(boxes[key])

    return len(unlocked) == len(boxes)
