import tkinter as tk
import random

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    """tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)"""

    draw_sky(canvas)
    draw_ground(canvas)
    draw_sun(canvas)
    draw_cloud(canvas)
    draw_tree(canvas)
    draw_grass(canvas)
    draw_wind(canvas)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky(canvas):
    width = 800
    height = 500
    canvas.create_rectangle(0, 0, width, height, fill="steelBlue1", outline="steelBlue1")


def draw_ground(canvas):
    width = 800
    height = 500
    canvas.create_rectangle(0, 350, width, height, fill="gray80", outline="gray70")
    canvas.create_rectangle(0, 400, width, height, fill="seaGreen2", outline="seaGreen3")


def draw_cloud(canvas):
    width = 800
    height = 200

    for i in range(0, 4, 1):
        x = random.randint(25, width-75)
        y = random.randint(15, 100)
        x1 = random.randint(x + 15, width)
        y1 = random.randint(y + 15, height)
        
        canvas.create_oval(x, y, x1, y1, fill="ghostWhite", outline="lightBlue1")

def draw_tree(canvas):
    width = 0
    height = 420

    canvas.create_rectangle(width, height, width + 35, height - 150, fill="darkGoldenrod4", outline="orange4")

    x = -125
    y = 375
    x1 = 60
    y1 = 295
    for i in range(0, 15, 1):
        y -= 13
        y1 -= 13
        canvas.create_arc(x, y, x1, y1, fill="springGreen4", outline="darkGreen", style=tk.CHORD)

def draw_sun(canvas):
    canvas.create_oval(650, 25, 750, 125, fill="yellow", outline="gold")

def draw_grass(canvas):
    width = 800
    height = 500

    for i in range(0, 2500, 1):
        x = random.randint(0, width)
        y = random.randint(395, height - 15)
        x1 = x + 2
        y1 = y + 7
        
        canvas.create_rectangle(x, y, x1, y1, fill="green4", outline="green4")

def draw_wind(canvas):
    width = 800
    height = 500
    for i in range(0, 12, 1):
        x = random.randint(0, 400)
        y = random.randint(200, height - 35)
        x1 = x + 500
        y1 = y + 10
        canvas.create_arc(x, y, x1, y1, fill="gray85", outline="gray78", width=5, style=tk.ARC)


"""
def draw_pine_tree(canvas, peak_x, peak_y, height):
    
   
    COMMENT OUT
    Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    COMMENT OUT

    
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")
"""


# Call the main function so that
# this program will start executing.
main()