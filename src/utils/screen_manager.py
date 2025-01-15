class ScreenManager:
    def __init__(self, icurrent_state):
        self.current_state = icurrent_state
    def get_state(self):
        return self.current_state
    def set_state(self, new_state):
        self.current_state = new_state