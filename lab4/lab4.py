# this will import the "arcade" library
import arcade
# this will open an window
arcade.open_window(800, 600, "Drawing Example")

# this will turn the sky blue
arcade.set_background_color(arcade.color.DARK_BLUE)

arcade.draw_circle_filled(20, 580, 20, arcade.color.WHITE)
# this is the green pasture
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)
# this is the parking spot of wendy
arcade.draw_lrtb_rectangle_filled(0, 300, 200, 0, arcade.color.GRAY)
# the road near to wendy
arcade.draw_lrtb_rectangle_filled(0, 50, 200, 0, arcade.color.BLACK)

# WENDY cement base
arcade.draw_lrtb_rectangle_filled(30, 350, 210, 170, arcade.color.BLACK_BEAN)

# Bottom half
arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, arcade.color.BROWN)



# Rail above the door
arcade.draw_rectangle_filled(190, 280, 180, 5, arcade.color.BONE)
# wendy's black wall glass
arcade.draw_lrtb_rectangle_filled(80, 350, 350, 210, arcade.color.BLACK)
# Wendy white door
arcade.draw_rectangle_filled(190, 230, 100, 100, arcade.color.BONE)

# Left-bottom window
arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(70, 260, 20, 30, arcade.color.BLACK)

arcade.draw_rectangle_filled(71, 265, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(71, 265, 20, 30, arcade.color.BLACK)

# Right-bottom window
arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 260, 20, 30, arcade.color.BLACK)



arcade.finish_render()

arcade.run()