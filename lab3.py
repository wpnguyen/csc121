import arcade


arcade.open_window(800, 600, "Drawing Example")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, 170, arcade.color.BISQUE)

arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, arcade.color.BROWN)

arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE)
arcade.draw_