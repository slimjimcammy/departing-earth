from quickdraw import QuickDrawData
from quickdraw import QuickDrawDataGroup

qd = QuickDrawData()
drawingNames = qd.drawing_names

for groupName in drawingNames:
    currGroup = QuickDrawDataGroup(groupName, max_drawings=50)
    for i, drawing in enumerate(currGroup.drawings):
        drawing.image.save(f"./images/{groupName}-{i}.jpg")