import struct
import color
import Obj
class Texture(object):

    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        # Procedimiento inverso
        with open(self.path, "rb") as image:
            image.seek(2 + 4 + 2 + 2)
            head_size = struct.unpack("=l", image.read(4))[0]
            image.seek(2 + 4 + 2 + 2 + 4 + 4)
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            image.seek(head_size)
            self.pixels = []

            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))

                    self.pixels[y].append(
                        color.color_RGB_to_GBR(r/255, g/255, b/255)
                    )
    
    def get_color(self, tx, ty):
        x = round(tx * self.width)
        y = round(ty * self.width)

        return self.pixels[y][x]

    def get_intensity(self, tx, ty, intensity):
        
        x = round(tx * self.width)
        y = round(ty * self.width)
        

        if(x >= self.width or y >= self.height):
            return color.color_RGB_to_GBR(1, 1, 0)
        
        else:
            b = self.pixels[y][x][0] * intensity
            g = self.pixels[y][x][1] * intensity
            r = self.pixels[y][x][2] * intensity

            return color.color_RGB_to_GBR(r/255, g/255, b/255)

    def getTexture(self):
        return self.pixels
