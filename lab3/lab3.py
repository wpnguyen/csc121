import arcade


arcade.open_window(800, 600, "Drawing Example")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BITTER_LIME)

arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, 170, arcade.color.BISQUE)

arcade.draw_lrtb_rectangle_filled(30, 350, 350, 210, arcade.color.BROWN)

arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(70, 260, 30, 40, arcade.color.BLACK)

arcade.draw_rectangle_filled(310, 260, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(310, 260, 20, 30, arcade.color.BLACK)

arcade.draw_rectangle_filled(190, 230 ,100 100, arcade.color.BLACK_BEAN)

arcade.draw_rectangle_filled(190. 280, 180, 5, arcade.color.BONE)

arcade.draw_polygon_filled([[20, 350],
                            [100, 470],
                            [280, 470],
                            [360, 340]],
                            arcade.color.BROWN)

arcade.draw_triangle_filled(100, 470, 280, 470, 190, 500, arcade.color.BROWN)

arcade.draw_rectangle_filled(130, 440, 30, 40, arcade.color.BONE)
arcade.draw_rectangle_filled(130, 440, 20, 30, arcade.color.BLACK)


arcade.draw_rectangle_outline(190, 310,30,60, arcade.color.BONE, 5)
arcade.draw_rectangle_filled(600, 120, 140, 70, arcade.color.BLACK)

arcade.draw_rectangle_filled(580, 175, 10, 40, arcade.color.BLACK)
arcade.draw_circle_filled(490, 110, 50, aracde)