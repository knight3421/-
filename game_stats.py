class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score = 0
        self.game_active = False
    def reset_stats(self):
        self.score = 0