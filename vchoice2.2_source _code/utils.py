def generateBackground(path):
    from PIL import Image
    x = 512    
    y = 512    
    rgb=[61,61,61]
    im = Image.new("RGB", (x, y))
    for i in range(x):
        for j in range(y):
            im.putpixel((i, j), (int(rgb[0]), int(rgb[1]), int(rgb[2])))
    im.save(path)


class NoValuableDataException(Exception):
    pass