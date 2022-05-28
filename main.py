
from raylibpy import *

import pymunk
import pyglfw.pyglfw as fw

MAX_BUILDINGS = 100

def main():

    # Initialization
    # ---------------------------------------------------------------
    screen_width = 800
    screen_height = 450

    init_window(screen_width, screen_height, "raylib [core] example - 2d camera")



    startAngle =0.0
    endAngle   =180.0

    set_target_fps(60)
    # ---------------------------------------------------------------

    # Main game loop
    while not window_should_close():

     

        # Draw
        # -----------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        startAngle = gui_slider_bar(Rectangle( 600, 40, 120, 20), "StartAngle", "", startAngle, 90, 720)
        endAngle = gui_slider_bar(Rectangle(600, 70, 120, 20), "EndAngle", "", endAngle, 0, 720)

        gui_button(Rectangle(600, 120, 120, 20), "Button")

        draw_text("SCREEN AREA", 640, 10, 20, RED)

        draw_rectangle(0, 0, screen_width, 5, RED)
        draw_rectangle(0, 5, 5, screen_height - 10, RED)
        draw_rectangle(screen_width - 5, 5, 5, screen_height - 10, RED)
        draw_rectangle(0, screen_height - 5, screen_width, 5, RED)

        draw_rectangle( 10, 10, 250, 113, fade(SKYBLUE, 0.5))
        draw_rectangle_lines( 10, 10, 250, 113, BLUE)

        draw_text("Free 2d camera controls:", 20, 20, 10, BLACK)
        draw_text("- Right/Left to move Offset", 40, 40, 10, DARKGRAY)
        draw_text("- Mouse Wheel to Zoom in-out", 40, 60, 10, DARKGRAY)
        draw_text("- A / S to Rotate", 40, 80, 10, DARKGRAY)
        draw_text("- R to reset Zoom and Rotation", 40, 100, 10, DARKGRAY)

        end_drawing()
        # -----------------------------------------------------------

    # De-Initialization
    # ---------------------------------------------------------------
    close_window()       # Close window and OpenGL context
    # ---------------------------------------------------------------


if __name__ == '__main__':
    main()