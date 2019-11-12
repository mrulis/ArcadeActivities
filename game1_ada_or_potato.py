import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Introduction"
GAME_SPEED = 1/60
TIMER_MAXIMUM = 100
ADA_IMAGE = arcade.load_texture("images/ada.png")
POTATO_IMAGE = arcade.load_texture("images/potato.png", scale =.2)


class ImageSwap(arcade.Sprite):
    timer: int
    score: int

    def __init__(self):
        super().__init__()
        self.texture = ADA_IMAGE
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.timer = 0
        self.score = 0

    def mousepress(self):
        if self.texture == ADA_IMAGE:
            self.score += 1
        else:
            self.score -= 1

    def update(self):
        self.timer += 1
        if self.timer > TIMER_MAXIMUM:
            if self.texture == ADA_IMAGE:
                self.texture = POTATO_IMAGE
                self.timer = 0
            elif self.texture == POTATO_IMAGE:
                self.texture = ADA_IMAGE
                self.timer = 0


class GameOne(arcade.Window, ImageSwap):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.logo_list = None

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.logo_list = arcade.SpriteList()
        self.logo_list.append(ImageSwap())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.logo_list.draw()
        arcade.draw_text("score: " + str(self.logo_list[0].score), 25, 25, arcade.color.WHITE, 12)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        for x in self.logo_list:
            x.mousepress()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.logo_list.update()

def main():
    window = GameOne()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
