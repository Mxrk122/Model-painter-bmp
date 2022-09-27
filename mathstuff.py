from collections import namedtuple
from vector3 import *

# Necesario para vector 2 y 3 dimensiones
V2 = namedtuple('Point2', ['x', 'y'])
# Archivo dedicado a operaciones matematicas
def cross_p(v0, v1):
    return V3(
        v0.y * v1.z - v0.z * v1.y,
        v0.z * v1.x - v0.x * v1.z,
        v0.x * v1.y - v0.y * v1.x,
    )

def bounding_box(A, B, C):
    coordinates = [(A.x, A.y), (B.x, B.y), (C.x, C.y)]

    xmin = 99999
    xmax = -99999
    ymin = 99999
    ymax = -99999

    for (x, y) in coordinates: 
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin: 
            ymin = y
        if y > ymax:
            ymax = y

    #print("Coordenadas del bounding box: ", coordinates)

    return V3(xmin, ymin), V3(xmax, ymax)

def barycentric(A, B, C, P):

    cx, cy, cz = V3.getValues(V3(
        B.x - A.x, C.x - A.x, A.x - P.x
    )*V3(
        B.y - A.y, C.y - A.y, A.y - P.y
    ))
    
    if cz == 0:
        u, v, w = -1, -1, -1
        return(u, v, w)

    else:
        u = cx/cz
        v = cy/cz
        w = 1 - (u + v)

        return (w, v, u)