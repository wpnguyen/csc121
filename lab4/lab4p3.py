# this will import the "arcade" library
import arcade
import math
# this will open an window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "MOON EXAMPLE"

CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_WIDTH // 2
RADIANS_PER_FRAME = 0.02
SWEEP_LENGTH = 250

def on_draw(_delta_time):

    on_draw.angle += RADIANS_PER_FRAME

    x = SWEEP_LENGTH * math.sin(on_draw.angle) + CENTER_X
    y = SWEEP_LENGTH * math.cos(on_draw.angle) + CENTER_Y

    arcade.start_render()

    arcade.draw_circle_filled(CENTER_X, CENTER_Y, x, arcade.color.BONE, 4)

    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

    arcade.draw_lrtb_rectangle_filled(0, 300, 200, 0, arcade.color.GRAY)

    arcade.draw_lrtb_rectangle_filled(0, 50, 200, 0, arcade.color.BLACK)


    arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.BLACK_BEAN)


    arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, arcade.color.BROWN)

    arcade.draw_rectangle_filled(190, 280, 180, 5, arcade.color.BONE)

    arcade.draw_lrtb_rectangle_filled(80, 350, 350, 210, arcade.color.BLACK)

    arcade.draw_rectangle_filled(190, 230, 100, 100, arcade.color.BONE)


    arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE)
    arcade.draw_rectangle_filled(70, 260, 20, 30, arcade.color.BLACK)

    arcade.draw_rectangle_filled(71, 265, 30, 40, arcade.color.BONE)
    arcade.draw_rectangle_filled(71, 265, 20, 30, arcade.color.BLACK)

    arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.color.BONE)
    arcade.draw_rectangle_filled(310, 260, 20, 30, arcade.color.BLACK)


on_draw.angle = 0

def main():

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.DARK_BLUE)

    
    arcade.schedule(on_draw, 1 / 80)

    arcade.run()

    arcade.close_window()


if __name__ == "__main__":
    main()