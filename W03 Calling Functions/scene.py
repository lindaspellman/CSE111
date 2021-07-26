import tkinter as tk
import random
import math 


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
    
    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom, 1)

    draw_land(canvas, scene_left, scene_top, scene_right, scene_bottom, 1)
    
    draw_sun_yellow(canvas, 100, 100)
    draw_sun_red(canvas, 525, 150, 600, 220)
    
    draw_cloud(canvas=canvas, left=400, top=220, right=500, bottom=300)
    draw_cloud(canvas=canvas, left=500, top=50, right=600, bottom=100)

    tree_center = scene_left + 500
    tree_top = scene_top + 300
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    
    tree_center = scene_left + 600
    tree_top = scene_top + 250
    tree_height = 200
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 700
    tree_top = scene_top + 100
    tree_height = 350
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    draw_grass_blade(canvas)

    # draw_grid(canvas, scene_left, scene_top, scene_right, scene_bottom, 100)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky(canvas, left, top, right, bottom, grid_spacing):
    # Draw horizontal lines
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i, fill="#AFF0FF")
    # canvas.create_rectangle(0, 0, 799, 599, fill="")
    
    # Draw vertical lines
    # for i in range(left, right, grid_spacing):
        # canvas.create_line(i, top, i, bottom, fill="#AFF0FF")

def draw_land(canvas, left, top, right, bottom, grid_spacing):
    # Draw horizontal lines
    for i in range(400, bottom, grid_spacing):
        canvas.create_line(left, i, right, i, fill="#B6FFC5")
    # canvas.create_rectangle(0, 474, 799, 599, fill="")

def draw_sun_yellow(canvas, sun_left, sun_top, scale=1, ray_count=10, fill="#FFF7B4"):
    sun_width = 100 * scale 
    sun_height = 100 * scale 
    ray_length = 100 * scale 
    ray_width = 3 * scale 

    sun_right = sun_left + sun_width
    sun_bottom = sun_top + sun_height 
    sun_center_x = sun_left + (sun_width / 2)
    sun_center_y = sun_top + (sun_height / 2)

    canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill="#FFF7B4", width=False)
    for i in range(ray_count):
        angle = (2 * math.pi / ray_count) * i 
        ray_x = sun_center_x + math.cos(angle) * ray_length
        ray_y = sun_center_y + math.sin(angle) * ray_length
        canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width=ray_width, fill="#FFF7B4")

def draw_sun_red(canvas, left, top, right, bottom):
    canvas.create_oval(left, top, right, bottom, fill="#DB6D66", width=False)

def draw_cloud(canvas, left, top, right, bottom):
    upper_top = top - 50
    upper_bottom = bottom - 50
    lower_top = top + 50
    lower_bottom = bottom + 50

    for i in range(0, 4):
        canvas.create_oval(left, top, right, bottom, fill="#FDFEFE", width=False)
        left -= 50
        right -= 50
    
    left = 380
    right = 480

    for i in range(0, 3):
        canvas.create_oval(left, upper_top, right, upper_bottom, fill="#FDFEFE", width=False)
        left -= 50
        right -= 50

# def draw_cloud(canvas, cloud_groups, clouds_per_group):
    # if cloud_groups > 56
        # cloud_groups = 56
        # print("Cannot guarantee accuracy above 56...")

    """for _ in range(2250):
        x1 = random.randint(0, 799)
        y1 = random.randint(0, 599)
        fullCol = ["4", "", "A", "", "1", ""]
        fullCol[1], ...
        """ 

def draw_grid(canvas, left, top, right, bottom, grid_spacing):
    text_horizontal_margin = 20
    text_vertical_margin = 10

    # Draw horizontal lines
    for i in range(top, bottom, grid_spacing):
        canvas.create_line(left, i, right, i)
        canvas.create_text(left + text_horizontal_margin, i + text_vertical_margin, text=f"{i}")
    
    # Draw vertical lines
    for i in range(left, right, grid_spacing):
        canvas.create_line(i, top, i, bottom)
        canvas.create_text(i, top + text_vertical_margin, text=f"{i}")

def draw_grass_blade(canvas):
    left = 0
    right = 5
    for i in range(0, 799):
        canvas.create_rectangle(left, 410, right, 725, fill="green", width=0)
        left += 10
        right += 10


# ===================================================================================================================

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
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



# Call the main function so that
# this program will start executing.
main()