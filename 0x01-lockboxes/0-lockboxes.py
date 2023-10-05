def canUnlockAll(boxes):
    unlocked_boxes = [0]
    keys = boxes[0]

    while keys:
        new_keys = []
        for key in keys:
            if key < len(boxes) and key not in unlocked_boxes:
                unlocked_boxes.append(key)
                new_keys += boxes[key]
        keys = new_keys

    return len(unlocked_boxes) == len(boxes)
