import numpy as np
import matplotlib.pyplot as plt
def getLineData():
    houseCoord=np.array([
        [0,3,   4,  4,4.5,4.5,6,5,5,1,1,0],
        [3,5,4.25,4.5,4.5,  4,3,3,1,1,3,3]
    ])
    shape = [
        {'coords': houseCoord, 'color': '#000000'},
    ]
    return shape
def drawLines(ax, shapes):
    for shape in shapes:
        coords = shape['coords']
        color = shape['color']
        ax.plot(coords[0, :], coords[1, :], color=color)
def transformLine(ax,shapes,transMat,addedMat):
    for shape in shapes:
        coords = shape['coords']
        newCoords = np.dot(transMat,coords)+addedMat
        color = shape['color']
        ax.plot(newCoords[0, :], newCoords[1, :], color="#ff0000")
transMat1=np.array([
    [0.25,0],
    [0,-2]
])
transMat2=np.array([
    [5],
    [0]
])
fig, ax = plt.subplots(figsize=(8, 8))
shape = getLineData()
drawLines(ax,shape)
transformLine(ax,shape,transMat1,transMat2)
ax.set_xlim(-1, 8)
ax.set_ylim(-10, 6)
ax.grid(True, which='both', linestyle='-', alpha=1)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_aspect(1/3.3)
plt.show()