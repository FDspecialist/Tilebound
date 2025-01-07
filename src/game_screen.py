class GameScreen:
    def __init__(self, _display, _ScreenManager):
        self.display = _display
        self.ScreenManager = _ScreenManager
    def run(self):
        self.display.fill('green')