picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
line = ''
def Xmas_tree(): 
    for row in picture:
        for pixel in row:
            if (pixel== 1):
                print("*", end='')
            else:
                print(" ", end='')
        print('') # need a line after the row-loop

Xmas_tree()