def draw_swastika(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if i < rows // 2:
                if j < cols // 2:
                    if j == 0:
                        print("*", end="")
                    else:
                        print(" ", end=" ")
                elif j == cols // 2:
                    print(" *", end="")
                else:
                    if i == 0:
                        print(" *", end="")
            elif i == rows // 2:
                print("* ", end="")
            else:
                if j == cols // 2 or j == cols - 1:
                    print("* ", end="")
                elif i == rows - 1:
                    if j <= cols // 2 or j == cols - 1:
                        print("* ", end="")
                    else:
                        print(" ", end=" ")
                else:
                    print(" ", end=" ")
        print()

rows = 7
cols = 7
draw_swastika(rows, cols)


# Answer: 
#  *     * * * *
#  *     *
#  *     *
#  * * * * * * * 
#        *     * 
#        *     * 
#  * * * *     * 
