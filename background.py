from turtle import Screen, Turtle


class Background:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=1200, height=806)
        self.screen.title("Where is the ISS?")
        self.screen.bgpic("images/world_long_lat.png")