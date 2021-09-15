import arcade


class Apple:
    pass

class Snake:
    pass

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self,600,400,"Super Snake", antialiasing=False)
        #arcade.open_window(500, 500, "Welcome to GFG " , False,  False)
        #arcade.set_background_color(arcade.color.PINK)
        arcade.set_background_color(arcade.color.SAND)

    def on_draw(self):
        #arcade.start_render()
        pass



game=Game()


arcade.run()
