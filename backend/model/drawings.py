from quickdraw import QuickDrawData
from quickdraw import QuickDrawDataGroup

qd = QuickDrawData()
drawingNames = qd.drawing_names
names = [
    "dragon",
    "angel",
    "sword",
    "castle",
    "crown",
    "dog",
    "teapot",
    "sea turtle",
    "tornado",
    "whale",
    "flying saucer",
    "lighthouse"
]

for groupName in names:
    currGroup = QuickDrawDataGroup(groupName, max_drawings=100)
    for i, drawing in enumerate(currGroup.drawings):
        drawing.image.save(f"./images/{groupName}-{i}.jpg")

