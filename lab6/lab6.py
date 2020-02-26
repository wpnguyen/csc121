import arcade


def draw_section_outlines():
    color = arcade.color.BLACK

    #Draw the squares on the bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, color)
    arcade.draw_rectangle_outline(450, 150, 300, 300, color)
    arcade.draw_rectangle_outline(750, 150, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, color)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, color)
    arcade.draw_rectangle_outline(450, 450, 300, 300, color)
    arcade.draw_rectangle_outline(750, 450, 300, 300, color)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, color)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            # Intead of zero, calculate the proper x location using
            # colum
            x = (column * 10) + 5

            # Instead of zero, calucate the proper y location using row
            y = (row * 10) + 5

            arcade.draw_xywh_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    #
    # Use the modules operator and an if statement to select the
    # color.
    #
    # Don't loop from 30 to 60 to shift everything over, just add 300
    # to x.
    pass


def draw_section_3():
    # use the modulus operator and an if/else statement to select the
    # color.
    # 
    # don't use multiple "if" statements.
    pass


def draw_section_4():
    # Use the modulus operator and just one "if state"
    # the color
    pass


def draw_section_5():
    # Do not use "if" statements to complete 5-8. manipulate the loops
    # instead.
    pass

def draw_section_6():
    pass

def draw_section_7():
    pass

def draw_section_8():
    pass

def main():
    #create a window
    arcade.open_window(1200, 600, "lab 05 - loopy lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()

if __name__=='__main__':
    main()