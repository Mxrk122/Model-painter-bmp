from asyncio.windows_events import NULL
import render
# importing the sys module
import sys

import color

from Obj import *
 
# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
 
sys.setrecursionlimit(10**8)


class gl(object):

    def __init__(self, filename):
        self.filename = filename
        self.r = render.Render()
    
    def glCreateWindow(self, width, height):
        self.height = height
        self.width = width
        self.r.setSize(width, height)
    
    def glClearColor(self, r, g, b):
        self.r.set_clear_color(r, g, b)
    
    def glClear(self):
        self.r.clear()
    
    def glFinish(self):
        self.r.write(self.filename)

    def glViewPort(self, x, y, width, height):
        self.r.createViewPort(x, y, width, height)

    def glVertex(self, x, y):
        self.r.point(x, y)
    
    def glColor(self, r, g, b):
        self.r.set_vertex_color(r, g, b)

    def glClearViewPort(self):
        self.r.clearViewPort()
    
    def simplyPoint(self, x, y):
        self.r.simply_point(x,y)
    
    def glLine(self, x_0, y_0, x_1, y_1):
        self.r.line(x_0, y_0, x_1, y_1)
    
    def glLineNormal(self, x_0, y_0, x_1, y_1):
        self.r.line_normal(x_0, y_0, x_1, y_1)
    
    def glFill(self, x, y):
        oldColor = self.r.extractColor(x, y)
        self.r.fill(x, y, oldColor)
    
    def glSetFillColor(self, r, g, b):
        self.r.set_vertex_color(r, g, b)
    
    def glSetObject(self, objname):
        self.object = Obj(objname)

        return self.object
    
    def glObjectMode(self, scale, translate, rotate, current_color, texture=None):

        self.r.giveTexture(texture)

        o = self.object

        o.setSize(self.height, self.width)

        o.loadModelMatrix(scale, translate, rotate)

        for face in o.faces:
            if len(face) == 4:
                # Extraer caras
                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1
                f4 = face[3][0] - 1

                # REcibir coordenadas transformadas
                v1 = o.transform_vertex(o.vertex[f1])
                v2 = o.transform_vertex(o.vertex[f2])
                v3 = o.transform_vertex(o.vertex[f3])
                v4 = o.transform_vertex(o.vertex[f4])

                # Solo realizar si el usuario mando una textura
                if texture:
                    
                    # Extraer caras
                    
                    f1 = face[0][1] - 1
                    f2 = face[1][1] - 1
                    f3 = face[2][1] - 1
                    f4 = face[3][1] - 1


                    # REcibir coordenadas transformadas
                    vt1 = V3(
                        *o.texture_vertex[f1]
                    )
                    vt2 = V3(
                        *o.texture_vertex[f2]
                    )
                    vt3 = V3(
                        *o.texture_vertex[f3]
                    )
                    vt4 = V3(
                        *o.texture_vertex[f4]
                    )

                    self.r.triangle((v1, v2, v3), current_color, (vt1, vt2, vt3))

                    self.r.triangle((v1, v4, v3), current_color, (vt1, vt4, vt3))

                else:

                    
                    self.r.triangle((v1, v2, v3), current_color)

                    self.r.triangle((v1, v4, v3), current_color)
                
                #print(f1, f2, f3, f4)


            if len(face) == 3:
                
                f1 = face[0][0] - 1
                f2 = face[1][0] - 1
                f3 = face[2][0] - 1

                v1 = o.transform_vertex(o.vertex[f1])
                v2 = o.transform_vertex(o.vertex[f2])
                v3 = o.transform_vertex(o.vertex[f3])
                
                # Solo realizar si el usuario mando una textura
                if texture:
                    
                    # Extraer caras
                    f1 = face[0][1] - 1
                    f2 = face[1][1] - 1
                    f3 = face[2][1] - 1


                    # REcibir coordenadas transformadas
                    vt1 = V3(
                        *o.texture_vertex[f1]
                    )
                    vt2 = V3(
                        *o.texture_vertex[f2]
                    )
                    vt3 = V3(
                        *o.texture_vertex[f3]
                    )

                    self.r.triangle((v1, v2, v3), current_color, (vt1, vt2, vt3))

                else:

                    # si no hay textura, simplemente pintar el triangulo con colores
                    self.r.triangle((v1, v2, v3), current_color)
        return o
    
    def glTriangle(self, A, B, C):
        self.r.triangle(A, B, C)

    def glGiveTexture(self, texture):
        self.r.giveTexture(texture)

    def glPaintTexture(self, texture):
        self.r.framebuffer = texture

    
