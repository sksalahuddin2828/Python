from tkinter import Canvas, Tk
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1

def main():
    root = Tk()
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    # Set up the player and goal rectangles
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, fill="blue")
    goal = canvas.create_rectangle(360, 360, 380, 380, fill="red")

    # Set the initial movement direction
    movement_direction = [1, 0]

    # Event handling
    root.bind("<KeyPress>", lambda event: handle_key_press(event, movement_direction))
    root.focus_set()

    # Animation loop
    while True:
        canvas.move(player, SIZE * movement_direction[0], SIZE * movement_direction[1])

        # Update the world for one heartbeat
        player_x = canvas.coords(player)[0]
        player_y = canvas.coords(player)[1]

        if player_x > CANVAS_WIDTH - SIZE or player_x < 0 or player_y > CANVAS_HEIGHT - SIZE or player_y < 0:
            game_over(canvas, root)
            break

        if player_x == canvas.coords(goal)[0] and player_y == canvas.coords(goal)[1]:
            hit_goal(canvas, goal)
        
        root.update()
        time.sleep(DELAY)

def handle_key_press(event, movement_direction):
    key = event.keysym
    if key == "Left":
        movement_direction[0] = -1
        movement_direction[1] = 0
    elif key == "Right":
        movement_direction[0] = 1
        movement_direction[1] = 0
    elif key == "Up":
        movement_direction[0] = 0
        movement_direction[1] = -1
    elif key == "Down":
        movement_direction[0] = 0
        movement_direction[1] = 1

def game_over(canvas, root):
    # Display game over message
    canvas.create_text(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, text="Game Over!", font=("Arial", 30), fill="red")
    root.quit()

def hit_goal(canvas, goal):
    # Generate random x-coordinate as a multiple of SIZE
    rand_x = random.randrange(0, CANVAS_WIDTH - SIZE + 1, SIZE)

    # Generate random y-coordinate as a multiple of SIZE
    rand_y = random.randrange(0, CANVAS_HEIGHT - SIZE + 1, SIZE)
    canvas.coords(goal, rand_x, rand_y, rand_x + SIZE, rand_y + SIZE)

if __name__ == '__main__':
    main()
