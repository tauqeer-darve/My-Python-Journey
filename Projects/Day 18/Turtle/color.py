import colorgram

def color_generator():
    colors = colorgram.extract('spots.jpeg',35)
    colour_list = []
    for i in range(1, len(colors)):
        color_list = colors[i]
        rgb = color_list.rgb
        colours = (rgb[0],rgb[1],rgb[2])
        colour_list.append(colours)
    return colour_list
