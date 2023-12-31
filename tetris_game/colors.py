class Colors:
    dark_grey = (26, 31, 40) # color of the empty cell
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (155, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    
    @classmethod #class decorator 
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
    # the order of the list is important, the index of each color will be used to draw each cell on the screen
    # the index corresponds to the block id 