from quickdraw import QuickDrawData
from quickdraw import QuickDrawDataGroup

qd = QuickDrawData()
drawingNames = qd.drawing_names
names = [
    "Dragon",
    "Angel",
    "Sword",
    "Castle",
    "Crown",
    "Dog",
    "Teapot",
    "Sea Turtle",
    "Tornado",
    "Whale",
    "Flying Saucer",
    "Lighthouse"
]

for groupName in names:
    currGroup = QuickDrawDataGroup(groupName, max_drawings=100)
    for i, drawing in enumerate(currGroup.drawings):
        drawing.image.save(f"./images/{groupName}-{i}.jpg")

