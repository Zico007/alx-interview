#!/usr/bin/python3
def canUnlockAll(boxes):
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
    