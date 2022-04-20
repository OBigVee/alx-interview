#!/usr/bin/python3
# def canUnlockAll(boxes):
#     checker = False
#     for boxList in boxes:
#         print(boxList)
#         for boxItem in boxList:
#             print(boxes.index(boxes[boxList][boxItem]))
#             print(boxItem)
#             if (boxList[boxItem] == boxes.index(boxes[boxList][boxItem])):
#                 return True
#             else:
#                 return False




def canUnlockAll(boxes):
    """Determines if boxes can be trackUnlockedBox"""
    index = 0
    trackUnlockedBox = {}

    for box in boxes:
        if len(box) == 0 or index == 0:
            trackUnlockedBox[index] = "opened"
        for key in box:
            if key < len(boxes) and key != index:
                trackUnlockedBox[key] = key
        if len(trackUnlockedBox) == len(boxes):
            return True
        index += 1
    return False