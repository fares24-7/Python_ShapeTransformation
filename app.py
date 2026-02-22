import numpy as np
import matplotlib.pyplot as plt

def get_frog_data():
    body_coords = np.array([
        [ 3, 6, 6, 8,11,12,12,14,14,15,18,20,20,23,23,22,17,18,18,16,10,8,8,9,4,3],
        [11,15,17,19,19,17,16,16,17,19,19,17,15,11, 8, 6, 2, 5, 8, 9, 9,8,5,2,6,8]  
    ])
    leg1_coords = np.array([
        [2,2,4,2,2,3,4,9],
        [2,3,3,4,5,6,6,2]  
    ])
    leg1_coords = np.array([
        [2,2,4,2,2,3,4,9],
        [2,3,3,4,5,6,6,2]  
    ])
    leg2_coords = np.array([
        [17,24,24,22,24,24,23,22],
        [ 2, 2, 3, 3, 4, 5, 6, 6]  
    ])
    belly_coords = np.array([
        [9,8,8,10,16,18,18,17],
        [2,5,8, 9, 9, 8, 5, 2]  
    ])
    left_big_coords = np.array([
        [ 7, 7, 8,10,11,11,10, 8],
        [15,17,18,18,17,15,14,14]
    ])
    left_small_coords = np.array([
        [ 8, 8, 9, 9],
        [16,17,17,16]
    ])
    right_big_coords = np.array([
        [16,15,15,16,18,19,19,18],
        [14,15,17,18,18,17,15,14]
    ])
    right_small_coords = np.array([
        [16,16,17,17],
        [16,17,17,16]
    ])
    
    shapes = [
        {'coords': body_coords, 'color': '#8FBC8F'},
        {'coords': leg1_coords, 'color': '#8FBC8F'},
        {'coords': leg2_coords, 'color': '#8FBC8F'},
        {'coords': belly_coords, 'color': '#c7d962'},
        {'coords': left_big_coords, 'color': '#000000'},
        {'coords': left_small_coords, 'color': '#ffffff'},
        {'coords': right_big_coords, 'color': '#000000'},
        {'coords': right_small_coords, 'color': '#8a8a8a'},
    ]
    
    return shapes
def get_frog_data_mouth():
    mouthCoord=np.array([
        [6,7,19,20],
        [13,12,12,13]
    ])
    shape = [
        {'coords': mouthCoord, 'color': '#000000'},
    ]
    return shape
def draw_frog(ax, shapes):
    for shape in shapes:
        coords = shape['coords']
        color = shape['color']
        ax.fill(coords[0, :], coords[1, :], color=color, edgecolor='black')
def transformFrog(ax,shapes,transMat):
    for shape in shapes:
        coords = shape['coords']
        newCoords = np.dot(transMat,coords)
        color = shape['color']
        ax.fill(newCoords[0, :], newCoords[1, :], color=color, edgecolor='black')
def draw_frog_line(ax, shapes):
    for shape in shapes:
        coords = shape['coords']
        color = shape['color']
        ax.plot(coords[0, :], coords[1, :], color=color)
def transformFrogLine(ax,shapes,transMat):
    for shape in shapes:
        coords = shape['coords']
        newCoords = np.dot(transMat,coords)
        color = shape['color']
        ax.plot(newCoords[0, :], newCoords[1, :], color=color)
transformation_matrix1 = np.array([
        [0,-0.5],
        [-0.5,0.0]
    ])
transformation_matrix2 = np.array([
        [-0.5,0],
        [0,0.5]
    ])
fig, ax = plt.subplots(figsize=(8, 8))
frog_shapes = get_frog_data()
frog_shapes_line = get_frog_data_mouth()
draw_frog(ax, frog_shapes)
draw_frog_line(ax,frog_shapes_line)
transformFrog(ax,frog_shapes,transformation_matrix1)
transformFrog(ax,frog_shapes,transformation_matrix2)
transformFrogLine(ax,frog_shapes_line,transformation_matrix1)
transformFrogLine(ax,frog_shapes_line,transformation_matrix2)
ax.set_xlim(-15, 25)
ax.set_ylim(-15, 20)
ax.grid(True, which='both', linestyle='--', alpha=0.7)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_aspect('equal')
plt.show()