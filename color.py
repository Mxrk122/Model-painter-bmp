def color_RGB_to_GBR(r, g, b):
    #retornar en bytes
    return bytes([int(b * 255), int(g * 255), int(r * 255)])